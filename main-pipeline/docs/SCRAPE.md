# Scrape Process

Minimal documentation for the scraping infrastructure.

## Purpose

Scraping fetches and caches HTML content for later processing. All scrapes are cached indefinitely to avoid repeated network requests.

## Key Functions

**`compute_scrape(url, kind, wait_for="load")`**
- Scrapes URL with playwright
- Stores HTML in `data/scraped/<hash>.html.zst` (Zstandard compression level 15)
- Records metadata in `scrape` table
- Returns path to scraped file
- Raises on scrape failure

**`get_scrape_path(url)`**
- Returns pathlib.Path to scraped file (may not exist yet)

**`open_scraped(url, mode)`**
- Opens scraped file with smart_open (handles .zst compression)

## Scrape Behavior

- **User agent**: Realistic browser UA with playwright
- **Wait strategy**: Configurable wait_for parameter ("load", "networkidle", etc.)
- **Scrolling**: Scrolls page to trigger lazy-loaded content
- **Caching**: Both successful and failed scrapes cached
- **Deduplication**: One scrape per URL (regardless of `kind` parameter)
- **kind parameter**: Stored in DB for context but doesn't affect caching

## Error Handling

- Network errors, timeouts: Cached as `scrape_error`
- HTTP errors (4xx, 5xx): Cached with status_code
- Errors NOT retried automatically (cache prevents re-scraping)

## Database Schema

See `docs/DATA.md` for scrape table schema.

