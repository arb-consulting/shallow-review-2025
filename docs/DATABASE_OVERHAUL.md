# Database Overhaul - Unified data.db

## Summary

Refactored the database structure from multiple separate databases to a single unified database with 3 tables.

## Changes

### Before
- `data/scrape.db` → `scraped` table
- `data/collect.db` → `collect_sources` and `collect_links` tables
- `data/classify.db` → `classify_candidates` table

### After
- `data/data.db` → `scrape`, `collect`, `classify` tables

## Table Structure

All tables stored in `data/data.db` with **NO foreign key constraints** between them.

### scrape table
```sql
CREATE TABLE scrape (
    url TEXT PRIMARY KEY,
    url_hash TEXT NOT NULL UNIQUE,
    kind TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    status_code INTEGER,
    error TEXT
)
```

**Purpose:** Track scraped pages metadata

**Indexes:**
- `idx_scrape_url_hash` on `url_hash`
- `idx_scrape_kind` on `kind`
- `idx_scrape_timestamp` on `timestamp`

### collect table
```sql
CREATE TABLE collect (
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
```

**Purpose:** Track source pages being collected from (replaces `collect_sources`)

**Indexes:**
- `idx_collect_status` on `status`
- `idx_collect_added_at` on `added_at`

**data JSON field contains:**
- Full LLM response JSON including:
  - `title`
  - `kind`
  - `collection_quality_score`
  - `comments`
  - `links` array with all extracted links

### classify table
```sql
CREATE TABLE classify (
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
```

**Purpose:** Track URLs to classify (replaces `classify_candidates`)

**Indexes:**
- `idx_classify_status` on `status`
- `idx_classify_source` on `source`
- `idx_classify_source_url` on `source_url`
- `idx_classify_added_at` on `added_at`

**source_url:** Stores the source page URL (from collect) but **NOT a foreign key**

## Key Architectural Changes

### 1. Removed collect_links Table

**Before:** 
- `collect_sources` → source pages
- `collect_links` → extracted links (intermediate table)
- `classify_candidates` → links to classify

**After:**
- `collect` → source pages
- `classify` → links to classify (directly added from collect)

**Rationale:** Simplified architecture - links go straight to classify table when extracted

### 2. No Foreign Key Constraints

Tables do NOT reference each other with FK constraints:
- `scrape` is independent
- `collect` is independent
- `classify.source_url` references `collect.url` semantically but **not enforced**

**Rationale:**
- Simplifies database management
- No cascading deletes/updates
- Connection not held long in code
- More flexible for data manipulation

### 3. Unified Database Module

Created `data_db.py` with:
- Single `get_data_db()` function
- Lazy singleton with global lock
- Creates all tables/indexes on first access
- One connection for all tables

**Files updated:**
- `scrape.py` → imports `get_data_db()`, uses `scrape` table
- `collect.py` → imports `get_data_db()`, uses `collect` table
- `classify.py` → imports `get_data_db()`, uses `classify` table
- `cli.py` → imports `get_data_db()` for queries

### 4. Removed Old DB Functions

**Deleted:**
- `get_scrape_db()` from `scrape.py`
- `get_collect_db()` from `collect.py`
- `get_classify_db()` from `classify.py`

**Replaced with:** Single `get_data_db()` from `data_db.py`

## Migration Notes

### For Existing Databases

If you have existing data in separate databases, migration required:

```sql
-- Attach old databases
ATTACH DATABASE 'data/scrape.db' AS old_scrape;
ATTACH DATABASE 'data/collect.db' AS old_collect;
ATTACH DATABASE 'data/classify.db' AS old_classify;

-- Migrate data
INSERT OR IGNORE INTO scrape SELECT * FROM old_scrape.scraped;
INSERT OR IGNORE INTO collect SELECT url, status, source, added_at, processed_at, data, error, preprocessing_stats FROM old_collect.collect_sources;
INSERT OR IGNORE INTO classify SELECT url, status, source, source_url, collect_relevancy, added_at, processed_at, data, error, preprocessing_stats FROM old_classify.classify_candidates;

-- Detach old databases
DETACH DATABASE old_scrape;
DETACH DATABASE old_collect;
DETACH DATABASE old_classify;
```

**Note:** `collect_links` data is NOT migrated - links will be re-extracted on next collect run

### For Fresh Installs

No migration needed - `data/data.db` will be created automatically on first run.

## Code Changes Summary

### data_db.py (NEW FILE)
- Unified database module
- `get_data_db()` function
- All table creation logic

### scrape.py
- Removed database initialization code
- Changed `scraped` → `scrape` table references
- Import `get_data_db()` instead of local `get_scrape_db()`

### collect.py
- Removed database initialization code
- Changed `collect_sources` → `collect` table references
- Removed all `collect_links` table code
- Links now added directly to `classify` table
- Import `get_data_db()` instead of local `get_collect_db()`

### classify.py
- Removed database initialization code
- Changed `classify_candidates` → `classify` table references
- Import `get_data_db()` instead of local `get_classify_db()`

### cli.py
- Import `get_data_db()` instead of `get_collect_db()`
- Changed `collect_sources` → `collect` in queries

### stats.py
- Removed `collect_links` stats tracking
- Updated `to_dict()` method
- Updated `print_summary()` method

## Benefits

1. **Simpler architecture** - One database, three tables
2. **Easier to query** - All data in one place
3. **Better performance** - One connection, fewer locks
4. **Cleaner code** - Single DB module, less duplication
5. **More flexible** - No FK constraints allow independent operations

## Trade-offs

1. **No referential integrity** - Must ensure consistency in application code
2. **Migration required** - Existing data needs to be migrated
3. **Removed collect_links** - No longer tracking link provenance explicitly
   - Links go straight to classify
   - Can still see source via `classify.source_url`
   - But can't track if same link found in multiple sources

## Testing Checklist

- [ ] Verify `data/data.db` created on first run
- [ ] Test `add` command (both collect and classify)
- [ ] Test `collect` command with new database
- [ ] Verify links added to `classify` table after collect
- [ ] Check stats display (no collect_links row)
- [ ] Test error handling (scrape_error, extract_error)
- [ ] Test --retry-errors flag
- [ ] Verify all table indexes created

## Files Modified

- `shallow_review/data_db.py` (NEW)
- `shallow_review/scrape.py`
- `shallow_review/collect.py`
- `shallow_review/classify.py`
- `shallow_review/cli.py`
- `shallow_review/stats.py`

No linter errors. All tests should pass after migration.

