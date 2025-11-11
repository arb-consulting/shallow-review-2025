"""Smart URL adding: auto-detect collection sources vs single content."""

import logging
import re
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

import yaml
from pydantic import BaseModel, Field

from .classify import add_classify_candidate
from .collect import add_collect_source
from .common import PROMPTS_PATH
from .llm import get_completion
from .scrape import compute_scrape, open_scraped
from .utils import format_error, normalize_url, preprocess_html

logger = logging.getLogger(__name__)


class URLTypeDetection(BaseModel):
    """Result of URL type detection."""

    url_type: str = Field(description="Either 'collection_source' or 'single_content'")
    confidence: float = Field(ge=0.0, le=1.0)
    reason: str


def is_valid_url(url: str) -> bool:
    """
    Check if a string is a valid URL.
    
    Args:
        url: String to validate
        
    Returns:
        True if valid URL, False otherwise
    """
    try:
        parsed = urlparse(url)
        # Must have scheme and netloc
        return bool(parsed.scheme) and bool(parsed.netloc)
    except Exception:
        return False


def check_url_exists(url: str) -> tuple[bool, str | None]:
    """
    Check if URL already exists in collect or classify tables.
    
    Args:
        url: URL to check (should be normalized before calling)
        
    Returns:
        Tuple of (exists, phase) where:
        - exists: True if URL found in any table
        - phase: "collect" or "classify" if found, None if not found
    """
    from .data_db import data_db_locked

    with data_db_locked() as db:
        # Check collect table
        cursor = db.execute("SELECT 1 FROM collect WHERE url = ?", (url,))
        if cursor.fetchone():
            return (True, "collect")

        # Check classify table
        cursor = db.execute("SELECT 1 FROM classify WHERE url = ?", (url,))
        if cursor.fetchone():
            return (True, "classify")

    return (False, None)


def detect_url_type(url: str, model: str = "anthropic/claude-haiku-4-5") -> URLTypeDetection:
    """
    Detect if URL is a collection source or single content.
    
    Uses LLM to analyze page content and determine type. Scrapes page,
    strips HTML, and sends preview to LLM.
    
    Args:
        url: URL to analyze
        model: Model to use for detection (default: Haiku for speed/cost)
        
    Returns:
        URLTypeDetection with type, confidence, and reasoning
        
    Raises:
        RuntimeError: If scraping or detection fails
    """
    # Step 1: Scrape the page
    try:
        compute_scrape(url, kind="add_detect", headless=True)
    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed to scrape {url} for type detection: {error_msg}")
        raise RuntimeError(f"Scrape error: {e}") from e

    # Step 2: Read and preprocess HTML
    try:
        with open_scraped(url, "rt", encoding="utf-8") as f:
            raw_html = f.read()

        cleaned_html, preprocessing_stats = preprocess_html(raw_html, model)
        
        # Take a preview (first ~10k chars) for quick detection
        # This keeps token usage low while providing enough context
        content_preview = cleaned_html[:10000]
        if len(cleaned_html) > 10000:
            content_preview += "\n\n... [content truncated for preview] ..."

    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed to preprocess HTML for {url}: {error_msg}")
        raise RuntimeError(f"Preprocessing error: {e}") from e

    # Step 3: Run LLM detection (fast model, no caching needed)
    try:
        # Load prompts
        prompts_file = PROMPTS_PATH / "add_items.yaml"
        with open(prompts_file) as f:
            prompts = yaml.safe_load(f)

        # Call LLM
        result = get_completion(
            template_vars={"url": url, "content_preview": content_preview},
            model=model,
            stats_subtree="add_detect_tokens",
            response_type=URLTypeDetection,
            system_prompt_template=prompts["detect_url_type"]["system"],
            user_prompt_template=prompts["detect_url_type"]["user"],
            system_cache_ttl=None,  # No caching for detection (fast, changes frequently)
            thinking_budget=1024,
            max_tokens=2000,  # Detection is short output
        )

        logger.info(
            f"Detected URL type for {url}: {result.url_type} "
            f"(confidence: {result.confidence:.2f}, reason: {result.reason})"
        )

        return result

    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed URL type detection for {url}: {error_msg}")
        raise RuntimeError(f"LLM detection error: {e}") from e


def check_url_exists(url: str, phase: str | None = None) -> tuple[bool, str | None]:
    """
    Check if URL already exists in collect or classify tables.
    
    Args:
        url: URL to check
        phase: If specified ("collect" or "classify"), only check that table.
               If None (default), check both tables.
        
    Returns:
        Tuple of (exists, phase) where phase is "collect", "classify", or None
    """
    from .data_db import data_db_locked
    
    with data_db_locked() as db:
        if phase is None or phase == "collect":
            # Check collect table
            cursor = db.execute("SELECT 1 FROM collect WHERE url = ?", (url,))
            if cursor.fetchone():
                return (True, "collect")
        
        if phase is None or phase == "classify":
            # Check classify table
            cursor = db.execute("SELECT 1 FROM classify WHERE url = ?", (url,))
            if cursor.fetchone():
                return (True, "classify")
        
        return (False, None)


def add_item_auto(
    url: str,
    source: str | None = None,
    model: str = "anthropic/claude-haiku-4-5",
) -> tuple[str, str, bool]:
    """
    Automatically add URL to appropriate table (collect or classify).
    
    Checks if URL exists first, normalizes URLs (arXiv, tracking params, etc.),
    detects type using LLM, and adds to correct table.
    
    Args:
        url: URL to add
        source: Optional source label for tracking
        model: Model for type detection (default: Haiku for speed)
        
    Returns:
        Tuple of (phase, normalized_url, is_new) where:
        - phase: "collect" or "classify"
        - normalized_url: The normalized URL
        - is_new: True if added, False if already existed
        
    Raises:
        RuntimeError: If detection or adding fails
    """
    # Step 1: Normalize URL (arXiv, tracking params, fragments)
    normalized_url = normalize_url(url)
    
    # Step 2: Check if URL already exists in either table
    exists, existing_phase = check_url_exists(normalized_url)
    if exists:
        logger.info(f"URL already exists in {existing_phase}: {normalized_url}")
        return (existing_phase, normalized_url, False)
    
    # Step 3: Detect URL type (only if new)
    detection = detect_url_type(normalized_url, model=model)
    
    # Step 4: Add to appropriate table
    if detection.url_type == "collection_source":
        # Add to collect table
        added = add_collect_source(normalized_url, source=source)
        phase = "collect"
        logger.info(
            f"Added to collect: {normalized_url} "
            f"({'new' if added else 'already exists'}) - {detection.reason}"
        )
    elif detection.url_type == "single_content":
        # Add to classify table
        added = add_classify_candidate(
            url=normalized_url,
            source=source or "manual",
            source_url=None,
            collect_relevancy=None,
        )
        phase = "classify"
        logger.info(
            f"Added to classify: {normalized_url} "
            f"({'new' if added else 'already exists'}) - {detection.reason}"
        )
    else:
        raise RuntimeError(f"Invalid url_type from detection: {detection.url_type}")
    
    return (phase, normalized_url, added)

