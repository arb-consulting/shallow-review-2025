"""Typer CLI interface for shallow-review pipeline."""

import logging
import signal
import sys
from typing import Optional

import typer

from . import __version__
from .common import RUNS_PATH, is_shutdown_requested, request_shutdown
from .utils import console, setup_logging

logger = logging.getLogger(__name__)


def _signal_handler(signum, frame):
    """Handle Ctrl+C gracefully."""
    console.print("\n[yellow]⚠ Received interrupt signal, shutting down gracefully...[/yellow]")
    request_shutdown()
    # Don't exit immediately - let current operation complete

app = typer.Typer(
    name="shallow-review",
    help="Shallow review data pipeline and research tools",
    add_completion=False,
)


@app.command()
def info(
    source: Optional[str] = typer.Option(None, help="Filter statistics by source (applies to collect and classify tables)"),
) -> None:
    """Show configuration, paths, and database statistics."""
    import json
    from rich.table import Table
    from .common import DATA_PATH, PROMPTS_PATH, ROOT_PATH
    from .data_db import data_db_locked
    from .utils import one_line_histogram

    console.print("[bold]Shallow Review Configuration[/bold]\n")
    console.print(f"Version: {__version__}")
    console.print(f"Root path: {ROOT_PATH}")
    console.print(f"Data path: {DATA_PATH}")
    console.print(f"Prompts path: {PROMPTS_PATH}")
    console.print(f"Runs path: {RUNS_PATH}")
    if source:
        console.print(f"[cyan]Filter: source = {source}[/cyan]")
    console.print()

    # Database statistics
    console.print("[bold]Database Statistics[/bold]\n")
    
    with data_db_locked() as db:
        # Scrape table stats
        scrape_table = Table(title="Scrape Table", show_header=True, header_style="bold cyan")
        scrape_table.add_column("Total", justify="right")
        scrape_table.add_column("Success (2xx)", justify="right")
        scrape_table.add_column("Errors", justify="right")

        total_scrapes = db.execute("SELECT COUNT(*) as cnt FROM scrape").fetchone()["cnt"]
        success_scrapes = db.execute("SELECT COUNT(*) as cnt FROM scrape WHERE status_code >= 200 AND status_code < 300").fetchone()["cnt"]
        error_scrapes = db.execute("SELECT COUNT(*) as cnt FROM scrape WHERE error IS NOT NULL OR status_code >= 400").fetchone()["cnt"]

        scrape_table.add_row(str(total_scrapes), str(success_scrapes), str(error_scrapes))
    
    console.print(scrape_table)
    
    # Scrape distributions
    with data_db_locked() as db:
        # Extract JSON metrics
        scrapes_data = db.execute("SELECT data FROM scrape WHERE data IS NOT NULL AND status_code >= 200 AND status_code < 300").fetchall()
        if scrapes_data:
            size_full = [json.loads(row["data"]).get("size_full") for row in scrapes_data if json.loads(row["data"]).get("size_full")]
            if size_full:
                console.print(f"  [dim]{'size_full (bytes)':<25}[/dim] {one_line_histogram(size_full, bins=20, field_width=12)}")
            
            size_compressed = [json.loads(row["data"]).get("size_compressed") for row in scrapes_data if json.loads(row["data"]).get("size_compressed")]
            if size_compressed:
                console.print(f"  [dim]{'size_compressed':<25}[/dim] {one_line_histogram(size_compressed, bins=20, field_width=12)}")
            
            tokens_full = [json.loads(row["data"]).get("tokens_full") for row in scrapes_data if json.loads(row["data"]).get("tokens_full")]
            if tokens_full:
                console.print(f"  [dim]{'tokens_full':<25}[/dim] {one_line_histogram(tokens_full, bins=20, field_width=12)}")
            
            tokens_stripped = [json.loads(row["data"]).get("tokens_stripped") for row in scrapes_data if json.loads(row["data"]).get("tokens_stripped")]
            if tokens_stripped:
                console.print(f"  [dim]{'tokens_stripped':<25}[/dim] {one_line_histogram(tokens_stripped, bins=20, field_width=12)}")
            
            scrape_duration = [json.loads(row["data"]).get("scrape_duration") for row in scrapes_data if json.loads(row["data"]).get("scrape_duration")]
            if scrape_duration:
                console.print(f"  [dim]{'scrape_duration':<25}[/dim] {one_line_histogram(scrape_duration, bins=20, field_width=12)}")
    
    console.print()

    # Collect table stats
    with data_db_locked() as db:
        collect_table = Table(title="Collect Table", show_header=True, header_style="bold cyan")
        collect_table.add_column("Total", justify="right")
        collect_table.add_column("New", justify="right")
        collect_table.add_column("Done", justify="right")
        collect_table.add_column("Scrape Errors", justify="right")
        collect_table.add_column("Extract Errors", justify="right")

        # Build WHERE clause for source filter
        source_filter = ""
        source_params = []
        if source:
            source_filter = " AND source = ?"
            source_params = [source]

        total_collect = db.execute(f"SELECT COUNT(*) as cnt FROM collect{source_filter.replace('AND', 'WHERE') if source_filter else ''}", source_params).fetchone()["cnt"]
        new_collect = db.execute(f"SELECT COUNT(*) as cnt FROM collect WHERE status = 'new'{source_filter}", source_params).fetchone()["cnt"]
        done_collect = db.execute(f"SELECT COUNT(*) as cnt FROM collect WHERE status = 'done'{source_filter}", source_params).fetchone()["cnt"]
        scrape_err_collect = db.execute(f"SELECT COUNT(*) as cnt FROM collect WHERE status = 'scrape_error'{source_filter}", source_params).fetchone()["cnt"]
        extract_err_collect = db.execute(f"SELECT COUNT(*) as cnt FROM collect WHERE status = 'extract_error'{source_filter}", source_params).fetchone()["cnt"]

        collect_table.add_row(
            str(total_collect),
            str(new_collect),
            str(done_collect),
            str(scrape_err_collect),
            str(extract_err_collect)
        )
    
    console.print(collect_table)
    
    # Collect distributions
    with data_db_locked() as db:
        collect_query = "SELECT data FROM collect WHERE status = 'done' AND data IS NOT NULL"
        if source:
            collect_query += " AND source = ?"
            collect_data = db.execute(collect_query, [source]).fetchall()
        else:
            collect_data = db.execute(collect_query).fetchall()
        
        if collect_data:
            tokens_full = [json.loads(row["data"]).get("tokens_full") for row in collect_data if json.loads(row["data"]).get("tokens_full")]
            if tokens_full:
                console.print(f"  [dim]{'tokens_full':<25}[/dim] {one_line_histogram(tokens_full, bins=20, field_width=12)}")
            
            tokens_stripped = [json.loads(row["data"]).get("tokens_stripped") for row in collect_data if json.loads(row["data"]).get("tokens_stripped")]
            if tokens_stripped:
                console.print(f"  [dim]{'tokens_stripped':<25}[/dim] {one_line_histogram(tokens_stripped, bins=20, field_width=12)}")
            
            collect_duration = [json.loads(row["data"]).get("collect_duration") for row in collect_data if json.loads(row["data"]).get("collect_duration")]
            if collect_duration:
                console.print(f"  [dim]{'collect_duration':<25}[/dim] {one_line_histogram(collect_duration, bins=20, field_width=12)}")
            
            quality_scores = [json.loads(row["data"]).get("collection_quality_score") for row in collect_data if json.loads(row["data"]).get("collection_quality_score")]
            if quality_scores:
                console.print(f"  [dim]{'quality_score':<25}[/dim] {one_line_histogram(quality_scores, bins=20, field_width=12)}")
            
            # Extract all link relevancy scores
            all_relevancy = []
            for row in collect_data:
                data_obj = json.loads(row["data"])
                links = data_obj.get("links", [])
                for link in links:
                    if isinstance(link, dict) and "ai_safety_relevancy" in link:
                        all_relevancy.append(link["ai_safety_relevancy"])
            if all_relevancy:
                console.print(f"  [dim]{'link_relevancy':<25}[/dim] {one_line_histogram(all_relevancy, bins=20, field_width=12)}")
    
    console.print()

    # Classify table stats
    with data_db_locked() as db:
        classify_table = Table(title="Classify Table", show_header=True, header_style="bold cyan")
        classify_table.add_column("Total", justify="right")
        classify_table.add_column("New", justify="right")
        classify_table.add_column("Done", justify="right")
        classify_table.add_column("Scrape Errors", justify="right")
        classify_table.add_column("Classify Errors", justify="right")

        # Build WHERE clause for source filter
        source_filter = ""
        source_params = []
        if source:
            source_filter = " AND source = ?"
            source_params = [source]

        total_classify = db.execute(f"SELECT COUNT(*) as cnt FROM classify{source_filter.replace('AND', 'WHERE') if source_filter else ''}", source_params).fetchone()["cnt"]
        new_classify = db.execute(f"SELECT COUNT(*) as cnt FROM classify WHERE status = 'new'{source_filter}", source_params).fetchone()["cnt"]
        done_classify = db.execute(f"SELECT COUNT(*) as cnt FROM classify WHERE status = 'done'{source_filter}", source_params).fetchone()["cnt"]
        scrape_err_classify = db.execute(f"SELECT COUNT(*) as cnt FROM classify WHERE status = 'scrape_error'{source_filter}", source_params).fetchone()["cnt"]
        classify_err_classify = db.execute(f"SELECT COUNT(*) as cnt FROM classify WHERE status = 'classify_error'{source_filter}", source_params).fetchone()["cnt"]

        classify_table.add_row(
            str(total_classify),
            str(new_classify),
            str(done_classify),
            str(scrape_err_classify),
            str(classify_err_classify)
        )
    
    console.print(classify_table)
    
    # Classify distributions
    with data_db_locked() as db:
        # Relevance scores from columns
        ai_safety_query = "SELECT ai_safety_relevance FROM classify WHERE ai_safety_relevance IS NOT NULL"
        if source:
            ai_safety_query += " AND source = ?"
            ai_safety_relevance = [row["ai_safety_relevance"] for row in db.execute(ai_safety_query, [source]).fetchall()]
        else:
            ai_safety_relevance = [row["ai_safety_relevance"] for row in db.execute(ai_safety_query).fetchall()]
        if ai_safety_relevance:
            console.print(f"  [dim]{'ai_safety_relevance':<25}[/dim] {one_line_histogram(ai_safety_relevance, bins=20, field_width=12)}")
        
        shallow_review_query = "SELECT shallow_review_inclusion FROM classify WHERE shallow_review_inclusion IS NOT NULL"
        if source:
            shallow_review_query += " AND source = ?"
            shallow_review_inclusion = [row["shallow_review_inclusion"] for row in db.execute(shallow_review_query, [source]).fetchall()]
        else:
            shallow_review_inclusion = [row["shallow_review_inclusion"] for row in db.execute(shallow_review_query).fetchall()]
        if shallow_review_inclusion:
            console.print(f"  [dim]{'shallow_review_inclusion':<25}[/dim] {one_line_histogram(shallow_review_inclusion, bins=20, field_width=12)}")
        
        collect_relevancy_query = "SELECT collect_relevancy FROM classify WHERE collect_relevancy IS NOT NULL"
        if source:
            collect_relevancy_query += " AND source = ?"
            collect_relevancy = [row["collect_relevancy"] for row in db.execute(collect_relevancy_query, [source]).fetchall()]
        else:
            collect_relevancy = [row["collect_relevancy"] for row in db.execute(collect_relevancy_query).fetchall()]
        if collect_relevancy:
            console.print(f"  [dim]{'collect_relevancy':<25}[/dim] {one_line_histogram(collect_relevancy, bins=20, field_width=12)}")
        
        # Extract JSON metrics
        classify_data_query = "SELECT data FROM classify WHERE status = 'done' AND data IS NOT NULL"
        if source:
            classify_data_query += " AND source = ?"
            classify_data = db.execute(classify_data_query, [source]).fetchall()
        else:
            classify_data = db.execute(classify_data_query).fetchall()
        if classify_data:
            tokens_full = [json.loads(row["data"]).get("tokens_full") for row in classify_data if json.loads(row["data"]).get("tokens_full")]
            if tokens_full:
                console.print(f"  [dim]{'tokens_full':<25}[/dim] {one_line_histogram(tokens_full, bins=20, field_width=12)}")
            
            tokens_stripped = [json.loads(row["data"]).get("tokens_stripped") for row in classify_data if json.loads(row["data"]).get("tokens_stripped")]
            if tokens_stripped:
                console.print(f"  [dim]{'tokens_stripped':<25}[/dim] {one_line_histogram(tokens_stripped, bins=20, field_width=12)}")
            
            classify_duration = [json.loads(row["data"]).get("classify_duration") for row in classify_data if json.loads(row["data"]).get("classify_duration")]
            if classify_duration:
                console.print(f"  [dim]{'classify_duration':<25}[/dim] {one_line_histogram(classify_duration, bins=20, field_width=12)}")


