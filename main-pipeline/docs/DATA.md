# Data Storage and Database Schemas

**Ground truth for all data structures, database schemas, and file formats.**

## Directory Structure

```
data/
├── .llm_cache/          # Litellm disk cache (gitignored)
├── data.db              # Unified database (scrape, collect, classify tables)
├── taxonomy.yaml        # Classification category taxonomy (ground truth)
└── scraped/             # Scraped HTML content
    └── <hash>.html.zst  # Zstandard-compressed HTML files
```

## Unified Database: data.db

All tables stored in `data/data.db` with **NO foreign key constraints**.

**Note on column order:** Schemas below show the canonical column order for tables created from scratch. Databases migrated from earlier versions may have different column orders (with migrated columns at the end) due to SQLite's `ALTER TABLE` behavior. This is functionally equivalent - SQLite doesn't care about column order, and all queries use column names.

### scrape table

Stores metadata for scraped web pages.

```sql
CREATE TABLE scrape (
    url TEXT PRIMARY KEY,
    url_hash TEXT NOT NULL UNIQUE,
    url_hash_short TEXT,
    kind TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    status_code INTEGER,
    error TEXT,
    data JSON
);

CREATE INDEX idx_scrape_url_hash ON scrape(url_hash);
CREATE INDEX idx_scrape_url_hash_short ON scrape(url_hash_short);
CREATE INDEX idx_scrape_kind ON scrape(kind);
CREATE INDEX idx_scrape_timestamp ON scrape(timestamp);
```

**Fields:**
- `url`: Original URL (primary key - unique)
- `url_hash`: SHA256(url) - full 64-char hex for file naming
- `url_hash_short`: First 8 chars of SHA256(url) - for human-readable IDs
- `kind`: Context/type of scrape (e.g., "collect", "classify")
- `timestamp`: ISO 8601 UTC timestamp with timezone
- `status_code`: HTTP status code (if successful)
- `error`: Error message (if failed)
- `data`: JSON with scrape metrics (see below)

**data JSON structure** (when successful):
```json
{
  "size_full": 1234567,
  "size_compressed": 234567,
  "tokens_full": 50000,
  "tokens_stripped": 15000,
  "scrape_duration": 3.45
}
```

**Notes:**
- `size_full`: Full HTML size in bytes
- `size_compressed`: Compressed file size in bytes (.zst)
- `tokens_full`: Token count of full HTML
- `tokens_stripped`: Token count after preprocessing (scripts/styles removed)
- `scrape_duration`: Time taken to scrape in seconds
- Each URL scraped only once, cached indefinitely
- Failed scrapes are cached to avoid repeated failures
- File path: `data/scraped/{url_hash}.html.zst`
- Debug file (stripped HTML): `data/scraped/{url_hash}-stripped.html` (uncompressed, for inspection)
- Use `get_scrape_path(url)` or `open_scraped(url, mode)` to access files

### collect table

Tracks source pages being collected from (conferences, newsletters, etc.).

```sql
CREATE TABLE collect (
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
);

CREATE INDEX idx_collect_status ON collect(status);
CREATE INDEX idx_collect_added_at ON collect(added_at);
CREATE INDEX idx_collect_url_hash ON collect(url_hash);
CREATE INDEX idx_collect_url_hash_short ON collect(url_hash_short);
```

**Fields:**
- `url`: Source page URL (primary key)
- `url_hash`: SHA256(url) - full 64-char hex
- `url_hash_short`: First 8 chars of SHA256(url) - for human-readable IDs
- `status`: Processing state (new → scrape_error/extract_error/done)
- `source`: Optional user-supplied label for tracking
- `added_at`: ISO 8601 UTC timestamp when added
- `processed_at`: ISO 8601 UTC timestamp when completed
- `data`: JSON with LLM-extracted data and preprocessing info (see below)
- `error`: Error message if failed

