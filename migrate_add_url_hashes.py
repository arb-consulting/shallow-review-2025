#!/usr/bin/env python3
"""
One-time migration: Add url_hash and url_hash_short columns to all tables.

This migration adds:
- url_hash_short (8 chars) to scrape table
- url_hash (64 chars) and url_hash_short (8 chars) to collect table
- url_hash (64 chars) and url_hash_short (8 chars) to classify table

Run once with: uv run python migrate_add_url_hashes.py
"""

import hashlib
import sqlite3
import sys
from pathlib import Path

# Determine project root
ROOT = Path(__file__).parent
DB_PATH = ROOT / "data" / "data.db"


def compute_url_hash(url: str) -> str:
    """Compute full SHA256 hash of URL."""
    return hashlib.sha256(url.encode("utf-8")).hexdigest()


def compute_url_hash_short(url: str) -> str:
    """Compute 8-char shortened SHA256 hash of URL."""
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:8]


def main():
    """Run migration."""
    if not DB_PATH.exists():
        print(f"Error: Database not found at {DB_PATH}")
        sys.exit(1)
    
    print(f"Running migration on {DB_PATH}")
    print()
    
    # Connect to database
    db = sqlite3.connect(str(DB_PATH))
    db.row_factory = sqlite3.Row
    
    try:
        # Check if migration already ran
        cursor = db.execute("PRAGMA table_info(scrape)")
        scrape_columns = {row["name"] for row in cursor.fetchall()}
        
        if "url_hash_short" in scrape_columns:
            print("Migration already completed (url_hash_short exists in scrape table)")
            return
        
        print("Starting migration...")
        print()
        
        # ===== SCRAPE TABLE =====
        print("1. Adding url_hash_short to scrape table...")
        
        # Add column
        db.execute("ALTER TABLE scrape ADD COLUMN url_hash_short TEXT")
        
        # Populate from url (recompute for consistency)
        rows = db.execute("SELECT url FROM scrape").fetchall()
        for row in rows:
            url = row["url"]
            url_hash_short = compute_url_hash_short(url)
            db.execute(
                "UPDATE scrape SET url_hash_short = ? WHERE url = ?",
                (url_hash_short, url)
            )
        
        # Verify
        count = db.execute("SELECT COUNT(*) as cnt FROM scrape WHERE url_hash_short IS NOT NULL").fetchone()["cnt"]
        print(f"   ✓ Populated {count} rows")
        
        # Create index
        db.execute("CREATE INDEX IF NOT EXISTS idx_scrape_url_hash_short ON scrape(url_hash_short)")
        print("   ✓ Created index idx_scrape_url_hash_short")
        print()
        
        # ===== COLLECT TABLE =====
        print("2. Adding url_hash and url_hash_short to collect table...")
        
        # Add columns
        db.execute("ALTER TABLE collect ADD COLUMN url_hash TEXT")
        db.execute("ALTER TABLE collect ADD COLUMN url_hash_short TEXT")
        
        # Populate from url
        rows = db.execute("SELECT url FROM collect").fetchall()
        for row in rows:
            url = row["url"]
            url_hash = compute_url_hash(url)
            url_hash_short = url_hash[:8]
            db.execute(
                "UPDATE collect SET url_hash = ?, url_hash_short = ? WHERE url = ?",
                (url_hash, url_hash_short, url)
            )
        
        # Verify
        count = db.execute("SELECT COUNT(*) as cnt FROM collect WHERE url_hash IS NOT NULL").fetchone()["cnt"]
        print(f"   ✓ Populated {count} rows")
        
        # Create indexes
        db.execute("CREATE INDEX IF NOT EXISTS idx_collect_url_hash ON collect(url_hash)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_collect_url_hash_short ON collect(url_hash_short)")
        print("   ✓ Created indexes")
        print()
        
        # ===== CLASSIFY TABLE =====
        print("3. Adding url_hash and url_hash_short to classify table...")
        
        # Add columns
        db.execute("ALTER TABLE classify ADD COLUMN url_hash TEXT")
        db.execute("ALTER TABLE classify ADD COLUMN url_hash_short TEXT")
        
        # Populate from url
        rows = db.execute("SELECT url FROM classify").fetchall()
        for row in rows:
            url = row["url"]
            url_hash = compute_url_hash(url)
            url_hash_short = url_hash[:8]
            db.execute(
                "UPDATE classify SET url_hash = ?, url_hash_short = ? WHERE url = ?",
                (url_hash, url_hash_short, url)
            )
        
        # Verify
        count = db.execute("SELECT COUNT(*) as cnt FROM classify WHERE url_hash IS NOT NULL").fetchone()["cnt"]
        print(f"   ✓ Populated {count} rows")
        
        # Create indexes
        db.execute("CREATE INDEX IF NOT EXISTS idx_classify_url_hash ON classify(url_hash)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_classify_url_hash_short ON classify(url_hash_short)")
        print("   ✓ Created indexes")
        print()
        
        # Commit all changes
        db.commit()
        
        print("✓ Migration completed successfully!")
        print()
        
        # Print summary
        print("Summary:")
        print(f"  - scrape:   added url_hash_short")
        print(f"  - collect:  added url_hash, url_hash_short")
        print(f"  - classify: added url_hash, url_hash_short")
        print(f"  - Created 5 new indexes")
        
    except Exception as e:
        print(f"\n✗ Migration failed: {e}")
        db.rollback()
        sys.exit(1)
    finally:
        db.close()


if __name__ == "__main__":
    main()

