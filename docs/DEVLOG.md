# Development Log

This log documents major problems, solutions, lessons learned, and design decisions during development.

## 2025-10-22: URL Hash Standardization

**What was done:**
- Added `url_hash` (full SHA256) and `url_hash_short` (8 chars) to all database tables
- Migrated existing database with 892 scrapes, 189 collect, and 1657 classify entries
- Updated all INSERT statements to populate hash columns
- Updated `export-taxonomy` CLI command to use database hashes instead of computing

**Changes:**
- **scrape**: Added `url_hash_short` column (already had full `url_hash`)
- **collect**: Added `url_hash` and `url_hash_short` columns
- **classify**: Added `url_hash` and `url_hash_short` columns
- All three tables now have indexes on both hash columns

**Rationale:**
- Short hash (8 chars) provides human-readable IDs for citation/tracking
- Full hash enables efficient lookups and deduplication
- Computing once at insert time avoids repeated computation
- Consistent across all tables for referencing items

**Implementation notes:**
- Migration script computed hashes from URL column (not dependent on scrape table)
- Hash format: SHA256(url).hexdigest(), short = first 8 chars
- Used in markdown export as `[item:5ad3d4e2]` for robust parsing after manual edits

## 2025-10-20: Initial Infrastructure Setup

**What was done:**
- Created core module structure under `shallow_review/`
- Implemented scraping infrastructure with playwright
- Set up stats tracking system with thread-safe context manager
- Configured litellm with disk caching and Helicone integration
- Created CLI framework with typer

**Key design decisions:**
- All paths derived from `ROOT_PATH` (from `__file__`) for pwd-independence
- Scrape cache uses `kind` parameter to distinguish contexts for same URL
- Hash computed as SHA256(`"{kind}:{url}"`) to allow URL reuse across contexts
- Stats use sets of IDs to avoid double-counting in multi-threaded scenarios
- Compression: Zstandard level 15 for all cached content
- Logging: Timestamped files in `runs/` directory with PID in filename

**Modules:**
- `common.py`: Paths, shutdown flag, base types
- `utils.py`: `smart_open()` for transparent compression, logging setup
- `stats.py`: Thread-safe stats tracking with CountStats and TokenStats
- `llm.py`: LLM integration with retry logic, cache invalidation on validation errors
- `scrape.py`: Playwright-based scraping with DB caching
- `cli.py`: Typer CLI with version/info commands
- `collect.py`, `classify.py`: Placeholder modules for future phases

**Technical notes:**
- LLM cache invalidation on ValidationError: Deletes bad cache entry before retry
- Scraping DB stores both successful scrapes and errors for caching
- Stats context manager ensures only one active stats instance per thread

**Scraping schema refactoring:**
- Changed URL to primary key (was url_hash) - ensures no duplicate scrapes
- Hash now only of URL, not `kind:url` - allows one scrape per URL
- Removed `content_path` column - path computed via `get_scrape_path(url)`
- Added `url_hash` column with UNIQUE constraint and index
- Added utility functions: `get_scrape_path(url)` and `open_scraped(url, mode)`
- Added `SCRAPED_PATH` constant to `common.py`
- Stats tracking uses `url` as unique ID (stored in sets to prevent duplicates)

## 2025-10-20: Collection Phase Implementation

**What was done:**
- Designed and implemented collection phase
- Created `collect.py` module with `compute_collect()` processing pipeline
- Designed collection prompts in `prompts/collect.yaml`
- Added HTML preprocessing utilities (`preprocess_html()`, `count_tokens()`)
- Implemented `add` CLI command for adding URLs
- Implemented `collect` CLI command with progress bars and stats
- Added `tiktoken` dependency for accurate token counting

**Key design decisions:**
- Links with relevancy ≥ threshold directly added to classify table (no intermediate table)
- Per-item commits for resumability and graceful shutdown
- HTML preprocessing strips scripts/styles/base64 images (50-90% token reduction)
- 2-level traceback formatting for errors
- Rich progress bars for top-level operations only
- Signal handlers for graceful shutdown (SIGINT/SIGTERM)

**Collection workflow:**
1. Add source URLs via CLI
2. Scrape and preprocess HTML
3. LLM extracts links with relevancy scores
4. Links above threshold promoted directly to classify table
5. Store full LLM response in JSON data field

## 2025-10-20: Database Overhaul - Unified data.db

**What was done:**
- Consolidated all databases into single `data/data.db` file
- Created `data_db.py` module with thread-safe singleton pattern
- Unified three tables: `scrape`, `collect`, `classify`
- Removed foreign key constraints between tables
- Eliminated intermediate `collect_links` table