@app.command()
def reset_classify(
    kind: Optional[str] = typer.Option(None, help="Filter by kind"),
    source: Optional[str] = typer.Option(None, help="Filter by source"),
    status: Optional[str] = typer.Option(None, help="Filter by current status"),
    remove_scrapes: bool = typer.Option(False, "--remove-scrapes", help="Also delete scrapes for matching URLs"),
) -> None:
    """Reset classify table entries to 'new' status, optionally deleting their scrapes."""
    from pathlib import Path
    
    from .common import ClassifyStatus, SCRAPED_PATH
    from .data_db import data_db_locked
    from .scrape import get_scrape_path
    from .utils import url_hash

    # Build WHERE clause and parameters
    conditions = []
    params = []
    
    if kind:
        conditions.append("kind = ?")
        params.append(kind)
    
    if source:
        conditions.append("source = ?")
        params.append(source)
    
    if status:
        conditions.append("status = ?")
        params.append(status)
    
    where_clause = ""
    if conditions:
        where_clause = " WHERE " + " AND ".join(conditions)
    
    # Get matching entries and their current status
    with data_db_locked() as db:
        query = f"SELECT url, status FROM classify{where_clause}"
        cursor = db.execute(query, params)
        matching_rows = cursor.fetchall()
    
    if not matching_rows:
        console.print("[yellow]No matching entries found[/yellow]")
        return
    
    total_affected = len(matching_rows)
    already_new = sum(1 for row in matching_rows if row["status"] == ClassifyStatus.NEW.value)
    to_change = total_affected - already_new
    
    # Show what will be affected
    console.print(f"[bold]Found {total_affected} matching entries[/bold]")
    if to_change == 0:
        console.print("[yellow]All entries are already 'new', nothing to change[/yellow]")
        if not remove_scrapes:
            return
    else:
        console.print(f"  - {already_new} already 'new'")
        console.print(f"  - {to_change} will be reset to 'new'")
    console.print()
    
    # Update entries to 'new'
    if to_change > 0:
        with data_db_locked() as db:
            # Build update query - add condition to only update non-new entries
            update_conditions = conditions.copy()
            if not status:
                # Only add status filter if not already filtering by status
                update_conditions.append("status != ?")
            
            update_where = " WHERE " + " AND ".join(update_conditions)
            update_params = [ClassifyStatus.NEW.value] + params
            if not status:
                update_params.append(ClassifyStatus.NEW.value)
            
            update_query = f"UPDATE classify SET status = ?{update_where}"
            db.execute(update_query, update_params)
            db.commit()
        
        console.print(f"[green]✓ Reset {to_change} entries to 'new'[/green]")
    
    # Delete scrapes if requested (primary: database rows, secondary: files)
    scrapes_deleted = 0
    if remove_scrapes:
        urls_to_delete = [row["url"] for row in matching_rows]
        
        # Primary: Delete from scrape table
        with data_db_locked() as db:
            url_placeholders = ",".join("?" * len(urls_to_delete))
            delete_query = f"DELETE FROM scrape WHERE url IN ({url_placeholders})"
            cursor = db.execute(delete_query, urls_to_delete)
            scrapes_deleted = cursor.rowcount
            db.commit()
        
        console.print(f"[green]✓ Deleted {scrapes_deleted} scrape table rows[/green]")
        
        # Secondary: Delete scrape files (if they exist)
        files_deleted = 0
        stripped_deleted = 0
        for url in urls_to_delete:
            scrape_path = get_scrape_path(url)
            if scrape_path.exists():
                scrape_path.unlink()
                files_deleted += 1
            
            # Also check for stripped HTML file (if SAVE_STRIPPED_HTML was enabled)
            hash_value = url_hash(url)
            stripped_path = SCRAPED_PATH / f"{hash_value}-stripped.html"
            if stripped_path.exists():
                stripped_path.unlink()
                stripped_deleted += 1
        
        if files_deleted > 0:
            console.print(f"[green]✓ Deleted {files_deleted} scrape files[/green]")
        if stripped_deleted > 0:
            console.print(f"[green]✓ Deleted {stripped_deleted} stripped HTML files[/green]")
    
    # Print summary
    console.print()
    console.print("[bold]Summary:[/bold]")
    console.print(f"  Total affected: {total_affected}")
    console.print(f"  Changed to 'new': {to_change}")
    if remove_scrapes:
        console.print(f"  Scrapes deleted: {scrapes_deleted}")


