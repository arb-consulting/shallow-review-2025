"""LLM integration utilities with litellm."""

import json
import logging
import os
import re
import threading
from pathlib import Path
from typing import Any, Type, TypeVar

import litellm
from jinja2 import Template
from litellm import completion_cost
from litellm.caching.caching import Cache
from litellm.exceptions import BudgetExceededError
from openai import APIError, RateLimitError
from pydantic import BaseModel, ValidationError
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from .common import DATA_PATH, is_shutdown_requested, request_shutdown
from .stats import get_stats

T = TypeVar("T", bound=BaseModel)
logger = logging.getLogger(__name__)

# Global setup lock
_setup_lock = threading.Lock()
_setup_done = False

# Thread-local storage for tracking retry attempt number for cache bypass
_thread_locals = threading.local()


def _get_retry_attempt() -> int:
    """Get current retry attempt number (0 for first attempt, 1+ for retries)."""
    return getattr(_thread_locals, "retry_attempt", 0)


def _set_retry_attempt(attempt: int) -> None:
    """Set retry attempt number for this thread."""
    _thread_locals.retry_attempt = attempt


def setup_litellm(cache_dir: Path | None = None) -> None:
    """
    Set up litellm with disk-based caching.

    Args:
        cache_dir: Directory for LLM response caching. Defaults to data/.llm_cache
    """
    global _setup_done

    with _setup_lock:
        if _setup_done:
            return

        if cache_dir is None:
            cache_dir = DATA_PATH / ".llm_cache"

        cache_dir.mkdir(exist_ok=True, parents=True)
        litellm.cache = Cache(type="disk", disk_cache_dir=str(cache_dir))  # type: ignore[arg-type]

        # Suppress litellm INFO logs
        litellm.set_verbose = False
        # Also configure litellm logger to WARNING level
        litellm_logger = logging.getLogger("LiteLLM")
        litellm_logger.setLevel(logging.WARNING)

        # Configure Helicone as proxy
        helicone_api_key = os.getenv("HELICONE_API_KEY")
        if helicone_api_key:
            litellm.api_base = "https://anthropic.helicone.ai/v1"
            litellm.headers = {"Helicone-Auth": f"Bearer {helicone_api_key}"}
            logger.info("Helicone proxy configured")
        else:
            logger.warning("HELICONE_API_KEY not set, Helicone proxy disabled")

        _setup_done = True
        logger.info(f"Litellm initialized with cache at {cache_dir}")


def extract_json_from_response(content: str) -> str:
    """
    Extract JSON from LLM response, handling markdown code blocks.

    Args:
        content: Raw response content from LLM

    Returns:
        Extracted JSON string

    Raises:
        ValueError: If no valid JSON found in response
    """
    # Try to find JSON in markdown code blocks first
    json_block_pattern = r"```(?:json)?\s*\n(.*?)\n```"
    matches = re.findall(json_block_pattern, content, re.DOTALL)

    if matches:
        # Return the last JSON block found (usually the main response)
        return matches[-1].strip()

    raise ValueError("No json MD codeblock in answer")


def _should_retry(exception):
    """Determine if we should retry on this exception (but never retry KeyboardInterrupt)."""
    if isinstance(exception, KeyboardInterrupt):
        return False
    # Retry on API errors, rate limits, and parsing/validation errors
    return isinstance(
        exception,
        (
            RateLimitError,
            APIError,
            ValidationError,
            ValueError,  # JSON extraction errors
            json.JSONDecodeError,  # JSON parsing errors
        ),
    )


def _on_retry_before_sleep(retry_state):
    """
    Callback before retry sleep - tracks retry attempt for cache bypass via max_tokens increment.

    When parsing or validation errors occur, we bypass cache by incrementing max_tokens
    by 1, 2, 3, ... starting from the first retry, creating a different cache key for each retry.
    - First attempt (attempt_number=1) fails -> next retry uses increment=1
    - First retry (attempt_number=2) fails -> next retry uses increment=2
    - Second retry (attempt_number=3) fails -> next retry uses increment=3
    """
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