**data JSON structure** (when status='done'):
```json
{
  "tokens_full": 50000,
  "tokens_stripped": 15000,
  "collect_duration": 12.34,
  "title": "Page title",
  "kind": "conference|newsletter|blog_aggregator|...",
  "collection_quality_score": 0.85,
  "comments": "2-4 sentence description",
  "links": [
    {
      "url": "https://...",
      "link_text": "verbatim link text",
      "context": "one-sentence context",
      "ai_safety_relevancy": 0.75
    }
  ]
}
```

**Notes:**
- `tokens_full`: Token count of full HTML
- `tokens_stripped`: Token count after preprocessing (scripts/styles removed)
- `collect_duration`: Total time for collection process in seconds
- Other fields are LLM-extracted

### classify table

Tracks URLs to classify (for AI safety/alignment relevance).

```sql
CREATE TABLE classify (
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
);

CREATE INDEX idx_classify_status ON classify(status);
CREATE INDEX idx_classify_source ON classify(source);
CREATE INDEX idx_classify_source_url ON classify(source_url);
CREATE INDEX idx_classify_added_at ON classify(added_at);
CREATE INDEX idx_classify_ai_safety_relevance ON classify(ai_safety_relevance);
CREATE INDEX idx_classify_shallow_review_inclusion ON classify(shallow_review_inclusion);
CREATE INDEX idx_classify_kind ON classify(kind);
CREATE INDEX idx_classify_url_hash ON classify(url_hash);
CREATE INDEX idx_classify_url_hash_short ON classify(url_hash_short);
```

**Fields:**
- `url`: URL to classify (primary key)
- `url_hash`: SHA256(url) - full 64-char hex
- `url_hash_short`: First 8 chars of SHA256(url) - for human-readable IDs
- `status`: Processing state (new → scrape_error/classify_error/done)
- `source`: "collect" or user-supplied label
- `source_url`: URL of collect source page (if from collect, **not a foreign key**)
- `collect_relevancy`: Relevancy score from collect phase (if applicable)
- `added_at`: ISO 8601 UTC timestamp when added
- `processed_at`: ISO 8601 UTC timestamp when completed
- `ai_safety_relevance`: AI safety/alignment topic relevance score 0.0-1.0 (from LLM)
- `shallow_review_inclusion`: Suitability for Shallow Review inclusion score 0.0-1.0 (from LLM)
- `kind`: Content type - independent of relevancy (see ClassifyKind enum below)
- `data`: JSON with classification results and preprocessing info (see below)
- `error`: Error message if failed

**data JSON structure** (when status='done'):
```json
{
  "tokens_full": 50000,
  "tokens_stripped": 15000,
  "classify_duration": 8.76,
  "title": "...",
  "authors": ["Author 1", "Author 2"],
  "author_organizations": ["Anthropic", "OpenAI"],
  "date": "2025-01-15",
  "published_year": 2025,
  "venue": "NeurIPS 2025",
  "kind": "paper_published",
  "contribution_type": "empirical_results",
  "summary": "2-3 sentence summary of the work",
  "key_result": "Main finding or contribution",
  "ai_safety_relevance": 0.85,
  "shallow_review_inclusion": 0.90,
  "categories": [
    {"id": "interpretability_mech", "score": 0.95},
    {"id": "evals_safety", "score": 0.75}
  ],
  "category_comment": "Explanation of category assignments",
  "confidence": 0.88
}
```

**Notes:**
- `tokens_full`: Token count of full HTML
- `tokens_stripped`: Token count after preprocessing
- `classify_duration`: Total time for classification process in seconds
- `title`, `authors`, `author_organizations`, `summary`, `key_result`: Basic metadata
- `date`: Publication date in ISO format YYYY-MM-DD (nullable)
- `published_year`: Publication year as integer (nullable)
- `venue`: Publication venue (nullable)
- `kind`: Content type (one of ClassifyKind enum values, also stored as column)
- `contribution_type`: Type of contribution (e.g., "empirical_results", "theoretical_framework")
- `ai_safety_relevance`, `shallow_review_inclusion`: Scores 0.0-1.0 (also stored as columns)
- `categories`: List of 1-3 category assignments with taxonomy leaf IDs and fit scores
- `category_comment`: Explanation for category assignments
- `confidence`: Overall classification confidence 0.0-1.0
- Other fields are LLM-extracted

