#!/usr/bin/env -S uv run python
"""Process draft shallow review documents.

Provides tools to extract links and parse structured content from draft markdown documents.
"""

import json
import logging
import re
import sys
from pathlib import Path
import litellm
import typer
import yaml
from jinja2 import Template
from litellm.caching.caching import Cache
from pydantic import ValidationError
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from shallow_review.draft_parser import (
    extract_all_links_from_file,
    parse_document,
)
from shallow_review.draft_types import (
    BROAD_APPROACHES,
    ORTHODOX_PROBLEMS,
    TARGET_CASES,
    AgendaAttributes,
    DocumentItem,
    ItemType,
    ProcessedDocument,
)

# Setup
console = Console()
logger = logging.getLogger(__name__)

# Import shallow_review modules for database access
try:
    from shallow_review.data_db import data_db_locked
    from shallow_review.utils import normalize_url
    _SHALLOW_REVIEW_AVAILABLE = True
except ImportError:
    _SHALLOW_REVIEW_AVAILABLE = False
    logger.warning("shallow_review modules not available - URL enrichment will be disabled")

# CLI app
app = typer.Typer(
    name="process-draft",
    help="Process draft shallow review documents",
    add_completion=False,
)

# LLM setup flag
_llm_setup_done = False


def setup_litellm(cache_dir: Path | None = None) -> None:
    """Set up litellm with disk-based caching.

    Args:
        cache_dir: Directory for LLM response caching
    """
    global _llm_setup_done

    if _llm_setup_done:
        return

    if cache_dir is None:
        cache_dir = Path.cwd() / ".llm_cache"

    cache_dir.mkdir(exist_ok=True, parents=True)
    litellm.cache = Cache(type="disk", disk_cache_dir=str(cache_dir))  # type: ignore[arg-type]

    _llm_setup_done = True
    logger.info(f"Litellm initialized with cache at {cache_dir}")


