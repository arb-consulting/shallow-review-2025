"""Draft document processing: extract structured metadata from research agendas.

Provides parallelized LLM extraction of agenda attributes from draft markdown documents.
"""

import json
import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml
from anthropic import transform_schema, Anthropic
from jinja2 import Template
from pydantic import ValidationError
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from .common import PROMPTS_PATH, is_shutdown_requested
from .draft_types import DocumentItem
from .llm import _get_retry_attempt, _set_retry_attempt, setup_litellm

logger = logging.getLogger(__name__)


def extract_agenda_attributes(
    item,  # DocumentItem (avoiding import to keep this module standalone)
    content: str,
    agenda_list: list[dict[str, str]],
    orthodox_problems: dict,
    target_cases: dict,
    broad_approaches: dict,
) -> object:  # Returns DocumentItem
    """Extract structured metadata from agenda content using Claude Haiku.

    Takes a DocumentItem with structural fields (id, name, header_level, parent_id)
    and content separately. Returns the same DocumentItem with agenda_attributes populated.

    Args:
        item: DocumentItem with id, name, header_level, parent_id filled (content should be None)
        content: Markdown content to extract from
        agenda_list: List of all agendas/sections for see_also resolution (dicts with 'id' and 'name')
        orthodox_problems: Dictionary of orthodox problem IDs to info
        target_cases: Dictionary of target case IDs to info
        broad_approaches: Dictionary of broad approach IDs to info

    Returns:
        DocumentItem with agenda_attributes populated (and parsing_issues added)
    """
    from litellm import completion

    # Defensive checks
    if item.content is not None:
        logger.warning(f"Item {item.id} has non-null content field, should be null for extraction")
    
    if not content or not content.strip():
        logger.warning(f"Empty content for {item.id}, returning item with empty attributes")
        # Import AgendaAttributes here to avoid circular imports
        from .draft_types import AgendaAttributes
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append("Empty content provided for extraction")
        return item

    if not agenda_list:
        logger.warning(f"Empty agenda_list for {item.id}, see_also resolution may fail")

    # Load prompt template
    prompts_file = PROMPTS_PATH / "draft.yaml"
    with open(prompts_file) as f:
        prompts = yaml.safe_load(f)
    
    prompt_template = prompts["extract_agenda_attributes"]["user"]

    # Create input item JSON (without content field for prompt)
    item_for_prompt = item.model_copy()
    item_for_prompt.content = None  # Ensure content is None
    item_json = item_for_prompt.model_dump_json(indent=2, exclude_none=False)

    # Render prompt with item structure and content
    try:
        template = Template(prompt_template)
        prompt = template.render(
            item_json=item_json,
            content=content,
            orthodox_problems=orthodox_problems,
            target_cases=target_cases,
            broad_approaches=broad_approaches,
            agenda_list=agenda_list,
        )
    except Exception as e:
        logger.error(f"Failed to render prompt for {item.id}: {e}")
        from .draft_types import AgendaAttributes
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append(f"Prompt rendering failed: {str(e)}")
        return item

    # Helper function to fix JSON escape issues from LLM output
    def fix_json_escapes(text: str) -> str:
        """Fix invalid backslash escapes in JSON text."""
        result = text.replace('\\', '\\\\')  # Escape all backslashes
        # Now unescape the valid JSON escapes (they're now double-escaped)
        result = result.replace('\\\\n', '\\n')
        result = result.replace('\\\\t', '\\t')
        result = result.replace('\\\\r', '\\r')
        result = result.replace('\\\\f', '\\f')
        result = result.replace('\\\\b', '\\b')
        result = result.replace('\\\\/', '\\/')
        result = result.replace('\\\\"', '\\"')
        result = result.replace('\\\\\\\\', '\\\\')  # Fix double-escaped backslashes
        return result

    def _on_retry_before_sleep(retry_state):
        """Callback before retry - tracks retry attempt for cache bypass via max_tokens increment."""
        exception = retry_state.outcome.exception()
        if isinstance(exception, (ValidationError, ValueError, json.JSONDecodeError)):
            # Store retry increment: use attempt_number as the increment for the next retry
            # attempt_number=1 (first attempt fails) -> increment=1 for next retry
            # attempt_number=2 (first retry fails) -> increment=2 for next retry
            retry_increment = retry_state.attempt_number
            _set_retry_attempt(retry_increment)
            logger.warning(
                f"{type(exception).__name__} on attempt {retry_state.attempt_number}, "
                f"will bypass cache by incrementing max_tokens by {retry_increment} on next retry"
            )
        # Call the default before_sleep logger
        before_sleep_log(logger, logging.WARNING)(retry_state)

    def _should_retry(exception):
        """Determine if we should retry on this exception."""
        from openai import APIError, RateLimitError
        # Retry on API errors, rate limits, and parsing/validation errors
        return isinstance(
            exception,
            (RateLimitError, APIError, ValidationError, ValueError, json.JSONDecodeError),
        )

    # Call LLM and parse response with retry logic for parsing/validation errors
    # This inner function will be retried if parsing/validation fails
    @retry(
        retry=retry_if_exception(_should_retry),
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=2, min=4, max=64),
        before_sleep=_on_retry_before_sleep,
        reraise=True,
    )
    def _call_llm_and_parse() -> DocumentItem:
        """Call LLM and parse response. Raises parsing/validation errors to trigger retry."""
        
        assert os.environ.get("ANTHROPIC_API_KEY") is not None, "ANTHROPIC_API_KEY is not set"
        assert os.environ.get("HELICONE_API_KEY") is not None, "HELICONE_API_KEY is not set"
        
        # Get retry attempt number for cache bypass (increment max_tokens to create different cache key)
        base_max_tokens = 16000
        retry_increment = _get_retry_attempt()
        adjusted_max_tokens = base_max_tokens + retry_increment
        
        # Reset retry attempt for next call
        _set_retry_attempt(0)
        
        if retry_increment > 0:
            logger.info(
                f"Bypassing cache for {item.id} ({item.name}): "
                f"using max_tokens={adjusted_max_tokens} "
                f"(base={base_max_tokens} + {retry_increment})"
            )

        # Initialize Anthropic client with Helicone integration
        client = Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY"),
            base_url="https://anthropic.helicone.ai",
            default_headers={
                "Helicone-Auth": f"Bearer {os.environ.get('HELICONE_API_KEY')}",
                "Helicone-Cache-Enabled": "true",
            },
        )

        # Call Anthropic API with extended thinking
        response = client.messages.create(
            model="claude-sonnet-4-5",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=adjusted_max_tokens,
            thinking={"type": "enabled", "budget_tokens": 2048},
        )

        # Extract response text
        # With extended thinking, response.content contains ThinkingBlock(s) followed by TextBlock(s)
        if not response or not response.content:
            raise ValueError("Invalid LLM response structure")

        # Find the first TextBlock (skip ThinkingBlocks)
        response_text = None
        for block in response.content:
            if hasattr(block, 'text'):
                response_text = block.text
                break
        
        if not response_text:
            raise ValueError("Empty LLM response or no TextBlock found")

        # Parse JSON from response (handle markdown code blocks)
        json_match = re.search(r"```(?:json)?\s*\n(.*?)\n```", response_text, re.DOTALL)
        if json_match:
            json_text = json_match.group(1)
        else:
            json_text = response_text

        # Fix common JSON escape issues
        json_text = fix_json_escapes(json_text)

        # Parse and validate as DocumentItem
        # This will raise ValidationError or JSONDecodeError if parsing fails
        try:
            return DocumentItem.model_validate_json(json_text)
        except ValidationError as e:
            # Log the full JSON that failed validation for debugging
            logger.error(f"ValidationError for {item.id} ({item.name}): {e}")
            logger.error(f"Failed JSON (full):\n{json_text}")
            raise  # Re-raise to trigger retry mechanism

    # Call with retry logic - parsing/validation errors will trigger retries
    try:
        returned_item = _call_llm_and_parse()
    except (json.JSONDecodeError, ValidationError, ValueError) as e:
        # After all retries exhausted, log and return error
        logger.error(f"Failed to parse JSON for {item.id} after retries: {e}")
        logger.debug(f"Last error: {str(e)[:500]}")
        from .draft_types import AgendaAttributes
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append(f"JSON parsing failed after retries: {str(e)}")
        return item
    except Exception as e:
        # Other errors (API errors, etc.)
        logger.error(f"LLM call failed for {item.id}: {e}")
        from .draft_types import AgendaAttributes
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append(f"LLM call failed: {str(e)}")
        return item
    
    # Validate structural fields are unchanged
    validation_errors = []
    if returned_item.id != item.id:
        validation_errors.append(f"ID mismatch: expected {item.id}, got {returned_item.id}")
    if returned_item.name != item.name:
        validation_errors.append(f"Name mismatch: expected {item.name}, got {returned_item.name}")
    if returned_item.header_level != item.header_level:
        validation_errors.append(f"Header level mismatch: expected {item.header_level}, got {returned_item.header_level}")
    if returned_item.parent_id != item.parent_id:
        validation_errors.append(f"Parent ID mismatch: expected {item.parent_id}, got {returned_item.parent_id}")
    if returned_item.item_type != item.item_type:
        validation_errors.append(f"Item type mismatch: expected {item.item_type}, got {returned_item.item_type}")
    if returned_item.content is not None:
        validation_errors.append(f"Content should be null, got: {returned_item.content[:50] if returned_item.content else 'None'}...")
    
    if validation_errors:
        logger.error(f"LLM changed structural fields for {item.id}: {validation_errors}")
        from .draft_types import AgendaAttributes
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.extend(validation_errors)
        return item

    # Validate agenda_attributes content
    if not returned_item.agenda_attributes:
        logger.warning(f"LLM didn't populate agenda_attributes for {item.id}")
        from .draft_types import AgendaAttributes
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append("LLM response missing agenda_attributes")
        return item
    
    attrs = returned_item.agenda_attributes
    
    # Validate see_also IDs exist in agenda_list
    # Note: Items that don't start with "a:" or "sec:" are markdown links and are valid
    valid_agenda_ids = {a["id"] for a in agenda_list}
    if attrs.see_also:
        # Filter to only check items that look like IDs (start with a: or sec:)
        id_refs = [ref for ref in attrs.see_also if ref.startswith(("a:", "sec:"))]
        invalid_see_also = set(id_refs) - valid_agenda_ids
        if invalid_see_also:
            logger.warning(
                f"Invalid see_also IDs for {item.id}: {invalid_see_also}. "
                f"Valid IDs: {sorted(valid_agenda_ids)[:10]}..."
            )
            returned_item.parsing_issues.append(
                f"Invalid see_also IDs: {sorted(invalid_see_also)}"
            )

    # Validate orthodox_problems IDs
    # Note: Items starting with "other:" are allowed as catch-all for non-matching problems
    if attrs.orthodox_problems:
        # Filter out "other:" entries before validation
        id_problems = [p for p in attrs.orthodox_problems if not p.startswith("other:")]
        invalid_problems = [p for p in id_problems if p not in orthodox_problems]
        if invalid_problems:
            logger.warning(
                f"Invalid orthodox_problem IDs for {item.id}: {invalid_problems}"
            )
            returned_item.parsing_issues.append(
                f"Invalid orthodox_problem IDs: {invalid_problems}"
            )

    # Validate target_case ID
    if attrs.target_case and attrs.target_case not in target_cases:
        logger.warning(
            f"Invalid target_case ID for {item.id}: {attrs.target_case}"
        )
        returned_item.parsing_issues.append(f"Invalid target_case ID: {attrs.target_case}")

    # Validate broad_approach ID
    if attrs.broad_approach and attrs.broad_approach not in broad_approaches:
        logger.warning(
            f"Invalid broad_approach ID for {item.id}: {attrs.broad_approach}"
        )
        returned_item.parsing_issues.append(f"Invalid broad_approach ID: {attrs.broad_approach}")

    # Success - return the filled item
    return returned_item


