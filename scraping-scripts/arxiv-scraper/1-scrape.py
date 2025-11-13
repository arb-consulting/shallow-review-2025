#!/usr/bin/env python3
"""
ArXiv Search Script
Searches arXiv for papers matching specified criteria and saves results to CSV.
"""

import argparse
import time
import logging
from pathlib import Path
import arxiv
import pandas as pd

# Default configuration
DEFAULT_QUERY = 'cat:cs.* AND (all:"ai safety" OR all:"ai alignment")'
DEFAULT_MAX_RESULTS = 1000
DEFAULT_START_DATE = "202501010000"  # YYYYMMDDHHSS format
DEFAULT_END_DATE = "202512312359"
DEFAULT_OUTPUT_FILE = "1-arxiv_raw_search_results.csv"
DEFAULT_PAGE_SIZE = 500
DEFAULT_DELAY_SECONDS = 3.0
DEFAULT_RETRIES = 5

# Setup logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("arxiv-search")


def search_arxiv(
    query: str,
    limit: int = 10_000,
    page_size: int = 500,
    delay_seconds: float = 3.0,
    retries: int = 5,
    sort_by: arxiv.SortCriterion = arxiv.SortCriterion.SubmittedDate,
    sort_order: arxiv.SortOrder = arxiv.SortOrder.Descending,
):
    """
    Robust arXiv fetcher that:
      - Uses Client.results(search, offset=...) (correct for v2 API)
      - Recovers from UnexpectedEmptyPageError / HTTPError by resuming at the current offset
      - De-dups by arXiv ID
    Returns: list[dict]
    """
    client = arxiv.Client(
        page_size=page_size,
        delay_seconds=delay_seconds,
        num_retries=retries,
    )

    search = arxiv.Search(
        query=query,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    results, seen = [], set()
    offset = 0
    consecutive_failures = 0
    backoff = delay_seconds

    def add_result(r):
        arxiv_id = r.entry_id.split("/")[-1]
        if arxiv_id in seen:
            return False
        seen.add(arxiv_id)
        results.append({
            "title": r.title,
            "authors": ", ".join(a.name for a in r.authors),
            "published": r.published.strftime("%Y-%m-%d"),
            "updated": r.updated.strftime("%Y-%m-%d"),
            "summary": (r.summary or "").replace("\n", " ").strip(),
            "primary_category": r.primary_category,
            "categories": ", ".join(r.categories or []),
            "arxiv_id": arxiv_id,
            "pdf_url": r.pdf_url,
            "doi": r.doi or "N/A",
        })
        return True

    log.info(f"Starting fetch (limit={limit}, page_size={page_size})")

    while len(results) < limit:
        try:
            # Stream from current offset to the end (or until we hit our limit)
            for r in client.results(search, offset=offset):
                added = add_result(r)
                offset += 1  # offset is count of yielded records so far
                if added and len(results) % 100 == 0:
                    log.info(f"✓ Collected {len(results)} (offset={offset})")
                if len(results) >= limit:
                    break

            # If we got here without exceptions, we reached the end cleanly.
            log.info("Reached end of result set.")
            break

        except (arxiv.UnexpectedEmptyPageError, arxiv.HTTPError) as e:
            consecutive_failures += 1
            log.warning(f"{type(e).__name__} at offset={offset}. "
                        f"Retrying after {backoff:.1f}s (failure #{consecutive_failures})…")
            time.sleep(backoff)
            # Exponential backoff, capped
            backoff = min(backoff * 1.5, 30.0)
            # Loop will restart generator from the same offset

            # Optional safety: give up after too many consecutive failures
            if consecutive_failures >= 8:
                log.error("Too many consecutive failures; returning partial results.")
                break
        else:
            # On success, reset failure counters/backoff
            consecutive_failures = 0
            backoff = delay_seconds

    log.info(f"Done. Collected {len(results)} results.")
    return results


def build_query(args):
    """Build the arXiv query string from command line arguments."""
    if args.query:
        # User provided a custom query
        query = args.query
    else:
        # Build query from default base query and date range
        base_query = args.base_query or DEFAULT_QUERY
        start_date = args.start_date or DEFAULT_START_DATE
        end_date = args.end_date or DEFAULT_END_DATE
        
        # Check if base query already has date range
        if "submittedDate:" not in base_query:
            query = f"{base_query} AND submittedDate:[{start_date} TO {end_date}]"
        else:
            query = base_query
    
    return query


def save_results_to_csv(results, output_path):
    """Save search results to a CSV file."""
    df = pd.DataFrame(results)
    
    # Create results directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(output_path, index=False)
    log.info(f"Results saved to {output_path}")
    log.info(f"Total papers saved: {len(df)}")


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Search arXiv for papers and save results to CSV",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default query and date range
  python main.py

  # Custom query
  python main.py --query "cat:cs.AI AND all:machine learning"

  # Specify max results and output file
  python main.py --max-results 500 --output my_results.csv

  # Custom date range
  python main.py --start-date 202401010000 --end-date 202412312359

  # Combine multiple options
  python main.py --query "cat:cs.LG" --max-results 100 --output ml_papers.csv
        """
    )
    
    parser.add_argument(
        "--query",
        type=str,
        help="Full arXiv search query (overrides base-query and date parameters)"
    )
    
    parser.add_argument(
        "--base-query",
        type=str,
        default=DEFAULT_QUERY,
        help=f"Base search query without date range (default: {DEFAULT_QUERY})"
    )
    
    parser.add_argument(
        "--start-date",
        type=str,
        default=DEFAULT_START_DATE,
        help=f"Start date in YYYYMMDDHHSS format (default: {DEFAULT_START_DATE})"
    )
    
    parser.add_argument(
        "--end-date",
        type=str,
        default=DEFAULT_END_DATE,
        help=f"End date in YYYYMMDDHHSS format (default: {DEFAULT_END_DATE})"
    )
    
    parser.add_argument(
        "--max-results",
        type=int,
        default=DEFAULT_MAX_RESULTS,
        help=f"Maximum number of results to fetch (default: {DEFAULT_MAX_RESULTS})"
    )
    
    parser.add_argument(
        "--output",
        type=str,
        default=DEFAULT_OUTPUT_FILE,
        help=f"Output CSV filename (default: {DEFAULT_OUTPUT_FILE})"
    )
    
    parser.add_argument(
        "--page-size",
        type=int,
        default=DEFAULT_PAGE_SIZE,
        help=f"Page size for API requests (default: {DEFAULT_PAGE_SIZE})"
    )
    
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY_SECONDS,
        help=f"Delay between requests in seconds (default: {DEFAULT_DELAY_SECONDS})"
    )
    
    return parser.parse_args()


def main():
    """Main execution function."""
    args = parse_arguments()
    
    # Build the query
    query = build_query(args)
    
    log.info(f"Search query: {query}")
    log.info(f"Max results: {args.max_results}")
    
    # Search arXiv
    results = search_arxiv(
        query=query,
        limit=args.max_results,
        page_size=args.page_size,
        delay_seconds=args.delay,
        retries=DEFAULT_RETRIES
    )
    
    # Prepare output path
    output_path = Path("results") / args.output
    
    # Save results
    save_results_to_csv(results, output_path)
    
    log.info("Search completed successfully!")


if __name__ == "__main__":
    main()

