#!/usr/bin/env python3
"""
Curate Unique ArXiv Links Script
Evaluates new ArXiv papers against the post content to determine which should be added.
"""

import os
import argparse
import logging
from pathlib import Path
import pandas as pd
from openai import OpenAI
from pydantic import BaseModel
from typing import Literal
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("arxiv-curate")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("KEY"))

# Default configuration
DEFAULT_ARXIV_INPUT = "results/3-arxiv_new_links_only.csv"
DEFAULT_POST_CONTENT = "input/shallow-review-2025.txt"
DEFAULT_ANNOTATED_OUTPUT = "results/6-arxiv_curated_with_flags.csv"
DEFAULT_RELEVANT_ONLY_OUTPUT = "results/6-arxiv_curated_relevant_only.csv"
DEFAULT_MODEL = "gpt-5-mini"

# System prompt for the LLM
SYSTEM_PROMPT = """You are an expert curator for a 2025 shallow review of technical AI alignment research.

Your task is to evaluate whether newly discovered arXiv papers should be included in the review document. The review aims to cover the most important and relevant technical AI alignment work from the period.

**Evaluation Criteria:**

1. **Relevance & Quality Bar** - The paper must be:
   - Directly relevant to technical AI alignment research
   - High-quality with novel contributions or important empirical findings
   - Interesting enough to merit inclusion in a curated review
   - Not redundant with content already covered in the post

2. **Contribution Type** - Determine if the paper:
   - **Contributes to existing agenda**: Advances topics/themes already discussed in the post
   - **Contributes to new agenda**: Introduces important new research directions (HIGH BAR - must be significant)
   - **Neither**: Not relevant enough or quality enough to include

**Agenda Categories** (common themes in AI alignment):
- Interpretability / Mechanistic interpretability
- Scalable oversight
- Evaluations / Benchmarking
- Adversarial robustness / Red teaming / Jailbreaking
- RLHF / RLAIF / Alignment techniques
- Deceptive alignment / Misalignment
- Safety / AI safety
- Control theory / AI control
- Multimodal safety
- Model evaluation
- Constitutional AI / Value alignment
- Reward hacking / Specification gaming
- etc.

For each paper, provide:
1. **is_relevant**: "y" if the paper should be included in the review, "n" if not
2. **reasoning**: Brief explanation of your decision (2-3 sentences)
3. **agenda**: Comma-separated keywords describing the paper's alignment agendas (empty if not relevant)

Be selective - only mark papers as relevant if they make meaningful contributions worthy of inclusion in a curated review.

Do not add low-quality or uninteresting papers that would not add value to the review."""

USER_PROMPT_TEMPLATE = """Post Content (full document):
{post_content}

---

Evaluate this arXiv paper for inclusion in the shallow review.

ArXiv Paper:
- Title: {title}
- Authors: {authors}
- Abstract: {summary}

Should this paper be included in the review? Provide relevance flag, reasoning, and agenda keywords."""


class CurationDecision(BaseModel):
    """Structured output for curation decision."""
    is_relevant: Literal["y", "n"]  # "y" if should be included, "n" if not
    reasoning: str  # Brief explanation (2-3 sentences)
    agenda: str  # Comma-separated keywords (empty string if not relevant)


def load_post_content(post_path: Path) -> str:
    """
    Load the post content for context.
    
    Args:
        post_path: Path to the post text file
        
    Returns:
        Post content as string
    """
    if not post_path.exists():
        log.warning(f"Post content file not found: {post_path}")
        return ""
    
    content = post_path.read_text(encoding="utf-8")
    return content


