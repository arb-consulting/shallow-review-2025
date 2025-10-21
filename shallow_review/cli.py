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
def info() -> None:
    """Show configuration, paths, and database statistics."""
    from rich.table import Table
    from .common import DATA_PATH, PROMPTS_PATH, ROOT_PATH
    from .data_db import get_data_db

    console.print("[bold]Shallow Review Configuration[/bold]\n")
    console.print(f"Version: {__version__}")
    console.print(f"Root path: {ROOT_PATH}")
    console.print(f"Data path: {DATA_PATH}")
    console.print(f"Prompts path: {PROMPTS_PATH}")
    console.print(f"Runs path: {RUNS_PATH}")
    console.print()

    # Database statistics
    console.print("[bold]Database Statistics[/bold]\n")
    db = get_data_db()

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
    console.print()

    # Collect table stats
    collect_table = Table(title="Collect Table", show_header=True, header_style="bold cyan")
    collect_table.add_column("Total", justify="right")
    collect_table.add_column("New", justify="right")
    collect_table.add_column("Done", justify="right")
    collect_table.add_column("Scrape Errors", justify="right")
    collect_table.add_column("Extract Errors", justify="right")

    total_collect = db.execute("SELECT COUNT(*) as cnt FROM collect").fetchone()["cnt"]
    new_collect = db.execute("SELECT COUNT(*) as cnt FROM collect WHERE status = 'new'").fetchone()["cnt"]
    done_collect = db.execute("SELECT COUNT(*) as cnt FROM collect WHERE status = 'done'").fetchone()["cnt"]
    scrape_err_collect = db.execute("SELECT COUNT(*) as cnt FROM collect WHERE status = 'scrape_error'").fetchone()["cnt"]
    extract_err_collect = db.execute("SELECT COUNT(*) as cnt FROM collect WHERE status = 'extract_error'").fetchone()["cnt"]

    collect_table.add_row(
        str(total_collect),
        str(new_collect),
        str(done_collect),
        str(scrape_err_collect),
        str(extract_err_collect)
    )
    console.print(collect_table)
    console.print()

    # Classify table stats
    classify_table = Table(title="Classify Table", show_header=True, header_style="bold cyan")
    classify_table.add_column("Total", justify="right")
    classify_table.add_column("New", justify="right")
    classify_table.add_column("Done", justify="right")
    classify_table.add_column("Scrape Errors", justify="right")
    classify_table.add_column("Classify Errors", justify="right")

    total_classify = db.execute("SELECT COUNT(*) as cnt FROM classify").fetchone()["cnt"]
    new_classify = db.execute("SELECT COUNT(*) as cnt FROM classify WHERE status = 'new'").fetchone()["cnt"]
    done_classify = db.execute("SELECT COUNT(*) as cnt FROM classify WHERE status = 'done'").fetchone()["cnt"]
    scrape_err_classify = db.execute("SELECT COUNT(*) as cnt FROM classify WHERE status = 'scrape_error'").fetchone()["cnt"]
    classify_err_classify = db.execute("SELECT COUNT(*) as cnt FROM classify WHERE status = 'classify_error'").fetchone()["cnt"]

    classify_table.add_row(
        str(total_classify),
        str(new_classify),
        str(done_classify),
        str(scrape_err_classify),
        str(classify_err_classify)
    )
    console.print(classify_table)