def extract_agendas_parallel(
    agenda_items: list,  # List of DocumentItem objects
    agenda_list: list[dict[str, str]],
    orthodox_problems: dict,
    target_cases: dict,
    broad_approaches: dict,
    max_workers: int = 4,
    progress_callback=None,  # Optional callback(current, total, item_id) for progress updates
) -> list:  # Returns list of DocumentItem objects
    """Extract attributes for multiple agendas in parallel.

    Args:
        agenda_items: List of DocumentItem objects to process
        agenda_list: List of all agendas/sections for see_also resolution
        orthodox_problems: Dictionary of orthodox problem IDs to info
        target_cases: Dictionary of target case IDs to info
        broad_approaches: Dictionary of broad approach IDs to info
        max_workers: Number of parallel workers (default: 4)
        progress_callback: Optional callback function for progress updates

    Returns:
        List of DocumentItem objects with agenda_attributes populated
    """
    from .draft_parser import scrub_markdown
    
    def process_item(item):
        """Process a single item (for ThreadPoolExecutor)."""
        try:
            # Scrub content before passing to LLM
            content_for_llm = scrub_markdown(item.content or "")
            
            # Create input item with content=None
            item_for_llm = item.model_copy()
            item_for_llm.content = None
            
            # Call LLM extraction (returns filled DocumentItem)
            filled_item = extract_agenda_attributes(
                item_for_llm,
                content_for_llm,
                agenda_list,
                orthodox_problems,
                target_cases,
                broad_approaches,
            )
            
            return filled_item, None  # (result, error)
            
        except Exception as e:
            logger.error(f"Failed to extract attributes for {item.id}: {e}")
            item.parsing_issues.append(f"Extraction failed: {str(e)}")
            return item, str(e)  # (original_item_with_error, error_message)

    # Process items in parallel
    filled_items = [None] * len(agenda_items)  # Preserve order
    item_to_idx = {id(item): idx for idx, item in enumerate(agenda_items)}
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_item = {
            executor.submit(process_item, item): item
            for item in agenda_items
        }
        
        # Process completed tasks
        processed = 0
        for future in as_completed(future_to_item):
            if is_shutdown_requested():
                logger.info("Shutdown requested, cancelling remaining tasks...")
                executor.shutdown(wait=False, cancel_futures=True)
                break
            
            processed += 1
            item = future_to_item[future]
            idx = item_to_idx[id(item)]
            
            try:
                filled_item, error = future.result()
                filled_items[idx] = filled_item
                
                # Call progress callback if provided
                if progress_callback:
                    progress_callback(processed, len(agenda_items), item.id, error)
                    
            except Exception as e:
                logger.error(f"Unexpected error processing {item.id}: {e}")
                item.parsing_issues.append(f"Unexpected error: {str(e)}")
                filled_items[idx] = item
                
                if progress_callback:
                    progress_callback(processed, len(agenda_items), item.id, str(e))
    
    return filled_items