def call_openai_api(paper_info: dict, post_content: str, response_format: type[BaseModel]) -> CurationDecision | None:
    """
    Call OpenAI API to evaluate paper for inclusion.
    
    Args:
        paper_info: Dictionary with paper information
        post_content: The post content for context
        response_format: The Pydantic model class for response parsing
        
    Returns:
        Parsed CurationDecision object or None if error
    """
    try:
        user_message = USER_PROMPT_TEMPLATE.format(
            title=paper_info["title"],
            authors=paper_info["authors"],
            summary=paper_info["summary"],
            tags=paper_info["tags"],
            post_content=post_content
        )
        
        response = client.responses.parse(
            model=DEFAULT_MODEL,
            reasoning={
                "effort": "medium",
            },
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


def curate_paper(row: pd.Series, post_content: str, index: int, total: int) -> dict:
    """
    Evaluate if a single paper should be included in the review.
    
    Args:
        row: DataFrame row containing paper information
        post_content: The post content for context
        index: Current index (for logging)
        total: Total number of papers (for logging)
        
    Returns:
        Dictionary with is_relevant, reasoning, and agenda
    """
    log.info(f"Curating paper {index + 1}/{total}: {row['title'][:60]}...")
    
    paper_info = {
        "title": row["title"],
        "authors": row["authors"],
        "summary": row["summary"],
        "tags": row.get("tags", "")
    }
    
    # Call API to evaluate
    result = call_openai_api(paper_info, post_content, CurationDecision)
    
    if result is None:
        log.warning(f"Failed to curate paper {index + 1}, marking as not relevant (safe default)...")
        return {
            "is_relevant": "n",
            "curation_reasoning": "Error during curation",
            "agenda": ""
        }
    
    status = "INCLUDE" if result.is_relevant == "y" else "EXCLUDE"
    log.info(f"  → Decision: {status}")
    if result.is_relevant == "y" and result.agenda:
        log.info(f"  → Agenda: {result.agenda}")
    
    return {
        "is_relevant": result.is_relevant,
        "curation_reasoning": result.reasoning,
        "agenda": result.agenda
    }


def process_curation(arxiv_path: Path, post_path: Path,
                     annotated_output: Path, relevant_only_output: Path):
    """
    Process arXiv papers to curate which should be included in the review.
    
    Args:
        arxiv_path: Path to new ArXiv papers CSV
        post_path: Path to post content text file
        annotated_output: Path for annotated output CSV (with curation columns)
        relevant_only_output: Path for relevant papers only CSV
    """
    # Load post content
    log.info(f"Loading post content from: {post_path}")
    post_content = load_post_content(post_path)
    log.info(f"Loaded {len(post_content)} characters of post content")
    
    # Read arXiv input CSV
    log.info(f"Reading new arXiv papers from: {arxiv_path}")
    df = pd.read_csv(arxiv_path)
    log.info(f"Found {len(df)} new arXiv papers to curate")
    
    # Initialize new columns
    df["is_relevant"] = None
    df["curation_reasoning"] = None
    df["agenda"] = None
    
    # Curate each paper
    for idx, row in df.iterrows():
        curation_result = curate_paper(row, post_content, idx, len(df))
        
        df.at[idx, "is_relevant"] = curation_result["is_relevant"]
        df.at[idx, "curation_reasoning"] = curation_result["curation_reasoning"]
        df.at[idx, "agenda"] = curation_result["agenda"]
    
    # Save annotated results
    annotated_output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(annotated_output, index=False)
    log.info(f"Saved annotated results to: {annotated_output}")
    
    # Filter for relevant papers only
    relevant_papers_df = df[df["is_relevant"] == "y"].copy()
    relevant_papers_df.to_csv(relevant_only_output, index=False)
    log.info(f"Saved {len(relevant_papers_df)} relevant papers to: {relevant_only_output}")
    
    # Print summary statistics
    log.info("\n" + "="*50)
    log.info("CURATION SUMMARY")
    log.info("="*50)
    log.info(f"Total papers curated: {len(df)}")
    log.info(f"Relevant (to include): {len(df[df['is_relevant'] == 'y'])} "
             f"({len(df[df['is_relevant'] == 'y']) / len(df) * 100:.1f}%)")
    log.info(f"Not relevant (to exclude): {len(df[df['is_relevant'] == 'n'])} "
             f"({len(df[df['is_relevant'] == 'n']) / len(df) * 100:.1f}%)")
    
    # Show top agendas if any relevant papers
    if len(relevant_papers_df) > 0:
        log.info("\n" + "-"*50)
        log.info("TOP AGENDAS IN RELEVANT PAPERS:")
        log.info("-"*50)
        all_agendas = []
        for agenda_str in relevant_papers_df["agenda"].dropna():
            if agenda_str:
                agendas = [a.strip() for a in agenda_str.split(",")]
                all_agendas.extend(agendas)
        
        from collections import Counter
        agenda_counts = Counter(all_agendas)
        for agenda, count in agenda_counts.most_common(10):
            log.info(f"  {agenda}: {count}")
    
    log.info("="*50)


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Curate new arXiv papers for inclusion in the shallow review",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default files
  python 6-curate-unique-arxiv-links.py

  # Specify custom input files
  python 6-curate-unique-arxiv-links.py --arxiv my_papers.csv --post my_post.txt

  # Use different model
  python 6-curate-unique-arxiv-links.py --model gpt-4o
        """
    )
    
    parser.add_argument(
        "--arxiv",
        type=str,
        default=DEFAULT_ARXIV_INPUT,
        help=f"Input CSV file with new arXiv papers (default: {DEFAULT_ARXIV_INPUT})"
    )
    
    parser.add_argument(
        "--post",
        type=str,
        default=DEFAULT_POST_CONTENT,
        help=f"Input text file with post content (default: {DEFAULT_POST_CONTENT})"
    )
    
    parser.add_argument(
        "--annotated",
        type=str,
        default=DEFAULT_ANNOTATED_OUTPUT,
        help=f"Output CSV file with curation annotations (default: {DEFAULT_ANNOTATED_OUTPUT})"
    )
    
    parser.add_argument(
        "--relevant-only",
        type=str,
        default=DEFAULT_RELEVANT_ONLY_OUTPUT,
        help=f"Output CSV file with only relevant papers (default: {DEFAULT_RELEVANT_ONLY_OUTPUT})"
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
    post_path = Path(args.post)
    annotated_output = Path(args.annotated)
    relevant_only_output = Path(args.relevant_only)
    
    # Check if input files exist
    if not arxiv_path.exists():
        log.error(f"ArXiv input file not found: {arxiv_path}")
        log.error("Please run 5-find-unique-arxiv-links.py first to generate new papers list.")
        return
    
    if not post_path.exists():
        log.error(f"Post content file not found: {post_path}")
        log.error("Please ensure the post content text file exists.")
        return
    
    # Process curation
    log.info("Starting curation...")
    process_curation(arxiv_path, post_path, annotated_output, relevant_only_output)
    log.info("Curation complete!")


if __name__ == "__main__":
    main()