@retry(
    retry=retry_if_exception(_should_retry),
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=4, max=64),
    before_sleep=_on_retry_before_sleep,
    reraise=True,
)
def get_completion(
    template_vars: dict[str, Any],
    model: str = "claude-sonnet-4-5",
    stats_subtree: str | None = None,
    response_type: Type[T] | None = None,
    thinking_budget: int | None = None,
    system_cache_ttl: str | None = "5m",
    message_cache_ttl: str | None = None,
    max_tokens: int = 8000,
    system_prompt_path: Path | str | None = None,
    user_prompt_path: Path | str | None = None,
    system_prompt_template: str | None = None,
    user_prompt_template: str | None = None,
    **kwargs: Any,
) -> T | str:
    """
    Get completion from LLM with automatic prompt loading, stats tracking, and retry logic.

    Uses tenacity for intelligent retries on rate limits, API errors, and validation failures.
    For structured output, extracts JSON from response and validates with Pydantic.

    On parsing/validation errors, bypasses cache by incrementing max_tokens by
    (attempt_number - 1), creating a different cache key for each retry.

    Args:
        template_vars: Variables for Jinja2 template rendering (used for both prompts)
        model: Model name for litellm (e.g., "claude-sonnet-4-5", "gpt-4o")
        stats_subtree: Name of stats subtree for token accounting (e.g., "collection_tokens")
        response_type: Pydantic model type for structured output. If None, returns raw string.
        thinking_budget: Token budget for extended thinking (Anthropic Claude only, default: None)
        system_cache_ttl: Cache TTL for system prompt (default: "5m", can be None, "1h", etc.)
        message_cache_ttl: Cache TTL for user message (default: None, can be "5m", "1h", etc.)
        max_tokens: Maximum tokens for the LLM response
        system_prompt_path: Path to system prompt file (Jinja2 template) - mutually exclusive with system_prompt_template
        user_prompt_path: Path to user prompt file (Jinja2 template) - mutually exclusive with user_prompt_template
        system_prompt_template: System prompt template string (Jinja2) - mutually exclusive with system_prompt_path
        user_prompt_template: User prompt template string (Jinja2) - mutually exclusive with user_prompt_path
        **kwargs: Additional parameters for litellm completion

    Returns:
        Parsed response as Pydantic model instance or raw string

    Raises:
        RateLimitError: If rate limit is exceeded after all retries
        APIError: If API call fails after all retries
        ValidationError: If response validation fails after all retries
        ValueError: If neither path nor template is provided for prompts
    """
    # Ensure litellm is initialized
    setup_litellm()

    # Load or use provided prompt templates
    if system_prompt_template is not None:
        system_template_text = system_prompt_template
    elif system_prompt_path is not None:
        if isinstance(system_prompt_path, str):
            system_prompt_path = Path(system_prompt_path)
        with open(system_prompt_path, "r") as f:
            system_template_text = f.read()
    else:
        raise ValueError("Either system_prompt_path or system_prompt_template must be provided")

    if user_prompt_template is not None:
        user_template_text = user_prompt_template
    elif user_prompt_path is not None:
        if isinstance(user_prompt_path, str):
            user_prompt_path = Path(user_prompt_path)
        with open(user_prompt_path, "r") as f:
            user_template_text = f.read()
    else:
        raise ValueError("Either user_prompt_path or user_prompt_template must be provided")

    # Render both templates with the same variables
    system_template = Template(system_template_text)
    system_prompt = system_template.render(**template_vars)

    user_template = Template(user_template_text)
    user_prompt = user_template.render(**template_vars)

    # Build messages with optional caching
    messages = []

    # System message with optional caching
    if system_cache_ttl:
        messages.append(
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": system_prompt,
                        "cache_control": {"type": "ephemeral", "ttl": system_cache_ttl},
                    }
                ],
            }
        )
    else:
        messages.append({"role": "system", "content": system_prompt})

    # User message with optional caching
    if message_cache_ttl:
        messages.append(
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_prompt,
                        "cache_control": {
                            "type": "ephemeral",
                            "ttl": message_cache_ttl,
                        },
                    }
                ],
            }
        )
    else:
        messages.append({"role": "user", "content": user_prompt})

    # Check for shutdown request before making API call
    if is_shutdown_requested():
        raise KeyboardInterrupt("Shutdown requested before API call")

    # Get retry attempt number for cache bypass (increment max_tokens to create different cache key)
    retry_increment = _get_retry_attempt()
    adjusted_max_tokens = max_tokens + retry_increment
    
    # Reset retry attempt for next call
    _set_retry_attempt(0)

    # Build completion kwargs with request timeout
    # Adjust max_tokens on retries to bypass cache (creates different cache key)
    completion_kwargs = {
        "model": model,
        "messages": messages,
        "caching": True,
        "max_tokens": adjusted_max_tokens,
        "timeout": 120.0,  # 2 minute timeout for API calls
        **kwargs,
    }
    
    if retry_increment > 0:
        logger.info(f"Bypassing cache by using max_tokens={adjusted_max_tokens} (base={max_tokens} + {retry_increment})")

    # Check if model is Anthropic
    model_lower = model.lower()
    is_anthropic = "claude" in model_lower or "anthropic" in model_lower

    if thinking_budget == 0:
        thinking_budget = None

    # Validate thinking_budget usage
    if thinking_budget is not None and not is_anthropic:
        raise ValueError(
            f"thinking_budget parameter is only supported for Anthropic models. "
            f"Got thinking_budget={thinking_budget} for model={model}"
        )

    # Add thinking parameter for Anthropic models
    if is_anthropic and thinking_budget is not None:
        completion_kwargs["thinking"] = {
            "type": "enabled",
            "budget_tokens": thinking_budget,
        }

    # Make API call with litellm
    try:
        response = litellm.completion(**completion_kwargs)
    except (KeyboardInterrupt, BudgetExceededError):
        # Set shutdown flag and re-raise critical exceptions
        request_shutdown()
        raise

    # Log input tokens
    input_tokens = 0
    if response and hasattr(response, "usage") and response.usage:
        input_tokens = getattr(response.usage, "prompt_tokens", 0) or 0
    logger.info(f"LLM call ({model}): {input_tokens} input tokens")

    # Update stats
    _update_stats(response, stats_subtree)

    # Extract content
    content = response.choices[0].message.content

    # Handle structured output if response_type is provided
    if response_type is not None:
        # Extract JSON from response (handles markdown blocks)
        json_str = extract_json_from_response(content)

        # Parse and validate with Pydantic
        json_data = json.loads(json_str)
        try:
            validated_response = response_type.model_validate(json_data)
        except ValidationError as e:
            # Log the full JSON that failed validation for debugging
            logger.error(f"ValidationError: {e}")
            logger.error(f"Failed JSON (full):\n{json_str}")
            raise  # Re-raise to trigger retry mechanism

        return validated_response
    else:
        # Return raw content for unstructured responses
        return content


