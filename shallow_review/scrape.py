"""Web scraping utilities with playwright."""

import hashlib
import logging
import sqlite3
import threading
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import Browser, sync_playwright

from .common import DATA_PATH
from .stats import get_stats
from .utils import smart_open

logger = logging.getLogger(__name__)

# Global database connection (lazy singleton)
_scrape_db: sqlite3.Connection | None = None
_scrape_db_lock = threading.Lock()


def get_scrape_db() -> sqlite3.Connection:
    """
    Get or create the scraping database connection (lazy singleton).

    Schema:
        scraped (
            url_hash TEXT PRIMARY KEY,
            url TEXT NOT NULL,
            kind TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            status_code INTEGER,
            content_path TEXT,  -- relative path to .html.zst file
            error TEXT
        )

    Returns:
        SQLite connection
    """
    global _scrape_db

    with _scrape_db_lock:
        if _scrape_db is None:
            db_path = DATA_PATH / "scrape.db"
            _scrape_db = sqlite3.connect(str(db_path), check_same_thread=False)
            _scrape_db.row_factory = sqlite3.Row

            # Create tables and indexes
            _scrape_db.execute(
                """
                CREATE TABLE IF NOT EXISTS scraped (
                    url_hash TEXT PRIMARY KEY,
                    url TEXT NOT NULL,
                    kind TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    status_code INTEGER,
                    content_path TEXT,
                    error TEXT
                )
                """
            )

            # Indexes for common queries
            _scrape_db.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_scraped_kind 
                ON scraped(kind)
                """
            )

            _scrape_db.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_scraped_timestamp 
                ON scraped(timestamp)
                """
            )

            _scrape_db.commit()
            logger.info(f"Initialized scraping database at {db_path}")

        return _scrape_db


def _compute_url_hash(url: str, kind: str) -> str:
    """
    Compute hash for URL and kind combination.

    Args:
        url: URL to hash
        kind: Kind/context of scrape

    Returns:
        Hex digest of hash
    """
    # Include kind in hash to allow same URL with different contexts
    hash_input = f"{kind}:{url}".encode("utf-8")
    return hashlib.sha256(hash_input).hexdigest()


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
    cache_dir: Path | None = None,
    headless: bool = True,
    wait_for: str = "networkidle",
    scroll: bool = True,
) -> Path:
    """
    Scrape URL with playwright, cache to data/scraped/<hash>.html.zst

    Caches results in SQLite database and file system. Subsequent calls with
    same URL and kind will return cached path without re-scraping.

    Args:
        url: URL to scrape
        kind: Kind/context of scrape (e.g., "incident", "report")
        cache_dir: Directory for cached HTML files. Defaults to data/scraped/
        headless: Run browser in headless mode
        wait_for: Playwright wait condition ("networkidle", "load", "domcontentloaded")
        scroll: Scroll page to trigger lazy loading

    Returns:
        Path to cached .html.zst file

    Raises:
        RuntimeError: If scraping fails after retries
    """
    if cache_dir is None:
        cache_dir = DATA_PATH / "scraped"

    cache_dir.mkdir(parents=True, exist_ok=True)

    # Compute hash for this URL+kind combination
    url_hash = _compute_url_hash(url, kind)

    # Check database cache
    db = get_scrape_db()
    cursor = db.execute(
        "SELECT content_path, status_code, error FROM scraped WHERE url_hash = ?",
        (url_hash,),
    )
    row = cursor.fetchone()

    if row is not None:
        content_path = row["content_path"]
        status_code = row["status_code"]
        error = row["error"]

        if content_path:
            # Have cached content
            full_path = DATA_PATH / content_path
            if full_path.exists():
                # Update stats
                try:
                    stats = get_stats()
                    with stats.lock:
                        stats.scraped_pages.cached.add(url_hash)
                except RuntimeError:
                    pass

                logger.debug(f"Using cached scrape for {url} (kind={kind})")
                return full_path

        if error:
            # Have cached error
            logger.warning(f"Using cached error for {url} (kind={kind}): {error}")
            raise RuntimeError(f"Cached scraping error: {error}")

    # Need to scrape
    logger.info(f"Scraping {url} (kind={kind})")

    try:
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

        # Save to file
        relative_path = f"scraped/{url_hash}.html.zst"
        full_path = DATA_PATH / relative_path

        with smart_open(full_path, "wt", encoding="utf-8") as f:
            f.write(content)

        # Update database
        timestamp = datetime.now(timezone.utc).isoformat()
        db.execute(
            """
            INSERT OR REPLACE INTO scraped 
            (url_hash, url, kind, timestamp, status_code, content_path, error)
            VALUES (?, ?, ?, ?, ?, ?, NULL)
            """,
            (url_hash, url, kind, timestamp, status_code, relative_path),
        )
        db.commit()

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.scraped_pages.new.add(url_hash)
        except RuntimeError:
            pass

        logger.info(f"Successfully scraped {url} (kind={kind}, status={status_code})")
        return full_path

    except Exception as e:
        error_msg = str(e)
        logger.error(f"Failed to scrape {url} (kind={kind}): {error_msg}")

        # Cache error in database
        timestamp = datetime.now(timezone.utc).isoformat()
        db.execute(
            """
            INSERT OR REPLACE INTO scraped 
            (url_hash, url, kind, timestamp, status_code, content_path, error)
            VALUES (?, ?, ?, ?, NULL, NULL, ?)
            """,
            (url_hash, url, kind, timestamp, error_msg),
        )
        db.commit()

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.scraped_pages.errors[url_hash] = error_msg
        except RuntimeError:
            pass

        raise RuntimeError(f"Scraping failed: {error_msg}") from e


