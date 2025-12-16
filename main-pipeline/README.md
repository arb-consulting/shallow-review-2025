# Shallow Review of Technical AI Safety 2025 - data and pipelines

This is the main repository for the Shallow Review of Technical AI Safety 2025, containing both the data and code of our pipeline, in the hopes that it may be useful to others.

## Data

### Exported agendas and outputs

The exported agendas (86) and included output items (827) are also available as CSV files in the [`main-pipeline/data/2025-12-16-draft-post-review`](main-pipeline/data/2025-12-16-draft-post-review) directory as `agendas.csv` and `papers.csv`. Note that these do not contain all the information available in the machine-readable data below (e.g. some extra attributes for "Labs" agendas, subsections of outputs, etc.) but may be suitable for simple analysis and data processing. Note that in `papers.csv`, the `link_text` column is what we are using in the review (it may or may not match the `title` column). The agendas do not contain the China and Other "Labs" agendas, and the other "Labs" agendas use slightly different attributes from all the others, limiting their usefulness for further processing (feel free to filter them out).

You can also find the tables as Google sheets here: [agendas](https://docs.google.com/spreadsheets/d/1uwqeSkl1fGO7bWbbDdNi5QbJ_Zw_a6HO-XlnO18ohLc/edit?gid=249818450#gid=249818450), [outputs](https://docs.google.com/spreadsheets/d/1uwqeSkl1fGO7bWbbDdNi5QbJ_Zw_a6HO-XlnO18ohLc/edit?gid=803096912#gid=803096912).

### Full machine-readable data

The machine-readable export of the final version is stored in the [`main-pipeline/data/2025-12-16-draft-post-review`](main-pipeline/data/2025-12-16-draft-post-review) directory as both JSON and YAML (same data). [`source.md`](main-pipeline/data/2025-12-16-draft-post-review/source.md) is the final version of the reviewer document as Markdown the data was extracted from with `uv run ./process_draft.py parse []...]`.

[`main-pipeline/data/taxonomy.yaml`](main-pipeline/data/taxonomy.yaml) is the taxonomy of the categories and subcategories as of the final version of the source document.

### Data.db

The main SQLite database file is [`main-pipeline/data/data.db`](main-pipeline/data/data.db) and has the following tables (no foreign key constraints though there are relations between the tables):

- The `classify` table has the most valuable informationcontains the information about all the collected links, and for most of them their extracted metadata (title, authors, summary, etc.) and their classification scores (ai_safety_relevance, shallow_review_inclusion). Note that some of the category IDs suggested there do not match the current `taxonomy.yaml`, as the hierarchy has been evolving throughout our process.
- The `scrape` table contains the metadata for the scraped links. These are stored under `main-pipeline/data/scraped`.
- The `collect` is an auxiliary table collecting pages to collect additional paper links from, and the collection results.

The database is the main source of truth about the outputs (scrapes, metadata, LLM classification etc.) but also stores the state of each record, allowing for incremental processing of various stages of the pipeline.

### Link and paper scrapes

All the links were scraped with a selenium browser, and the HTML was stored in the  directory. These are URL hashes, and primarily referenced by the `scrape` table in the `data.db` database.

### URL lists

We collected URLs from a variety of sources. Most (but not all) of them can be found in various forms under the `main-pipeline/data/sources-links` directory.

## Pipeline code

*Caveat emptor:* The pipline code has evolved dramatically over the course of the project, and is not meant to be a stable codebase. The current version was used to generate the machine-readable data of the final version of the reviewer document but some components may be outdated in various ways (e.g. early link collection). The main use of the codebase is for the prompts and templates, querying details of the process of LLMs, internally as the basis for next-gen tooling we'll create, and code archeology material.

### Technical overview

Requires Python ≥3.12 and `uv` for package management.

```bash
# Install dependencies
uv sync

# Install playwright browsers
uv run playwright install chromium
```

Create a `.env` file in the project root:

```bash
# Optional: Helicone API key for LLM observability
# Required for data extraction pipeline
HELICONE_API_KEY=your_key_here

# Add your LLM provider API keys (e.g., OpenAI, Anthropic)
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

## License

(To be determined)

