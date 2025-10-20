"""Classification phase: classify AI safety/alignment content."""

import logging
import sqlite3
from datetime import datetime, timezone

from .common import ClassifyStatus
from .data_db import get_data_db
from .stats import get_stats

logger = logging.getLogger(__name__)


def add_classify_candidate(
    url: str,
    source: str,
    source_url: str | None = None,
    collect_relevancy: float | None = None,
) -> bool:
    """
    Add a URL to classification queue.

    Args:
        url: URL to classify
        source: Source label ("collect" or user-supplied)
        source_url: URL of source page (if from collect)
        collect_relevancy: Relevancy score from collect phase (if applicable)

    Returns:
        True if added (new), False if already exists
    """
    db = get_data_db()
    timestamp = datetime.now(timezone.utc).isoformat()

    try:
        db.execute(
            """
            INSERT INTO classify 
            (url, status, source, source_url, collect_relevancy, added_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (url, ClassifyStatus.NEW.value, source, source_url, collect_relevancy, timestamp),
        )
        db.commit()

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


# TODO: Implement compute_classify function
# def compute_classify(url: str, config: RunClassifyConfig) -> ClassificationResult:
#     """Classify a URL and extract metadata."""
#     ...
