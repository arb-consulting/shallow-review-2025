# Shallow review tools and pipelines

A collection of tools and pipelines for Shallow Review of Technical AI Safety 2025.

## `collect-classify`

One of the main pipelines for Shallow Review of Technical AI Safety 2025. It collects prospective links to papers & posts from given pages, scrape these, and classify them for inclusion/exclusion into the review and assigns best-guess categories. It also contains the current taxonomy tree (`taxnonomy.yaml`), code to record changes on the main doc as human feedback about the papers (inclusion/exclusion and assigned categories), and several other utility scripts. It also contains the scraped pages (`data/scraped/`) and an SQLite database with all the collected and classified documents (`data/data.db`). Written and maintained by gavento.

## `scraping-scripts`

Contains the Alignment Forum / LessWrong and Arxiv scrapers.

Standalone scrapers and small pipelines used to gather candidate content for the review. These produce CSVs and text artifacts that can be inspected directly or fed into other tooling. `AF-and-LW-scraper` is used to gather candidate content from the Alignment Forum and LessWrong, while `arxiv-scraper` is used to gather candidate content from Arxiv. Both produce CSV files as output. Both directories also contain scripts for filtering and curating the output to produce a final list of candidate content. For installation and usage examples and `scraping-scripts/README.md`. Written by smcaleese.
