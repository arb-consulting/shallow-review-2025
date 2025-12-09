"""Draft document processing: extract structured metadata from research agendas.

Provides parallelized LLM extraction of agenda attributes from draft markdown documents.
"""

import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml
from jinja2 import Template
from pydantic import ValidationError

from .common import PROMPTS_PATH, is_shutdown_requested

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

    # Call LLM
    try:
        response = completion(
            model="claude-sonnet-4-5",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=8000,  # Increased for full DocumentItem output
            reasoning_effort="medium",
        )
    except Exception as e:
        logger.error(f"LLM call failed for {item.id}: {e}")
        from .draft_types import AgendaAttributes
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append(f"LLM call failed: {str(e)}")
        return item

    # Extract response
    if not response or not response.choices or not response.choices[0].message:
        logger.error(f"Invalid LLM response for {item.id}")
        from .draft_types import AgendaAttributes
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append("Invalid LLM response structure")
        return item

    response_text = response.choices[0].message.content
    if not response_text:
        logger.error(f"Empty LLM response for {item.id}")
        from .draft_types import AgendaAttributes
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append("Empty LLM response")
        return item

    # Parse JSON from response (handle markdown code blocks)
    import re
    json_match = re.search(r"```(?:json)?\s*\n(.*?)\n```", response_text, re.DOTALL)
    if json_match:
        json_text = json_match.group(1)
    else:
        json_text = response_text
    
    # Fix common JSON escape issues from LLM output
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
    
    json_text = fix_json_escapes(json_text)

    # Parse as DocumentItem
    from .draft_types import DocumentItem
    try:
        returned_item = DocumentItem.model_validate_json(json_text)
    except (json.JSONDecodeError, ValidationError) as e:
        logger.error(f"Failed to parse JSON for {item.id}: {e}")
        logger.debug(f"Response text: {response_text[:500]}")
        from .draft_types import AgendaAttributes
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append(f"JSON parsing failed: {str(e)}")
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
