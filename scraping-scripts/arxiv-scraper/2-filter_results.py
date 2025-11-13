#!/usr/bin/env python3
"""
ArXiv Results Filter Script
Uses LLM to tag and filter arXiv papers by relevance to technical AI alignment.
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
log = logging.getLogger("arxiv-filter")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("KEY"))

# Default configuration
DEFAULT_INPUT_FILE = "results/1-arxiv_raw_search_results.csv"
DEFAULT_ANNOTATED_OUTPUT = "results/2-arxiv_annotated_results.csv"
DEFAULT_FILTERED_OUTPUT = "results/2-arxiv_highly_relevant_results.csv"
DEFAULT_MODEL = "gpt-4.1"

# System prompt for the LLM
SYSTEM_PROMPT = """You are an expert in technical AI alignment research helping to conduct a 2025 shallow review of the field.

Your task is to analyze arXiv papers and determine their relevance to technical AI alignment work. We are specifically interested in papers that:

**Core Technical AI Alignment Areas:**
- AI safety and alignment methodologies (RLHF, RLAIF, constitutional AI, etc.)
- Mechanistic interpretability and transparency
- Scalable oversight techniques
- Adversarial robustness and jailbreaking
- Model evaluation and benchmarking for safety
- Reward hacking and specification gaming
- Deceptive alignment and misalignment
- Value alignment and preference learning
- AI control and monitoring
- Red teaming and adversarial testing

**Novel Contributions We're Looking For:**
- New techniques, frameworks, or methodologies
- Empirical findings that advance understanding
- Novel theoretical insights
- Practical tools and benchmarks
- Case studies revealing important failure modes
- Interdisciplinary approaches bringing new perspectives

**What to Deprioritize:**
- Pure capabilities research without safety implications
- Generic ML papers not specifically addressing alignment
- Applications of AI in specific domains (unless they reveal alignment insights)
- Papers that only tangentially mention safety/alignment
- Purely philosophical discussions without technical content

For each paper, provide:
1. **Tags**: 2-5 specific tags categorizing the paper's contribution areas
2. **Relevance**: Rate as "not relevant", "moderately relevant", or "highly relevant"
   - "highly relevant": Core technical alignment work with novel contributions
   - "moderately relevant": Related to alignment but peripheral or applied
   - "not relevant": Not about AI alignment or safety

Be selective - only rate papers as "highly relevant" if they make meaningful technical contributions to AI alignment."""

USER_PROMPT_TEMPLATE = """Analyze this arXiv paper for relevance to technical AI alignment:

Title: {title}

Authors: {authors}

Abstract: {summary}

Categories: {categories}