@app.command()
def add(
    file: str = typer.Argument(..., help="File with URLs (one per line, or CSV)"),
    phase: str = typer.Option("auto", help="Phase: auto|collect|classify (auto=detect automatically)"),
    source: Optional[str] = typer.Option(None, help="Source label for tracking"),
    workers: int = typer.Option(1, help="Number of worker threads (safe with Selenium, use 1 with Playwright)"),
    model: str = typer.Option("anthropic/claude-haiku-4-5", help="Model for auto-detection"),
) -> None:
    """Add URLs to collect or classify phases (auto-detects by default)."""
    from pathlib import Path

    from .add_items import add_item_auto, check_url_exists, normalize_url
    from .classify import add_classify_candidate
    from .collect import add_collect_source
    from .scrape import USE_SELENIUM
    from .stats import stats_context

    # Validate phase
    if phase not in ["auto", "collect", "classify"]:
        console.print(f"[red]Error: Invalid phase '{phase}'. Must be 'auto', 'collect', or 'classify'[/red]")
        sys.exit(1)

    # Read URLs from file
    file_path = Path(file)
    if not file_path.exists():
        console.print(f"[red]Error: File not found: {file}[/red]")
        sys.exit(1)

    from .add_items import is_valid_url
    
    urls = []
    invalid_urls = []
    with open(file_path) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue
            
            # Validate URL
            if not is_valid_url(line):
                invalid_urls.append((line_num, line))
                continue
            
            urls.append(line)

    if invalid_urls:
        console.print("[yellow]⚠ Warning: Invalid URLs found (skipped):[/yellow]")
        for line_num, url in invalid_urls[:10]:  # Show first 10
            console.print(f"  Line {line_num}: {url[:80]}")
        if len(invalid_urls) > 10:
            console.print(f"  ... and {len(invalid_urls) - 10} more")
        console.print()

    if not urls:
        console.print("[yellow]No valid URLs found in file[/yellow]")
        return

    backend = "selenium" if USE_SELENIUM else "playwright"
    if phase == "auto":
        console.print(f"Adding {len(urls)} URLs with [bold]auto-detection[/bold] (model: {model}, workers: {workers}, backend: {backend})...")
        if workers > 1 and not USE_SELENIUM:
            console.print("[yellow]⚠ WARNING: Playwright backend with workers > 1 may cause errors. Use workers=1 or switch to Selenium.[/yellow]")
    else:
        console.print(f"Adding {len(urls)} URLs to [bold]{phase}[/bold] phase...")
    console.print()

    # Process function for threading
    def process_url_add(url: str) -> tuple[str, str, str, bool]:
        """
        Process a single URL addition.
        
        Returns: (phase, normalized_url, status, is_new)
        - status: "added_collect", "added_classify", "exists", "error"
        """
        try:
            if phase == "auto":
                detected_phase, normalized_url, is_new = add_item_auto(url, source=source, model=model)
                if is_new:
                    status = f"added_{detected_phase}"
                else:
                    status = "exists"
                return (detected_phase, normalized_url, status, is_new)
                
            elif phase == "collect":
                normalized_url = normalize_url(url)
                # Only check collect table when explicitly adding to collect
                url_exists, existing_phase = check_url_exists(normalized_url, phase="collect")
                if url_exists:
                    return (existing_phase or "collect", normalized_url, "exists", False)
                else:
                    is_new = add_collect_source(normalized_url, source)
                    return ("collect", normalized_url, "added_collect" if is_new else "exists", is_new)
                    
            else:  # classify
                normalized_url = normalize_url(url)
                # Only check classify table when explicitly adding to classify
                url_exists, existing_phase = check_url_exists(normalized_url, phase="classify")
                if url_exists:
                    return (existing_phase or "classify", normalized_url, "exists", False)
                else:
                    is_new = add_classify_candidate(normalized_url, source or "manual", None, None)
                    return ("classify", normalized_url, "added_classify" if is_new else "exists", is_new)
                    
        except Exception as e:
            logger.error(f"Failed to add {url}: {e}", exc_info=True)
            raise

    # Add URLs with stats tracking and threading
    with stats_context(commandline=f"add {file} --phase {phase}") as stats:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        
        added_collect = 0
        added_classify = 0
        exists = 0
        errors = 0
        
        # Threading only useful for auto mode (scrapes + LLM calls)
        # Manual modes are fast (just DB inserts) so use 1 worker
        max_workers = workers if phase == "auto" else 1
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            future_to_url = {
                executor.submit(process_url_add, url): url
                for url in urls
            }
            
            # Process completed tasks
            processed = 0
            for future in as_completed(future_to_url):
                if is_shutdown_requested():
                    console.print("\n[yellow]Shutdown requested, stopping...[/yellow]")
                    executor.shutdown(wait=False, cancel_futures=True)
                    break
                
                processed += 1
                url = future_to_url[future]
                try:
                    detected_phase, normalized_url, status, is_new = future.result()
                    
                    if status == "added_collect":
                        added_collect += 1
                        console.print(f"[{processed}/{len(urls)}] [green]✓[/green] {url[:70]} → [cyan]collect[/cyan]")
                    elif status == "added_classify":
                        added_classify += 1
                        console.print(f"[{processed}/{len(urls)}] [green]✓[/green] {url[:70]} → [green]classify[/green]")
                    elif status == "exists":
                        exists += 1
                        console.print(f"[{processed}/{len(urls)}] [yellow]⊙[/yellow] {url[:70]} (in {detected_phase})")
                        
                except Exception as e:
                    errors += 1
                    console.print(f"[{processed}/{len(urls)}] [red]✗[/red] {url[:70]}: {str(e)[:50]}")

        console.print()
        
        if phase == "auto":
            console.print(f"[green]✓ Added {added_collect} to collect, {added_classify} to classify[/green]")
        else:
            total_added = added_collect + added_classify
            console.print(f"[green]✓ Added {total_added} new URLs[/green]")
            
        if exists > 0:
            console.print(f"[yellow]! {exists} URLs already existed[/yellow]")
        if errors > 0:
            console.print(f"[red]✗ {errors} URLs failed[/red]")

        stats.print_summary()


