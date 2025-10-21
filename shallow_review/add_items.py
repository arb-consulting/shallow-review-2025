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
from .utils import format_error, preprocess_html

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


# Common tracking parameters to remove
TRACKING_PARAMS = {
    # Google Analytics and UTM
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "utm_name", "utm_id", "utm_source_platform", "utm_creative_format",
    "utm_marketing_tactic",
    # Facebook
    "fbclid", "fb_action_ids", "fb_action_types", "fb_source", "fb_ref",
    # Google
    "gclid", "gclsrc", "dclid",
    # Twitter/X
    "twclid", "s", "t",
    # LinkedIn
    "lipi", "licu",
    # Mailchimp
    "mc_cid", "mc_eid",
    # Other common
    "ref", "source", "campaign", "affiliate", "click_id", "referrer",
    # Session/tracking
    "session", "sessionid", "sid", "ssid", "_ga", "_gid",
    # Misc
    "share", "sharesource", "via", "from",
}


def normalize_google_docs_url(url: str) -> str:
    """
    Normalize Google Docs URLs to view mode.
    
    Converts edit/comment URLs to view mode, preserving gid and tab params:
    - .../edit?... → .../view?...
    - .../comment?... → .../view?...
    - Preserves gid (sheet ID) and tab params
    
    Args:
        url: Original URL
        
    Returns:
        Normalized URL (view mode if Google Docs, otherwise unchanged)
    """
    # Match Google Docs URLs
    # docs.google.com/document/d/{id}/edit or /comment
    # docs.google.com/spreadsheets/d/{id}/edit or /comment
    # docs.google.com/presentation/d/{id}/edit or /comment
    
    if "docs.google.com" not in url:
        return url
    
    # Replace /edit or /comment with /view
    url = re.sub(r'/(edit|comment)(\?|#|$)', r'/view\2', url)
    
    return url


def normalize_url(
    url: str,
    remove_tracking: bool = True,
    remove_fragment: bool = True,
    normalize_trailing_slash: bool = True,
) -> str:
    """
    Normalize URLs for deduplication.
    
    Performs:
    - Convert arXiv PDF → abstract page
    - Convert Google Docs edit/comment → view (preserve gid, tab)
    - Remove tracking parameters (utm_*, fbclid, etc.)
    - Remove fragments (#anchor)
    - Normalize trailing slashes
    
    Args:
        url: Original URL
        remove_tracking: Remove tracking query parameters
        remove_fragment: Remove fragment (#anchor)
        normalize_trailing_slash: Add trailing slash to directory-like URLs
        
    Returns:
        Normalized URL
    """
    # First: arXiv normalization (specific handling)
    url = normalize_arxiv_url(url)
    
    # Second: Google Docs normalization
    url = normalize_google_docs_url(url)
    
    # Parse URL
    parsed = urlparse(url)
    
    # Remove fragment if requested
    fragment = "" if remove_fragment else parsed.fragment
    
    # Process query parameters
    if remove_tracking and parsed.query:
        # Parse query string
        params = parse_qs(parsed.query, keep_blank_values=True)
        
        # Filter out tracking parameters
        filtered_params = {
            k: v for k, v in params.items()
            if k.lower() not in TRACKING_PARAMS
        }
        
        # Rebuild query string
        if filtered_params:
            # Flatten lists and sort for consistency
            sorted_params = sorted(
                (k, v[0] if isinstance(v, list) and len(v) == 1 else v)
                for k, v in filtered_params.items()
            )
            query = urlencode(sorted_params, doseq=True)
        else:
            query = ""
    else:
        query = parsed.query
    
    # Normalize path
    path = parsed.path
    if normalize_trailing_slash and path and not path.endswith('/'):
        # Add trailing slash if it looks like a directory (no file extension)
        # Don't add to root or if it has an extension
        if path != "/" and "." not in path.split("/")[-1]:
            # Only for paths that look like directories
            # Actually, this can cause issues - skip for now
            pass
    
    # Rebuild URL
    normalized = urlunparse((
        parsed.scheme,
        parsed.netloc,
        path,
        parsed.params,
        query,
        fragment,
    ))
    
    if normalized != url:
        logger.debug(f"Normalized URL: {url} → {normalized}")
    
    return normalized


def normalize_arxiv_url(url: str) -> str:
    """
    Normalize arXiv URLs to abstract page format.
    
    Converts PDF URLs to HTML abstract pages:
    - https://arxiv.org/pdf/2404.12345.pdf → https://arxiv.org/abs/2404.12345
    - https://arxiv.org/pdf/2404.12345v2.pdf → https://arxiv.org/abs/2404.12345
    
    Args:
        url: Original URL
        
    Returns:
        Normalized URL (abstract page if arXiv, otherwise unchanged)
    """
    # Match arXiv PDF URLs
    # Pattern: arxiv.org/pdf/YYMM.NNNNN[vN].pdf
    arxiv_pdf_pattern = r"(https?://arxiv\.org)/pdf/(\d{4}\.\d{4,5})(v\d+)?\.pdf"
    match = re.match(arxiv_pdf_pattern, url)
    
    if match:
        base_url = match.group(1)
        paper_id = match.group(2)
        # Convert to abstract page (ignore version)
        normalized = f"{base_url}/abs/{paper_id}"
        logger.debug(f"Normalized arXiv URL: {url} → {normalized}")
        return normalized
    
    return url


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
            max_tokens=500,  # Detection is short output
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


def check_url_exists(url: str) -> tuple[bool, str | None]:
    """
    Check if URL already exists in collect or classify tables.
    
    Args:
        url: URL to check
        
    Returns:
        Tuple of (exists, phase) where phase is "collect", "classify", or None
    """
    from .data_db import get_data_db
    
    db = get_data_db()
    
    # Check collect table
    cursor = db.execute("SELECT 1 FROM collect WHERE url = ?", (url,))
    if cursor.fetchone():
        return (True, "collect")
    
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

