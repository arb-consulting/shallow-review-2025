"""Typer CLI interface for shallow-review pipeline."""

import logging
import signal
import sys
from typing import Optional

import typer

from . import __version__
from .common import RUNS_PATH, request_shutdown
from .stats import stats_context
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
def version() -> None:
    """Show version information."""
    console.print(f"shallow-review version {__version__}")


@app.command()
def info() -> None:
    """Show configuration and paths."""
    from .common import DATA_PATH, PROMPTS_PATH, ROOT_PATH

    console.print("[bold]Shallow Review Configuration[/bold]\n")
    console.print(f"Version: {__version__}")
    console.print(f"Root path: {ROOT_PATH}")
    console.print(f"Data path: {DATA_PATH}")
    console.print(f"Prompts path: {PROMPTS_PATH}")
    console.print(f"Runs path: {RUNS_PATH}")


@app.command()
def add(
    file: str = typer.Argument(..., help="File with URLs (one per line, or CSV)"),
    phase: str = typer.Option("classify", help="Phase to add URLs to: collect|classify"),
    source: Optional[str] = typer.Option(None, help="Source label for tracking"),
) -> None:
    """Add URLs to collect or classify phases."""
    from pathlib import Path

    from .classify import add_classify_candidate
    from .collect import add_collect_source
    from .stats import stats_context

    # Validate phase
    if phase not in ["collect", "classify"]:
        console.print(f"[red]Error: Invalid phase '{phase}'. Must be 'collect' or 'classify'[/red]")
        sys.exit(1)

    # Read URLs from file
    file_path = Path(file)
    if not file_path.exists():
        console.print(f"[red]Error: File not found: {file}[/red]")
        sys.exit(1)

    urls = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                # Simple handling: assume one URL per line
                # TODO: Add CSV parsing if needed
                urls.append(line)

    if not urls:
        console.print("[yellow]No URLs found in file[/yellow]")
        return

    console.print(f"Adding {len(urls)} URLs to [bold]{phase}[/bold] phase...")

    # Add URLs with stats tracking
    with stats_context(commandline=f"add {file} --phase {phase}") as stats:
        added = 0
        exists = 0

        for url in urls:
            if phase == "collect":
                if add_collect_source(url, source):
                    added += 1
                else:
                    exists += 1
            else:  # classify
                if add_classify_candidate(url, source or "manual", None, None):
                    added += 1
                else:
                    exists += 1

        console.print(f"\n[green]✓ Added {added} new URLs[/green]")
        if exists > 0:
            console.print(f"[yellow]! {exists} URLs already existed[/yellow]")

        stats.print_summary()


@app.command()
def collect(
    limit: int = typer.Option(100, help="Maximum sources to process"),
    workers: int = typer.Option(4, help="Number of worker threads"),
    relevancy: float = typer.Option(0.3, help="Minimum relevancy threshold for links"),
    model: str = typer.Option("claude-sonnet-4", help="LLM model to use"),
    max_tokens: int = typer.Option(100000, help="Max HTML tokens before error"),
    retry_errors: bool = typer.Option(False, "--retry-errors", help="Retry sources with extract_error status"),
) -> None:
    """Collect links from source pages."""
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

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

    # Process sources with stats tracking and progress bar
    with stats_context(commandline=f"collect --limit {limit}") as stats:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Collecting sources...", total=len(sources))

            for url in sources:
                if is_shutdown_requested():
                    console.print("\n[yellow]Shutdown requested, stopping...[/yellow]")
                    break

                progress.update(task, description=f"[cyan]Processing: {url[:60]}...")

                try:
                    result = compute_collect(url, config, force_recompute=retry_errors)
                    console.print(
                        f"[green]✓[/green] {url[:70]}: "
                        f"{len(result.links)} links (quality: {result.collection_quality_score:.2f})"
                    )
                except Exception as e:
                    console.print(f"[red]✗[/red] {url[:70]}: {str(e)[:80]}")

                progress.advance(task)

        console.print()
        stats.print_summary()


# TODO: Implement classify command when classify.py is complete


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


