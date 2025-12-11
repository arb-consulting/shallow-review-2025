"""Classification phase: classify AI safety/alignment content."""

import json
import logging
import sqlite3
from datetime import datetime, timezone

import yaml
from pydantic import BaseModel, Field

from .common import (
    PROMPTS_PATH,
    ClassifyStatus,
    RunClassifyConfig,
)
from .data_db import data_db_locked
from .llm import get_completion
from .scrape import compute_scrape, open_scraped
from .stats import get_stats
from .taxonomy import load_taxonomy, format_taxonomy_for_prompt
from .utils import format_error, normalize_url, preprocess_html, url_hash, url_hash_short

logger = logging.getLogger(__name__)


# Pydantic models for LLM responses
class CategoryAssignment(BaseModel):
    """A category assignment with score."""

    id: str = Field(description="Leaf category ID from taxonomy")
    score: float = Field(ge=0.0, le=1.0, description="Fit score for this category")


class ClassificationResult(BaseModel):
    """Result of classifying a piece of content."""

    title: str
    authors: list[str]
    author_organizations: list[str]
    date: str | None = None  # ISO format YYYY-MM-DD
    published_year: int | None = None
    venue: str | None = None
    kind: str  # One of the ClassifyKind enum values
    contribution_type: str  # One of: empirical_results, theoretical_framework, etc.
    summary: str
    key_result: str | None = None
    ai_safety_relevance: float = Field(ge=0.0, le=1.0)
    shallow_review_inclusion: float = Field(ge=0.0, le=1.0)
    categories: list[CategoryAssignment] = Field(min_length=1, max_length=3)
    category_comment: str
    confidence: float = Field(ge=0.0, le=1.0)
    tokens_full: int | None = None  # Full HTML token count
    tokens_stripped: int | None = None  # Stripped HTML token count