@app.command()
def collect(
    limit: int = typer.Option(100, help="Maximum sources to process"),
    workers: int = typer.Option(1, help="Number of worker threads (safe with Selenium, use 1 with Playwright)"),
    relevancy: float = typer.Option(0.3, help="Minimum relevancy threshold for links"),
    model: str = typer.Option("anthropic/claude-sonnet-4-5", help="LLM model to use"),
    max_tokens: int = typer.Option(100000, help="Max HTML tokens before error"),
    retry_errors: bool = typer.Option(False, "--retry-errors", help="Retry sources with extract_error status"),
) -> None:
    """Collect links from source pages."""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    from .collect import compute_collect
    from .common import CollectStatus, RunCollectConfig
    from .data_db import data_db_locked
    from .scrape import USE_SELENIUM
    from .stats import stats_context

    # Create config
    config = RunCollectConfig(
        limit=limit,
        workers=workers,
        relevancy_threshold=relevancy,
        model=model,
        max_html_tokens=max_tokens,
    )

    backend = "selenium" if USE_SELENIUM else "playwright"
    console.print("[bold]Starting collection phase...[/bold]\n")
    console.print(f"Config: limit={limit}, workers={workers}, relevancy≥{relevancy}, model={model}, backend={backend}")
    if workers > 1 and not USE_SELENIUM:
        console.print("[yellow]⚠ WARNING: Playwright backend with workers > 1 may cause errors. Switch USE_SELENIUM=True in scrape.py.[/yellow]")
    if retry_errors:
        console.print("[yellow]Retry mode: Will retry sources with extract_error status[/yellow]")
    console.print()

    # Get sources to process
    with data_db_locked() as db:
        if retry_errors:
            # Include both new and extract_error sources
            cursor = db.execute(
                """
                SELECT url FROM collect 
                WHERE status IN (?, ?) 
                ORDER BY added_at 
                LIMIT ?
                """,
                (CollectStatus.NEW.value, CollectStatus.EXTRACT_ERROR.value, limit),
            )
        else:
            # Only new sources
            cursor = db.execute(
                """
                SELECT url FROM collect 
                WHERE status = ? 
                ORDER BY added_at 
                LIMIT ?
                """,
                (CollectStatus.NEW.value, limit),
            )
        
        sources = [row["url"] for row in cursor.fetchall()]

    if not sources:
        console.print("[yellow]No sources to process[/yellow]")
        return

    console.print(f"Found {len(sources)} sources to process\n")

    # Process sources with stats tracking
    with stats_context(commandline=f"collect --limit {limit}") as stats:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        
        # Thread pool for parallel processing
        with ThreadPoolExecutor(max_workers=workers) as executor:
            # Submit all tasks
            future_to_url = {
                executor.submit(compute_collect, url, config, retry_errors): url
                for url in sources
            }
            
            # Process completed tasks
            processed = 0
            for future in as_completed(future_to_url):
                if is_shutdown_requested():
                    console.print("\n[yellow]Shutdown requested, stopping...[/yellow]")
                    executor.shutdown(wait=False, cancel_futures=True)
                    break
                
                processed += 1
                url = future_to_url[future]
                try:
                    result = future.result()
                    console.print(
                        f"[{processed}/{len(sources)}] [green]✓[/green] {url[:70]}: "
                        f"{len(result.links)} links (quality: {result.collection_quality_score:.2f})"
                    )
                except Exception as e:
                    # Log full error details (still captured in log file)
                    logger.error(f"Failed to process {url}: {str(e)}", exc_info=True)
                    console.print(f"[{processed}/{len(sources)}] [red]✗[/red] {url[:70]}: {str(e)[:80]}")

        console.print()
        stats.print_summary()


