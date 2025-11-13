# Shallow Review 2025 Scraping Scripts

Automated pipeline for conducting AI alignment literature reviews using arXiv papers, with intelligent filtering, deduplication, and curation.

## 1. AF and LW Scraper (Alignment Forum / LessWrong)

Fetch community posts for a given year and analyze them.

### Scrape

```bash
python AF-and-LW-scraper/1-scrape-AF-or-LW.py \
  --site alignment-forum --year 2025 --max-pages 200 --delay 1.0 \
  --out AF-and-LW-scraper/results/1-af_raw_posts.csv
```

LessWrong:

```bash
python AF-and-LW-scraper/1-scrape-AF-or-LW.py \
  --site lesswrong --year 2025 --max-pages 200 --delay 1.0 \
  --out AF-and-LW-scraper/results/1-lw_raw_posts.csv
```

### Analyze

```bash
python AF-and-LW-scraper/2-analyze-AF-or-LW-links.py \
  --in AF-and-LW-scraper/results/1-af_raw_posts.csv \
  --out-dir AF-and-LW-scraper/results \
  --year 2025 \
  --curated-max 200
```

Outputs in `AF-and-LW-scraper/results/`: filtered CSV, curated CSV, and summaries (`3-af_summaries_and_tags.{csv,md}`).

---

## 2. Arxiv Scraper

### 1. Install Dependencies

```bash
uv sync
```

### 2. Set OpenAI API Key

Create a `.env` file in the project root:

```bash
KEY=your-api-key-here
```

### 3. Run the Complete Pipeline

```bash
cd arxiv-scraper
./main.sh
```

This runs all scripts in sequence:
1. Scrape arXiv for papers
2. Filter by relevance to AI alignment
3. Extract existing links from DOCX (if needed)
4. Find unique papers (not in existing review or Lenz database)
5. Curate papers against review content
6. Generate taxonomy and editorial

**Final output:** `results/6-taxonomy-and-editorial.txt`

---

## Complete Pipeline Overview

See also: `AF-and-LW-scraper/README.md` for Alignment Forum / LessWrong usage.

### Script 1: ArXiv Scraper (`1-scrape.py`)

Searches arXiv and saves results to CSV.

**Usage:**
```bash
python 1-scrape.py [OPTIONS]
```

**Key Options:**
- `--query`: Custom arXiv search query
- `--start-date`: Start date (YYYYMMDDHHSS format, default: 202501010000)
- `--end-date`: End date (YYYYMMDDHHSS format, default: 202512312359)
- `--max-results`: Maximum results (default: 1000)
- `--output`: Output file (default: results/1-arxiv_raw_search_results.csv)

**Example:**
```bash
python 1-scrape.py --max-results 500
```

**Output:** `results/1-arxiv_raw_search_results.csv`

---

### Script 2: Relevance Filter (`2-filter_results.py`)

Uses LLM to tag and filter papers by relevance to technical AI alignment.

**Usage:**
```bash
python 2-filter_results.py [OPTIONS]
```

**Key Options:**
- `--input`: Input CSV (default: results/1-arxiv_raw_search_results.csv)
- `--annotated`: Output with all papers annotated (default: results/2-arxiv_annotated_results.csv)
- `--filtered`: Output with only highly relevant papers (default: results/2-arxiv_highly_relevant_results.csv)
- `--model`: OpenAI model (default: gpt-4.1)

**What's Filtered:**
- Core technical AI alignment work
- Novel contributions (techniques, empirical findings, tools)
- Papers with meaningful safety implications

**Output:**
- `results/2-arxiv_annotated_results.csv` - All papers with tags and ratings
- `results/2-arxiv_highly_relevant_results.csv` - Only highly relevant papers

---

### Script 3: DOCX Link Extractor (`3-docx_links_to_csv.py`)

Extracts all hyperlinks from a DOCX file for deduplication.

**Usage:**
```bash
python 3-docx_links_to_csv.py [OPTIONS]
```

**Key Options:**
- `--docx`: Input DOCX file (default: ./input/shallow-review-2025.docx)
- `--out`: Output CSV (default: results/shallow-review-2025-links.csv)

**Output:** `results/shallow-review-2025-links.csv` with columns: `title`, `url`

---

### Script 4: Find Unique Papers (`4-find-unique-arxiv-links.py`)

Identifies which papers are new (not already in the review or Lenz AI safety papers database).

**Usage:**
```bash
python 4-find-unique-arxiv-links.py [OPTIONS]
```

