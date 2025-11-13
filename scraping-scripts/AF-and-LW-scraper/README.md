### AF and LW Scraper

Minimal scripts to fetch posts from Alignment Forum or LessWrong by year and write CSV outputs.

### Structure

- `1-scrape-AF-or-LW.py`: Scrape AF or LW posts for a year into CSV.
- `results/`: Outputs (e.g., `1-af_raw_posts.csv`).
- `notebooks/`, `archive/`, `input/`: Supporting/archived materials.
- `utils.py` and other scripts may exist for follow-up processing.

### Quickstart

Scrape Alignment Forum (2025):

```bash
python AF-and-LW-scraper/1-scrape-AF-or-LW.py \
  --site alignment-forum --year 2025 --max-pages 200 --delay 1.0 \
  --out AF-and-LW-scraper/results/1-af_raw_posts.csv
```

Scrape LessWrong (2025):

```bash
python AF-and-LW-scraper/1-scrape-AF-or-LW.py \
  --site lesswrong --year 2025 --max-pages 200 --delay 1.0 \
  --out AF-and-LW-scraper/results/1-lw_raw_posts.csv
```

Flags:
- `--site`: `alignment-forum` or `lesswrong`
- `--year`: year to fetch (default 2025)
- `--max-pages`: number of 50-item pages to request (default 200)
- `--delay`: seconds between requests (default 1.0)
- `--out`: output CSV path

Notes:
- Pagination uses limit=50 and offset; the script stops when fewer than 50 items are returned.
- Titles are written as-is from the API.

### Analyze and curate

Run the analysis script to filter, dedupe, rank, and emit summaries files.

Basic usage (Alignment Forum raw CSV):

```bash
python AF-and-LW-scraper/2-analyze-AF-or-LW-links.py \
  --in AF-and-LW-scraper/results/1-af_raw_posts.csv \
  --out-dir AF-and-LW-scraper/results \
  --year 2025 \
  --curated-max 200
```

Outputs written to `results/`:
- `2-af_filtered_posts.csv`
- `3-af_summaries_and_tags.csv`
- `3-af_summaries_and_tags.md`
- `4-af_curated.csv`

Optional flags:
- `--keywords kw1 kw2 ...`: override default relevance keywords
- `--summarize`: reserved flag; summary fields are currently derived from excerpts
