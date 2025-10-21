"""Web scraping utilities with playwright."""

import hashlib
import logging
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import IO, Any, Literal

from playwright.sync_api import Browser, sync_playwright

from .common import SCRAPED_PATH
from .data_db import get_data_db
from .stats import get_stats
from .utils import smart_open

logger = logging.getLogger(__name__)

# Global lock for Playwright operations
# Playwright's sync API uses greenlets which are not thread-safe.
# This lock ensures only ONE thread scrapes at a time, preventing
# "browser has been closed" errors from greenlet context switching.
# This is acceptable since:
# - Scraping is I/O-bound (network waits)
# - Most scrapes hit cache (instant)
# - LLM calls still run in parallel (the expensive part)
_playwright_lock = threading.Lock()


def _compute_url_hash(url: str) -> str:
    """
    Compute hash for URL.

    Args:
        url: URL to hash

    Returns:
        Hex digest of hash
    """
    return hashlib.sha256(url.encode("utf-8")).hexdigest()


def get_scrape_path(url: str) -> Path:
    """
    Get the file path for a scraped URL.

    Args:
        url: URL to get path for

    Returns:
        Path to .html.zst file
    """
    url_hash = _compute_url_hash(url)
    return SCRAPED_PATH / f"{url_hash}.html.zst"


def open_scraped(
    url: str,
    mode: Literal["rt", "wt", "rb", "wb"],
    encoding: str | None = None,
    **kwargs: Any,
) -> IO:
    """
    Open a scraped file with automatic compression.

    Args:
        url: URL to open scraped content for
        mode: Open mode (rt/wt for text, rb/wb for binary)
        encoding: Text encoding (for text modes)
        **kwargs: Additional args passed to smart_open()

    Returns:
        File-like object
    """
    path = get_scrape_path(url)
    return smart_open(path, mode, encoding=encoding, **kwargs)


def get_browser_context(browser: Browser, **kwargs):
    """
    Create browser context with realistic settings.

    Args:
        browser: Playwright browser instance
        **kwargs: Additional context options

    Returns:
        Browser context
    """
    # Realistic user agent
    default_kwargs = {
        "user_agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "viewport": {"width": 1920, "height": 1080},
        "locale": "en-US",
        "timezone_id": "America/New_York",
    }

    # Merge with user-provided kwargs
    default_kwargs.update(kwargs)

    return browser.new_context(**default_kwargs)


