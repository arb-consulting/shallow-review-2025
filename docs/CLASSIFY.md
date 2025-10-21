# Classify Process

Documentation for the classification phase: determining AI safety/alignment relevance.

## Purpose

Classify processes candidate URLs (from collect or manual addition) to determine if they are relevant AI safety/alignment content and extract detailed metadata.

**AI Safety Scope**: Following the Shallow Review 2024 definition, we target "work that intends to prevent very competent cognitive systems from having large unintended effects on the world." This includes:
- Technical AI alignment and safety research
- Interpretability and understanding of AI systems
- AI control, monitoring, and evaluation methods
- Multi-agent AI safety and coordination
- Formal methods, verification, and provable safety
- Agent foundations and theoretical alignment work
- Governance-adjacent technical work (evals, standards, etc.)
- Borderline technical topics that offer novel causal perspectives on AI X-risk

**Intent over method**: If work aims to understand or prevent unintended effects from advanced AI systems, it's relevant, regardless of the specific technical approach or framing used.

**Content types**: Papers, blog posts, videos, social media announcements (see criteria in DATA.md), etc. - format matters less than content and intent.

## Design Philosophy

- **Fine-grained filtering**: More selective than collect phase
- **Rich metadata extraction**: Extracts title, authors, topics, summary, etc.
- **Prioritization**: High-relevancy candidates from collect processed first
- **Flexible sources**: Accepts both auto-added (from collect) and manually added URLs

## Process Flow

1. **Add candidates manually** (optional):
   - `pipeline.py add <file> --phase classify --source "label"`
   - URLs added to `classify` table with status='new'
   - Optional source label for tracking

2. **Auto-add from collect**:
   - Links with relevancy ≥ threshold automatically added during collect
   - source='collect', source_url set, collect_relevancy stored

3. **Run classification**: `pipeline.py classify --limit N --workers W --relevancy 0.5`
   - Queries `classify` table WHERE status='new'
   - Optional prioritization by collect_relevancy (high → low)
   - For each candidate:
     a. Scrape page (kind="classify")
     b. Preprocess HTML
     c. Check token limit
     d. Send to LLM with classification prompt
     e. Parse and validate JSON response
     f. Store results in `classify.data` JSON field
     g. Update status to 'done' or error status

## Configuration

Via `RunClassifyConfig` in `common.py`:
- `limit`: Max candidates to process (default: 100)
- `workers`: Thread pool size (default: 4, max: 32)
- `relevancy_threshold`: Min score for high priority (default: 0.5)
  - Used for prioritization, not filtering
- `model`: LLM model (default: "claude-sonnet-4")
- `max_html_tokens`: Token limit (default: 100,000)

## Classification Output

Stored as columns:
- `classify_relevancy`: 0.0-1.0 score (AI safety/alignment relevance)
- `kind`: Content type - independent of relevancy (see ClassifyKind enum in DATA.md)
  - Example: `paper_page` can be relevant (0.9) or irrelevant (0.1)
  - All content gets both a kind and a relevancy score
  - For `social_media` kind: stricter criteria apply (see DATA.md) - only announcements and major events etc.
- `category`: One leaf category ID from taxonomy (see taxonomy section below)

LLM extracts detailed metadata (stored in data JSON):
- `tokens_full`: Full HTML token count
- `tokens_stripped`: Stripped HTML token count
- `title`: Paper/post title
- `authors`: List of authors
- `published_date`: Publication date (if available)
- `topics`: List of topics (alignment, interpretability, etc.)
- `summary`: 2-3 sentence summary
- `key_points`: List of key points
- `venue`: Publication venue (if applicable)
- `arxiv_id`: ArXiv ID (if applicable)
- `organization`: Affiliated organization (if applicable)

**Exact schema TBD** - prompts not yet implemented.

## Taxonomy

**Ground truth:** `data/taxonomy.yaml` (see DATA.md for details)

