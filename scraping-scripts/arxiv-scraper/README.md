### ArXiv Scraper

Scripts to search arXiv, filter for AI alignment relevance, dedupe against existing links, curate, and generate a taxonomy/editorial.

### Quickstart

1) From this folder:

```bash
./main.sh
```

This runs the full pipeline and writes the final output to:
- `results/6-taxonomy-and-editorial.txt`

2) Run individual steps (examples):

```bash
# 1) Scrape arXiv
python 1-scrape.py --max-results 500 --output results/1-arxiv_raw_search_results.csv

# 2) Filter for relevance (writes annotated + highly-relevant CSVs)
python 2-filter_results.py --input results/1-arxiv_raw_search_results.csv

# 4) Find unique new links vs prior review + Lenz database
python 4-find-unique-arxiv-links.py \
  --arxiv results/2-arxiv_highly_relevant_results.csv \
  --docx-links results/shallow-review-2025-links.csv \
  --lenz-papers input/lenz-ai-safety-papers.csv

# 6) Create taxonomy + editorial from curated links
python 6-create-taxonomy-and-editorial-from-curated-links.py \
  --input results/5-arxiv_curated_relevant_only.csv \
  --output results/6-taxonomy-and-editorial.txt
```

### Outputs
- `results/1-arxiv_raw_search_results.csv`
- `results/2-arxiv_annotated_results.csv`
- `results/2-arxiv_highly_relevant_results.csv`
- `results/4-arxiv_links_with_new_flag.csv`
- `results/4-arxiv_new_links_only.csv`
- `results/5-arxiv_curated_with_flags.csv`
- `results/5-arxiv_curated_relevant_only.csv`
- `results/6-taxonomy-and-editorial.txt` (final)

### Notes
- See the project root `README.md` for detailed options, costs, and troubleshooting.