@app.command()
def add(
    file: str = typer.Argument(..., help="File with URLs (one per line, or CSV)"),
    phase: str = typer.Option("auto", help="Phase: auto|collect|classify (auto=detect automatically)"),
    source: Optional[str] = typer.Option(None, help="Source label for tracking"),
    workers: int = typer.Option(1, help="Number of worker threads (WARNING: >1 may cause Playwright issues)"),
    model: str = typer.Option("anthropic/claude-haiku-4-5", help="Model for auto-detection"),
) -> None:
    """Add URLs to collect or classify phases (auto-detects by default).
    
    Note: Auto-detection involves scraping, which uses Playwright. Due to Playwright's 
    greenlet-based implementation, workers > 1 may cause errors. Use workers=1 (default) 
    for stability.
    """
    from pathlib import Path

    from .add_items import add_item_auto, check_url_exists, normalize_url
    from .classify import add_classify_candidate
    from .collect import add_collect_source
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

    if phase == "auto":
        console.print(f"Adding {len(urls)} URLs with [bold]auto-detection[/bold] (model: {model}, workers: {workers})...")
        if workers > 1:
            console.print("[yellow]⚠ WARNING: workers > 1 may cause Playwright errors. Use workers=1 for stability.[/yellow]")
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
                url_exists, existing_phase = check_url_exists(normalized_url)
                if url_exists:
                    return (existing_phase or "collect", normalized_url, "exists", False)
                else:
                    is_new = add_collect_source(normalized_url, source)
                    return ("collect", normalized_url, "added_collect" if is_new else "exists", is_new)
                    
            else:  # classify
                normalized_url = normalize_url(url)
                url_exists, existing_phase = check_url_exists(normalized_url)
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
    workers: int = typer.Option(1, help="Number of worker threads (>1 may cause Playwright issues, use with caution)"),
    relevancy: float = typer.Option(0.3, help="Minimum relevancy threshold for links"),
    model: str = typer.Option("anthropic/claude-sonnet-4-5", help="LLM model to use"),
    max_tokens: int = typer.Option(100000, help="Max HTML tokens before error"),
    retry_errors: bool = typer.Option(False, "--retry-errors", help="Retry sources with extract_error status"),
) -> None:
    """Collect links from source pages.
    
    Note: Uses Playwright for scraping. workers > 1 may cause errors due to Playwright's 
    greenlet-based implementation. Default workers=1 is recommended. With scrape caching, 
    this is usually fast enough.
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    from .collect import compute_collect
    from .common import CollectStatus, RunCollectConfig
    from .data_db import get_data_db
    from .stats import stats_context

    # Create config
    config = RunCollectConfig(
        limit=limit,
        workers=workers,
        relevancy_threshold=relevancy,
        model=model,
        max_html_tokens=max_tokens,
    )

    console.print("[bold]Starting collection phase...[/bold]\n")
    console.print(f"Config: limit={limit}, workers={workers}, relevancy≥{relevancy}, model={model}")
    if workers > 1:
        console.print("[yellow]⚠ WARNING: workers > 1 may cause Playwright errors. Use workers=1 for stability.[/yellow]")
    if retry_errors:
        console.print("[yellow]Retry mode: Will retry sources with extract_error status[/yellow]")
    console.print()

    # Get sources to process
    db = get_data_db()
    
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
    workers: int = typer.Option(1, help="Number of worker threads (>1 may cause Playwright issues, use with caution)"),
    min_relevancy: float = typer.Option(0.0, help="Minimum collect_relevancy to process (filter)"),
    model: str = typer.Option("anthropic/claude-sonnet-4-5", help="LLM model to use"),
    max_tokens: int = typer.Option(100000, help="Max HTML tokens before error"),
    retry_errors: bool = typer.Option(False, "--retry-errors", help="Retry candidates with classify_error status"),
) -> None:
    """Classify AI safety/alignment content.
    
    Note: Uses Playwright for scraping. workers > 1 may cause errors due to Playwright's 
    greenlet-based implementation. Default workers=1 is recommended. With scrape caching,  
    this is usually fast enough.
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    from .classify import compute_classify
    from .common import ClassifyStatus, RunClassifyConfig
    from .data_db import get_data_db
    from .stats import stats_context

    # Create config
    config = RunClassifyConfig(
        limit=limit,
        workers=workers,
        min_relevancy=min_relevancy,
        model=model,
        max_html_tokens=max_tokens,
    )

    console.print("[bold]Starting classification phase...[/bold]\n")
    console.print(f"Config: limit={limit}, workers={workers}, model={model}")
    if workers > 1:
        console.print("[yellow]⚠ WARNING: workers > 1 may cause Playwright errors. Use workers=1 for stability.[/yellow]")
    if retry_errors:
        console.print("[yellow]Retry mode: Will retry candidates with classify_error status[/yellow]")
    if min_relevancy > 0.0:
        console.print(f"[cyan]Filtering: only candidates with collect_relevancy ≥ {min_relevancy}[/cyan]")
    console.print()

    # Get candidates to process
    db = get_data_db()
    
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
                        f"rel={result.classify_relevancy:.2f}, "
                        f"cat={top_cat}, "
                        f"conf={result.confidence:.2f}"
                    )
                except Exception as e:
                    # Log full error details (still captured in log file)
                    logger.error(f"Failed to classify {url}: {str(e)}", exc_info=True)
                    console.print(f"[{processed}/{len(candidates)}] [red]✗[/red] {url[:60]}: {str(e)[:60]}")

        console.print()
        stats.print_summary()


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


