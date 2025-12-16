#!/usr/bin/env -S uv run python
"""Process draft shallow review documents.

Provides tools to extract links and parse structured content from draft markdown documents.
"""

import csv
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
    from shallow_review.common import ClassifyStatus, SCRAPED_PATH
    from shallow_review.data_db import data_db_locked
    from shallow_review.scrape import get_scrape_path
    from shallow_review.utils import normalize_url, url_hash
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


def enrich_papers_from_db(doc: ProcessedDocument, verbose: bool = False, list_error_urls: int = 20, retry_errors: bool = False) -> tuple[int, int]:
    """Enrich Paper objects with data from classify database and add missing papers.
    
    Args:
        doc: ProcessedDocument with parsed papers
        verbose: If True, show detailed list of missing URLs
        list_error_urls: Number of error URLs to list (0 to disable listing)
        retry_errors: If True, reset error papers to 'new' status and remove their scrapes
        
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
    error_urls: list[tuple[str, str, str]] = []  # (original_url, normalized_url, status)
    
    # Look up papers in database
    with data_db_locked() as db:
        for url in paper_urls:
            normalized = normalize_url(url)
            
            # Try normalized URL first, then original - get status and data
            row = db.execute(
                "SELECT status, data FROM classify WHERE url = ? OR url = ?",
                (normalized, url)
            ).fetchone()
            
            if row:
                status = row["status"]
                data_json = row["data"]
                
                # Check for error statuses or missing data
                if status in ("scrape_error", "classify_error") or (status == "new" and not data_json):
                    # Paper exists but has error or not yet processed
                    error_urls.append((url, normalized, status))
                elif data_json:
                    # Enrich all Paper objects with this URL
                    try:
                        data = json.loads(data_json)
                        for paper in papers_by_url[url]:
                            paper.title = data.get("title")
                            paper.authors = data.get("authors", [])
                            paper.author_organizations = data.get("author_organizations", [])
                            paper.date = data.get("date")
                            paper.published_year = data.get("published_year")
                            paper.venue = data.get("venue")
                            paper.kind = data.get("kind")
                            enriched_count += 1
                    except (json.JSONDecodeError, KeyError) as e:
                        logger.warning(f"Failed to parse classify data for {url}: {e}")
                        error_urls.append((url, normalized, f"parse_error: {e}"))
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
    
    # Retry papers with errors if requested
    retried_count = 0
    scrapes_deleted = 0
    files_deleted = 0
    if retry_errors and error_urls:
        console.print(f"\n[cyan]Retrying {len(error_urls)} papers with errors...[/cyan]")
        
        # Collect URLs to retry (use normalized URLs)
        urls_to_retry = [normalized_url for _, normalized_url, _ in error_urls]
        
        # Update classify table: reset status to 'new' and clear data/error
        with data_db_locked() as db:
            url_placeholders = ",".join("?" * len(urls_to_retry))
            update_query = f"""
                UPDATE classify 
                SET status = ?, data = NULL, error = NULL, processed_at = NULL
                WHERE url IN ({url_placeholders})
            """
            cursor = db.execute(update_query, [ClassifyStatus.NEW.value] + urls_to_retry)
            retried_count = cursor.rowcount
            db.commit()
        
        console.print(f"[green]✓ Reset {retried_count} papers to 'new' status[/green]")
        
        # Delete scrapes from database
        with data_db_locked() as db:
            url_placeholders = ",".join("?" * len(urls_to_retry))
            delete_query = f"DELETE FROM scrape WHERE url IN ({url_placeholders})"
            cursor = db.execute(delete_query, urls_to_retry)
            scrapes_deleted = cursor.rowcount
            db.commit()
        
        if scrapes_deleted > 0:
            console.print(f"[green]✓ Deleted {scrapes_deleted} scrape table rows[/green]")
        
        # Delete scrape files
        for normalized_url in urls_to_retry:
            scrape_path = get_scrape_path(normalized_url)
            if scrape_path.exists():
                scrape_path.unlink()
                files_deleted += 1
            
            # Also check for stripped HTML file (if SAVE_STRIPPED_HTML was enabled)
            hash_value = url_hash(normalized_url)
            stripped_path = SCRAPED_PATH / f"{hash_value}-stripped.html"
            if stripped_path.exists():
                stripped_path.unlink()
        
        if files_deleted > 0:
            console.print(f"[green]✓ Deleted {files_deleted} scrape files[/green]")
    
    # List papers with errors (if not retrying or if listing is enabled)
    if error_urls and list_error_urls > 0 and not retry_errors:
        console.print(f"\n[yellow]Found {len(error_urls)} papers with classification errors or pending status:[/yellow]")
        for original_url, normalized_url, status in error_urls[:list_error_urls]:
            display_url = normalized_url if original_url == normalized_url else f"{original_url} → {normalized_url}"
            console.print(f"  [dim]- {display_url} [{status}][/dim]")
        if len(error_urls) > list_error_urls:
            console.print(f"  [dim]... and {len(error_urls) - list_error_urls} more[/dim]")
    elif retry_errors and error_urls:
        console.print(f"[green]✓ Ready to retry {len(error_urls)} papers (run classify to process them)[/green]")
    
    return (enriched_count, added_count)


# ============================================================================
# Validation Functions
# ============================================================================


def validate_document_structure(
    doc: ProcessedDocument, llm_processed_agenda_ids: set[str] | None = None
) -> tuple[list[str], list[str]]:
    """Validate document structure and return (errors, warnings).

    Checks:
    - Header levels make sense (all agendas at level 3, can be 1-2 levels below their section)
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
            # Validate agenda is at level 3 (can be 1 or 2 levels below its section)
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
                    # All agendas should be at level 3
                    if item.header_level != 3:
                        errors.append(
                            f"Agenda '{item.name}' ({item.id}) has level {item.header_level}, "
                            f"expected level 3 (all agendas must be at level 3)"
                        )
                    # Verify agenda is below its parent section
                    if item.header_level <= parent.header_level:
                        errors.append(
                            f"Agenda '{item.name}' ({item.id}) has level {item.header_level} "
                            f"which is not below parent section '{parent.name}' (level {parent.header_level})"
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
                        1 if item.agenda_attributes.target_case_text else 0,
                        1 if item.agenda_attributes.broad_approach_text else 0,
                        1 if item.agenda_attributes.some_names else 0,
                        1 if item.agenda_attributes.estimated_ftes else 0,
                        1 if item.agenda_attributes.critiques else 0,
                        1 if item.agenda_attributes.funded_by else 0,
                        1 if item.agenda_attributes.outputs else 0,
                        len(item.agenda_attributes.other_attributes) if item.agenda_attributes.other_attributes else 0,
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
    list_error_urls: int = typer.Option(
        20, "--list-error-urls", help="Number of error URLs to list (0 to disable, default: 20)"
    ),
    retry_errors: bool = typer.Option(
        False, "--retry-errors", help="Reset papers with errors to 'new' status and remove their scrapes for re-classification"
    ),
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
    console.print(f"[cyan]Step 2: Extracting metadata with LLM ({workers} workers)...[/cyan]")

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
    enriched_count, added_count = enrich_papers_from_db(doc, verbose=verbose, list_error_urls=list_error_urls, retry_errors=retry_errors)
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
# generate-doc subcommand
# ============================================================================


def _sort_papers_by_relevancy(doc: ProcessedDocument, verbose: bool = False) -> int:
    """Sort papers in each agenda's outputs by shallow_review_inclusion score (descending).
    
    Papers without a score in the database are sorted first (before ranked papers).
    If OutputSectionHeaders are present, papers are sorted within each section.
    
    Args:
        doc: ProcessedDocument to modify in-place
        verbose: If True, show debug information
        
    Returns:
        Number of paper outputs sorted
    """
    from shallow_review.draft_types import Paper, OutputSectionHeader
    
    # Collect all paper URLs
    paper_urls: set[str] = set()
    for item in doc.items:
        if item.agenda_attributes and item.agenda_attributes.outputs:
            for output in item.agenda_attributes.outputs:
                if isinstance(output, Paper) and output.link_url:
                    paper_urls.add(output.link_url)
    
    if not paper_urls:
        return 0
    
    # Query database for relevancy scores
    url_to_score: dict[str, float] = {}
    
    with data_db_locked() as db:
        # Batch query for all URLs
        placeholders = ','.join('?' * len(paper_urls))
        query = f"""
            SELECT url, shallow_review_inclusion 
            FROM classify 
            WHERE url IN ({placeholders})
            AND shallow_review_inclusion IS NOT NULL
        """
        
        rows = db.execute(query, list(paper_urls)).fetchall()
        for row in rows:
            url_to_score[row["url"]] = row["shallow_review_inclusion"]
        
        if verbose:
            console.print(f"[dim]  Found scores for {len(url_to_score)}/{len(paper_urls)} papers[/dim]")
    
    # Sort outputs in each agenda
    papers_sorted = 0
    
    for item in doc.items:
        if not item.agenda_attributes or not item.agenda_attributes.outputs:
            continue
        
        outputs = item.agenda_attributes.outputs
        
        if not outputs:
            continue
        
        # Group outputs into sections (separated by OutputSectionHeaders)
        sections = []
        current_section = []
        current_header = None
        
        for output in outputs:
            if isinstance(output, OutputSectionHeader):
                # Save previous section if it has content
                if current_section:
                    sections.append((current_header, current_section))
                # Start new section
                current_header = output
                current_section = []
            elif isinstance(output, Paper):
                current_section.append(output)
        
        # Add last section
        if current_section:
            sections.append((current_header, current_section))
        
        # Sort papers within each section
        new_outputs = []
        for header, papers in sections:
            # Add header if present
            if header:
                new_outputs.append(header)
            
            # Sort papers by score (descending), missing scores go to start
            papers_with_scores = [
                (url_to_score.get(p.link_url, float('inf')) if p.link_url else float('inf'), p)
                for p in papers
            ]
            papers_with_scores.sort(key=lambda x: x[0], reverse=True)
            
            # Add sorted papers
            new_outputs.extend(p for _, p in papers_with_scores)
            papers_sorted += len(papers)
        
        item.agenda_attributes.outputs = new_outputs
        
        if verbose and sections:
            total_papers = sum(len(papers) for _, papers in sections)
            console.print(f"[dim]  {item.id}: sorted {total_papers} papers in {len(sections)} section(s)[/dim]")
    
    return papers_sorted


@app.command("generate-doc")
def generate_doc(
    input_file: str = typer.Argument(..., help="Path to parsed YAML or JSON file"),
    output_file: str | None = typer.Option(
        None, "--output", "-o", help="Output file path (default: <input>-doc.md)"
    ),
    template_file: str | None = typer.Option(
        None, "--template", "-t", help="Path to Jinja2 template (default: templates/document-lists.md.jinja)"
    ),
    format: str = typer.Option(
        "md", "--format", "-f", help="Output format: md or html (not yet implemented)"
    ),
    sort_by_relevancy: bool = typer.Option(
        False, "--sort-by-relevancy", "-s", help="Sort papers by shallow_review_inclusion score (descending)"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging"),
) -> None:
    """Generate formatted documentation from parsed YAML/JSON.
    
    Takes the YAML or JSON output from the parse command and renders it using
    a Jinja2 template into a nicely formatted markdown document suitable for
    publishing or review.
    """
    setup_logging(verbose)
    
    input_path = Path(input_file)
    if not input_path.exists():
        console.print(f"[red]Error: File not found: {input_file}[/red]")
        raise typer.Exit(1)
    
    # Determine template path
    if template_file is None:
        template_path = Path(__file__).parent / "templates" / "document-lists.md.jinja"
    else:
        template_path = Path(template_file)
    
    if not template_path.exists():
        console.print(f"[red]Error: Template not found: {template_path}[/red]")
        raise typer.Exit(1)
    
    # Determine output path
    if output_file is None:
        suffix = ".md" if format == "md" else f".{format}"
        output_path = input_path.parent / f"{input_path.stem.replace('-parsed', '')}-doc{suffix}"
    else:
        output_path = Path(output_file)
    
    console.print(f"[cyan]Loading parsed data from {input_file}...[/cyan]")
    
    # Load parsed YAML or JSON
    try:
        if input_path.suffix in ['.yaml', '.yml']:
            data = yaml.safe_load(input_path.read_text())
        else:
            data = json.loads(input_path.read_text())
    except (yaml.YAMLError, json.JSONDecodeError) as e:
        console.print(f"[red]Error: Invalid YAML/JSON in {input_file}: {e}[/red]")
        raise typer.Exit(1)
    
    # Validate data structure
    try:
        doc = ProcessedDocument(**data)
    except ValidationError as e:
        console.print(f"[red]Error: Invalid document structure: {e}[/red]")
        if verbose:
            logger.exception("Validation error")
        raise typer.Exit(1)
    
    console.print(f"[green]Loaded {len(doc.items)} items[/green]")
    
    # Count sections and agendas
    sections = [item for item in doc.items if item.item_type == ItemType.SECTION]
    agendas = [item for item in doc.items if item.item_type == ItemType.AGENDA]
    console.print(f"[dim]  {len(sections)} sections, {len(agendas)} agendas[/dim]")
    
    # Sort papers by relevancy if requested
    if sort_by_relevancy:
        if not _SHALLOW_REVIEW_AVAILABLE:
            console.print("[yellow]Warning: shallow_review modules not available - cannot sort by relevancy[/yellow]")
        else:
            console.print("[cyan]Sorting papers by shallow_review_inclusion score...[/cyan]")
            papers_sorted = _sort_papers_by_relevancy(doc, verbose)
            console.print(f"[green]Sorted {papers_sorted} paper outputs[/green]")
    
    # Load template
    console.print(f"[cyan]Applying template {template_path.name}...[/cyan]")
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    
    # Create Jinja2 environment with template directory
    env = Environment(
        loader=FileSystemLoader(template_path.parent),
        autoescape=select_autoescape(['html', 'xml']) if format == 'html' else False,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    
    # Register custom filters
    def format_see_also_ref(ref: str, items_by_id: dict) -> str:
        """Format a see_also reference."""
        if ref.startswith(("http://", "https://")):
            return ref
        elif ref in items_by_id:
            return f"[{items_by_id[ref].name}](#{ref})"
        else:
            return ref
    
    def split_critiques(critiques_text: str) -> list[str]:
        """Split critiques string by commas, but not commas inside markdown links.
        
        Markdown links are [text](url), so we split by commas that are NOT
        inside square brackets or parentheses.
        """
        if not critiques_text:
            return []
        
        # First normalize whitespace (replace newlines with spaces)
        critiques_text = ' '.join(critiques_text.split())
        
        items = []
        current = []
        paren_depth = 0
        bracket_depth = 0
        
        for char in critiques_text:
            if char == '[':
                bracket_depth += 1
                current.append(char)
            elif char == ']':
                bracket_depth -= 1
                current.append(char)
            elif char == '(':
                paren_depth += 1
                current.append(char)
            elif char == ')':
                paren_depth -= 1
                current.append(char)
            elif char == ',' and paren_depth == 0 and bracket_depth == 0:
                # Split here - comma is outside both brackets and parentheses
                if current:
                    items.append(''.join(current).strip())
                current = []
            else:
                current.append(char)
        
        # Add last item
        if current:
            items.append(''.join(current).strip())
        
        return [item for item in items if item]
    
    env.filters['format_see_also_ref'] = format_see_also_ref
    env.filters['split_critiques'] = split_critiques
    
    # Load and render template
    try:
        template = env.get_template(template_path.name)
        
        # Prepare template context
        context = {
            'items': doc.items,
            'source_file': doc.source_file,
            'orthodox_problems': ORTHODOX_PROBLEMS,
            'target_cases': TARGET_CASES,
            'broad_approaches': BROAD_APPROACHES,
        }
        
        rendered = template.render(**context)
    except Exception as e:
        console.print(f"[red]Error: Template rendering failed: {e}[/red]")
        if verbose:
            logger.exception("Template rendering error")
        raise typer.Exit(1)
    
    # Write output
    output_path.write_text(rendered)
    
    console.print(f"[green]Generated document written to {output_path}[/green]")
    console.print(f"[dim]Format: {format}, Size: {len(rendered)} chars[/dim]")


# ============================================================================
# export-csv subcommand
# ============================================================================


@app.command("export-csv")
def export_csv(
    input_file: str = typer.Argument(..., help="Path to parsed JSON file"),
    output_dir: str | None = typer.Option(
        None, "--output-dir", "-o", help="Output directory (default: same as input file)"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging"),
) -> None:
    """Export parsed JSON to CSV files: one for agendas, one for papers.
    
    Creates two CSV files:
    - agendas.csv: One row per agenda with all attributes
    - papers.csv: One row per paper/link with agenda context
    """
    setup_logging(verbose)
    
    input_path = Path(input_file)
    if not input_path.exists():
        console.print(f"[red]Error: File not found: {input_file}[/red]")
        raise typer.Exit(1)
    
    # Determine output directory
    if output_dir is None:
        output_dir_path = input_path.parent
    else:
        output_dir_path = Path(output_dir)
        output_dir_path.mkdir(parents=True, exist_ok=True)
    
    console.print(f"[cyan]Loading parsed data from {input_file}...[/cyan]")
    
    # Load parsed JSON
    try:
        data = json.loads(input_path.read_text())
    except json.JSONDecodeError as e:
        console.print(f"[red]Error: Invalid JSON in {input_file}: {e}[/red]")
        raise typer.Exit(1)
    
    # Validate data structure
    try:
        doc = ProcessedDocument(**data)
    except ValidationError as e:
        console.print(f"[red]Error: Invalid document structure: {e}[/red]")
        if verbose:
            logger.exception("Validation error")
        raise typer.Exit(1)
    
    console.print(f"[green]Loaded {len(doc.items)} items[/green]")
    
    # Build item lookup map
    items_by_id: dict[str, DocumentItem] = {item.id: item for item in doc.items}
    
    # Build section hierarchy: for each item, find top-level section and sub-section
    def get_section_hierarchy(item: DocumentItem) -> tuple[str | None, str | None]:
        """Return (top_level_section_name, sub_section_name) for an item.
        
        Top-level section is header_level 1, sub-section is header_level 2.
        Traverses up the parent chain to find both.
        """
        top_section = None
        sub_section = None
        
        # Traverse up parent chain
        current_id = item.parent_id
        while current_id:
            parent = items_by_id.get(current_id)
            if not parent:
                break
            
            if parent.item_type == ItemType.SECTION:
                if parent.header_level == 1:
                    top_section = parent.name
                    break  # Found top-level, stop
                elif parent.header_level == 2:
                    sub_section = parent.name
                    # Continue to find top-level section
            
            current_id = parent.parent_id
        
        return (top_section, sub_section)
    
    # Collect agendas
    agendas = [item for item in doc.items if item.item_type == ItemType.AGENDA]
    console.print(f"[dim]Found {len(agendas)} agendas[/dim]")
    
    # Prepare agendas CSV
    agendas_rows = []
    papers_rows = []
    
    for agenda in agendas:
        if not agenda.agenda_attributes:
            continue
        
        top_section, sub_section = get_section_hierarchy(agenda)
        
        # Convert orthodox_problems IDs to names
        orthodox_problem_names = []
        for problem_id in agenda.agenda_attributes.orthodox_problems:
            if problem_id in ORTHODOX_PROBLEMS:
                orthodox_problem_names.append(ORTHODOX_PROBLEMS[problem_id]["name"])
            else:
                orthodox_problem_names.append(problem_id)  # Fallback to ID if not found
        
        # Count outputs (papers and links, not OutputSectionHeaders)
        from shallow_review.draft_types import Paper, OutputSectionHeader
        outputs_count = sum(
            1 for output in agenda.agenda_attributes.outputs
            if isinstance(output, Paper)
        )
        
        # Format see_also as comma-separated
        see_also_str = ", ".join(agenda.agenda_attributes.see_also) if agenda.agenda_attributes.see_also else ""
        
        # Format some_names as comma-separated
        some_names_str = ", ".join(agenda.agenda_attributes.some_names) if agenda.agenda_attributes.some_names else ""
        
        # Format orthodox_problems as comma-separated names
        orthodox_problems_str = ", ".join(orthodox_problem_names) if orthodox_problem_names else ""
        
        # Build agenda full name (same format as for papers)
        parts = []
        if top_section:
            parts.append(top_section)
        if sub_section:
            parts.append(sub_section)
        parts.append(agenda.name)
        agenda_full_name = " / ".join(parts)
        
        # Build agenda row
        agenda_row = {
            "name": agenda.name,
            "section": top_section or "",
            "sub_section": sub_section or "",
            "full_name": agenda_full_name,
            "one_sentence_summary": agenda.agenda_attributes.one_sentence_summary or "",
            "theory_of_change": agenda.agenda_attributes.theory_of_change or "",
            "see_also": see_also_str,
            "orthodox_problems": orthodox_problems_str,
            "target_case_text": agenda.agenda_attributes.target_case_text or "",
            "broad_approach_text": agenda.agenda_attributes.broad_approach_text or "",
            "some_names": some_names_str,
            "estimated_ftes": agenda.agenda_attributes.estimated_ftes or "",
            "critiques": agenda.agenda_attributes.critiques or "",
            "funded_by": agenda.agenda_attributes.funded_by or "",
            "outputs_count": outputs_count,
        }
        agendas_rows.append(agenda_row)
        
        # Extract papers from outputs
        for output in agenda.agenda_attributes.outputs:
            if isinstance(output, Paper):
                # Format authors as comma-separated
                authors_str = ", ".join(output.authors) if output.authors else ""
                
                # Format author_organizations as comma-separated
                author_orgs_str = ", ".join(output.author_organizations) if output.author_organizations else ""
                
                paper_row = {
                    "agenda_name": agenda.name,
                    "agenda_section": top_section or "",
                    "agenda_sub_section": sub_section or "",
                    "agenda_full_name": agenda_full_name,
                    "link_url": output.link_url or "",
                    "link_text": output.link_text or "",
                    "title": output.title or "",
                    "authors": authors_str,
                    "author_organizations": author_orgs_str,
                    "published_year": str(output.published_year) if output.published_year else "",
                    "date": output.date or "",
                }
                papers_rows.append(paper_row)
    
    # Write agendas CSV
    agendas_csv_path = output_dir_path / "agendas.csv"
    if agendas_rows:
        with open(agendas_csv_path, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "name", "section", "sub_section", "full_name", "one_sentence_summary",
                "theory_of_change", "see_also", "orthodox_problems",
                "target_case_text", "broad_approach_text", "some_names",
                "estimated_ftes", "critiques", "funded_by", "outputs_count"
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(agendas_rows)
        console.print(f"[green]Agendas CSV written to {agendas_csv_path}[/green]")
        console.print(f"[dim]  {len(agendas_rows)} agendas[/dim]")
    else:
        console.print(f"[yellow]No agendas found to export[/yellow]")
    
    # Write papers CSV
    papers_csv_path = output_dir_path / "papers.csv"
    if papers_rows:
        with open(papers_csv_path, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "agenda_name", "agenda_section", "agenda_sub_section",
                "agenda_full_name", "link_url", "link_text", "title",
                "authors", "author_organizations", "published_year", "date"
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(papers_rows)
        console.print(f"[green]Papers CSV written to {papers_csv_path}[/green]")
        console.print(f"[dim]  {len(papers_rows)} papers/links[/dim]")
    else:
        console.print(f"[yellow]No papers found to export[/yellow]")


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
