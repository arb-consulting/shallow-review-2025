"""Collection phase: gather links from AI safety/alignment aggregator pages."""

import json
import logging
import sqlite3
from datetime import datetime, timezone

import yaml
from pydantic import BaseModel, Field

from .common import (
    PROMPTS_PATH,
    CollectStatus,
    RunCollectConfig,
    SourceKind,
)
from .data_db import data_db_locked
from .llm import get_completion
from .scrape import compute_scrape, open_scraped
from .stats import get_stats
from .utils import normalize_url, url_hash, url_hash_short
from .utils import format_error, preprocess_html

logger = logging.getLogger(__name__)


# Pydantic models for LLM responses
class ExtractedLink(BaseModel):
    """A link extracted from a collection page."""

    url: str
    link_text: str
    context: str
    ai_safety_relevancy: float = Field(ge=0.0, le=1.0)


class CollectionResult(BaseModel):
    """Result of collecting from a source page."""

    title: str
    kind: SourceKind
    collection_quality_score: float = Field(ge=0.0, le=1.0)
    comments: str
    links: list[ExtractedLink] = Field(default_factory=list)
    tokens_full: int | None = None  # Full HTML token count (before stripping)
    tokens_stripped: int | None = None  # Stripped HTML token count (after stripping)


def add_collect_source(url: str, source: str | None = None) -> bool:
    """
    Add a URL to collect from.

    Args:
        url: URL of source page (will be normalized)
        source: Optional user-supplied source label

    Returns:
        True if added (new), False if already exists
    """
    # Normalize URL for consistent handling
    url = normalize_url(url)
    
    timestamp = datetime.now(timezone.utc).isoformat()
    hash_value = url_hash(url)
    hash_short = url_hash_short(url)

    try:
        with data_db_locked() as db:
            db.execute(
                """
                INSERT INTO collect (url, url_hash, url_hash_short, status, source, added_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (url, hash_value, hash_short, CollectStatus.NEW.value, source, timestamp),
            )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.collect_sources.new.add(url)
        except RuntimeError:
            pass

        logger.info(f"Added collect source: {url}")
        return True

    except sqlite3.IntegrityError:
        # URL already exists
        try:
            stats = get_stats()
            with stats.lock:
                stats.collect_sources_already_exist += 1
        except RuntimeError:
            pass

        logger.debug(f"Collect source already exists: {url}")
        return False


def compute_collect(url: str, config: RunCollectConfig, force_recompute: bool = False) -> CollectionResult:
    """
    Collect links from a source page.

    Workflow:
    1. Scrape the page (kind="collect")
    2. Preprocess HTML (strip scripts/styles/base64)
    3. Check token limit
    4. Run LLM extraction
    5. Store results in database
    6. Promote links to classify phase

    Args:
        url: URL of source page to collect from
        config: Configuration for collection run
        force_recompute: If True, re-run LLM extraction even if status is extract_error

    Returns:
        CollectionResult with extracted links

    Raises:
        RuntimeError: If scraping, preprocessing, or extraction fails
    """
    import time
    
    collect_start = time.time()

    # Check if already processed
    with data_db_locked() as db:
        cursor = db.execute("SELECT status FROM collect WHERE url = ?", (url,))
        row = cursor.fetchone()

        if row and row["status"] != CollectStatus.NEW.value:
            # Allow retrying extract_error with force_recompute
            if force_recompute and row["status"] == CollectStatus.EXTRACT_ERROR.value:
                logger.info(f"Retrying extraction for {url} (was extract_error)")
                # Reset status to new so it can be reprocessed
                db.execute(
                    "UPDATE collect SET status = ? WHERE url = ?",
                    (CollectStatus.NEW.value, url),
                )
            elif row["status"] == CollectStatus.DONE.value:
                logger.warning(f"Source {url} already processed successfully")
                # Return cached result
                cursor = db.execute("SELECT data FROM collect WHERE url = ?", (url,))
                data_row = cursor.fetchone()
                if data_row and data_row["data"]:
                    data = json.loads(data_row["data"])
                    return CollectionResult(**data)
                raise RuntimeError(f"Source {url} marked done but no data found")
            else:
                raise RuntimeError(f"Source {url} in status {row['status']}, use --retry-errors for extract_error")

    timestamp = datetime.now(timezone.utc).isoformat()

    # Step 1: Scrape the page
    try:
        compute_scrape(url, kind="collect", headless=True)
    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed to scrape {url}: {error_msg}")
        with data_db_locked() as db:
            db.execute(
                """
                UPDATE collect
                SET status = ?, processed_at = ?, error = ?
                WHERE url = ?
                """,
                (CollectStatus.SCRAPE_ERROR.value, timestamp, error_msg, url),
            )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.collect_sources.errors[url] = error_msg
        except RuntimeError as stat_err:
            logger.warning(f"Failed to update stats: {stat_err}")

        raise RuntimeError(f"Scrape error: {e}") from e

    # Step 2: Read and preprocess HTML
    try:
        with open_scraped(url, "rt", encoding="utf-8") as f:
            raw_html = f.read()

        cleaned_html, preprocessing_stats = preprocess_html(raw_html, config.model)

    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed to preprocess HTML for {url}: {error_msg}")
        with data_db_locked() as db:
            db.execute(
                """
                UPDATE collect
                SET status = ?, processed_at = ?, error = ?
                WHERE url = ?
                """,
                (CollectStatus.EXTRACT_ERROR.value, timestamp, error_msg, url),
            )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.collect_sources.errors[url] = error_msg
        except RuntimeError as stat_err:
            logger.warning(f"Failed to update stats: {stat_err}")

        raise RuntimeError(f"Preprocessing error: {e}") from e

    # Step 3: Check token limit
    tokens_after = preprocessing_stats["tokens_after"]
    if tokens_after > config.max_html_tokens:
        error_msg = (
            f"HTML exceeds max_html_tokens limit: {tokens_after} > {config.max_html_tokens}"
        )
        logger.error(f"{error_msg} for {url}")

        with data_db_locked() as db:
            db.execute(
                """
                UPDATE collect
                SET status = ?, processed_at = ?, error = ?
                WHERE url = ?
                """,
                (
                    CollectStatus.EXTRACT_ERROR.value,
                    timestamp,
                    error_msg,
                    url,
                ),
            )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.collect_sources.errors[url] = error_msg
        except RuntimeError as stat_err:
            logger.warning(f"Failed to update stats: {stat_err}")

        raise RuntimeError(error_msg)

    # Step 4: Run LLM extraction
    try:
        # Load prompts
        prompts_file = PROMPTS_PATH / "collect.yaml"
        with open(prompts_file) as f:
            prompts = yaml.safe_load(f)

        # Call LLM
        result = get_completion(
            template_vars={"url": url, "html_content": cleaned_html},
            model=config.model,
            stats_subtree="collect_tokens",
            response_type=CollectionResult,
            system_prompt_template=prompts["collect_page"]["system"],
            user_prompt_template=prompts["collect_page"]["user"],
            thinking_budget=2048,
            max_tokens=10000,
        )

    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed LLM extraction for {url}: {error_msg}")
        with data_db_locked() as db:
            db.execute(
                """
                UPDATE collect
                SET status = ?, processed_at = ?, error = ?
                WHERE url = ?
                """,
                (
                    CollectStatus.EXTRACT_ERROR.value,
                    timestamp,
                    error_msg,
                    url,
                ),
            )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.collect_sources.errors[url] = error_msg
        except RuntimeError as stat_err:
            logger.warning(f"Failed to update stats: {stat_err}")

        raise RuntimeError(f"LLM extraction error: {e}") from e

    # Step 5: Add preprocessing stats and timing to result
    collect_duration = time.time() - collect_start
    result.tokens_full = preprocessing_stats["tokens_before"]
    result.tokens_stripped = preprocessing_stats["tokens_after"]

    # Step 6: Add links directly to classify table
    from .classify import add_classify_candidate

    # Get the source from collect table to preserve it
    with data_db_locked() as db:
        cursor = db.execute("SELECT source FROM collect WHERE url = ?", (url,))
        source_row = cursor.fetchone()
    
    original_source = source_row["source"] if source_row else None
    
    # Build collected source label
    if original_source:
        collected_source = f"collected:{original_source}"
    else:
        collected_source = "collected"

    for link in result.links:
        # Only add links above threshold
        if link.ai_safety_relevancy >= config.relevancy_threshold:
            # Add directly to classify (no intermediate collect_links table)
            add_classify_candidate(
                url=link.url,
                source=collected_source,
                source_url=url,
                collect_relevancy=link.ai_safety_relevancy,
            )

    # Step 7: Update source status to done and add timing
    # Add timing info to data
    data_dict = result.model_dump()
    data_dict["collect_duration"] = round(collect_duration, 2)
    data_json = json.dumps(data_dict)

    with data_db_locked() as db:
        db.execute(
            """
            UPDATE collect
            SET status = ?, processed_at = ?, data = ?
            WHERE url = ?
            """,
            (
                CollectStatus.DONE.value,
                timestamp,
                data_json,
                url,
            ),
        )

    # Update stats
    try:
        stats = get_stats()
        with stats.lock:
            stats.collect_sources.cached.add(url)  # Mark as completed
            # Track preprocessing stats
            if not hasattr(stats, "collect_preprocessing"):
                stats.collect_preprocessing = []
            stats.collect_preprocessing.append(preprocessing_stats)
    except RuntimeError:
        pass

    logger.info(
        f"Successfully collected {len(result.links)} links from {url} "
        f"(quality: {result.collection_quality_score:.2f})"
    )

    # Step 7: Promote links to classify (done in separate function/CLI command)
    # This allows for batch promotion with filtering

    return result
