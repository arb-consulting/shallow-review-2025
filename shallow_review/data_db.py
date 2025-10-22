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
from contextlib import contextmanager

from .common import DATA_PATH

logger = logging.getLogger(__name__)

# Global database connection (lazy singleton)
_data_db: sqlite3.Connection | None = None
_data_db_init_lock = threading.Lock()

# Global database operation lock
# Use with data_db_locked() context manager for thread-safe operations
_data_db_op_lock = threading.Lock()


def _create_tables(data_db: sqlite3.Connection, db_path: str) -> None:
    """Create all tables and indexes in the data database."""
    statements = [
        # Scrape table
        """CREATE TABLE IF NOT EXISTS scrape (
            url TEXT PRIMARY KEY,
            url_hash TEXT NOT NULL UNIQUE,
            url_hash_short TEXT,
            kind TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            status_code INTEGER,
            error TEXT,
            data JSON
        )""",
        "CREATE INDEX IF NOT EXISTS idx_scrape_url_hash ON scrape(url_hash)",
        "CREATE INDEX IF NOT EXISTS idx_scrape_url_hash_short ON scrape(url_hash_short)",
        "CREATE INDEX IF NOT EXISTS idx_scrape_kind ON scrape(kind)",
        "CREATE INDEX IF NOT EXISTS idx_scrape_timestamp ON scrape(timestamp)",
        # Collect table
        """CREATE TABLE IF NOT EXISTS collect (
            url TEXT PRIMARY KEY,
            url_hash TEXT,
            url_hash_short TEXT,
            status TEXT NOT NULL,
            source TEXT,
            added_at TEXT NOT NULL,
            processed_at TEXT,
            data JSON,
            error TEXT,
            CHECK(status IN ('new', 'scrape_error', 'extract_error', 'done'))
        )""",
        "CREATE INDEX IF NOT EXISTS idx_collect_status ON collect(status)",
        "CREATE INDEX IF NOT EXISTS idx_collect_added_at ON collect(added_at)",
        "CREATE INDEX IF NOT EXISTS idx_collect_url_hash ON collect(url_hash)",
        "CREATE INDEX IF NOT EXISTS idx_collect_url_hash_short ON collect(url_hash_short)",
        # Classify table
        """CREATE TABLE IF NOT EXISTS classify (
            url TEXT PRIMARY KEY,
            url_hash TEXT,
            url_hash_short TEXT,
            status TEXT NOT NULL,
            source TEXT NOT NULL,
            source_url TEXT,
            collect_relevancy REAL,
            added_at TEXT NOT NULL,
            processed_at TEXT,
            ai_safety_relevance REAL,
            shallow_review_inclusion REAL,
            kind TEXT,
            data JSON,
            error TEXT,
            CHECK(status IN ('new', 'scrape_error', 'classify_error', 'done'))
        )""",
        "CREATE INDEX IF NOT EXISTS idx_classify_status ON classify(status)",
        "CREATE INDEX IF NOT EXISTS idx_classify_source ON classify(source)",
        "CREATE INDEX IF NOT EXISTS idx_classify_source_url ON classify(source_url)",
        "CREATE INDEX IF NOT EXISTS idx_classify_added_at ON classify(added_at)",
        "CREATE INDEX IF NOT EXISTS idx_classify_ai_safety_relevance ON classify(ai_safety_relevance)",
        "CREATE INDEX IF NOT EXISTS idx_classify_shallow_review_inclusion ON classify(shallow_review_inclusion)",
        "CREATE INDEX IF NOT EXISTS idx_classify_kind ON classify(kind)",
        "CREATE INDEX IF NOT EXISTS idx_classify_url_hash ON classify(url_hash)",
        "CREATE INDEX IF NOT EXISTS idx_classify_url_hash_short ON classify(url_hash_short)",
    ]

    for statement in statements:
        data_db.execute(statement)

    data_db.commit()
    logger.info(f"Initialized unified database at {db_path}")


def get_data_db() -> sqlite3.Connection:
    """
    Get or create the unified data database connection (lazy singleton).
    
    DEPRECATED: Use data_db_locked() context manager instead for thread-safety.

    Creates all tables and indexes if they don't exist.
    Uses WAL mode for better concurrency.

    Returns:
        SQLite connection to data/data.db
    """
    global _data_db

    with _data_db_init_lock:
        if _data_db is None:
            db_path = DATA_PATH / "data.db"
            data_db = sqlite3.connect(
                str(db_path),
                check_same_thread=False,
                timeout=30.0,  # Wait up to 30 seconds for locks
                isolation_level=None,  # Autocommit mode (no transactions by default)
            )
            data_db.row_factory = sqlite3.Row
            
            # Enable WAL mode for better concurrency
            # WAL allows concurrent reads and one writer
            data_db.execute("PRAGMA journal_mode=WAL")
            data_db.execute("PRAGMA synchronous=NORMAL")  # Faster with WAL
            
            _create_tables(data_db, str(db_path))
            _data_db = data_db
        return _data_db


@contextmanager
def data_db_locked():
    """
    Context manager for thread-safe database operations.
    
    Acquires lock, yields database connection, releases lock on exit.
    Use for all database operations in multi-threaded code.
    
    Example:
        with data_db_locked() as db:
            cursor = db.execute("SELECT * FROM scrape WHERE url = ?", (url,))
            row = cursor.fetchone()
            db.execute("INSERT INTO collect ...", (...))
            
    Note: Keep operations inside the context minimal. Don't hold lock
    while doing expensive operations like scraping or LLM calls.
    
    Yields:
        SQLite connection with lock held
    """
    # Ensure DB is initialized
    db = get_data_db()
    
    # Acquire lock for thread-safe operations
    with _data_db_op_lock:
        yield db

