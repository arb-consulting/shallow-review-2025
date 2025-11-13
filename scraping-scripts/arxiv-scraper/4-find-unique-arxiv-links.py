#!/usr/bin/env python3
"""
Find Unique ArXiv Links Script
Compares highly relevant arXiv papers against links already in the DOCX to identify new papers.
"""

import os
import argparse
import logging
from pathlib import Path
import pandas as pd
from openai import OpenAI
from pydantic import BaseModel
from typing import Literal

# Setup logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("arxiv-unique-links")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("KEY"))

# Default configuration
DEFAULT_ARXIV_INPUT = "results/2-arxiv_highly_relevant_results.csv"
DEFAULT_DOCX_LINKS = "results/shallow-review-2025-links.csv"
DEFAULT_LENZ_PAPERS = "input/lenz-ai-safety-papers.csv"
DEFAULT_ANNOTATED_OUTPUT = "results/3-arxiv_links_with_new_flag.csv"
DEFAULT_NEW_ONLY_OUTPUT = "results/3-arxiv_new_links_only.csv"
DEFAULT_MODEL = "gpt-4.1"

# System prompt for the LLM
SYSTEM_PROMPT = """You are helping to identify duplicate arXiv papers.

Your task is to determine if an arXiv paper is already referenced in a list of existing links from a document.

An arXiv paper should be considered "already present" if ANY of the following are true:
1. The exact arXiv ID appears in any of the existing URLs (e.g., "2510.20223" in "https://arxiv.org/abs/2510.20223")
2. The paper title closely matches any existing link title (allowing for minor formatting differences)
3. Any existing URL points to the same arXiv paper (even if in different format like abs/ vs pdf/)

Be strict: if there's clear evidence the paper is already referenced, mark it as NOT new.
Only mark a paper as new if you're confident it's not already in the existing links."""

USER_PROMPT_TEMPLATE = """Determine if this arXiv paper is already present in the existing document links or Lenz AI safety papers list.

ArXiv Paper to Check:
- Title: {title}
- ArXiv ID: {arxiv_id}
- PDF URL: {pdf_url}

Existing Links and Papers (showing up to 1000):
{existing_links}

Is this arXiv paper already present in the existing links or papers?"""


class DuplicateCheck(BaseModel):
    """Structured output for duplicate checking."""
    is_new: Literal["y", "n"]  # "y" if new, "n" if already present
    reasoning: str  # Brief explanation of the decision
    matched_link: str | None  # If not new, which existing link matches (or None)


def load_existing_links(docx_links_path: Path) -> list[dict]:
    """
    Load existing links from the DOCX CSV file.
    
    Args:
        docx_links_path: Path to the CSV file with DOCX links
        
    Returns:
        List of dictionaries with 'title' and 'url' keys
    """
    df = pd.read_csv(docx_links_path)
    links = []
    for _, row in df.iterrows():
        links.append({
            "title": str(row["title"]) if pd.notna(row["title"]) else "",
            "url": str(row["url"]) if pd.notna(row["url"]) else ""
        })
    return links


def load_lenz_papers(lenz_papers_path: Path) -> list[dict]:
    """
    Load paper titles from the Lenz AI safety papers CSV.
    
    Args:
        lenz_papers_path: Path to the Lenz papers CSV file
        
    Returns:
        List of dictionaries with 'title' and 'url' keys
    """
    if not lenz_papers_path.exists():
        log.warning(f"Lenz papers file not found: {lenz_papers_path}")
        return []
    
    try:
        df = pd.read_csv(lenz_papers_path)
        links = []
        for _, row in df.iterrows():
            # Extract paper title from "Paper title" column
            if "Paper title" in row and pd.notna(row["Paper title"]):
                links.append({
                    "title": str(row["Paper title"]),
                    "url": ""  # No URL available from Lenz papers
                })
        log.info(f"Loaded {len(links)} papers from Lenz AI safety papers")
        return links
    except Exception as e:
        log.warning(f"Error loading Lenz papers: {e}")
        return []


