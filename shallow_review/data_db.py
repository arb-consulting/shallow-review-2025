"""Unified database module for all pipeline tables.

All data stored in a single SQLite database: data/data.db

Tables:
- scrape: Scraped page metadata
- collect: Collection source pages
- classify: Classification candidates (links to classify)
"""

import logging
import sqlite3
import threading

from .common import DATA_PATH

logger = logging.getLogger(__name__)

# Global database connection (lazy singleton)
_data_db: sqlite3.Connection | None = None
_data_db_lock = threading.Lock()


def _create_tables(data_db: sqlite3.Connection, db_path: str) -> None:
    """Create all tables and indexes in the data database."""
    # Create scrape table
    data_db.execute(
        """
        CREATE TABLE IF NOT EXISTS scrape (
            url TEXT PRIMARY KEY,
            url_hash TEXT NOT NULL UNIQUE,
            kind TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            status_code INTEGER,
            error TEXT
        )
        """
    )

    data_db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_scrape_url_hash 
        ON scrape(url_hash)
        """
    )

    data_db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_scrape_kind 
        ON scrape(kind)
        """
    )

    data_db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_scrape_timestamp 
        ON scrape(timestamp)
        """
    )

    # Create collect table (source pages being collected from)
    data_db.execute(
        """
        CREATE TABLE IF NOT EXISTS collect (
            url TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            source TEXT,
            added_at TEXT NOT NULL,
            processed_at TEXT,
            data JSON,
            error TEXT,
            preprocessing_stats JSON,
            CHECK(status IN ('new', 'scrape_error', 'extract_error', 'done'))
        )
        """
    )

    data_db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_collect_status 
        ON collect(status)
        """
    )

    data_db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_collect_added_at 
        ON collect(added_at)
        """
    )

    # Create classify table (links to classify)
    data_db.execute(
        """
        CREATE TABLE IF NOT EXISTS classify (
            url TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            source TEXT NOT NULL,
            source_url TEXT,
            collect_relevancy REAL,
            added_at TEXT NOT NULL,
            processed_at TEXT,
            data JSON,
            error TEXT,
            preprocessing_stats JSON,
            CHECK(status IN ('new', 'scrape_error', 'classify_error', 'done'))
        )
        """
    )

    data_db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_classify_status 
        ON classify(status)
        """
    )

    data_db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_classify_source 
        ON classify(source)
        """
    )

    data_db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_classify_source_url 
        ON classify(source_url)
        """
    )

    data_db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_classify_added_at 
        ON classify(added_at)
        """
    )

    data_db.commit()
    logger.info(f"Initialized unified database at {db_path}")


def get_data_db() -> sqlite3.Connection:
    """
    Get or create the unified data database connection (lazy singleton).

    Creates all tables and indexes if they don't exist.
    Connection should not be held for long periods.

    Returns:
        SQLite connection to data/data.db
    """
    global _data_db

    with _data_db_lock:
        if _data_db is None:
            db_path = DATA_PATH / "data.db"
            data_db = sqlite3.connect(str(db_path), check_same_thread=False)
            data_db.row_factory = sqlite3.Row
            _create_tables(data_db, str(db_path))
            _data_db = data_db
        return _data_db