Each classified item must be assigned to exactly ONE leaf category from the taxonomy. The taxonomy has 8 top-level categories with 95 assignable leaf categories:

1. **Understand existing models** - Evals, interpretability, learning dynamics, model psychology
2. **Control the thing** - Alignment, monitoring, control, deception detection
3. **Alternative architectures** - Safer-by-design AI systems
4. **Better data** - Data quality, filtering, attribution for safety
5. **Make AI solve it** - Scalable oversight, debate, task decomposition
6. **Theory** - Agent foundations, corrigibility, cooperation theory
7. **Sociotechnical** - Approaches combining technical and social elements
8. **Misc / for new agenda clustering** - Items not yet fitting other categories

**Usage:**
- Load: `from shallow_review.taxonomy import load_taxonomy; tax = load_taxonomy()`
- Format for prompts: `format_taxonomy_for_prompt(tax)` → hierarchical markdown
- Validate: `tax.validate_category_id(cat_id)` → bool (checks if valid leaf)
- Get all leaves: `tax.get_all_leaf_ids()` → list[str]

The taxonomy is formatted hierarchically in prompts, with non-leaf categories as headers and leaf categories as bulleted items with IDs.

## HTML Preprocessing

Same as collect phase:
- Remove completely: `<script>`, `<style>`, `<noscript>`, `<svg>` tags
- Remove: HTML comments (via BeautifulSoup)
- Remove: Base64-encoded images (data: URIs)
- Unwrap (keep content): `<div>`, `<span>` tags
- Strip attributes: Keep only href on links, src/alt on images
- Collapse excessive whitespace
- Track token counts (tokens_full, tokens_stripped stored in data JSON)

See COLLECT.md for detailed preprocessing policy and rationale.

## Deduplication

- **URL is primary key**: Each URL classified only once
- Duplicate additions fail silently (ON CONFLICT DO NOTHING)
- Stats track "already_exists" count

## Error Handling

**scrape_error:**
- Failed to fetch the page
- Cached in scrape table, propagated to classify
- NOT retried automatically

**classify_error:**
- LLM call failed or JSON parsing/validation failed
- Can retry with `--retry-errors` flag (re-runs LLM, uses cached HTML)
- Error message stored with 2 levels of traceback

**Token limit exceeded:**
- HTML exceeds max_html_tokens after preprocessing
- Status set to classify_error

## Prompt Design

**TODO:** `prompts/classify.yaml` not yet implemented.

**Planned aspects:**
- Clear definition of AI safety/alignment scope
- Examples of relevant vs irrelevant content
- Detailed output schema specification
- Instructions for extracting metadata
- JSON output format with validation

## CLI Flags

**`classify` command:**
- `--limit N`: Process at most N candidates
- `--workers W`: Use W worker threads (default: 4)
- `--relevancy R`: Min relevancy for high priority (default: 0.5)
- `--model M`: LLM model to use
- `--retry-errors`: Retry classify_error items (uses cached HTML)

## Statistics

Tracked per run:
- Candidates: new, cached, errors (by type)
- Tokens: HTML size (full vs stripped, mean, std, min, max)
- Tokens: LLM usage (cache_read, cache_write, uncached, cost)
- Relevancy distribution: How many at each classify_relevancy score level
- Kind distribution: Count by content type

## Implementation Status

- **Database**: ✅ Fully implemented (`classify` table in data.db)
- **CLI**: ✅ `add` command supports --phase classify
- **Processing**: ❌ `compute_classify()` not yet implemented
- **Prompts**: ❌ `prompts/classify.yaml` not yet created
- **CLI command**: ❌ `classify` command not yet implemented

## Notes

- Similar structure to collect phase
- Reuses scraping and preprocessing infrastructure
- Classification more detailed than collection relevancy scoring
- No multi-threading yet (deferred for MVP)

## Database Schema

See `docs/DATA.md` for classify table schema and JSON structures.