def format_existing_links(existing_links: list[dict], limit: int = 1000) -> str:
    """
    Format existing links for the LLM prompt.
    
    Args:
        existing_links: List of link dictionaries
        limit: Maximum number of links to include
        
    Returns:
        Formatted string of existing links
    """
    # Take only the first 'limit' links to avoid token limits
    links_to_show = existing_links[:limit]
    
    formatted = []
    for i, link in enumerate(links_to_show, 1):
        title = link["title"][:100]  # Truncate long titles
        url = link["url"]
        formatted.append(f"{i}. Title: {title}\n   URL: {url}")
    
    if len(existing_links) > limit:
        formatted.append(f"\n... and {len(existing_links) - limit} more links not shown")
    
    return "\n\n".join(formatted)


def call_openai_api(paper_info: dict, existing_links_str: str, response_format: type[BaseModel]) -> DuplicateCheck | None:
    """
    Call OpenAI API to check if paper is a duplicate.
    
    Args:
        paper_info: Dictionary with paper information
        existing_links_str: Formatted string of existing links
        response_format: The Pydantic model class for response parsing
        
    Returns:
        Parsed DuplicateCheck object or None if error
    """
    try:
        user_message = USER_PROMPT_TEMPLATE.format(
            title=paper_info["title"],
            arxiv_id=paper_info["arxiv_id"],
            pdf_url=paper_info["pdf_url"],
            existing_links=existing_links_str
        )
        
        response = client.responses.parse(
            model=DEFAULT_MODEL,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            text_format=response_format,
        )
        
        return response.output_parsed
        
    except Exception as e:
        log.error(f"Error calling OpenAI API: {e}")
        return None


def check_paper(row: pd.Series, existing_links: list[dict], index: int, total: int) -> dict:
    """
    Check if a single paper is new or already present in existing links.
    
    Args:
        row: DataFrame row containing paper information
        existing_links: List of existing link dictionaries
        index: Current index (for logging)
        total: Total number of papers (for logging)
        
    Returns:
        Dictionary with is_new, reasoning, and matched_link
    """
    log.info(f"Checking paper {index + 1}/{total}: {row['title'][:60]}...")
    
    paper_info = {
        "title": row["title"],
        "arxiv_id": row["arxiv_id"],
        "pdf_url": row["pdf_url"]
    }
    
    # Format existing links for the prompt
    existing_links_str = format_existing_links(existing_links)
    
    # Call API to check for duplicates
    result = call_openai_api(paper_info, existing_links_str, DuplicateCheck)
    
    if result is None:
        log.warning(f"Failed to check paper {index + 1}, marking as new (safe default)...")
        return {
            "is_new": "y",
            "reasoning": "Error during duplicate check",
            "matched_link": None
        }
    
    status = "NEW" if result.is_new == "y" else "DUPLICATE"
    log.info(f"  → Status: {status}")
    if result.matched_link:
        log.info(f"  → Matched: {result.matched_link[:80]}...")
    
    return {
        "is_new": result.is_new,
        "reasoning": result.reasoning,
        "matched_link": result.matched_link if result.matched_link else ""
    }