def _update_stats(response: Any, stats_subtree: str | None) -> None:
    """
    Update statistics from LLM response.

    Args:
        response: Raw LLM response object
        stats_subtree: Name of stats subtree to update
    """
    if not stats_subtree:
        return

    try:
        # Calculate cost and extract token usage
        cost = completion_cost(completion_response=response)
        usage = response.usage

        # Extract thinking/reasoning tokens
        thinking_tokens = 0
        if hasattr(usage, "completion_tokens_details") and usage.completion_tokens_details:
            thinking_tokens = (
                getattr(usage.completion_tokens_details, "reasoning_tokens", 0) or 0
            )

        # Update stats
        stats = get_stats()
        with stats.lock:
            tokens_attr = getattr(stats, stats_subtree, None)
            if tokens_attr is not None:
                tokens_attr.update(
                    cache_read=getattr(usage, "cache_read_input_tokens", 0),
                    cache_write=getattr(usage, "cache_creation_input_tokens", 0),
                    uncached=getattr(usage, "prompt_tokens", 0)
                    - getattr(usage, "cache_read_input_tokens", 0),
                    reasoning=thinking_tokens,
                    output=getattr(usage, "completion_tokens", 0),
                    cost=cost,
                )
    except RuntimeError:
        # No active stats context, skip tracking
        pass
    except Exception as e:
        # Log but don't fail on stats errors
        logger.warning(f"Failed to update stats: {e}")


