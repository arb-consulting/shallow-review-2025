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

### scrape table

Stores metadata for scraped web pages.

```sql
CREATE TABLE scrape (
    url TEXT PRIMARY KEY,
    url_hash TEXT NOT NULL UNIQUE,
    kind TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    status_code INTEGER,
    error TEXT,
    data JSON
);

CREATE INDEX idx_scrape_url_hash ON scrape(url_hash);
CREATE INDEX idx_scrape_kind ON scrape(kind);
CREATE INDEX idx_scrape_timestamp ON scrape(timestamp);
```

**Fields:**
- `url`: Original URL (primary key - unique)
- `url_hash`: SHA256(url) for file naming
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
```

**Fields:**
- `url`: Source page URL (primary key)
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
    status TEXT NOT NULL,
    source TEXT NOT NULL,
    source_url TEXT,
    collect_relevancy REAL,
    added_at TEXT NOT NULL,
    processed_at TEXT,
    classify_relevancy REAL,
    kind TEXT,
    data JSON,
    error TEXT,
    CHECK(status IN ('new', 'scrape_error', 'classify_error', 'done'))
);

CREATE INDEX idx_classify_status ON classify(status);
CREATE INDEX idx_classify_source ON classify(source);
CREATE INDEX idx_classify_source_url ON classify(source_url);
CREATE INDEX idx_classify_added_at ON classify(added_at);
CREATE INDEX idx_classify_relevancy ON classify(classify_relevancy);
CREATE INDEX idx_classify_kind ON classify(kind);
```

**Fields:**
- `url`: URL to classify (primary key)
- `status`: Processing state (new → scrape_error/classify_error/done)
- `source`: "collect" or user-supplied label
- `source_url`: URL of collect source page (if from collect, **not a foreign key**)
- `collect_relevancy`: Relevancy score from collect phase (if applicable)
- `added_at`: ISO 8601 UTC timestamp when added
- `processed_at`: ISO 8601 UTC timestamp when completed
- `classify_relevancy`: AI safety/alignment relevancy score 0.0-1.0 (from LLM)
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
  "authors": ["..."],
  "published_date": "...",
  "topics": ["alignment", "interpretability"],
  "summary": "2-3 sentence summary",
  "key_points": ["..."],
  "venue": "...",
  "arxiv_id": "...",
  "organization": "..."
}
```

**Notes:**
- `tokens_full`: Token count of full HTML
- `tokens_stripped`: Token count after preprocessing
- `classify_duration`: Total time for classification process in seconds
- `classify_relevancy` and `kind` stored as columns (not in data JSON)
- `category`: Assigned category ID from taxonomy (stored as column in future versions)
- Other fields are LLM-extracted

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
- Total: **95 leaf categories** (as of 2025-10-21)

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

**Important:** `kind` describes the content type only. AI safety/alignment relevance is determined by the `classify_relevancy` score (0.0-1.0). Any kind can have any relevancy score.

Examples:
- `paper_page` + `classify_relevancy=0.9` → relevant AI safety paper
- `paper_page` + `classify_relevancy=0.1` → irrelevant paper (e.g., biology)
- `blog_post` + `classify_relevancy=0.8` → relevant alignment blog post
- `blog_post` + `classify_relevancy=0.0` → irrelevant blog post

**Kind values:**

Research content:
- `paper_page` - Academic paper page (HTML)
- `paper_pdf` - PDF paper
- `arxiv` - ArXiv paper page

Online content:
- `blog_post` - Blog post or article
- `lesswrong` - LessWrong or AI Alignment Forum post
- `news_article` - News article
- `social_media` - Twitter, Reddit, etc. posts (announcements only - see below)

Media:
- `video` - Video content (YouTube, etc.)
- `podcast` - Podcast episode

Educational:
- `course` - Course or tutorial
- `slides` - Presentation slides

Other:
- `commercial` - Product/service pages
- `personal_page` - Personal homepage
- `404` - Page not found
- `blocked` - Blocked access (captcha, login, etc.)
- `other` - Other types

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