**Key Options:**
- `--arxiv`: Input highly relevant papers (default: results/2-arxiv_highly_relevant_results.csv)
- `--docx-links`: Existing review links (default: results/shallow-review-2025-links.csv)
- `--lenz-papers`: Lenz AI safety papers (default: input/lenz-ai-safety-papers.csv)
- `--new-only`: Output with only new papers (default: results/4-arxiv_new_links_only.csv)

**How it works:**
- Uses LLM to intelligently compare paper titles and arXiv IDs
- Checks against both review links and Lenz database
- Handles different URL formats (abs/ vs pdf/)

**Output:**
- `results/4-arxiv_links_with_new_flag.csv` - All papers with is_new flag
- `results/4-arxiv_new_links_only.csv` - Only new papers

---

### Script 5: Curate Papers (`5-curate-unique-arxiv-links.py`)

Evaluates new papers against the full review content to determine which should be included.

**Usage:**
```bash
python 5-curate-unique-arxiv-links.py [OPTIONS]
```

**Key Options:**
- `--arxiv`: Input new papers (default: results/4-arxiv_new_links_only.csv)
- `--post`: Review content (default: input/shallow-review-2025.txt)
- `--relevant-only`: Output with curated papers (default: results/5-arxiv_curated_relevant_only.csv)
- `--model`: OpenAI model (default: gpt-5-mini)

**Curation Criteria:**
- Relevance and quality bar
- Contribution to existing agenda
- Contribution to new agenda (high bar)
- Not redundant with existing content

**Output:**
- `results/5-arxiv_curated_with_flags.csv` - All papers with curation flags
- `results/5-arxiv_curated_relevant_only.csv` - Only papers to include

---

### Script 6: Generate Taxonomy & Editorial (`6-create-taxonomy-and-editorial-from-curated-links.py`)

Creates final structured output with taxonomy, editorial, and paper summaries.

**Usage:**
```bash
python 6-create-taxonomy-and-editorial-from-curated-links.py [OPTIONS]
```

**Key Options:**
- `--input`: Curated papers (default: results/5-arxiv_curated_relevant_only.csv)
- `--output`: Output text file (default: results/6-taxonomy-and-editorial.txt)
- `--model`: OpenAI model (default: gpt-5-mini)

**Output Structure:**
1. **EDITORIAL** - 100-500 word overview of AI alignment progress in 2025
2. **TAXONOMY** - Hierarchical categorization of all papers
3. **TODO LIST** - Checklist of all papers with `- [ ]` format
4. **PAPER SUMMARIES** - Full details with links, summaries, and taxonomy tags

**Output:** `results/6-taxonomy-and-editorial.txt`

---

## Running Individual Scripts

You can run any script individually for testing or custom workflows:

```bash
# Just scrape papers
python 1-scrape.py --max-results 100

# Just filter existing results
python 2-filter_results.py --input my_papers.csv

# Just generate taxonomy from curated papers
python 6-create-taxonomy-and-editorial-from-curated-links.py
```

---

## File Structure

```
arxiv-scraper/
├── 1-scrape.py                    # ArXiv scraper
├── 2-filter_results.py            # Relevance filter
├── 3-docx_links_to_csv.py         # DOCX link extractor
├── 4-find-unique-arxiv-links.py   # Deduplication
├── 5-curate-unique-arxiv-links.py # Curation
├── 6-create-taxonomy-and-editorial-from-curated-links.py  # Final generation
├── main.sh                        # Complete pipeline
├── input/                         # Input files
│   ├── shallow-review-2025.docx   # Existing review (DOCX)
│   ├── shallow-review-2025.txt    # Existing review (text)
│   └── lenz-ai-safety-papers.csv  # Lenz database
└── results/                       # Output files
    ├── 1-arxiv_raw_search_results.csv
    ├── 2-arxiv_annotated_results.csv
    ├── 2-arxiv_highly_relevant_results.csv
    ├── 4-arxiv_links_with_new_flag.csv
    ├── 4-arxiv_new_links_only.csv
    ├── shallow-review-2025-links.csv
    ├── 5-arxiv_curated_with_flags.csv
    ├── 5-arxiv_curated_relevant_only.csv
    └── 6-taxonomy-and-editorial.txt  # ← Final output
```

---


## Development

### Adding Dependencies

```bash
# Add a new package
uv add package-name

# Update all packages
uv sync
```

### Modifying System Prompts

Each script has a `SYSTEM_PROMPT` constant near the top. Modify these to change LLM behavior for filtering, deduplication, or curation.
