# Collect Process

Documentation for the collection phase: extracting links from aggregator pages.

## Purpose

Collect scrapes and parses HTML pages of conferences, newsletters, survey posts, summer schools, etc., extracting links that potentially point to AI safety/alignment-relevant content.

**AI Safety Scope**: Following the Shallow Review 2024 definition, we target "work that intends to prevent very competent cognitive systems from having large unintended effects on the world." This includes:
- Technical AI alignment and safety research
- Interpretability and understanding of AI systems
- AI control and monitoring
- Multi-agent AI safety and coordination
- Formal methods and verification for AI
- Governance-adjacent technical work
- Borderline technical topics (e.g., Gradual Disempowerment, Multi-Agent Risk scenarios) that offer novel causal views on AI X-risk

**Intent over method**: If work aims to understand or prevent unintended effects from advanced AI, it's relevant, regardless of specific technical approach.

## Source Types

We collect from diverse aggregator pages:
- **Academic**: Conference pages, workshop pages, summer schools
- **Community**: Newsletter archives, blog aggregators, reading lists
- **Organizations**: Research org pages, resource compilations
- **Social media**: Twitter/X threads, Reddit posts (STRICT CRITERIA - see below)

**Social media inclusion criteria**:
- ✅ Include: Major announcements (new agendas, breakthrough results, paper releases)
- ❌ Exclude: Commentary, opinions, discussions, retweets
- Use sparingly - most social media content is too ephemeral or low-signal

Examples:
- ✅ "Announcing our new interpretability research agenda..."
- ✅ "Released: paper on X-risk from multi-agent systems"
- ❌ "Here's my hot take on the latest alignment debate..."
- ❌ "Thread: why I'm skeptical of approach X"

## Design Philosophy

- **Inclusive over exclusive**: Better false positives than false negatives
- **Coarse filtering**: This phase casts a wide net; fine filtering happens in classify
- **Context-aware**: Uses surrounding text and page structure, not just link text
- **Traceable**: Stores relevancy scores and context for debugging

## Process Flow

1. **Add sources**: `pipeline.py add <file> --phase collect --source "label"`
   - URLs added to `collect` table with status='new'
   - Optional source label for tracking provenance

2. **Run collection**: `pipeline.py collect --limit N --workers W --relevancy 0.3`
   - Queries `collect` table WHERE status='new'
   - For each source:
     a. Scrape page (kind="collect")
     b. Preprocess HTML (strip scripts, styles, base64 images)
     c. Check token limit (error if exceeds max_html_tokens)
     d. Send to LLM with collection prompt
     e. Parse and validate JSON response
     f. Store results in `collect.data` JSON field
     g. Add links with relevancy ≥ threshold to `classify` table
     h. Update status to 'done' or error status

## Configuration

Via `RunCollectConfig` in `common.py`:
- `limit`: Max sources to process (default: 100)
- `workers`: Thread pool size (default: 4, max: 32)
- `relevancy_threshold`: Min score to promote to classify (default: 0.3)
- `model`: LLM model (default: "claude-sonnet-4")
- `max_html_tokens`: Token limit (default: 100,000)

## Link Extraction

LLM extracts links with:
- `url`: Link URL (verbatim from HTML)
- `link_text`: Text of the link (verbatim)
- `context`: One-sentence context about surrounding content
- `ai_safety_relevancy`: Score 0.0-1.0 (likelihood of relevance)

**Relevancy threshold:**
- Default: 0.3 (configurable)
- Links ≥ threshold automatically added to `classify` table
- Links < threshold discarded (not stored)

## HTML Preprocessing

Before sending to LLM:
1. **Remove completely**: `<script>`, `<style>`, `<noscript>`, `<svg>` tags and their content
2. **Remove**: HTML comments (via BeautifulSoup)
3. **Remove**: Base64-encoded images (data: URIs)
4. **Unwrap** (keep content): `<div>`, `<span>` tags
5. **Strip attributes**: Remove all except whitelisted ones (see below)
6. **Collapse whitespace**: Excessive newlines and spaces
7. **Track metrics**: Token counts (tokens_full, tokens_stripped stored in data JSON)

**Rationale:** Reduces tokens by 60-95% while preserving semantic content and links.

**Tags removed completely:**
- `<script>`, `<style>`: JavaScript and CSS (not needed)
- `<link>`: Stylesheets, fonts, preconnects (not needed)
- `<noscript>`, `<svg>`: Alternative content and graphics (not needed)

**Tags unwrapped (content preserved):**
- `<div>`, `<span>`: Layout containers (content inserted into parent)

**Attributes kept:**
- `href` on `<a>` tags (essential for link extraction)
- `src` and `alt` on `<img>` tags (for image context)
- **All other attributes removed**: data-*, id, class, style, onclick, aria-*, etc.

## Source Kind Classification

LLM classifies source page into one of these kinds:
- `conference`, `newsletter`, `blog_aggregator`, `resource_list`
- `workshop`, `summer_school`, `reading_list`, `organization_page`
- `paper_page` - Individual paper (no links to collect)
- `blocked_content` - Captcha, login wall, etc.
- `other` - Other types

**collection_quality_score (0.0-1.0):**
- Indicates how much the page is a collection of AI safety/alignment literature
- Helps catch mistakenly inserted links
- Identifies pages needing manual scraping (blocked_content)

## Deduplication

- **Sources**: URL is primary key in `collect` table
  - Same URL cannot be added twice
  - Re-adding tracked in stats as "already_exists"

- **Links**: No deduplication in collect phase
  - All extracted links sent to classify phase
  - Classify table enforces uniqueness (first insert wins)

## Error Handling

**scrape_error:**
- Failed to fetch the page
- Cached in scrape table, propagated to collect
- NOT retried automatically

**extract_error:**
- LLM call failed or JSON parsing/validation failed
- Can retry with `--retry-errors` flag (re-runs LLM, uses cached HTML)
- Error message stored with 2 levels of traceback

**Token limit exceeded:**
- HTML exceeds max_html_tokens after preprocessing
- Status set to extract_error
- Requires manual intervention or config adjustment

## Prompt Design

See `prompts/collect.yaml` for full prompts.

**Key aspects:**
- Clear scope definition (what IS and ISN'T AI safety/alignment)
- Positive and negative examples
- Scoring rubric with examples
- Instructions to extract links ≥ 0.3 relevancy
- Handles edge cases (relative URLs, navigation links)
- Requests JSON output with specified schema

## CLI Flags

**`collect` command:**
- `--limit N`: Process at most N sources
- `--workers W`: Use W worker threads (default: 4)
- `--relevancy R`: Min relevancy to promote to classify (default: 0.3)
- `--model M`: LLM model to use
- `--retry-errors`: Retry extract_error items (uses cached HTML)

## Statistics

Tracked per run:
- Sources: new, cached, errors (by type)
- Links: extracted, promoted to classify
- Tokens: HTML size (full vs stripped, mean, std, min, max)
- Tokens: LLM usage (cache_read, cache_write, uncached, cost)

## Notes and Observations

- **Link promotion**: Happens inline during collection (no separate step)
- **No multi-threading yet**: Single-threaded for MVP (threading flag accepted but not implemented)
- **Transaction scope**: Per-item commits (enables resume after failure/shutdown)
- **Graceful shutdown**: SIGINT/SIGTERM handled, completes current item
- **Progress bar**: Rich progress bar for top-level operation only

## Database Schema

See `docs/DATA.md` for collect table schema and JSON structures.