def process_arxiv_links(arxiv_path: Path, docx_links_path: Path, lenz_papers_path: Path,
                       annotated_output: Path, new_only_output: Path):
    """
    Process arXiv links to identify which are new.
    
    Args:
        arxiv_path: Path to highly relevant arXiv results CSV
        docx_links_path: Path to DOCX links CSV
        lenz_papers_path: Path to Lenz AI safety papers CSV
        annotated_output: Path for annotated output CSV (with is_new column)
        new_only_output: Path for new links only CSV
    """
    # Load existing links from DOCX
    log.info(f"Loading existing links from: {docx_links_path}")
    existing_links = load_existing_links(docx_links_path)
    log.info(f"Found {len(existing_links)} existing links in document")
    
    # Load Lenz papers
    log.info(f"Loading Lenz AI safety papers from: {lenz_papers_path}")
    lenz_papers = load_lenz_papers(lenz_papers_path)
    
    # Combine both sources
    all_existing = existing_links + lenz_papers
    log.info(f"Total existing papers/links to check against: {len(all_existing)}")
    
    # Read arXiv input CSV
    log.info(f"Reading arXiv papers from: {arxiv_path}")
    df = pd.read_csv(arxiv_path)
    log.info(f"Found {len(df)} highly relevant arXiv papers to check")
    
    # Initialize new columns
    df["is_new"] = None
    df["duplicate_reasoning"] = None
    df["matched_link"] = None
    
    # Check each paper
    for idx, row in df.iterrows():
        check_result = check_paper(row, all_existing, idx, len(df))
        
        df.at[idx, "is_new"] = check_result["is_new"]
        df.at[idx, "duplicate_reasoning"] = check_result["reasoning"]
        df.at[idx, "matched_link"] = check_result["matched_link"]
    
    # Save annotated results
    annotated_output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(annotated_output, index=False)
    log.info(f"Saved annotated results to: {annotated_output}")
    
    # Filter for new papers only
    new_papers_df = df[df["is_new"] == "y"].copy()
    new_papers_df.to_csv(new_only_output, index=False)
    log.info(f"Saved {len(new_papers_df)} new papers to: {new_only_output}")
    
    # Print summary statistics
    log.info("\n" + "="*50)
    log.info("SUMMARY STATISTICS")
    log.info("="*50)
    log.info(f"Total papers checked: {len(df)}")
    log.info(f"New papers: {len(df[df['is_new'] == 'y'])} "
             f"({len(df[df['is_new'] == 'y']) / len(df) * 100:.1f}%)")
    log.info(f"Already present: {len(df[df['is_new'] == 'n'])} "
             f"({len(df[df['is_new'] == 'n']) / len(df) * 100:.1f}%)")
    log.info("="*50)


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Find unique arXiv papers not already in the document",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default files
  python 5-find-unique-arxiv-links.py

  # Specify custom input files
  python 5-find-unique-arxiv-links.py --arxiv my_papers.csv --docx-links my_links.csv

  # Use different model
  python 5-find-unique-arxiv-links.py --model gpt-4o
        """
    )
    
    parser.add_argument(
        "--arxiv",
        type=str,
        default=DEFAULT_ARXIV_INPUT,
        help=f"Input CSV file with highly relevant arXiv papers (default: {DEFAULT_ARXIV_INPUT})"
    )
    
    parser.add_argument(
        "--docx-links",
        type=str,
        default=DEFAULT_DOCX_LINKS,
        help=f"Input CSV file with links from DOCX (default: {DEFAULT_DOCX_LINKS})"
    )
    
    parser.add_argument(
        "--lenz-papers",
        type=str,
        default=DEFAULT_LENZ_PAPERS,
        help=f"Input CSV file with Lenz AI safety papers (default: {DEFAULT_LENZ_PAPERS})"
    )
    
    parser.add_argument(
        "--annotated",
        type=str,
        default=DEFAULT_ANNOTATED_OUTPUT,
        help=f"Output CSV file with is_new annotations (default: {DEFAULT_ANNOTATED_OUTPUT})"
    )
    
    parser.add_argument(
        "--new-only",
        type=str,
        default=DEFAULT_NEW_ONLY_OUTPUT,
        help=f"Output CSV file with only new papers (default: {DEFAULT_NEW_ONLY_OUTPUT})"
    )
    
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        help=f"OpenAI model to use (default: {DEFAULT_MODEL})"
    )
    
    return parser.parse_args()


def main():
    """Main execution function."""
    args = parse_arguments()
    
    # Check for API key
    if not os.getenv("KEY"):
        log.error("KEY environment variable not set!")
        log.error("Please set it in your .env file")
        return
    
    # Set model
    global DEFAULT_MODEL
    DEFAULT_MODEL = args.model
    
    # Convert paths
    arxiv_path = Path(args.arxiv)
    docx_links_path = Path(args.docx_links)
    lenz_papers_path = Path(args.lenz_papers)
    annotated_output = Path(args.annotated)
    new_only_output = Path(args.new_only)
    
    # Check if input files exist
    if not arxiv_path.exists():
        log.error(f"ArXiv input file not found: {arxiv_path}")
        log.error("Please run 2-filter_results.py first to generate highly relevant papers.")
        return
    
    if not docx_links_path.exists():
        log.error(f"DOCX links file not found: {docx_links_path}")
        log.error("Please run 4-docx_links_to_csv.py first to extract DOCX links.")
        return
    
    # Lenz papers file is optional - warning already logged in load function if missing
    
    # Process links
    log.info("Starting duplicate checking...")
    process_arxiv_links(arxiv_path, docx_links_path, lenz_papers_path, annotated_output, new_only_output)
    log.info("Duplicate checking complete!")


if __name__ == "__main__":
    main()