**Key design decisions:**
- Single database simplifies architecture and queries
- No FK constraints for flexibility (semantic relationships only)
- Lazy singleton with global lock for thread-safe access
- Connection not held for long periods
- All timestamps in ISO 8601 format with timezone
- Links promoted inline during collect (no separate promotion step)

**Benefits:**
- Simpler codebase (single DB connection point)
- Easier queries (all data in one place)
- Better for small-scale operations (no complex multi-DB coordination)
- Resume-friendly (per-item commits)

## 2025-10-21: Classification Taxonomy System

**What was done:**
- Created hierarchical taxonomy system for classification categories
- Implemented `taxonomy.py` module with Pydantic models and utilities
- Created `data/taxonomy.yaml` with 103 leaf categories across 8 top-level groups
- Added taxonomy validation and prompt formatting functions
- Updated documentation (DATA.md, CODE.md, CLASSIFY.md)
- Added 4 megalab-specific categories: OpenAI Preparedness, DeepMind Frontier Safety, DeepMind Amplified Oversight, Anthropic Safeguards
- Expanded better_data with 5 subcategories (filtering, poisoning, attribution, synthetic, quality)
- Improved monitoring category descriptions for better disambiguation (control evals, mech anomaly, indirect, faithful CoT, whitebox, redteam)
- Added examples to interpretability categories and clarified theory category scopes
- Refined descriptions based on comparison with 2024 Shallow Review to ensure practical classificability
- Added 8 "other" catch-all categories for truly novel work not fitting existing categories

**Taxonomy structure:**
- 8 top-level categories: understand models, control, alternatives, data, AI solve, theory, sociotechnical, misc
- 103 assignable leaf categories (only leaves can be assigned to items)
- Hierarchical organization (3 levels: top-level → mid-level → leaf)
- Each category has: id, name, description, optional children, optional examples
- Includes org-specific programs: OpenAI Preparedness, DeepMind Frontier Safety Framework, DeepMind Amplified Oversight, Anthropic Safeguards
- Better data category expanded with 5 subcategories: filtering, poisoning, attribution, synthetic data, data quality
- Monitoring categories clarified with technique/org/problem distinctions
- Added 8 "other" catch-all categories for novel work: evals_other, interp_other, psych_other, deception_other, data_other, corrigibility_other, ontology_other, misc_other

**Key design decisions:**
- YAML as ground truth (not code, not docs)
- Recursive Pydantic models for validation and type safety
- `is_leaf` inferred from presence of children (can be explicitly set)
- Examples only allowed on leaf categories (validated)
- All category IDs unique across entire taxonomy (validated)
- IDs must be snake_case alphanumeric with underscores

**Prompt format:**
- Hierarchical markdown format (not flat list)
- Non-leaf categories as headers (h3-h5) with descriptions
- Leaf categories as bulleted items with IDs
- More readable and compact (~5,800 tokens)
- Provides context via headers, eliminates need for full paths

**Validation rules enforced:**
1. All IDs unique across taxonomy
2. IDs must be snake_case (alphanumeric + underscores/hyphens)
3. Only leaf categories can have examples
4. At least one leaf category must exist
5. No duplicate IDs allowed

**Usage pattern:**
```python
from shallow_review.taxonomy import load_taxonomy, format_taxonomy_for_prompt

# Load and validate
tax = load_taxonomy()  # From data/taxonomy.yaml

# Format for LLM prompt
prompt = format_taxonomy_for_prompt(tax, include_examples=False)

# Validate category ID
is_valid = tax.validate_category_id("evals_autonomy")  # True (leaf)
is_valid = tax.validate_category_id("evals")  # False (not leaf)

# Get all assignable categories
leaf_ids = tax.get_all_leaf_ids()  # 103 items
```

**Technical implementation:**
- Pydantic v2 with recursive models
- `validation_alias` for `is_leaf` field (YAML → model)
- `model_post_init` hook for cross-field validation
- Property shadowing for computed `is_leaf` value
- Thread-safe loading via lazy singleton pattern (future)

**Benefits:**
- Single source of truth for categories
- Type-safe validation at load time
- Easy to modify taxonomy (just edit YAML)
- Can version control taxonomy evolution
- Programmatic access to category tree
- Generate consistent prompts automatically

**Future work:**
- Add `category` column to classify table
- Implement classification prompts using taxonomy
- Add category-based filtering/analysis
- Track taxonomy version with data

