"""Typer CLI interface for shallow-review pipeline."""

import logging
import sys
from typing import Optional

import typer

from . import __version__
from .common import RUNS_PATH
from .stats import stats_context
from .utils import console, setup_logging

logger = logging.getLogger(__name__)

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


# TODO: Add phase-specific commands as they're implemented:
#
# @app.command()
# def collect(...) -> None:
#     """Collect items from sources."""
#     ...
#
# @app.command()
# def classify(...) -> None:
#     """Classify collected items."""
#     ...


def main() -> None:
    """Entry point for CLI."""
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