def compute_scrape(
    url: str,
    kind: str,
    headless: bool = True,
    wait_for: str = "networkidle",
    scroll: bool = True,
) -> Path:
    """
    Scrape URL with playwright, cache to data/scraped/<hash>.html.zst

    Caches results in SQLite database and file system. Subsequent calls with
    same URL will return cached path without re-scraping.

    Args:
        url: URL to scrape
        kind: Kind/context of scrape (e.g., "incident", "report")
        headless: Run browser in headless mode
        wait_for: Playwright wait condition ("networkidle", "load", "domcontentloaded")
        scroll: Scroll page to trigger lazy loading

    Returns:
        Path to cached .html.zst file

    Raises:
        RuntimeError: If scraping fails after retries
    """
    # Compute hash and get path
    url_hash = _compute_url_hash(url)
    scrape_path = get_scrape_path(url)

    # Check database cache
    db = get_data_db()
    cursor = db.execute(
        "SELECT status_code, error FROM scrape WHERE url = ?",
        (url,),
    )
    row = cursor.fetchone()

    if row is not None:
        status_code = row["status_code"]
        error = row["error"]

        if error:
            # Have cached error
            logger.warning(f"Using cached error for {url} (kind={kind}): {error}")
            # Update stats
            try:
                stats = get_stats()
                with stats.lock:
                    stats.scraped_pages.errors[url] = error
            except RuntimeError:
                pass
            raise RuntimeError(f"Cached scraping error: {error}")
        
        # Have cached successful scrape
        if scrape_path.exists():
            # Update stats
            try:
                stats = get_stats()
                with stats.lock:
                    stats.scraped_pages.cached.add(url)
            except RuntimeError:
                pass

            logger.debug(f"Using cached scrape for {url} (kind={kind})")
            return scrape_path

    # Need to scrape
    logger.info(f"Scraping {url} (kind={kind})")
    
    import json
    import time
    from .utils import count_tokens, preprocess_html

    scrape_start = time.time()
    
    try:
        # Lock around Playwright to prevent thread-safety issues
        # Playwright sync API is not fully thread-safe when creating browsers concurrently
        with _playwright_lock:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=headless)
                context = get_browser_context(browser)
                page = context.new_page()

                # Navigate to URL
                response = page.goto(url, wait_until=wait_for, timeout=60000)
                status_code = response.status if response else 0

                # Scroll to trigger lazy loading
                if scroll:
                    page.evaluate(
                        """
                        () => {
                            window.scrollTo(0, document.body.scrollHeight / 2);
                        }
                        """
                    )
                    page.wait_for_timeout(500)
                    page.evaluate("() => { window.scrollTo(0, document.body.scrollHeight); }")
                    page.wait_for_timeout(500)

                # Get page content
                content = page.content()

                browser.close()

        scrape_duration = time.time() - scrape_start

        # Calculate metrics
        size_full = len(content.encode('utf-8'))
        tokens_full = count_tokens(content)
        
        # Preprocess to get stripped HTML and token count
        stripped_html = None
        try:
            stripped_html, _ = preprocess_html(content, "gpt-4")
            tokens_stripped = count_tokens(stripped_html)
        except Exception:
            # If preprocessing fails, use full HTML metrics
            tokens_stripped = tokens_full

        # Save to file and update DB atomically with transaction
        try:
            # Write full HTML file first
            with open_scraped(url, "wt", encoding="utf-8") as f:
                f.write(content)
            
            # Save stripped HTML for debugging (uncompressed)
            if stripped_html:
                stripped_path = SCRAPED_PATH / f"{url_hash}-stripped.html"
                with open(stripped_path, "w", encoding="utf-8") as f:
                    f.write(stripped_html)
            
            # Get compressed file size
            size_compressed = scrape_path.stat().st_size if scrape_path.exists() else 0

            # Build data JSON
            data_json = json.dumps({
                "size_full": size_full,
                "size_compressed": size_compressed,
                "tokens_full": tokens_full,
                "tokens_stripped": tokens_stripped,
                "scrape_duration": round(scrape_duration, 2),
            })

            # Update database in transaction
            timestamp = datetime.now(timezone.utc).isoformat()
            db.execute("BEGIN TRANSACTION")
            db.execute(
                """
                INSERT OR REPLACE INTO scrape 
                (url, url_hash, kind, timestamp, status_code, error, data)
                VALUES (?, ?, ?, ?, ?, NULL, ?)
                """,
                (url, url_hash, kind, timestamp, status_code, data_json),
            )
            db.commit()
        except Exception as e:
            db.rollback()
            # Clean up file if DB update failed
            if scrape_path.exists():
                scrape_path.unlink()
            raise RuntimeError(f"Failed to save scrape atomically: {e}") from e

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.scraped_pages.new.add(url)
        except RuntimeError:
            pass

        logger.info(f"Successfully scraped {url} (kind={kind}, status={status_code})")
        return scrape_path

    except Exception as e:
        error_msg = str(e)
        logger.error(f"Failed to scrape {url} (kind={kind}): {error_msg}")

        # Cache error in database
        timestamp = datetime.now(timezone.utc).isoformat()
        db.execute(
            """
            INSERT OR REPLACE INTO scrape 
            (url, url_hash, kind, timestamp, status_code, error)
            VALUES (?, ?, ?, ?, NULL, ?)
            """,
            (url, url_hash, kind, timestamp, error_msg),
        )
        db.commit()

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.scraped_pages.errors[url] = error_msg
        except RuntimeError:
            pass

        raise RuntimeError(f"Scraping failed: {error_msg}") from e


