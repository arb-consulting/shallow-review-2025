#!/usr/bin/env python3
"""
Create Taxonomy and Editorial from Curated Links
Generates a structured output with paper listings, taxonomy, and editorial overview.
"""

import os
import argparse
import logging
from pathlib import Path
import pandas as pd
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("arxiv-taxonomy-editorial")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("KEY"))

# Default configuration
DEFAULT_INPUT_CSV = "results/6-arxiv_curated_relevant_only.csv"
DEFAULT_OUTPUT_TXT = "results/7-taxonomy-and-editorial.txt"
DEFAULT_MODEL = "gpt-5-mini"

# System prompt for taxonomy generation
TAXONOMY_SYSTEM_PROMPT = """You are an expert in technical AI alignment research creating a taxonomy of recent work.

Your task is to analyze a collection of curated arXiv papers and create:
1. A hierarchical taxonomy that organizes the papers by their main themes and contributions
2. An insightful editorial summarizing the state and progress of AI alignment in 2025

The taxonomy should:
- Group papers into coherent themes/categories
- Use clear, descriptive category names
- Be hierarchical (main categories with subcategories where appropriate)
- Cover all major themes present in the papers
- Be formatted as nested bullet points

The editorial should:
- Be 100-500 words
- Provide a high-level overview of AI alignment progress in 2025
- Highlight key trends, themes, and important developments
- Be engaging and insightful
- Focus on technical advancements and their implications

Base your analysis ONLY on the provided papers."""

TAXONOMY_USER_PROMPT_TEMPLATE = """Based on these curated AI alignment papers from 2025, create a taxonomy and editorial.

Papers:
{papers_text}

Generate:
1. A hierarchical taxonomy organizing these papers by themes
2. A 100-500 word editorial on AI alignment progress in 2025"""


class TaxonomyAndEditorial(BaseModel):
    """Structured output for taxonomy and editorial generation."""
    taxonomy: str  # Hierarchical taxonomy as formatted text with bullet points
    editorial: str  # 100-500 word editorial paragraph


class PaperTags(BaseModel):
    """Structured output for individual paper taxonomy tags."""
    tags: list[str]  # List of 2-5 taxonomy tags for this paper


def load_papers(csv_path: Path) -> pd.DataFrame:
    """
    Load the curated papers CSV.
    
    Args:
        csv_path: Path to the CSV file
        
    Returns:
        DataFrame with paper information
    """
    df = pd.read_csv(csv_path)
    log.info(f"Loaded {len(df)} curated papers")
    return df


def format_papers_for_prompt(df: pd.DataFrame) -> str:
    """
    Format papers into a text representation for the LLM prompt.
    
    Args:
        df: DataFrame with paper information
        
    Returns:
        Formatted string of all papers
    """
    papers = []
    for idx, row in df.iterrows():
        paper_text = f"""Paper {idx + 1}:
Title: {row['title']}
Authors: {row['authors']}
Abstract: {row['summary']}
Existing Agenda: {row.get('agenda', 'N/A')}
"""
        papers.append(paper_text)
    
    return "\n\n".join(papers)


