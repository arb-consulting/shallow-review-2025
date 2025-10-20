"""Collection phase: gather links from AI safety/alignment aggregator pages."""

import json
import logging
import sqlite3
from datetime import datetime, timezone
from typing import Any

import yaml
from pydantic import BaseModel, Field

from .common import (
    PROMPTS_PATH,
    CollectStatus,
    RunCollectConfig,
    SourceKind,
    is_shutdown_requested,
)
from .data_db import get_data_db
from .llm import get_completion
from .scrape import compute_scrape, open_scraped
from .stats import get_stats
from .utils import count_tokens, format_error, preprocess_html

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


def add_collect_source(url: str, source: str | None = None) -> bool:
    """
    Add a URL to collect from.

    Args:
        url: URL of source page
        source: Optional user-supplied source label

    Returns:
        True if added (new), False if already exists
    """
    db = get_data_db()
    timestamp = datetime.now(timezone.utc).isoformat()

    try:
        db.execute(
            """
            INSERT INTO collect (url, status, source, added_at)
            VALUES (?, ?, ?, ?)
            """,
            (url, CollectStatus.NEW.value, source, timestamp),
        )
        db.commit()

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
    db = get_data_db()

    # Check if already processed
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
            db.commit()
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
        scrape_path = compute_scrape(url, kind="collect", headless=True)
    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed to scrape {url}: {error_msg}")
        db.execute(
            """
            UPDATE collect
            SET status = ?, processed_at = ?, error = ?
            WHERE url = ?
            """,
            (CollectStatus.SCRAPE_ERROR.value, timestamp, error_msg, url),
        )
        db.commit()

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.collect_sources.errors[url] = error_msg
        except RuntimeError:
            pass

        raise RuntimeError(f"Scrape error: {e}") from e

    # Step 2: Read and preprocess HTML
    try:
        with open_scraped(url, "rt", encoding="utf-8") as f:
            raw_html = f.read()

        cleaned_html, preprocessing_stats = preprocess_html(raw_html, config.model)

    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed to preprocess HTML for {url}: {error_msg}")
        db.execute(
            """
            UPDATE collect
            SET status = ?, processed_at = ?, error = ?
            WHERE url = ?
            """,
            (CollectStatus.EXTRACT_ERROR.value, timestamp, error_msg, url),
        )
        db.commit()

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.collect_sources.errors[url] = error_msg
        except RuntimeError:
            pass

        raise RuntimeError(f"Preprocessing error: {e}") from e

    # Step 3: Check token limit
    tokens_after = preprocessing_stats["tokens_after"]
    if tokens_after > config.max_html_tokens:
        error_msg = (
            f"HTML exceeds max_html_tokens limit: {tokens_after} > {config.max_html_tokens}"
        )
        logger.error(f"{error_msg} for {url}")

        db.execute(
            """
            UPDATE collect
            SET status = ?, processed_at = ?, error = ?, preprocessing_stats = ?
            WHERE url = ?
            """,
            (
                CollectStatus.EXTRACT_ERROR.value,
                timestamp,
                error_msg,
                json.dumps(preprocessing_stats),
                url,
            ),
        )
        db.commit()

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.collect_sources.errors[url] = error_msg
        except RuntimeError:
            pass

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
        )

    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed LLM extraction for {url}: {error_msg}")
        db.execute(
            """
            UPDATE collect
            SET status = ?, processed_at = ?, error = ?, preprocessing_stats = ?
            WHERE url = ?
            """,
            (
                CollectStatus.EXTRACT_ERROR.value,
                timestamp,
                error_msg,
                json.dumps(preprocessing_stats),
                url,
            ),
        )
        db.commit()

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.collect_sources.errors[url] = error_msg
        except RuntimeError:
            pass

        raise RuntimeError(f"LLM extraction error: {e}") from e

    # Step 5: Add links directly to classify table
    from .classify import add_classify_candidate

    for link in result.links:
        # Only add links above threshold
        if link.ai_safety_relevancy >= config.relevancy_threshold:
            # Add directly to classify (no intermediate collect_links table)
            add_classify_candidate(
                url=link.url,
                source="collect",
                source_url=url,
                collect_relevancy=link.ai_safety_relevancy,
            )

    # Step 6: Update source status to done
    data_json = result.model_dump_json()

    db.execute(
        """
        UPDATE collect
        SET status = ?, processed_at = ?, data = ?, preprocessing_stats = ?
        WHERE url = ?
        """,
        (
            CollectStatus.DONE.value,
            timestamp,
            data_json,
            json.dumps(preprocessing_stats),
            url,
        ),
    )
    db.commit()

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