### classify_feedback table

Stores human feedback on classification decisions (category assignments, inclusions, exclusions).

```sql
CREATE TABLE classify_feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    url_hash_short TEXT,
    feedback_source TEXT NOT NULL,
    feedback_timestamp TEXT NOT NULL,
    action TEXT NOT NULL,
    human_category TEXT,
    paper_id TEXT,
    link_text TEXT,
    notes TEXT,
    CHECK(action IN ('include', 'exclude', 'reclassify', 'note'))
);

CREATE INDEX idx_feedback_url ON classify_feedback(url);
CREATE INDEX idx_feedback_url_hash_short ON classify_feedback(url_hash_short);
CREATE INDEX idx_feedback_action ON classify_feedback(action);
CREATE INDEX idx_feedback_human_category ON classify_feedback(human_category);
CREATE INDEX idx_feedback_source ON classify_feedback(feedback_source);

-- Partial unique indexes to prevent true duplicates while allowing multi-category
CREATE UNIQUE INDEX idx_feedback_unique_single_action 
  ON classify_feedback(url, feedback_source, action, feedback_timestamp) 
  WHERE action IN ('include', 'exclude', 'note');

CREATE UNIQUE INDEX idx_feedback_unique_reclassify 
  ON classify_feedback(url, feedback_source, action, human_category, feedback_timestamp) 
  WHERE action = 'reclassify';
```

**Fields:**
- `url`: URL being reviewed (must match classify.url)
- `url_hash_short`: First 8 chars of SHA256(url) - for human-readable IDs
- `feedback_source`: Source of feedback (e.g., "SR2025-WIP-doc", "manual-review")
- `feedback_timestamp`: ISO 8601 UTC timestamp when feedback was recorded
- `action`: What to do with this item
  - `include`: Force inclusion in exports (even if below thresholds)
  - `exclude`: Force exclusion from exports (even if above thresholds)
  - `reclassify`: Override LLM category with human category
  - `note`: Annotation only (no effect on inclusion/exclusion, used for tracking)
- `human_category`: Taxonomy leaf category ID assigned by human (required for action='reclassify')
- `paper_id`: Optional ID from source document (for tracking)
- `link_text`: Original link text from source (for reference)
- `notes`: Optional comments or reasoning

**Usage:**
- Import feedback via `pipeline.py import-feedback <csv-file> --source "label" [--reclassify-obsolete-llm]`
- Classification phase checks for existing feedback and respects reclassification
- Export phase respects include/exclude actions and uses human categories when available
- **Multi-category support**: A URL can have multiple `reclassify` entries with different `human_category` values
  - Paper appears in all assigned categories in exports
  - Partial unique indexes prevent true duplicates while allowing multi-category assignments
- Auto-increment `id` as primary key eliminates need for timestamp hacks

**Special one-time flag: `--reclassify-obsolete-llm`**
- Use when taxonomy has changed and old categories no longer exist
- For papers NOT in CSV but with obsolete LLM-assigned categories:
  - Instead of excluding them, marks them for re-classification
  - Resets their status to `new` in classify table
  - Creates feedback with `action='note'` (annotation only, no forced inclusion/exclusion)
  - Papers are re-classified with current taxonomy and normal thresholds apply
  - After re-classification, papers with sr>=0.4 appear in exports marked with 🔄 emoji
  - Papers with sr<0.4 after re-classification are excluded (as expected)
- This is a **one-time migration behavior** when restructuring taxonomy

**Precedence rules:**
1. Most recent feedback (by timestamp) takes precedence for same URL+source
2. `exclude` action always wins (safety-first approach) - EXCEPT when `--reclassify-obsolete-llm` applies
3. `reclassify` overrides LLM category in exports
4. `include` forces inclusion regardless of scores

**Note keywords (for robust matching in code):**
- `NEEDS_RECATEGORIZATION`: Paper from CSV with obsolete category ID
- `RECLASSIFY_OBSOLETE_LLM`: Paper had obsolete LLM category, was re-classified