def generate_taxonomy_and_editorial(papers_text: str) -> TaxonomyAndEditorial | None:
    """
    Generate taxonomy and editorial using OpenAI API.
    
    Args:
        papers_text: Formatted string of all papers
        
    Returns:
        TaxonomyAndEditorial object or None if error
    """
    try:
        log.info("Generating taxonomy and editorial...")
        
        user_message = TAXONOMY_USER_PROMPT_TEMPLATE.format(
            papers_text=papers_text
        )
        
        response = client.responses.parse(
            model=DEFAULT_MODEL,
            reasoning={
                "effort": "low",
            },
            input=[
                {"role": "system", "content": TAXONOMY_SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            text_format=TaxonomyAndEditorial,
        )
        
        return response.output_parsed
        
    except Exception as e:
        log.error(f"Error calling OpenAI API: {e}")
        return None


def generate_paper_tags(paper_title: str, paper_summary: str, taxonomy: str) -> list[str]:
    """
    Generate taxonomy tags for a single paper based on the overall taxonomy.
    
    Args:
        paper_title: Paper title
        paper_summary: Paper abstract/summary
        taxonomy: The generated taxonomy
        
    Returns:
        List of taxonomy tags
    """
    system_prompt = f"""You are tagging a paper based on this taxonomy:

{taxonomy}

Provide 2-5 specific tags from the taxonomy that best describe this paper."""
    
    user_prompt = f"""Paper Title: {paper_title}

Abstract: {paper_summary}

What taxonomy tags apply to this paper?"""
    
    try:
        response = client.responses.parse(
            model=DEFAULT_MODEL,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            text_format=PaperTags,
        )
        
        return response.output_parsed.tags
        
    except Exception as e:
        log.error(f"Error generating tags: {e}")
        return []


def create_output_document(df: pd.DataFrame, taxonomy: str, editorial: str, 
                          output_path: Path):
    """
    Create the final output document with papers, taxonomy, and editorial.
    
    Args:
        df: DataFrame with paper information and tags
        taxonomy: Generated taxonomy text
        editorial: Generated editorial text
        output_path: Path to save the output file
    """
    lines = []
    
    # 1. Add editorial section first
    log.info("Adding editorial...")
    lines.append("=" * 80)
    lines.append("EDITORIAL")
    lines.append("=" * 80)
    lines.append("")
    lines.append(editorial)
    lines.append("")
    
    # 2. Add taxonomy section
    log.info("Adding taxonomy...")
    lines.append("=" * 80)
    lines.append("TAXONOMY")
    lines.append("=" * 80)
    lines.append("")
    lines.append(taxonomy)
    lines.append("")
    
    # 3. Add checklist/todo section
    log.info("Adding checklist...")
    lines.append("=" * 80)
    lines.append("TODO: PAPERS TO REVIEW")
    lines.append("=" * 80)
    lines.append("")
    for _, row in df.iterrows():
        title = row['title']
        lines.append(f"- [ ] {title}")
    lines.append("")
    
    # 4. Add paper listings
    log.info("Formatting paper listings...")
    lines.append("=" * 80)
    lines.append("PAPER SUMMARIES")
    lines.append("=" * 80)
    lines.append("")
    for idx, row in df.iterrows():
        title = row['title']
        pdf_url = row['pdf_url']
        summary = row['summary']
        tags = row.get('taxonomy_tags', 'N/A')
        
        lines.append(title)
        lines.append(f"- Link: {pdf_url}")
        lines.append(f"- Summary: {summary}")
        lines.append(f"- Taxonomy tags: {tags}")
        lines.append("")  # Blank line between papers
    
    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    log.info(f"Saved output to: {output_path}")


def process_papers(input_csv: Path, output_txt: Path):
    """
    Main processing function.
    
    Args:
        input_csv: Path to input CSV with curated papers
        output_txt: Path to output text file
    """
    # Load papers
    df = load_papers(input_csv)
    
    # Format papers for the prompt
    papers_text = format_papers_for_prompt(df)
    
    # Generate taxonomy and editorial
    result = generate_taxonomy_and_editorial(papers_text)
    
    if result is None:
        log.error("Failed to generate taxonomy and editorial")
        return
    
    log.info("Successfully generated taxonomy and editorial")
    log.info(f"Taxonomy length: {len(result.taxonomy)} characters")
    log.info(f"Editorial length: {len(result.editorial.split())} words")
    
    # Generate individual paper tags based on taxonomy
    log.info("Generating taxonomy tags for each paper...")
    taxonomy_tags = []
    for idx, row in df.iterrows():
        log.info(f"Tagging paper {idx + 1}/{len(df)}: {row['title'][:60]}...")
        tags = generate_paper_tags(row['title'], row['summary'], result.taxonomy)
        taxonomy_tags.append(", ".join(tags) if tags else "N/A")
    
    df['taxonomy_tags'] = taxonomy_tags
    
    # Create output document
    create_output_document(df, result.taxonomy, result.editorial, output_txt)
    
    # Print summary
    log.info("\n" + "="*50)
    log.info("GENERATION COMPLETE")
    log.info("="*50)
    log.info(f"Papers processed: {len(df)}")
    log.info(f"Output saved to: {output_txt}")
    log.info("="*50)


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate taxonomy and editorial from curated ArXiv papers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default files
  python 7-create-taxonomy-and-editorial-from-curated-links.py

  # Specify custom input and output
  python 7-create-taxonomy-and-editorial-from-curated-links.py --input my_papers.csv --output my_output.txt

  # Use different model
  python 7-create-taxonomy-and-editorial-from-curated-links.py --model gpt-4o
        """
    )
    
    parser.add_argument(
        "--input",
        type=str,
        default=DEFAULT_INPUT_CSV,
        help=f"Input CSV file with curated papers (default: {DEFAULT_INPUT_CSV})"
    )
    
    parser.add_argument(
        "--output",
        type=str,
        default=DEFAULT_OUTPUT_TXT,
        help=f"Output text file for taxonomy and editorial (default: {DEFAULT_OUTPUT_TXT})"
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
    input_csv = Path(args.input)
    output_txt = Path(args.output)
    
    # Check if input file exists
    if not input_csv.exists():
        log.error(f"Input CSV file not found: {input_csv}")
        log.error("Please run 6-curate-unique-arxiv-links.py first.")
        return
    
    # Process papers
    log.info("Starting taxonomy and editorial generation...")
    process_papers(input_csv, output_txt)
    log.info("Complete!")


if __name__ == "__main__":
    main()