Provide tags and relevance rating."""


class PaperAnalysis(BaseModel):
    """Structured output for paper analysis."""
    tags: list[str]
    relevance: Literal["not relevant", "moderately relevant", "highly relevant"]
    reasoning: str  # Brief explanation of the rating


def call_openai_api(paper_info: dict, response_format: type[BaseModel]) -> PaperAnalysis | None:
    """
    Call OpenAI API with structured output parsing using responses API.

    Args:
        paper_info: Dictionary with paper information (title, authors, summary, categories)
        response_format: The Pydantic model class for response parsing

    Returns:
        Parsed PaperAnalysis object or None if error
    """
    try:
        # Format the user prompt with the paper information
        user_message = USER_PROMPT_TEMPLATE.format(
            title=paper_info["title"],
            authors=paper_info["authors"],
            summary=paper_info["summary"],
            categories=paper_info["categories"]
        )

        response = client.responses.parse(
            model=DEFAULT_MODEL,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            text_format=response_format,
        )

        # Get the parsed response
        parsed_response = response.output_parsed
        return parsed_response

    except Exception as e:
        log.error(f"Error calling OpenAI API: {e}")
        return None


def analyze_paper(row: pd.Series, index: int, total: int) -> dict:
    """
    Analyze a single paper and return tags and relevance.

    Args:
        row: DataFrame row containing paper information
        index: Current index (for logging)
        total: Total number of papers (for logging)

    Returns:
        Dictionary with tags, relevance, and reasoning
    """
    log.info(f"Analyzing paper {index + 1}/{total}: {row['title'][:60]}...")

    paper_info = {
        "title": row["title"],
        "authors": row["authors"],
        "summary": row["summary"],
        "categories": row["categories"]
    }

    analysis = call_openai_api(paper_info, PaperAnalysis)

    if analysis is None:
        log.warning(f"Failed to analyze paper {index + 1}, skipping...")
        return {
            "tags": [],
            "relevance": "not relevant",
            "reasoning": "Error during analysis"
        }

    log.info(f"  → Relevance: {analysis.relevance}")
    log.info(f"  → Tags: {', '.join(analysis.tags)}")

    return {
        "tags": analysis.tags,
        "relevance": analysis.relevance,
        "reasoning": analysis.reasoning
    }


def process_results(input_path: Path, annotated_output: Path, filtered_output: Path):
    """
    Process arXiv results: analyze, annotate, and filter.

    Args:
        input_path: Path to input CSV file
        annotated_output: Path for annotated output CSV
        filtered_output: Path for filtered (highly relevant only) output CSV
    """
    # Read input CSV
    log.info(f"Reading input file: {input_path}")
    df = pd.read_csv(input_path)
    log.info(f"Found {len(df)} papers to analyze")

    # Initialize new columns
    df["tags"] = None
    df["relevance"] = None
    df["reasoning"] = None

    # Analyze each paper
    for idx, row in df.iterrows():
        analysis_result = analyze_paper(row, idx, len(df))

        # Convert tags list to comma-separated string for CSV storage
        df.at[idx, "tags"] = ", ".join(analysis_result["tags"])
        df.at[idx, "relevance"] = analysis_result["relevance"]
        df.at[idx, "reasoning"] = analysis_result["reasoning"]

    # Save annotated results
    annotated_output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(annotated_output, index=False)
    log.info(f"Saved annotated results to: {annotated_output}")

    # Filter for highly relevant papers
    highly_relevant_df = df[df["relevance"] == "highly relevant"].copy()
    highly_relevant_df.to_csv(filtered_output, index=False)
    log.info(f"Saved {len(highly_relevant_df)} highly relevant papers to: {filtered_output}")

    # Print summary statistics
    log.info("\n" + "="*50)
    log.info("SUMMARY STATISTICS")
    log.info("="*50)
    log.info(f"Total papers analyzed: {len(df)}")
    log.info(f"Highly relevant: {len(df[df['relevance'] == 'highly relevant'])} "
             f"({len(df[df['relevance'] == 'highly relevant']) / len(df) * 100:.1f}%)")
    log.info(f"Moderately relevant: {len(df[df['relevance'] == 'moderately relevant'])} "
             f"({len(df[df['relevance'] == 'moderately relevant']) / len(df) * 100:.1f}%)")
    log.info(f"Not relevant: {len(df[df['relevance'] == 'not relevant'])} "
             f"({len(df[df['relevance'] == 'not relevant']) / len(df) * 100:.1f}%)")
    log.info("="*50)


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Filter arXiv papers by relevance to technical AI alignment",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default files
  python filter_results.py

  # Specify custom input and output files
  python filter_results.py --input my_results.csv --annotated my_annotated.csv --filtered my_filtered.csv

  # Process with custom model
  python filter_results.py --model gpt-4o-mini
        """
    )

    parser.add_argument(
        "--input",
        type=str,
        default=DEFAULT_INPUT_FILE,
        help=f"Input CSV file with raw arXiv results (default: {DEFAULT_INPUT_FILE})"
    )

    parser.add_argument(
        "--annotated",
        type=str,
        default=DEFAULT_ANNOTATED_OUTPUT,
        help=f"Output CSV file for annotated results (default: {DEFAULT_ANNOTATED_OUTPUT})"
    )

    parser.add_argument(
        "--filtered",
        type=str,
        default=DEFAULT_FILTERED_OUTPUT,
        help=f"Output CSV file for highly relevant results (default: {DEFAULT_FILTERED_OUTPUT})"
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
        log.error("Please set it in your .env file or environment")
        return

    # Set model
    global DEFAULT_MODEL
    DEFAULT_MODEL = args.model

    # Convert paths
    input_path = Path(args.input)
    annotated_output = Path(args.annotated)
    filtered_output = Path(args.filtered)

    # Check if input file exists
    if not input_path.exists():
        log.error(f"Input file not found: {input_path}")
        log.error("Please run scrape.py first to generate arXiv results.")
        return

    # Process results
    log.info("Starting analysis...")
    process_results(input_path, annotated_output, filtered_output)
    log.info("Analysis complete!")


if __name__ == "__main__":
    main()