**Multi-category example:**
```
CSV rows:
  https://arxiv.org/abs/2410.12345,interp_sparse_coding,abc123,Paper X
  https://arxiv.org/abs/2410.12345,interp_applied,abc123,Paper X
  https://arxiv.org/abs/2410.12345,model_diff,abc123,Paper X

Feedback entries created:
  (id=1, url=..., action='reclassify', human_category='interp_sparse_coding')
  (id=2, url=..., action='include')
  (id=3, url=..., action='reclassify', human_category='interp_applied')
  (id=4, url=..., action='reclassify', human_category='model_diff')

Export behavior:
  Paper X appears in THREE sections: interp_sparse_coding, interp_applied, and model_diff
```

**Markers in exports (shown in brackets after title):**
- ⚠️ : Paper with `NEEDS_RECATEGORIZATION` (rare, needs manual recategorization)
- 🔄 : Paper with `RECLASSIFY_OBSOLETE_LLM` (one-time migration, already re-classified)
- ✌️(in N categories) : Paper appears in N categories (multi-category assignment)

**Example formatting:**
```markdown
- **[Paper Title](url)**, *Authors*, 2025, Venue, [🔄 ✌️(in 2 categories) paper_preprint, sr=0.75, id:abc12345] Summary...
```
This indicates: re-classified due to obsolete LLM category, appears in 2 categories total

## Classification Taxonomy

**Ground truth:** `data/taxonomy.yaml`

The classification taxonomy defines a hierarchical category structure for classifying AI safety/alignment content. Each classified item must be assigned to exactly one **leaf category**.

### Structure

- **Hierarchical organization**: Categories can contain subcategories
- **Leaf categories**: Only leaf nodes (categories without children) are assignable
- **Category fields**:
  - `id`: Machine-readable identifier (snake_case, unique across entire taxonomy)
  - `name`: Human-readable name
  - `description`: Detailed description of what belongs in the category
  - `children`: List of subcategories (empty for leaf categories)
  - `examples`: Optional list of example items from 2024 (ONLY allowed on leaf categories)
  - `is_leaf`: Can be explicitly set in YAML, otherwise inferred from presence of children

### Top-Level Categories

1. **Understand existing models** - Evals, interpretability, learning dynamics, model psychology
2. **Control the thing** - Alignment, monitoring, control, deception detection
3. **Alternative architectures** - Safer-by-design AI systems
4. **Better data** - Data quality, filtering, attribution for safety
5. **Make AI solve it** - Scalable oversight, debate, task decomposition
6. **Theory** - Agent foundations, corrigibility, cooperation theory
7. **Sociotechnical** - Approaches combining technical and social elements
8. **Misc / for new agenda clustering** - Items not yet fitting other categories

### Usage

- Load via `load_taxonomy()` from `taxonomy.py`
- Format for LLM prompts via `format_taxonomy_for_prompt()`
- Validate category IDs via `taxonomy.validate_category_id(cat_id)`
- Total: **103 leaf categories** (as of 2025-10-21)
- Includes 8 "other" catch-all categories for novel work not fitting existing categories

### Validation Rules

1. All category IDs must be unique across entire taxonomy
2. Category IDs must be alphanumeric with underscores/hyphens (snake_case)
3. Only leaf categories can have examples
4. At least one leaf category must exist

## File Formats

### Scraped HTML (.html.zst)

- **Format:** HTML text compressed with Zstandard level 15
- **Location:** `data/scraped/<hash>.html.zst`
- **Hash:** SHA256 of URL only
- **Access:** Use `open_scraped(url, mode)` or `get_scrape_path(url)` from `scrape.py`

### Parquet Files

When used, parquet files written with:
- Compression: Zstandard level 15
- Location: TBD based on output

## Enums and Constants

### SourceKind (collect.data.kind)

