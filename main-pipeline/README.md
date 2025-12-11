# Shallow Review

A data pipeline and research project for collecting, analyzing, and classifying content from web sources.

## Overview

This project implements a multi-phase pipeline for:
1. **Scraping**: Collecting web content with playwright
2. **Collection**: Extracting structured items from sources (using LLMs)
3. **Classification**: Categorizing and analyzing collected items (using LLMs)

## Installation

Requires Python ≥3.12 and `uv` for package management.

```bash
# Install dependencies
uv sync

# Install playwright browsers
uv run playwright install chromium
```

## Configuration

Create a `.env` file in the project root:

```bash
# Optional: Helicone API key for LLM observability
HELICONE_API_KEY=your_key_here

# Add your LLM provider API keys (e.g., OpenAI, Anthropic)
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

## Usage

```bash
# Run the pipeline
uv run python pipeline.py --help

# Show configuration and database statistics
uv run python pipeline.py info

# Add URLs to collect or classify phases
uv run python pipeline.py add urls.txt --phase auto

# Run collection phase
uv run python pipeline.py collect --limit 100 --workers 4

# Run classification phase
uv run python pipeline.py classify --limit 100 --workers 4

# Export classified papers grouped by taxonomy
uv run python pipeline.py export-taxonomy \
  --min-shallow-review 0.5 \
  --min-ai-safety 0.5 \
  --kinds paper_page,arxiv > output.md
```

## Project Structure

```
shallow-review/
├── shallow_review/      # Main package
│   ├── common.py        # Shared types, constants, paths
│   ├── utils.py         # File I/O, logging, console
│   ├── stats.py         # Statistics tracking
│   ├── llm.py           # LLM integration (litellm)
│   ├── scrape.py        # Web scraping (playwright)
│   ├── collect.py       # Collection phase (TODO)
│   ├── classify.py      # Classification phase (TODO)
│   └── cli.py           # CLI interface (typer)
├── prompts/             # Jinja2 templates for LLM prompts
├── data/                # Data storage (gitignored)
│   ├── scrape.db        # Scraping metadata
│   └── scraped/         # Cached HTML files (.html.zst)
├── runs/                # Log files (gitignored)
├── docs/
│   ├── DATA.md          # Data schema documentation
│   └── DEVLOG.md        # Development log
├── pipeline.py          # Entry point
└── AGENTS.md            # Instructions for AI assistants

```

## Development

See [AGENTS.md](AGENTS.md) for detailed development guidelines and architecture.

Key principles:
- **KISS**: Simple, readable code for agile research
- **Defensive programming**: Type checks and assertions, but not excessive
- **Fail visibly**: Don't mask errors
- **Thread-safe**: Global stats and DB connections use proper locking

## Documentation

- [AGENTS.md](AGENTS.md) - Development guidelines and architecture
- [docs/DATA.md](docs/DATA.md) - Data schemas and formats
- [docs/DEVLOG.md](docs/DEVLOG.md) - Development log and lessons learned

## Technology Stack

- **Language**: Python ≥3.11
- **Package Manager**: uv
- **CLI**: typer, rich
- **LLM**: litellm, jinja2, pydantic
- **Scraping**: playwright, beautifulsoup4, requests
- **Data**: polars, sqlite3, zstandard
- **Observability**: Helicone.ai

## License

(To be determined)

