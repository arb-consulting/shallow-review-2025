"""Web scraping utilities with playwright and selenium."""

import logging
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import IO, Any, Literal

from playwright.sync_api import Browser, sync_playwright

from .common import SCRAPED_PATH
from .data_db import data_db_locked
from .stats import get_stats
from .utils import normalize_url, smart_open, url_hash, url_hash_short

logger = logging.getLogger(__name__)

# Scraping backend selection
# Set to True to use Selenium (thread-safe), False for Playwright (faster but needs workers=1)
USE_SELENIUM = True

# Save stripped HTML for debugging (uncompressed)
# Set to True to save preprocessed HTML as *-stripped.html files
SAVE_STRIPPED_HTML = False

# Global lock for Playwright operations (only used if USE_SELENIUM=False)
# Playwright's sync API uses greenlets which are not thread-safe.
# This lock ensures only ONE thread scrapes at a time, preventing
# "browser has been closed" errors from greenlet context switching.
_playwright_lock = threading.Lock()

# Lock for Selenium WebDriver creation (prevents ChromeDriver resource exhaustion)
# Creating too many WebDriver instances simultaneously can crash ChromeDriver
# Lock only driver creation, not the whole scraping (scraping can run in parallel)
_selenium_create_lock = threading.Lock()


def get_scrape_path(url: str) -> Path:
    """
    Get the file path for a scraped URL.

    Args:
        url: URL to get path for (will be normalized)

    Returns:
        Path to .html.zst file
    """
    hash_value = url_hash(url)
    return SCRAPED_PATH / f"{hash_value}.html.zst"


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


def scrape_playwright(url: str, headless: bool = True, wait_for: str = "networkidle", scroll: bool = True) -> tuple[str, int]:
    """
    Scrape URL using Playwright.
    
    NOT thread-safe - caller must use _playwright_lock.
    
    Args:
        url: URL to scrape
        headless: Run browser in headless mode
        wait_for: Wait condition ("networkidle", "load", "domcontentloaded")
        scroll: Scroll page to trigger lazy loading
        
    Returns:
        Tuple of (html_content, status_code)
        
    Raises:
        Exception: If scraping fails
    """
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
    
    return (content, status_code)


def scrape_selenium(url: str, headless: bool = True, scroll: bool = True) -> tuple[str, int]:
    """
    Scrape URL using Selenium.
    
    Thread-safe - each call creates its own WebDriver instance.
    
    Args:
        url: URL to scrape
        headless: Run browser in headless mode
        scroll: Scroll page to trigger lazy loading
        
    Returns:
        Tuple of (html_content, status_code)
        
    Raises:
        Exception: If scraping fails
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    import time
    
    # Configure Chrome options
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    # Realistic user agent
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    
    # Create driver with lock to prevent ChromeDriver resource exhaustion
    # Lock only creation, not the whole scraping (allows parallel scraping)
    with _selenium_create_lock:
        driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Navigate to URL
        driver.get(url)
        
        # Wait for page to be ready
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        
        # Additional wait for network idle (approximate)
        time.sleep(1)
        
        # Scroll to trigger lazy loading
        if scroll:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
            time.sleep(0.5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
        
        # Get page content
        content = driver.page_source
        
        # Selenium doesn't provide status codes directly
        # Assume 200 if we successfully loaded the page
        status_code = 200
        
        # Try to detect errors from page title/content
        title = driver.title.lower()
        if "404" in title or "not found" in title:
            status_code = 404
        elif "403" in title or "forbidden" in title:
            status_code = 403
        elif "500" in title or "error" in title:
            status_code = 500
            
        return (content, status_code)
        
    finally:
        driver.quit()


def compute_scrape(
    url: str,
    kind: str,
    headless: bool = True,
    wait_for: str = "networkidle",
    scroll: bool = True,
) -> Path:
    """
    Scrape URL and cache to data/scraped/<hash>.html.zst
    
    Backend selection via USE_SELENIUM constant:
    - Selenium: Thread-safe, slower, realistic browser (USE_SELENIUM=True)
    - Playwright: Faster, needs workers=1 due to greenlets (USE_SELENIUM=False)

    Caches results in SQLite database and file system. Subsequent calls with
    same URL will return cached path without re-scraping.

    Args:
        url: URL to scrape
        kind: Kind/context of scrape (e.g., "collect", "classify")
        headless: Run browser in headless mode
        wait_for: Wait condition for Playwright ("networkidle", "load", "domcontentloaded")
        scroll: Scroll page to trigger lazy loading

    Returns:
        Path to cached .html.zst file

    Raises:
        RuntimeError: If scraping fails
    """
    # Normalize URL for consistent handling
    url = normalize_url(url)
    
    # Compute hash and get path
    hash_value = url_hash(url)
    hash_short = url_hash_short(url)
    scrape_path = get_scrape_path(url)

    # Check database cache
    with data_db_locked() as db:
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
    backend = "selenium" if USE_SELENIUM else "playwright"
    logger.info(f"Scraping {url} (kind={kind}, backend={backend})")
    
    import json
    import time
    from .utils import count_tokens, preprocess_html

    scrape_start = time.time()
    
    try:
        if USE_SELENIUM:
            # Use Selenium (thread-safe)
            content, status_code = scrape_selenium(url, headless=headless, scroll=scroll)
        else:
            # Use Playwright (needs lock)
            with _playwright_lock:
                content, status_code = scrape_playwright(url, headless=headless, wait_for=wait_for, scroll=scroll)

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
            
            # Save stripped HTML for debugging (uncompressed) - optional
            if SAVE_STRIPPED_HTML and stripped_html:
                stripped_path = SCRAPED_PATH / f"{hash_value}-stripped.html"
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
            with data_db_locked() as db:
                db.execute("BEGIN TRANSACTION")
                try:
                    db.execute(
                        """
                        INSERT OR REPLACE INTO scrape 
                        (url, url_hash, url_hash_short, kind, timestamp, status_code, error, data)
                        VALUES (?, ?, ?, ?, ?, ?, NULL, ?)
                        """,
                        (url, hash_value, hash_short, kind, timestamp, status_code, data_json),
                    )
                    db.commit()
                except Exception:
                    db.rollback()
                    raise
        except Exception as e:
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
        with data_db_locked() as db:
            db.execute(
                """
                INSERT OR REPLACE INTO scrape 
                (url, url_hash, url_hash_short, kind, timestamp, status_code, error)
                VALUES (?, ?, ?, ?, ?, NULL, ?)
                """,
                (url, hash_value, hash_short, kind, timestamp, error_msg),
            )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.scraped_pages.errors[url] = error_msg
        except RuntimeError:
            pass

        raise RuntimeError(f"Scraping failed: {error_msg}") from e