Types of collection sources:
- `conference` - Conference websites
- `newsletter` - Email newsletters, digests
- `blog_aggregator` - Aggregator sites (LessWrong, EA Forum)
- `resource_list` - Curated resource lists
- `workshop` - Workshop pages
- `summer_school` - Summer school programs
- `reading_list` - Reading/bibliography lists
- `organization_page` - Organization homepages
- `paper_page` - Individual paper page (no links to collect)
- `blocked_content` - Captcha, login wall, etc.
- `other` - Other types

### ClassifyKind (classify.kind)

Content type classification (independent of AI safety/alignment relevancy).

**Important:** `kind` describes the content type only. AI safety/alignment relevance is determined by two independent scores (0.0-1.0 each):
- `ai_safety_relevance`: How relevant the topic is to AI safety/alignment
- `shallow_review_inclusion`: How suitable for inclusion in Shallow Review (technical contribution)

Any kind can have any combination of scores.

Examples:
- `paper_published` + `ai_safety_relevance=0.9` + `shallow_review_inclusion=0.9` → relevant technical AI safety paper
- `paper_published` + `ai_safety_relevance=0.1` + `shallow_review_inclusion=0.1` → irrelevant paper (e.g., biology)
- `blog_post` + `ai_safety_relevance=0.8` + `shallow_review_inclusion=0.7` → relevant technical alignment post
- `news_announcement` + `ai_safety_relevance=0.8` + `shallow_review_inclusion=0.3` → news about safety work (no original research)

**Kind values:**

Research outputs:
- `paper_published` - Peer-reviewed paper in journal or conference proceedings
- `paper_preprint` - Preprint (arXiv, SSRN, etc.)
- `blog_post` - Blog post or article (general blogs, personal blogs)
- `lesswrong` - LessWrong or AI Alignment Forum post (special category due to importance in AI safety community)
- `video` - Video, talk recording, lecture
- `podcast` - Podcast episode or audio content
- `code_tool` - Software, library, tool, implementation
- `dataset_benchmark` - Dataset or benchmark release
- `agenda_manifesto` - Research agenda, roadmap, or manifesto
- `news_announcement` - News article or official announcement
- `social_media` - Social media post (strict criteria: major announcements only - see below)
- `course_educational` - Course materials, tutorials, educational content

Non-research content:
- `commercial` - Product/service pages, company pages
- `personal_page` - Personal homepages, bios

Access issues:
- `blocked` - Blocked access (captcha, login wall, paywall - content exists but inaccessible)
- `error_detected` - Content could not be accessed (429, 404, 5xx, format errors, parsing failures, etc.)
- `other` - Other content type

**Social media inclusion criteria:**

Social media posts (`social_media` kind) should be included ONLY when they are significant announcements:
- ✅ Include: New agenda announcements, breakthrough discoveries, major paper releases, significant research updates
- ❌ Exclude: Commentary, opinions, discussions, retweets, summaries of others' work

Examples of what to include:
- "Announcing our new research agenda on X"
- "We've discovered Y breakthrough result"
- "Released: new paper on Z" (if from authors)

Examples of what to exclude:
- "Here's my take on recent AI developments..."
- "Thread: Why I think approach X won't work"
- "Great paper by @someone on topic Y" (unless adding substantial new insight)

### Status Values

**CollectStatus:**
- `new` - Not yet processed
- `scrape_error` - Failed to scrape
- `extract_error` - LLM/extraction failed
- `done` - Successfully completed

**ClassifyStatus:**
- `new` - Not yet processed
- `scrape_error` - Failed to scrape
- `classify_error` - LLM/classification failed
- `done` - Successfully completed

## Data Flow

1. **Scraping**: URL → `scrape` table + `data/scraped/<hash>.html.zst`
2. **Collection**: Source URL → `collect` table → extract links → `classify` table
3. **Classification**: Candidate URL → `classify` table with results

**Key points:**
- Scrapes are shared across all phases (one scrape per URL)
- Links from collect are directly added to classify table (no intermediate table)
- Tables do NOT reference each other with foreign key constraints
- All timestamps are ISO 8601 with timezone (UTC)

## Database Access

Use `get_data_db()` from `data_db.py` to access the unified database:
- Thread-safe lazy singleton
- Creates tables/indexes on first access
- Don't hold connection for long periods