def add_classify_candidate(
    url: str,
    source: str,
    source_url: str | None = None,
    collect_relevancy: float | None = None,
) -> bool:
    """
    Add a URL to classification queue.

    Args:
        url: URL to classify (will be normalized)
        source: Source label ("collect" or user-supplied)
        source_url: URL of source page (if from collect)
        collect_relevancy: Relevancy score from collect phase (if applicable)

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
                INSERT INTO classify 
                (url, url_hash, url_hash_short, status, source, source_url, collect_relevancy, added_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (url, hash_value, hash_short, ClassifyStatus.NEW.value, source, source_url, collect_relevancy, timestamp),
            )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.classify_candidates.new.add(url)
        except RuntimeError:
            pass

        logger.info(f"Added classify candidate: {url}")
        return True

    except sqlite3.IntegrityError:
        # URL already exists
        try:
            stats = get_stats()
            with stats.lock:
                stats.classify_candidates_already_exist += 1
        except RuntimeError:
            pass

        logger.debug(f"Classify candidate already exists: {url}")
        return False


def compute_classify(url: str, config: RunClassifyConfig, force_recompute: bool = False) -> ClassificationResult:
    """
    Classify a URL and extract metadata.

    Workflow:
    1. Scrape the page (kind="classify")
    2. Preprocess HTML (strip scripts/styles/base64)
    3. Check token limit
    4. Load taxonomy and format for prompt
    5. Run LLM classification
    6. Store results in database

    Args:
        url: URL to classify
        config: Configuration for classification run
        force_recompute: If True, re-run classification even if status is classify_error

    Returns:
        ClassificationResult with extracted metadata

    Raises:
        RuntimeError: If scraping, preprocessing, or classification fails
    """
    import time

    classify_start = time.time()

    # Check if already processed
    with data_db_locked() as db:
        cursor = db.execute("SELECT status FROM classify WHERE url = ?", (url,))
        row = cursor.fetchone()

        if row and row["status"] != ClassifyStatus.NEW.value:
            # Allow retrying classify_error with force_recompute
            if force_recompute and row["status"] == ClassifyStatus.CLASSIFY_ERROR.value:
                logger.info(f"Retrying classification for {url} (was classify_error)")
                db.execute(
                    "UPDATE classify SET status = ? WHERE url = ?",
                    (ClassifyStatus.NEW.value, url),
                )
            elif row["status"] == ClassifyStatus.DONE.value:
                logger.warning(f"URL {url} already classified successfully")
                # Return cached result
                cursor = db.execute("SELECT data FROM classify WHERE url = ?", (url,))
                data_row = cursor.fetchone()
                if data_row and data_row["data"]:
                    data = json.loads(data_row["data"])
                    return ClassificationResult(**data)
                raise RuntimeError(f"URL {url} marked done but no data found")
            else:
                raise RuntimeError(f"URL {url} in status {row['status']}, use --retry-errors for classify_error")

    timestamp = datetime.now(timezone.utc).isoformat()

    # Step 1: Scrape the page
    try:
        compute_scrape(url, kind="classify", headless=True)
    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed to scrape {url}: {error_msg}")
        with data_db_locked() as db:
            db.execute(
                """
                UPDATE classify
                SET status = ?, processed_at = ?, error = ?
                WHERE url = ?
                """,
                (ClassifyStatus.SCRAPE_ERROR.value, timestamp, error_msg, url),
            )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.classify_candidates.errors[url] = error_msg
        except RuntimeError as stat_err:
            logger.warning(f"Failed to update stats: {stat_err}")

        raise RuntimeError(f"Scrape error: {e}") from e

    # Step 2: Read and preprocess HTML (use stripped version)
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
                UPDATE classify
                SET status = ?, processed_at = ?, error = ?
                WHERE url = ?
                """,
                (ClassifyStatus.CLASSIFY_ERROR.value, timestamp, error_msg, url),
            )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.classify_candidates.errors[url] = error_msg
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

        db.execute(
            """
            UPDATE classify
            SET status = ?, processed_at = ?, error = ?
            WHERE url = ?
            """,
            (
                ClassifyStatus.CLASSIFY_ERROR.value,
                timestamp,
                error_msg,
                url,
            ),
        )
        db.commit()

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.classify_candidates.errors[url] = error_msg
        except RuntimeError as stat_err:
            logger.warning(f"Failed to update stats: {stat_err}")

        raise RuntimeError(error_msg)

    # Step 4: Load taxonomy and format for prompt
    try:
        taxonomy = load_taxonomy()
        taxonomy_text = format_taxonomy_for_prompt(taxonomy)
    except Exception as e:
        error_msg = f"Failed to load taxonomy: {format_error(e, levels=2)}"
        logger.error(error_msg)
        raise RuntimeError(error_msg) from e

    # Step 5: Get collect_relevancy from database if available
    with data_db_locked() as db:
        cursor = db.execute(
            "SELECT collect_relevancy FROM classify WHERE url = ?",
            (url,)
        )
        row = cursor.fetchone()
    collect_relevancy = row["collect_relevancy"] if row else None

    # Step 6: Run LLM classification
    try:
        # Load prompts
        prompts_file = PROMPTS_PATH / "classify.yaml"
        with open(prompts_file) as f:
            prompts = yaml.safe_load(f)

        # Prepare template variables
        template_vars = {
            "url": url,
            "content": cleaned_html,
            "taxonomy": taxonomy_text,
            "collect_relevancy": collect_relevancy,
        }

        # Call LLM with 1-hour cache for system prompt (taxonomy changes infrequently)
        result = get_completion(
            template_vars=template_vars,
            model=config.model,
            stats_subtree="classify_tokens",
            response_type=ClassificationResult,
            system_prompt_template=prompts["classify_content"]["system"],
            user_prompt_template=prompts["classify_content"]["user"],
            system_cache_ttl="1h",  # Cache system prompt (with taxonomy) for 1 hour
            thinking_budget=2048,
            max_tokens=10001,
        )

    except Exception as e:
        error_msg = format_error(e, levels=2)
        logger.error(f"Failed LLM classification for {url}: {error_msg}")
        with data_db_locked() as db:

            db.execute(
            """
            UPDATE classify
            SET status = ?, processed_at = ?, error = ?
            WHERE url = ?
            """,
            (
                ClassifyStatus.CLASSIFY_ERROR.value,
                timestamp,
                error_msg,
                url,
            ),
        )

        # Update stats
        try:
            stats = get_stats()
            with stats.lock:
                stats.classify_candidates.errors[url] = error_msg
        except RuntimeError as stat_err:
            logger.warning(f"Failed to update stats: {stat_err}")

        raise RuntimeError(f"LLM classification error: {e}") from e

    # Step 7: Add preprocessing stats and timing to result
    classify_duration = time.time() - classify_start
    result.tokens_full = preprocessing_stats["tokens_before"]
    result.tokens_stripped = preprocessing_stats["tokens_after"]

    # Step 8: Validate categories against taxonomy
    valid_leaf_ids = set(taxonomy.get_all_leaf_ids())
    for cat in result.categories:
        if cat.id not in valid_leaf_ids:
            error_msg = f"Invalid category ID: {cat.id} (not a valid leaf category)"
            logger.error(error_msg)
            with data_db_locked() as db:
                db.execute(
                    """
                    UPDATE classify
                    SET status = ?, processed_at = ?, error = ?
                    WHERE url = ?
                    """,
                    (ClassifyStatus.CLASSIFY_ERROR.value, timestamp, error_msg, url),
                )
            raise RuntimeError(error_msg)

    # Step 9: Update database with results
    data_dict = result.model_dump()
    data_dict["classify_duration"] = round(classify_duration, 2)
    data_json = json.dumps(data_dict)

    # Extract top category for indexed column
    top_category_id = result.categories[0].id if result.categories else None

    with data_db_locked() as db:
        db.execute(
            """
            UPDATE classify
            SET status = ?, processed_at = ?, ai_safety_relevance = ?, shallow_review_inclusion = ?, kind = ?, data = ?
            WHERE url = ?
            """,
            (
                ClassifyStatus.DONE.value,
                timestamp,
                result.ai_safety_relevance,
                result.shallow_review_inclusion,
                result.kind,
                data_json,
                url,
            ),
        )

    # Update stats
    try:
        stats = get_stats()
        with stats.lock:
            stats.classify_candidates.cached.add(url)
            # Track AI safety relevance distribution
            if not hasattr(stats, "ai_safety_relevance_scores"):
                stats.ai_safety_relevance_scores = []
            stats.ai_safety_relevance_scores.append(result.ai_safety_relevance)
            # Track shallow review inclusion distribution
            if not hasattr(stats, "shallow_review_inclusion_scores"):
                stats.shallow_review_inclusion_scores = []
            stats.shallow_review_inclusion_scores.append(result.shallow_review_inclusion)
            # Track confidence distribution
            if not hasattr(stats, "classify_confidence_scores"):
                stats.classify_confidence_scores = []
            stats.classify_confidence_scores.append(result.confidence)
            # Track preprocessing stats
            stats.classify_preprocessing.append(preprocessing_stats)
    except RuntimeError:
        pass

    logger.info(
        f"Successfully classified {url} "
        f"(safety_rel: {result.ai_safety_relevance:.2f}, "
        f"inclusion: {result.shallow_review_inclusion:.2f}, "
        f"top category: {top_category_id}, "
        f"confidence: {result.confidence:.2f})"
    )

    return result