@app.command()
def classify(
    limit: int = typer.Option(100, help="Maximum candidates to process"),
    workers: int = typer.Option(1, help="Number of worker threads (safe with Selenium, use 1 with Playwright)"),
    min_relevancy: float = typer.Option(0.0, help="Minimum collect_relevancy to process (filter)"),
    model: str = typer.Option("anthropic/claude-sonnet-4-5", help="LLM model to use"),
    max_tokens: int = typer.Option(100000, help="Max HTML tokens before error"),
    retry_errors: bool = typer.Option(False, "--retry-errors", help="Retry candidates with classify_error status"),
) -> None:
    """Classify AI safety/alignment content."""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    from .classify import compute_classify
    from .common import ClassifyStatus, RunClassifyConfig
    from .data_db import data_db_locked
    from .scrape import USE_SELENIUM
    from .stats import stats_context

    # Create config
    config = RunClassifyConfig(
        limit=limit,
        workers=workers,
        min_relevancy=min_relevancy,
        model=model,
        max_html_tokens=max_tokens,
    )

    backend = "selenium" if USE_SELENIUM else "playwright"
    console.print("[bold]Starting classification phase...[/bold]\n")
    console.print(f"Config: limit={limit}, workers={workers}, model={model}, backend={backend}")
    if workers > 1 and not USE_SELENIUM:
        console.print("[yellow]⚠ WARNING: Playwright backend with workers > 1 may cause errors. Switch USE_SELENIUM=True in scrape.py.[/yellow]")
    if retry_errors:
        console.print("[yellow]Retry mode: Will retry candidates with classify_error status[/yellow]")
    if min_relevancy > 0.0:
        console.print(f"[cyan]Filtering: only candidates with collect_relevancy ≥ {min_relevancy}[/cyan]")
    console.print()

    # Get candidates to process
    with data_db_locked() as db:
        if retry_errors:
            # Include both new and classify_error candidates
            cursor = db.execute(
                """
                SELECT url FROM classify 
                WHERE status IN (?, ?) 
                AND (collect_relevancy >= ? OR collect_relevancy IS NULL)
                ORDER BY added_at 
                LIMIT ?
                """,
                (ClassifyStatus.NEW.value, ClassifyStatus.CLASSIFY_ERROR.value, min_relevancy, limit),
            )
        else:
            # Only new candidates
            cursor = db.execute(
                """
                SELECT url FROM classify 
                WHERE status = ? 
                AND (collect_relevancy >= ? OR collect_relevancy IS NULL)
                ORDER BY added_at 
                LIMIT ?
                """,
                (ClassifyStatus.NEW.value, min_relevancy, limit),
            )
        
        candidates = [row["url"] for row in cursor.fetchall()]

    if not candidates:
        console.print("[yellow]No candidates to process[/yellow]")
        return

    console.print(f"Found {len(candidates)} candidates to process\n")

    # Process candidates with stats tracking
    with stats_context(commandline=f"classify --limit {limit}") as stats:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        
        # Thread pool for parallel processing
        with ThreadPoolExecutor(max_workers=workers) as executor:
            # Submit all tasks
            future_to_url = {
                executor.submit(compute_classify, url, config, retry_errors): url
                for url in candidates
            }
            
            # Process completed tasks
            processed = 0
            for future in as_completed(future_to_url):
                if is_shutdown_requested():
                    console.print("\n[yellow]Shutdown requested, stopping...[/yellow]")
                    executor.shutdown(wait=False, cancel_futures=True)
                    break
                
                processed += 1
                url = future_to_url[future]
                try:
                    result = future.result()
                    top_cat = result.categories[0].id if result.categories else "none"
                    console.print(
                        f"[{processed}/{len(candidates)}] [green]✓[/green] {url[:60]}: "
                        f"safety={result.ai_safety_relevance:.2f}, "
                        f"incl={result.shallow_review_inclusion:.2f}, "
                        f"cat={top_cat}, "
                        f"conf={result.confidence:.2f}"
                    )
                except Exception as e:
                    # Log full error details (still captured in log file)
                    logger.error(f"Failed to classify {url}: {str(e)}", exc_info=True)
                    console.print(f"[{processed}/{len(candidates)}] [red]✗[/red] {url[:60]}: {str(e)[:60]}")

        console.print()
        stats.print_summary()


@app.command()
def import_feedback(
    csv_file: str = typer.Argument(..., help="CSV file with human feedback (URL,CATEGORY_ID,PAPER_ID,LINK_TEXT)"),
    source: str = typer.Option("manual", help="Feedback source label (e.g., 'SR2025-WIP-doc')"),
    detect_exclusions: bool = typer.Option(True, help="Detect excluded papers by comparing with exportable items"),
    min_shallow_review: float = typer.Option(0.4, help="Threshold for 'exportable' items when detecting exclusions"),
    reclassify_obsolete_llm: bool = typer.Option(False, help="ONE-TIME: Reset papers with obsolete LLM categories to 'new' instead of excluding"),
) -> None:
    """Import human feedback from CSV file into classify_feedback table."""
    from datetime import datetime, timezone
    from pathlib import Path

    from .feedback import import_feedback_from_csv, get_action_counts

    csv_path = Path(csv_file)
    if not csv_path.exists():
        console.print(f"[red]Error: CSV file not found: {csv_file}[/red]")
        sys.exit(1)
    
    console.print(f"[bold]Importing feedback from {csv_path.name}[/bold]")
    console.print(f"Source: {source}")
    console.print(f"Timestamp: {datetime.now(timezone.utc).isoformat()}")
    console.print()
    
    # Import feedback
    try:
        stats = import_feedback_from_csv(
            csv_path=csv_path,
            source=source,
            detect_exclusions=detect_exclusions,
            min_shallow_review=min_shallow_review,
            reclassify_obsolete_llm=reclassify_obsolete_llm
        )
    except Exception as e:
        console.print(f"[red]Error during import: {e}[/red]")
        logger.exception("Failed to import feedback")
        sys.exit(1)
    
    # Display results
    console.print(f"Parsed {stats.urls_parsed} unique URLs from CSV ({stats.urls_skipped} skipped)")
    if stats.obsolete_csv_categories > 0:
        console.print(f"[yellow]⚠ Found {stats.obsolete_csv_categories} papers with obsolete category IDs (marked for recategorization)[/yellow]")
    console.print()
    
    console.print(f"Added {stats.added_to_classify} new URLs to classify table")
    console.print()
    
    if detect_exclusions:
        console.print(f"Found {stats.excluded_count + stats.obsolete_llm_count} papers not in CSV:")
        console.print(f"  - Excluding: {stats.excluded_count}")
        if reclassify_obsolete_llm and stats.obsolete_llm_count > 0:
            console.print(f"  - Marked for re-classification (obsolete LLM category): {stats.obsolete_llm_count}")
            console.print(f"    Reset {stats.obsolete_llm_count} papers to status='new' for re-classification")
        console.print()
    
    console.print(f"[green]✓ Inserted {stats.feedback_inserted} feedback entries[/green]")
    if stats.feedback_duplicates > 0:
        console.print(f"[yellow]! Skipped {stats.feedback_duplicates} duplicate entries[/yellow]")
        
        # Show duplicates for debugging
        if stats.duplicates_list:
            console.print("\n[yellow]Duplicate entries (caught by unique indexes):[/yellow]")
            
            # Group by action for cleaner display
            from collections import defaultdict
            dups_by_action = defaultdict(list)
            for dup in stats.duplicates_list:
                dups_by_action[dup['action']].append(dup)
            
            for action in sorted(dups_by_action.keys()):
                dups = dups_by_action[action]
                console.print(f"\n  [cyan]{action}[/cyan] ({len(dups)} duplicates):")
                
                # Show first 10 of each action type
                for dup in dups[:10]:
                    url_short = dup['url'][:70]
                    if dup['category']:
                        console.print(f"    - {url_short} → {dup['category']}")
                    else:
                        console.print(f"    - {url_short}")
                
                if len(dups) > 10:
                    console.print(f"    ... and {len(dups) - 10} more")
    
    # Summary stats by action
    console.print()
    console.print(f"[bold]Feedback summary for source '{source}':[/bold]")
    action_counts = get_action_counts(source)
    for action, count in sorted(action_counts.items()):
        console.print(f"  {action:<15} {count:>5}")