def setup_logging(verbose: bool = False) -> None:
    """Configure logging."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


# ============================================================================
# collect_links subcommand
# ============================================================================


@app.command()
def collect_links(
    input_file: str = typer.Argument(..., help="Path to draft markdown file"),
    output_file: str | None = typer.Option(
        None, "--output", "-o", help="Output file path (default: <input>-links.txt)"
    ),
    format: str = typer.Option(
        "txt", "--format", "-f", help="Output format: json or txt"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging"),
) -> None:
    """Extract all HTTP(S) links from a draft markdown document.

    Extracts both markdown-formatted links [text](url) and plain-text URLs.
    Uses smart boundary detection to avoid capturing trailing punctuation.
    """
    setup_logging(verbose)

    input_path = Path(input_file)
    if not input_path.exists():
        console.print(f"[red]Error: File not found: {input_file}[/red]")
        raise typer.Exit(1)

    # Determine output path
    if output_file is None:
        output_path = input_path.parent / f"{input_path.stem}-links.{format}"
    else:
        output_path = Path(output_file)

    # Extract links
    console.print(f"[cyan]Extracting links from {input_file}...[/cyan]")
    links = extract_all_links_from_file(input_path)

    console.print(f"[green]Found {len(links)} unique links[/green]")

    # Write output
    if format == "json":
        output_data = {
            "source_file": str(input_path),
            "total_links": len(links),
            "links": [link.model_dump() for link in links],
        }
        output_path.write_text(json.dumps(output_data, indent=2))
    elif format == "txt":
        # One URL per line
        lines = [link.url for link in links]
        output_path.write_text("\n".join(lines) + "\n")
    else:
        console.print(f"[red]Error: Unknown format '{format}'[/red]")
        raise typer.Exit(1)

    console.print(f"[green]Links written to {output_path}[/green]")


# ============================================================================
# parse subcommand
# ============================================================================


def _should_retry(exception):
    """Determine if we should retry on this exception."""
    if isinstance(exception, KeyboardInterrupt):
        return False
    from openai import APIError, RateLimitError

    return isinstance(exception, (RateLimitError, APIError, ValidationError))


@retry(
    retry=retry_if_exception(_should_retry),
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=4, max=64),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)
def clean_agenda_content(content: str) -> str:
    """Remove structured fields from content, keeping only unstructured prose.
    
    After LLM extraction, we remove all the "**Field Name:** value" patterns
    since they're now in structured fields. This keeps only unstructured text
    that doesn't fit into any specific field.
    
    Args:
        content: Original agenda content
        
    Returns:
        Cleaned content with only unstructured prose
    """
    if not content:
        return ""
    
    # Split by paragraphs (double newline)
    paragraphs = re.split(r'\n\n+', content)
    cleaned_paragraphs = []
    
    for para in paragraphs:
        # Skip empty paragraphs
        if not para.strip():
            continue
            
        # Skip marker lines like [a:openai] or [sec:...]
        if re.match(r'^\s*\\?\[(?:a|sec):[^\]]+\\?\]\s*$', para.strip()):
            logger.debug(f"Skipping marker line: {para.strip()[:50]}")
            continue
        
        # Skip paragraphs that start with a structured field marker "**Field:**" or "**Field**:"
        # This includes the entire paragraph (field name + value)
        # Handle both formats: **Field**: (colon outside) and **Field:** (colon inside bold)
        stripped = para.strip()
        if re.match(r'^\s*\*\*[^*]+(:\*\*|\*\*:)\s*', stripped):
            logger.debug(f"Skipping structured field: {stripped[:80]}")
            continue
        
        # Skip header markers that might be at the end (e.g., "## Next Section")
        if re.match(r'^\s*#+\s+', para.strip()):
            logger.debug(f"Skipping header: {para.strip()[:50]}")
            continue
        
        # Keep this paragraph - it's unstructured content
        logger.debug(f"Keeping paragraph: {para.strip()[:80]}")
        cleaned_paragraphs.append(para.strip())
    
    # Join paragraphs with double newline
    cleaned = '\n\n'.join(cleaned_paragraphs)
    
    logger.debug(f"Cleaned content length: {len(cleaned)} (from {len(content)})")
    return cleaned


# ============================================================================
# Paper Enrichment Functions
# ============================================================================


def enrich_papers_from_db(doc: ProcessedDocument, verbose: bool = False) -> tuple[int, int]:
    """Enrich Paper objects with data from classify database and add missing papers.
    
    Args:
        doc: ProcessedDocument with parsed papers
        verbose: If True, show detailed list of missing URLs
        
    Returns:
        Tuple of (enriched_count, added_count) - papers enriched and papers added to DB
    """
    if not _SHALLOW_REVIEW_AVAILABLE:
        logger.warning("shallow_review modules not available - skipping paper enrichment")
        return (0, 0)
    
    from shallow_review.draft_types import Paper
    
    # Collect all paper URLs from all agendas
    paper_urls: set[str] = set()
    papers_by_url: dict[str, list[Paper]] = {}
    
    for item in doc.items:
        if item.agenda_attributes and item.agenda_attributes.outputs:
            for output in item.agenda_attributes.outputs:
                if isinstance(output, Paper) and output.link_url:
                    paper_urls.add(output.link_url)
                    if output.link_url not in papers_by_url:
                        papers_by_url[output.link_url] = []
                    papers_by_url[output.link_url].append(output)
    
    if not paper_urls:
        return (0, 0)
    
    enriched_count = 0
    added_count = 0
    missing_urls: list[tuple[str, str]] = []  # (original_url, normalized_url)
    
    # Look up papers in database
    with data_db_locked() as db:
        for url in paper_urls:
            normalized = normalize_url(url)
            
            # Try normalized URL first, then original
            row = db.execute(
                "SELECT data FROM classify WHERE url = ? OR url = ?",
                (normalized, url)
            ).fetchone()
            
            if row and row["data"]:
                # Enrich all Paper objects with this URL
                try:
                    data = json.loads(row["data"])
                    for paper in papers_by_url[url]:
                        paper.title = data.get("title")
                        paper.authors = data.get("authors", [])
                        paper.author_organizations = data.get("author_organizations", [])
                        paper.date = data.get("date")
                        paper.published_year = data.get("published_year")
                        paper.venue = data.get("venue")
                        paper.kind = data.get("kind")
                        paper.summary = data.get("summary")
                        paper.key_result = data.get("key_result")
                        enriched_count += 1
                except (json.JSONDecodeError, KeyError) as e:
                    logger.warning(f"Failed to parse classify data for {url}: {e}")
            else:
                # Paper not in database - add it
                missing_urls.append((url, normalized))
    
    # Add missing papers to classify table
    if missing_urls:
        from shallow_review.classify import add_classify_candidate
        
        console.print(f"[yellow]Found {len(missing_urls)} papers not in database, adding to classify table...[/yellow]")
        for original_url, normalized_url in missing_urls:
            try:
                is_new = add_classify_candidate(
                    url=normalized_url,
                    source="draft_parser",
                    source_url=None,
                    collect_relevancy=None,
                )
                if is_new:
                    added_count += 1
                    logger.info(f"Added missing paper to classify: {normalized_url}")
                    if original_url != normalized_url:
                        logger.debug(f"  (normalized from: {original_url})")
                else:
                    # Race condition - was added between check and add
                    logger.debug(f"Paper already exists (race condition): {normalized_url}")
            except Exception as e:
                logger.error(f"Failed to add paper {normalized_url} to classify: {e}")
                console.print(f"[red]Error: Failed to add {normalized_url}: {e}[/red]")
        
        # Warn about all missing papers
        console.print(
            f"[yellow]Warning: {len(missing_urls)} paper URLs not found in database "
            f"({added_count} added, {len(missing_urls) - added_count} already existed or failed)[/yellow]"
        )
        if verbose:
            for original_url, normalized_url in missing_urls[:10]:  # Show first 10
                display_url = normalized_url if original_url == normalized_url else f"{original_url} → {normalized_url}"
                console.print(f"  [dim]- {display_url}[/dim]")
            if len(missing_urls) > 10:
                console.print(f"  [dim]... and {len(missing_urls) - 10} more[/dim]")
    
    return (enriched_count, added_count)


# ============================================================================
# Validation Functions
# ============================================================================


def validate_document_structure(
    doc: ProcessedDocument, llm_processed_agenda_ids: set[str] | None = None
) -> tuple[list[str], list[str]]:
    """Validate document structure and return (errors, warnings).

    Checks:
    - Header levels make sense (agendas exactly one level below their containing section)
    - Section levels increase by at most one
    - No nested agendas
    - No strange tags in names (e.g. no other `[`)
    - All LLM-processed agendas have reasonable amount of fields (at least 5)

    Args:
        doc: ProcessedDocument to validate
        llm_processed_agenda_ids: Set of agenda IDs that were LLM-processed (for field count check)

    Returns:
        Tuple of (errors, warnings) lists
    """
    if llm_processed_agenda_ids is None:
        llm_processed_agenda_ids = set()
    errors: list[str] = []
    warnings: list[str] = []

    # Build a map of item_id -> DocumentItem for quick lookup
    items_by_id: dict[str, DocumentItem] = {item.id: item for item in doc.items}

    # Track section hierarchy
    section_stack: list[DocumentItem] = []

    for item in doc.items:
        # Check for strange tags in names
        if "[" in item.name and not re.search(r"\[(?:sec|a):[^\]]+\]", item.name):
            errors.append(
                f"Item '{item.name}' ({item.id}) contains unexpected '[' tag in name"
            )

        if item.item_type == ItemType.SECTION:
            # Validate section header level progression
            if section_stack:
                parent_section = section_stack[-1]
                level_diff = item.header_level - parent_section.header_level
                if level_diff > 1:
                    errors.append(
                        f"Section '{item.name}' ({item.id}) jumps by {level_diff} levels "
                        f"from parent '{parent_section.name}' ({parent_section.id})"
                    )
                elif level_diff < 0:
                    # This is fine, it's a sibling or uncle
                    pass

            # Update stack: pop until we find a parent at lower level
            while section_stack and section_stack[-1].header_level >= item.header_level:
                section_stack.pop()

            section_stack.append(item)

        elif item.item_type == ItemType.AGENDA:
            # Validate agenda is exactly one level below its containing section
            # Use parent_id to find the actual parent (which should be a section)
            if not item.parent_id:
                errors.append(
                    f"Agenda '{item.name}' ({item.id}) has no parent section"
                )
            else:
                parent = items_by_id.get(item.parent_id)
                if not parent:
                    errors.append(
                        f"Agenda '{item.name}' ({item.id}) has invalid parent_id: {item.parent_id}"
                    )
                elif parent.item_type != ItemType.SECTION:
                    errors.append(
                        f"Agenda '{item.name}' ({item.id}) has parent '{parent.name}' ({parent.id}) "
                        f"which is not a section"
                    )
                else:
                    expected_level = parent.header_level + 1
                    if item.header_level != expected_level:
                        errors.append(
                            f"Agenda '{item.name}' ({item.id}) has level {item.header_level}, "
                            f"expected {expected_level} (one level below section '{parent.name}')"
                        )

            # Check for nested agendas (agenda as parent of another agenda)
            if item.parent_id and items_by_id.get(item.parent_id):
                parent = items_by_id[item.parent_id]
                if parent.item_type == ItemType.AGENDA:
                    errors.append(
                        f"Agenda '{item.name}' ({item.id}) is nested under another agenda "
                        f"'{parent.name}' ({parent.id})"
                    )

            # Check agenda has reasonable amount of fields (at least 5 non-empty)
            # Only check for agendas that were LLM-processed
            if item.agenda_attributes and item.id in llm_processed_agenda_ids:
                field_count = sum(
                    [
                        1 if item.agenda_attributes.who_edits else 0,
                        1 if item.agenda_attributes.one_sentence_summary else 0,
                        1 if item.agenda_attributes.theory_of_change else 0,
                        1 if item.agenda_attributes.see_also else 0,
                        1 if item.agenda_attributes.orthodox_problems else 0,
                        1 if item.agenda_attributes.target_case else 0,
                        1 if item.agenda_attributes.broad_approach else 0,
                        1 if item.agenda_attributes.some_names else 0,
                        1 if item.agenda_attributes.estimated_ftes else 0,
                        1 if item.agenda_attributes.critiques else 0,
                        1 if item.agenda_attributes.funded_by else 0,
                        1 if item.agenda_attributes.outputs else 0,
                        1 if item.agenda_attributes.other_attributes else 0,
                    ]
                )
                if field_count < 5:
                    warnings.append(
                        f"Agenda '{item.name}' ({item.id}) has only {field_count} fields "
                        f"(expected at least 5)"
                    )
                
                # Validate see_also IDs reference valid items
                # Note: Items that don't start with "a:" or "sec:" are markdown links and are valid
                if item.agenda_attributes.see_also:
                    valid_ids = set(items_by_id.keys())
                    # Only validate items that look like IDs (start with a: or sec:)
                    id_refs = [ref for ref in item.agenda_attributes.see_also if ref.startswith(("a:", "sec:"))]
                    invalid_refs = [ref for ref in id_refs if ref not in valid_ids]
                    if invalid_refs:
                        errors.append(
                            f"Agenda '{item.name}' ({item.id}) has invalid see_also references: "
                            f"{invalid_refs}"
                        )
                    
                    # Check for duplicate see_also entries
                    if len(item.agenda_attributes.see_also) != len(set(item.agenda_attributes.see_also)):
                        duplicates = [
                            ref for ref in set(item.agenda_attributes.see_also)
                            if item.agenda_attributes.see_also.count(ref) > 1
                        ]
                        warnings.append(
                            f"Agenda '{item.name}' ({item.id}) has duplicate see_also entries: "
                            f"{duplicates}"
                        )
                
                # Validate outputs URLs are valid if present
                if item.agenda_attributes.outputs:
                    from shallow_review.draft_types import Paper
                    for output in item.agenda_attributes.outputs:
                        if isinstance(output, Paper) and output.link_url:
                            if not output.link_url.startswith(("http://", "https://")):
                                warnings.append(
                                    f"Agenda '{item.name}' ({item.id}) has invalid output URL: "
                                    f"{output.link_url}"
                                )
    
    # Warn about agendas not LLM-processed
    all_agenda_ids = {item.id for item in doc.items if item.item_type == ItemType.AGENDA}
    unprocessed_count = len(all_agenda_ids - llm_processed_agenda_ids)
    if unprocessed_count > 0:
        warnings.append(
            f"{unprocessed_count} agenda(s) were not LLM-processed (skipped due to --limit or processing error)"
        )

    return errors, warnings


@app.command()
def parse(
    input_file: str = typer.Argument(..., help="Path to draft markdown file"),
    output_file: str | None = typer.Option(
        None, "--output", "-o", help="Output file path base (generates both .json and .yaml, default: <input>-parsed)"
    ),
    cache_dir: str | None = typer.Option(
        None, "--cache-dir", help="LLM cache directory (default: .llm_cache)"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging"),
    limit: int | None = typer.Option(
        None, "--limit", "-n", help="Limit LLM extraction to first N agendas (full document is always parsed)"
    ),
    workers: int = typer.Option(4, "--workers", "-w", help="Number of parallel workers for LLM extraction"),
) -> None:
    """Parse a draft document into structured JSON and YAML.

    Step 1: Parses the document structure (sections [sec:...] and agendas [a:...])
    Step 2: Uses Claude Sonnet to extract structured metadata from each agenda.
    Step 3: Outputs both JSON and YAML formats.
    """
    setup_logging(verbose)

    input_path = Path(input_file)
    if not input_path.exists():
        console.print(f"[red]Error: File not found: {input_file}[/red]")
        raise typer.Exit(1)

    # Setup LLM
    cache_path = Path(cache_dir) if cache_dir else None
    setup_litellm(cache_path)

    # Determine output paths (JSON and YAML)
    if output_file is None:
        output_json_path = input_path.parent / f"{input_path.stem}-parsed.json"
        output_yaml_path = input_path.parent / f"{input_path.stem}-parsed.yaml"
    else:
        output_json_path = Path(output_file)
        # Generate YAML path by replacing extension
        output_yaml_path = output_json_path.with_suffix('.yaml')

    # ========================================================================
    # Step 1: Parse document structure
    # ========================================================================
    console.print(f"[cyan]Step 1: Parsing document structure from {input_file}...[/cyan]")
    doc = parse_document(input_path)

    # Count all sections and agendas (always parse full document)
    all_agenda_items = [item for item in doc.items if item.item_type == ItemType.AGENDA]
    total_sections = len([i for i in doc.items if i.item_type == ItemType.SECTION])
    total_agendas = len(all_agenda_items)
    
    console.print(
        f"[green]Found {total_sections} sections with {total_agendas} agendas[/green]"
    )
    
    # Apply limit only to LLM processing (not document parsing)
    if limit is not None:
        agenda_items = all_agenda_items[:limit]
        console.print(
            f"[yellow]Limiting LLM processing to first {limit} agendas (out of {total_agendas})[/yellow]"
        )
    else:
        agenda_items = all_agenda_items

    # Build agenda list for LLM (for see_also resolution)
    agenda_list = [
        {"id": item.id, "name": item.name}
        for item in doc.items
        if item.item_type in (ItemType.SECTION, ItemType.AGENDA)
    ]

    # ========================================================================
    # Step 2: Extract metadata with LLM (parallelized)
    # ========================================================================
    console.print(f"[cyan]Step 2: Extracting metadata with Claude Haiku ({workers} workers)...[/cyan]")

    # Track which agendas were LLM-processed
    llm_processed_agenda_ids: set[str] = set()
    
    # Progress tracking for parallel processing
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task(f"Processing {len(agenda_items)} agendas...", total=len(agenda_items))
        
        def update_progress(current: int, total: int, item_id: str, error: str | None):
            """Progress callback for parallel extraction."""
            if error:
                progress.update(task, description=f"[yellow]Warning:[/yellow] {item_id} failed", advance=1)
            else:
                progress.update(task, description=f"Processed {item_id}", advance=1)
        
        # Run parallel extraction
        from shallow_review.draft_processing import extract_agendas_parallel
        
        filled_items = extract_agendas_parallel(
            agenda_items=agenda_items,
            agenda_list=agenda_list,
            orthodox_problems=ORTHODOX_PROBLEMS,
            target_cases=TARGET_CASES,
            broad_approaches=BROAD_APPROACHES,
            max_workers=workers,
            progress_callback=update_progress,
        )
        
        # Replace items in doc.items with filled versions
        item_id_to_filled = {item.id: item for item in filled_items}
        for doc_idx, doc_item in enumerate(doc.items):
            if doc_item.id in item_id_to_filled:
                doc.items[doc_idx] = item_id_to_filled[doc_item.id]
        
        # Track which agendas were LLM-processed
        for item in filled_items:
            if item.agenda_attributes:
                llm_processed_agenda_ids.add(item.id)

    # ========================================================================
    # Step 3: Enrich papers from database
    # ========================================================================
    console.print("[cyan]Step 3: Enriching papers from database...[/cyan]")
    enriched_count, added_count = enrich_papers_from_db(doc, verbose=verbose)
    console.print(
        f"[green]Enriched {enriched_count} papers, added {added_count} new papers to classify table[/green]"
    )

    # ========================================================================
    # Step 4: Validate structure
    # ========================================================================
    console.print("[cyan]Step 3: Validating parsed document...[/cyan]")
    errors, warnings = validate_document_structure(doc, llm_processed_agenda_ids)

    # Add LLM-detected parsing issues to warnings
    for item in doc.items:
        if item.parsing_issues:
            for issue in item.parsing_issues:
                warnings.append(f"{item.id}: {issue}")

    # Display errors and warnings
    if errors:
        console.print(f"\n[red]Errors found ({len(errors)}):[/red]")
        for error in errors:
            console.print(f"  [red]ERROR:[/red] {error}")

    if warnings:
        console.print(f"\n[yellow]Warnings found ({len(warnings)}):[/yellow]")
        for warning in warnings:
            console.print(f"  [yellow]WARNING:[/yellow] {warning}")

    if not errors and not warnings:
        console.print("[green]No errors or warnings found![/green]")

    # Convert PreparsedDocument to ProcessedDocument for output
    processed_doc = ProcessedDocument(
        source_file=doc.source_file,
        items=doc.items
    )

    # Write both JSON and YAML output
    # Use mode='json' to serialize enums and other Python objects as primitives
    output_data = processed_doc.model_dump(mode='json')
    
    # Write JSON
    output_json_path.write_text(json.dumps(output_data, indent=2, default=str))
    console.print(f"\n[green]JSON output written to {output_json_path}[/green]")
    
    # Write YAML
    output_yaml_path.write_text(yaml.dump(output_data, default_flow_style=False, sort_keys=False, allow_unicode=True))
    console.print(f"[green]YAML output written to {output_yaml_path}[/green]")

    # Exit with error code if errors found
    if errors:
        console.print(f"\n[red]Parsing completed with {len(errors)} errors[/red]")
        raise typer.Exit(1)


# ============================================================================
# Helper functions for format command
# ============================================================================


def shorten_title(title: str, max_length: int = 40) -> str:
    """Shorten a title to max_length, cutting at last word and adding '...'."""
    if len(title) <= max_length:
        return title

    # Cut at max_length and find last space
    truncated = title[:max_length]
    last_space = truncated.rfind(' ')

    if last_space > 0:
        # Cut at last word boundary
        return truncated[:last_space] + "..."
    else:
        # No space found, just truncate
        return truncated + "..."


def get_url_title_from_db(url: str) -> str | None:
    """Look up URL in database and return title if found.

    Args:
        url: URL to look up

    Returns:
        Title string if found in database, None otherwise
    """
    if not _SHALLOW_REVIEW_AVAILABLE:
        return None

    try:
        # Normalize URL for lookup
        normalized = normalize_url(url)

        # Check classify table first (has more metadata)
        with data_db_locked() as db:
            row = db.execute(
                "SELECT data FROM classify WHERE url = ? OR url = ?",
                (url, normalized)
            ).fetchone()

            if row and row["data"]:
                data = json.loads(row["data"])
                return data.get("title")

            # Fallback to scrape table
            row = db.execute(
                "SELECT data FROM scrape WHERE url = ? OR url = ?",
                (url, normalized)
            ).fetchone()

            if row and row["data"]:
                data = json.loads(row["data"])
                return data.get("title")

        return None
    except Exception as e:
        logger.debug(f"Failed to look up URL {url}: {e}")
        return None


def format_url_link(url: str) -> str:
    """Format a URL as markdown link with title from database if available.

    Args:
        url: URL to format

    Returns:
        Markdown link string: [title](url) if title found, else just url
    """
    title = get_url_title_from_db(url)

    if title:
        # Shorten title if needed
        title = shorten_title(title, max_length=40)
        return f"[{title}]({url})"
    else:
        # No title found, just return URL
        return url


def format_see_also_item(item: str) -> str:
    """Format a see_also item - either a a:/sec: reference or a URL.

    Args:
        item: A see_also reference (e.g., "a:interpretability" or "https://...")

    Returns:
        Formatted markdown string
    """
    # Check if it's a URL
    if item.startswith(("http://", "https://")):
        # Format as URL with DB lookup
        return format_url_link(item)
    else:
        # It's a category/section reference - return as-is
        return item


# ============================================================================
# format subcommand
# ============================================================================


@app.command()
def format(
    input_file: str = typer.Argument(..., help="Path to parsed JSON file"),
    output_file: str | None = typer.Option(
        None, "--output", "-o", help="Output markdown file path (default: <input>-formatted.md)"
    ),
    template_file: str | None = typer.Option(
        None, "--template", "-t", help="Path to Jinja2 markdown template (default: draft_template.md)"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging"),
) -> None:
    """Format a parsed JSON file into a nicely formatted markdown document.

    Takes the JSON output from the parse command and applies a Jinja2 template
    to generate a human-readable markdown document with all agendas and attributes.
    """
    setup_logging(verbose)

    input_path = Path(input_file)
    if not input_path.exists():
        console.print(f"[red]Error: File not found: {input_file}[/red]")
        raise typer.Exit(1)

    # Determine template path
    if template_file is None:
        template_path = Path(__file__).parent / "draft_template.md"
    else:
        template_path = Path(template_file)

    if not template_path.exists():
        console.print(f"[red]Error: Template not found: {template_path}[/red]")
        raise typer.Exit(1)

    # Determine output path
    if output_file is None:
        output_path = input_path.parent / f"{input_path.stem}-formatted.md"
    else:
        output_path = Path(output_file)

    console.print(f"[cyan]Loading parsed data from {input_file}...[/cyan]")

    # Load parsed JSON
    try:
        data = json.loads(input_path.read_text())
    except json.JSONDecodeError as e:
        console.print(f"[red]Error: Invalid JSON in {input_file}: {e}[/red]")
        raise typer.Exit(1)

    # Load template
    console.print(f"[cyan]Applying template {template_path}...[/cyan]")
    template_text = template_path.read_text()
    template = Template(template_text)

    # Render template with helper functions
    try:
        rendered = template.render(
            **data,
            format_url=format_url_link,  # Make helper available to template
            shorten_title=shorten_title,
            format_see_also=format_see_also_item,
        )
    except Exception as e:
        console.print(f"[red]Error: Template rendering failed: {e}[/red]")
        if verbose:
            logger.exception("Template rendering error")
        raise typer.Exit(1)

    # Write output
    output_path.write_text(rendered)

    console.print(f"[green]Formatted document written to {output_path}[/green]")
    console.print(f"[dim]Sections: {len(data.get('sections', []))}, " +
                  f"Agendas: {sum(len(s.get('agendas', [])) for s in data.get('sections', []))}[/dim]")


# ============================================================================
# Main entry point
# ============================================================================


def main() -> None:
    """Entry point for CLI."""
    try:
        app()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        if logger.isEnabledFor(logging.DEBUG):
            logger.exception("Unhandled exception")
        sys.exit(1)


if __name__ == "__main__":
    main()
