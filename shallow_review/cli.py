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
    
    # Collect distributions
    with data_db_locked() as db:
        collect_data = db.execute("SELECT data FROM collect WHERE status = 'done' AND data IS NOT NULL").fetchall()
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
    
    # Classify distributions
    with data_db_locked() as db:
        # Relevance scores from columns
        ai_safety_relevance = [row["ai_safety_relevance"] for row in db.execute("SELECT ai_safety_relevance FROM classify WHERE ai_safety_relevance IS NOT NULL").fetchall()]
        if ai_safety_relevance:
            console.print(f"  [dim]{'ai_safety_relevance':<25}[/dim] {one_line_histogram(ai_safety_relevance, bins=20, field_width=12)}")
        
        shallow_review_inclusion = [row["shallow_review_inclusion"] for row in db.execute("SELECT shallow_review_inclusion FROM classify WHERE shallow_review_inclusion IS NOT NULL").fetchall()]
        if shallow_review_inclusion:
            console.print(f"  [dim]{'shallow_review_inclusion':<25}[/dim] {one_line_histogram(shallow_review_inclusion, bins=20, field_width=12)}")
        
        collect_relevancy = [row["collect_relevancy"] for row in db.execute("SELECT collect_relevancy FROM classify WHERE collect_relevancy IS NOT NULL").fetchall()]
        if collect_relevancy:
            console.print(f"  [dim]{'collect_relevancy':<25}[/dim] {one_line_histogram(collect_relevancy, bins=20, field_width=12)}")
        
        # Extract JSON metrics
        classify_data = db.execute("SELECT data FROM classify WHERE status = 'done' AND data IS NOT NULL").fetchall()
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
def export_taxonomy(
    min_shallow_review: float = typer.Option(0.1, help="Minimum shallow_review_inclusion score"),
    min_ai_safety: float = typer.Option(0.1, help="Minimum ai_safety_relevance score"),
    min_collect: float = typer.Option(0.1, help="Minimum collect_relevancy score"),
    kinds: str = typer.Option("", help="Comma-separated list of accepted kinds (empty = all)"),
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

    # Query classified items
    with data_db_locked() as db:
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
        
        cursor = db.execute(query, params)
        rows = cursor.fetchall()

    if not rows:
        console.print("[yellow]No items found matching filters[/yellow]", file=sys.stderr)
        return

    # Parse data JSON and group by top category
    from datetime import date as date_type
    
    items_by_category = defaultdict(list)
    
    for row in rows:
        try:
            data = json.loads(row["data"])
            
            # Get top category ID
            categories = data.get("categories", [])
            if not categories:
                console.print(f"[yellow]Warning: Item {row['url']} has no categories, skipping[/yellow]", file=sys.stderr)
                continue
            
            top_category_id = categories[0]["id"]
            
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
                "summary": data.get("summary", ""),
                "key_points": data.get("key_points", []),
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
            
            if include_item:
                items_by_category[top_category_id].append(item)
            
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
    output_lines.append("")
    output_lines.append(f"**Total items:** {sum(len(items) for items in items_by_category.values())}")
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
        output_lines.append(f"{header_prefix} {cat.name} [cat:{cat.id}]")
        output_lines.append("")
        
        # Output description
        output_lines.append(cat.description.strip())
        output_lines.append("")
        
        # If leaf category, output items
        if cat.is_leaf and items_in_this_cat:
            for item in items_in_this_cat:
                # Format: - **Title**, *Authors*, Date, Venue [stats] Summary • Key points
                
                # Use url_hash_short from database
                url_hash_short = item["url_hash_short"] or "unknown"
                
                # Title (linked)
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
                
                # Stats in brackets
                stats_part = f"[{item['kind']}, ais={item['ai_safety_relevance']:.2f}, **sr={item['shallow_review_inclusion']:.2f}**, item:{url_hash_short}]"
                
                # Summary
                summary = item["summary"].replace("\n", " ").strip()
                
                # Key points
                key_points_str = ""
                if item["key_points"]:
                    # Join first 3 key points
                    kp_list = item["key_points"][:3]
                    key_points_str = " • ".join(kp.replace("\n", " ").strip() for kp in kp_list)
                
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