@app.command()
def export_taxonomy(
    min_shallow_review: float = typer.Option(0.1, help="Minimum shallow_review_inclusion score"),
    min_ai_safety: float = typer.Option(0.1, help="Minimum ai_safety_relevance score"),
    min_collect: float = typer.Option(0.1, help="Minimum collect_relevancy score"),
    kinds: str = typer.Option("", help="Comma-separated list of accepted kinds (empty = all)"),
    source: str = typer.Option("", help="Comma-separated list of accepted sources (empty = all)"),
    respect_feedback: bool = typer.Option(True, help="Respect human feedback (include/exclude/reclassify)"),
    feedback_source: str = typer.Option("", help="Only respect feedback from this source (empty = all sources)"),
) -> None:
    """Export taxonomy with classified papers as markdown to stdout."""
    import json
    from collections import defaultdict

    from .data_db import data_db_locked
    from .taxonomy import load_taxonomy

    # Load taxonomy
    taxonomy = load_taxonomy()
    
    # Parse kinds filter
    kinds_filter = set()
    if kinds:
        kinds_filter = {k.strip() for k in kinds.split(",") if k.strip()}
    
    # Parse source filter
    source_filter = set()
    if source:
        source_filter = {s.strip() for s in source.split(",") if s.strip()}

    # Load feedback if requested
    feedback_by_url = {}
    if respect_feedback:
        with data_db_locked() as db:
            # Get all feedback for each URL (may have multiple actions)
            feedback_query = """
                SELECT url, action, human_category, notes
                FROM classify_feedback
                WHERE 1=1
            """
            feedback_params = []
            
            if feedback_source:
                feedback_query += " AND feedback_source = ?"
                feedback_params.append(feedback_source)
            
            feedback_query += " ORDER BY feedback_timestamp DESC"
            
            cursor = db.execute(feedback_query, feedback_params)
            
            # Build feedback dict - consolidate all actions per URL
            from collections import defaultdict
            feedback_actions = defaultdict(list)
            for row in cursor.fetchall():
                feedback_actions[row['url']].append({
                    'action': row['action'],
                    'human_category': row['human_category'],
                    'notes': row['notes']
                })
            
            # For each URL, consolidate actions (most recent timestamp first)
            for url, actions in feedback_actions.items():
                # Collect ALL human categories from reclassify actions
                human_categories = [
                    a['human_category'] for a in actions 
                    if a['action'] == 'reclassify' and a['human_category']
                ]
                
                feedback_by_url[url] = {
                    'has_include': any(a['action'] == 'include' for a in actions),
                    'has_exclude': any(a['action'] == 'exclude' for a in actions),
                    'has_reclassify': any(a['action'] == 'reclassify' for a in actions),
                    'has_note': any(a['action'] == 'note' for a in actions),
                    'human_categories': human_categories,  # List of all human categories
                    'notes': next((a['notes'] for a in actions if a['notes']), None),
                }

    # Get URLs with explicit include feedback (if respecting feedback)
    include_feedback_urls = set()
    if respect_feedback and feedback_by_url:
        include_feedback_urls = {
            url for url, fb in feedback_by_url.items() 
            if fb['has_include']
        }
    
    # Query classified items - include either threshold-passing OR include-feedback papers
    with data_db_locked() as db:
        if respect_feedback and include_feedback_urls:
            # Two-part query: normal filters OR has include feedback
            url_placeholders = ",".join("?" * len(include_feedback_urls))
            query = f"""
                SELECT url, url_hash_short, ai_safety_relevance, shallow_review_inclusion, 
                       collect_relevancy, kind, data
                FROM classify
                WHERE status = 'done'
                  AND (
                    (ai_safety_relevance >= ? 
                     AND shallow_review_inclusion >= ?
                     AND (collect_relevancy >= ? OR collect_relevancy IS NULL))
                    OR url IN ({url_placeholders})
                  )
            """
            params = [min_ai_safety, min_shallow_review, min_collect] + list(include_feedback_urls)
        else:
            # Original simple query
            query = """
                SELECT url, url_hash_short, ai_safety_relevance, shallow_review_inclusion, 
                       collect_relevancy, kind, data
                FROM classify
                WHERE status = 'done'
                  AND ai_safety_relevance >= ?
                  AND shallow_review_inclusion >= ?
                  AND (collect_relevancy >= ? OR collect_relevancy IS NULL)
            """
            params = [min_ai_safety, min_shallow_review, min_collect]
        
        if kinds_filter:
            placeholders = ",".join("?" * len(kinds_filter))
            query += f" AND kind IN ({placeholders})"
            params.extend(kinds_filter)
        
        if source_filter:
            placeholders = ",".join("?" * len(source_filter))
            query += f" AND source IN ({placeholders})"
            params.extend(source_filter)
        
        cursor = db.execute(query, params)
        rows = cursor.fetchall()

    if not rows and not feedback_by_url:
        console.print("[yellow]No items found matching filters[/yellow]", file=sys.stderr)
        return

    # Parse data JSON and group by top category
    from datetime import date as date_type
    
    items_by_category = defaultdict(list)
    excluded_count = 0
    included_by_feedback = 0
    reclassified_count = 0
    needs_recategorization = 0
    obsolete_llm_reclassified = 0
    
    for row in rows:
        try:
            url = row["url"]
            
            # Check feedback
            feedback = feedback_by_url.get(url)
            
            # Apply exclusion feedback (highest priority)
            if respect_feedback and feedback and feedback['has_exclude']:
                excluded_count += 1
                continue
            
            data = json.loads(row["data"])
            
            # Get top category ID (may be overridden by feedback)
            categories = data.get("categories", [])
            if not categories:
                console.print(f"[yellow]Warning: Item {url} has no categories, skipping[/yellow]", file=sys.stderr)
                continue
            
            # Check if needs recategorization (obsolete category from CSV)
            needs_recat = (respect_feedback and feedback and feedback.get('notes') and 
                          'NEEDS_RECATEGORIZATION' in feedback['notes'])
            
            # Check if was re-classified due to obsolete LLM category (tracked via 'note' action with keyword)
            obsolete_llm = (respect_feedback and feedback and feedback['has_note'] and
                           feedback.get('notes') and 'RECLASSIFY_OBSOLETE_LLM' in feedback['notes'])
            
            if needs_recat:
                needs_recategorization += 1
            
            if obsolete_llm:
                obsolete_llm_reclassified += 1
            
            # Determine which categories this paper should appear in
            category_ids = []
            is_multi_category = False
            
            if respect_feedback and feedback and feedback['has_reclassify'] and feedback['human_categories']:
                # Use human categories (can be multiple!)
                category_ids = feedback['human_categories']
                is_multi_category = len(category_ids) > 1
                reclassified_count += 1
            else:
                # Use LLM's top category
                category_ids = [categories[0]["id"]]
            
            # Track if this was included by feedback
            if respect_feedback and feedback and feedback['has_include']:
                # Check if it would have been excluded by normal filters
                if (row["shallow_review_inclusion"] < min_shallow_review or 
                    row["ai_safety_relevance"] < min_ai_safety):
                    included_by_feedback += 1
            
            # Build item dict with all needed fields
            item = {
                "url": row["url"],
                "url_hash_short": row["url_hash_short"],
                "title": data.get("title", "Untitled"),
                "authors": data.get("authors", []),
                "organization": data.get("organization", ""),
                "date": data.get("date", ""),
                "published_year": data.get("published_year"),
                "venue": data.get("venue", ""),
                "kind": row["kind"],
                "ai_safety_relevance": row["ai_safety_relevance"],
                "shallow_review_inclusion": row["shallow_review_inclusion"],
                "collect_relevancy": row["collect_relevancy"],
                "confidence": data.get("confidence"),
                "top_category_score": categories[0].get("score") if categories else None,
                "summary": data.get("summary", ""),
                "key_points": data.get("key_points", []),
                "needs_recategorization": needs_recat,
                "obsolete_llm_category": obsolete_llm,
                "is_multi_category": is_multi_category,
                "category_count": len(category_ids),
            }
            
            # Filter by date: only include items from 2024-11-01 onwards
            include_item = True
            if item["date"]:
                # Full date available - check if >= 2024-11-01
                try:
                    item_date = date_type.fromisoformat(item["date"])
                    cutoff_date = date_type(2024, 11, 1)
                    if item_date < cutoff_date:
                        include_item = False
                except (ValueError, TypeError):
                    # Invalid date format - include by default
                    pass
            elif item["published_year"]:
                # Only year available - accept 2024 and 2025
                try:
                    year = int(item["published_year"])
                    if year < 2024:
                        include_item = False
                except (ValueError, TypeError):
                    # Invalid year - include by default
                    pass
            # If no date info, include_item stays True (include by default)
            
            # Add to all assigned categories
            if include_item:
                for category_id in category_ids:
                    items_by_category[category_id].append(item)
            
        except (json.JSONDecodeError, KeyError) as e:
            console.print(f"[yellow]Warning: Failed to parse data for {row['url']}: {e}[/yellow]", file=sys.stderr)
            continue

    # Sort items within each category by shallow_review_inclusion (descending)
    for cat_id in items_by_category:
        items_by_category[cat_id].sort(key=lambda x: x["shallow_review_inclusion"], reverse=True)

    # Generate markdown output
    from datetime import datetime
    
    output_lines = []
    output_lines.append("# AI Safety Shallow Review")
    output_lines.append("")
    output_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}")
    output_lines.append("")
    output_lines.append(f"**Filters:** shallow_review≥{min_shallow_review}, ai_safety≥{min_ai_safety}, collect≥{min_collect}")
    if kinds_filter:
        output_lines.append(f"**Kinds:** {', '.join(sorted(kinds_filter))}")
    if source_filter:
        output_lines.append(f"**Sources:** {', '.join(sorted(source_filter))}")
    if respect_feedback:
        feedback_msg = "**Human feedback:** Respected"
        if feedback_source:
            feedback_msg += f" (source: {feedback_source})"
        output_lines.append(feedback_msg)
        if excluded_count > 0:
            output_lines.append(f"  - Excluded by feedback: {excluded_count}")
        if reclassified_count > 0:
            output_lines.append(f"  - Reclassified by feedback: {reclassified_count}")
        if included_by_feedback > 0:
            output_lines.append(f"  - Included by feedback (below thresholds): {included_by_feedback}")
        if needs_recategorization > 0:
            output_lines.append(f"  - ⚠️ Needs recategorization (obsolete CSV category): {needs_recategorization}")
        if obsolete_llm_reclassified > 0:
            output_lines.append(f"  - 🔄 Re-classified (obsolete LLM category, one-time): {obsolete_llm_reclassified}")
    output_lines.append("")
    # Count unique URLs (not total items, since papers can appear in multiple categories)
    unique_urls = set()
    for items in items_by_category.values():
        for item in items:
            unique_urls.add(item["url"])
    total_appearances = sum(len(items) for items in items_by_category.values())
    output_lines.append(f"**Total unique papers:** {len(unique_urls)} (appearing {total_appearances} times across categories)")
    output_lines.append("")
    output_lines.append("---")
    output_lines.append("")

    # Walk taxonomy tree and output sections
    def output_category(cat, level=1):
        """Recursively output category sections."""
        # Check if this category or any child has items
        has_items = False
        items_in_this_cat = []
        
        if cat.is_leaf:
            items_in_this_cat = items_by_category.get(cat.id, [])
            has_items = len(items_in_this_cat) > 0
        else:
            # Check children recursively
            for child in cat.children:
                if child.is_leaf:
                    if cat.id in items_by_category or child.id in items_by_category:
                        has_items = True
                        break
                else:
                    # Recursive check (simplified - we'll just check all leaf descendants)
                    leaf_ids = child.get_all_leaf_ids()
                    if any(lid in items_by_category for lid in leaf_ids):
                        has_items = True
                        break
        
        # Skip categories with no items
        if not has_items and not cat.is_leaf:
            # Check all descendants
            all_leaf_ids = cat.get_all_leaf_ids()
            has_items = any(lid in items_by_category for lid in all_leaf_ids)
            if not has_items:
                return
        
        # Output section header with ID
        header_prefix = "#" * (level + 1)
        size = ["1.6em", "1.5em", "1.4em", "1.3em", "1.2em", "1.1em"][level]
        output_lines.append(f"{header_prefix} <span style=\"font-size:{size}\">{cat.name}</span> <span style=\"color:#bbb\">[cat:{cat.id}]</span>\n")

        # Output description
        # output_lines.append(f"**Taxonomy description (internal):** *{cat.description.strip()}*")
        # output_lines.append("")
        
        # If leaf category, output rubrics and items
        if cat.is_leaf:
            output_lines.append("**<span style=\"color:#777\">Who edits (internal):</span>** **<span style=\"color:#da5\">take me</span>**  ")

            # Get SR2024 data if available
            sr = cat.sr2024 if hasattr(cat, 'sr2024') and cat.sr2024 else {}
            
            # Output SR2024-style rubrics (prefilled from SR2024 where available)
            if sr.get('summary'):
                output_lines.append(f"**One-sentence summary:** *(SR2024: {sr['summary']})*  ")
            else:
                output_lines.append("**One-sentence summary:**  ")
            
            if sr.get('theory_of_change'):
                output_lines.append(f"**Theory of change:** *(SR2024: {sr['theory_of_change']})*  ")
            else:
                output_lines.append("**Theory of change:**  ")
            
            if sr.get('see_also'):
                output_lines.append(f"**See also:** *(SR2024: {sr['see_also']})*  ")
            else:
                output_lines.append("**See also:**  ")
            
            if sr.get('orthodox_problems'):
                output_lines.append(f"**Orthodox problems:** *(SR2024: {sr['orthodox_problems']})*  ")
            else:
                output_lines.append("**Orthodox problems:**  ")
            
            if sr.get('target_case'):
                output_lines.append(f"**Target case:** *(SR2024: {sr['target_case']})*  ")
            else:
                output_lines.append("**Target case:**  ")
            
            if sr.get('broad_approach'):
                output_lines.append(f"**Broad approach:** *(SR2024: {sr['broad_approach']})*  ")
            else:
                output_lines.append("**Broad approach:**  ")
            
            if sr.get('names'):
                output_lines.append(f"**Key people:** *(SR2024: {sr['names']})*  ")
            else:
                output_lines.append("**Key people:**  ")
            
            if sr.get('ftes'):
                output_lines.append(f"**Estimated FTEs:** *(SR2024: {sr['ftes']})*  ")
            else:
                output_lines.append("**Estimated FTEs:**  ")
            
            if sr.get('critiques'):
                output_lines.append(f"**Critiques:** *(SR2024: {sr['critiques']})*  ")
            else:
                output_lines.append("**Critiques:**  ")
            
            if sr.get('funded_by'):
                output_lines.append(f"**Funded by:** *(SR2024: {sr['funded_by']})*  ")
            else:
                output_lines.append("**Funded by:**  ")
            
            if sr.get('funding_2023_4'):
                output_lines.append(f"**Funding in 2025:** *(SR2024 funding 2023-4: {sr['funding_2023_4']})*  ")
            else:
                output_lines.append("**Funding in 2025:**  ")
        
            if sr.get('outputs'):
                output_lines.append(f"**Outputs in 2025:**  \n*(SR2024 outputs: {sr['outputs']})*  ")
            else:
                output_lines.append("**Outputs in 2025:**  ")

        # If leaf category with items, output them
        if cat.is_leaf and items_in_this_cat:
            for item in items_in_this_cat:
                # Format: - **Title**, *Authors*, Date, Venue [stats] Summary • Key points
                
                # Use url_hash_short from database
                url_hash_short = item["url_hash_short"] or "unknown"
                
                # Title (linked) - move markers to brackets, not title
                title_part = f"**[{item['title']}]({item['url']})**"
                
                # Authors (italicized)
                authors_str = ", ".join(item["authors"][:3])  # First 3 authors
                if len(item["authors"]) > 3:
                    authors_str += " et al."
                authors_part = f"*{authors_str}*" if authors_str else ""
                
                # Organization (if no authors)
                if not authors_str and item["organization"]:
                    authors_part = f"*{item['organization']}*"
                
                # Date/Year - prefer full date, fallback to year
                date_part = ""
                if item.get("date"):
                    date_part = item["date"]
                elif item.get("published_year"):
                    date_part = str(item["published_year"])
                
                # Venue
                venue_part = item["venue"] if item["venue"] else ""
                
                # Stats in brackets with status markers
                markers = []
                
                # Obsolete category markers
                if item.get('needs_recategorization'):
                    markers.append("⚠️")
                if item.get('obsolete_llm_category'):
                    markers.append("🔄")
                
                # Multi-category marker
                if item.get('is_multi_category'):
                    markers.append(f"✌️(in {item['category_count']} categories)")
                
                marker_str = "".join(markers) + " " if markers else ""
                stats_part = f"<span style=\"color:#777\">[{marker_str}{item['kind']}, sr={item['shallow_review_inclusion']:.2f}, id:{url_hash_short}]</span>"
                
                # Summary
                summary = item["summary"].replace("\n", " ").strip()
                if summary:
                    summary = f"<span style=\"color:#777\">Summary: {summary}</span>"
                
                # Key points
                key_points_str = ""
                if item["key_points"]:
                    # Join first 3 key points
                    kp_list = item["key_points"][:3]
                    key_points_str = " • ".join(kp.replace("\n", " ").strip() for kp in kp_list)
                if key_points_str:
                    key_points_str = f"<span style=\"color:#777\">Key points: {key_points_str}</span>"
                
                # Assemble line: - **Title**, *Authors*, Date, Venue [stats] Summary • Key points
                parts = [title_part]
                if authors_part:
                    parts.append(authors_part)
                if date_part:
                    parts.append(date_part)
                if venue_part:
                    parts.append(venue_part)
                parts.append(stats_part)
                if summary:
                    parts.append(summary)
                if key_points_str:
                    parts.append(key_points_str)
                
                # Add as list item
                output_lines.append(f"- {', '.join(parts)}")
            
            # Add blank line after list
            output_lines.append("")

        output_lines.append("\n---\n")
        # Recurse to children (for non-leaf categories)
        if not cat.is_leaf:
            for child in cat.children:
                output_category(child, level + 1)
    
    # Output all top-level categories
    for top_cat in taxonomy.taxonomy:
        output_category(top_cat, level=1)

    # Write to stdout (not console, which adds Rich formatting)
    for line in output_lines:
        print(line)


def main() -> None:
    """Entry point for CLI."""
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, _signal_handler)
    signal.signal(signal.SIGTERM, _signal_handler)

    # Set up logging before running any commands
    setup_logging()

    try:
        app()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        sys.exit(130)
    except Exception as e:
        logger.exception("Fatal error")
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)


