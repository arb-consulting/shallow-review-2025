"""Statistics tracking and reporting for the pipeline."""

import json
import threading
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field
from rich.console import Console
from rich.table import Table

console = Console()


class CountStats(BaseModel):
    """
    Statistics for countable operations.

    Tracks unique IDs to avoid double-counting when the same item
    is processed multiple times in different contexts.
    """

    model_config = {
        "frozen": False,
        "validate_assignment": True,
        "arbitrary_types_allowed": True,
    }

    new: set[str] = Field(default_factory=set)
    cached: set[str] = Field(default_factory=set)
    errors: dict[str, str] = Field(default_factory=dict)  # id -> error message

    @property
    def total(self) -> int:
        """Total count of all items."""
        return len(self.new) + len(self.cached) + len(self.errors)

    def model_dump(self, **kwargs: Any) -> dict[str, Any]:
        """Convert to dict with serializable types."""
        return {
            "new": len(self.new),
            "cached": len(self.cached),
            "errors": len(self.errors),
            "total": self.total,
            "new_ids": sorted(list(self.new)),
            "cached_ids": sorted(list(self.cached)),
            "error_details": dict(self.errors),
        }


class TokenStats(BaseModel):
    """Token usage and cost statistics."""

    model_config = {"frozen": False, "validate_assignment": True}

    cache_read: int = 0
    cache_write: int = 0
    uncached: int = 0
    reasoning: int = 0
    output: int = 0
    cost: float = 0.0

    def update(
        self,
        cache_read: int = 0,
        cache_write: int = 0,
        uncached: int = 0,
        reasoning: int = 0,
        output: int = 0,
        cost: float = 0.0,
    ) -> None:
        """Update token stats with new values."""
        self.cache_read += cache_read
        self.cache_write += cache_write
        self.uncached += uncached
        self.reasoning += reasoning
        self.output += output
        self.cost += cost


class Stats:
    """Pipeline statistics tracker with context management."""

    def __init__(self, commandline: str = ""):
        self.lock = threading.Lock()
        self.commandline = commandline
        self.timestamp = datetime.now(timezone.utc).isoformat()

        # Scraping
        self.scraped_pages = CountStats()

        # Collection
        self.collect_sources = CountStats()
        self.collect_sources_already_exist: int = 0
        self.collect_tokens = TokenStats()
        self.collect_preprocessing: list[dict[str, float]] = []

        # Classification
        self.classify_candidates = CountStats()
        self.classify_candidates_already_exist: int = 0
        self.classify_tokens = TokenStats()
        self.classify_preprocessing: list[dict[str, float]] = []

    def to_dict(self) -> dict[str, Any]:
        """Convert stats to dictionary format."""
        return {
            "commandline": self.commandline,
            "timestamp": self.timestamp,
            "scraped_pages": self.scraped_pages.model_dump(),
            "collect_sources": self.collect_sources.model_dump(),
            "collect_sources_already_exist": self.collect_sources_already_exist,
            "collect_tokens": self.collect_tokens.model_dump(),
            "collect_preprocessing": self.collect_preprocessing,
            "classify_candidates": self.classify_candidates.model_dump(),
            "classify_candidates_already_exist": self.classify_candidates_already_exist,
            "classify_tokens": self.classify_tokens.model_dump(),
            "classify_preprocessing": self.classify_preprocessing,
        }

    def save(self, output_dir: Path) -> Path:
        """Save stats to JSON file with timestamp."""
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_path = output_dir / f"run-stats-{timestamp}.json"

        with open(output_path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

        return output_path

    def print_summary(self) -> None:
        """Print a formatted summary of statistics using rich."""
        console.print("\n[bold cyan]Pipeline Statistics Summary[/bold cyan]")
        console.print(f"Timestamp: {self.timestamp}")
        console.print(f"Command: {self.commandline}\n")

        # Scraping section
        if self.scraped_pages.total > 0:
            table = Table(title="Scraping", show_header=True)
            table.add_column("Operation")
            table.add_column("New", justify="right")
            table.add_column("Cached", justify="right")
            table.add_column("Errors", justify="right")
            table.add_column("Total", justify="right")

            table.add_row(
                "Scraped pages",
                str(len(self.scraped_pages.new)),
                str(len(self.scraped_pages.cached)),
                str(len(self.scraped_pages.errors)),
                str(self.scraped_pages.total),
            )

            console.print(table)
            console.print()

        # Collection section
        if self.collect_sources.total > 0:
            table = Table(title="Collection", show_header=True)
            table.add_column("Operation")
            table.add_column("New", justify="right")
            table.add_column("Done", justify="right")
            table.add_column("Errors", justify="right")
            table.add_column("Already Exist", justify="right")
            table.add_column("Total", justify="right")

            table.add_row(
                "Sources",
                str(len(self.collect_sources.new)),
                str(len(self.collect_sources.cached)),
                str(len(self.collect_sources.errors)),
                str(self.collect_sources_already_exist),
                str(self.collect_sources.total),
            )

            console.print(table)

            if self.collect_tokens.cost > 0:
                self._print_token_stats("Collection Tokens", self.collect_tokens)
            
            if self.collect_preprocessing:
                self._print_preprocessing_stats("Collection Preprocessing", self.collect_preprocessing)
            
            console.print()

        # Classification section
        if self.classify_candidates.total > 0:
            table = Table(title="Classification", show_header=True)
            table.add_column("Operation")
            table.add_column("New", justify="right")
            table.add_column("Done", justify="right")
            table.add_column("Errors", justify="right")
            table.add_column("Already Exist", justify="right")
            table.add_column("Total", justify="right")

            table.add_row(
                "Candidates",
                str(len(self.classify_candidates.new)),
                str(len(self.classify_candidates.cached)),
                str(len(self.classify_candidates.errors)),
                str(self.classify_candidates_already_exist),
                str(self.classify_candidates.total),
            )

            console.print(table)

            if self.classify_tokens.cost > 0:
                self._print_token_stats("Classification Tokens", self.classify_tokens)
            
            if self.classify_preprocessing:
                self._print_preprocessing_stats("Classification Preprocessing", self.classify_preprocessing)
            
            console.print()

    def _print_token_stats(self, title: str, tokens: TokenStats) -> None:
        """Print token statistics in a formatted table."""
        table = Table(title=title, show_header=True)
        table.add_column("Metric")
        table.add_column("Value", justify="right")

        if tokens.cache_write > 0:
            table.add_row("Cache writes", f"{tokens.cache_write:,}")
        table.add_row("Cache reads", f"{tokens.cache_read:,}")
        table.add_row("Uncached input", f"{tokens.uncached:,}")
        table.add_row("Output", f"{tokens.output:,}")
        if tokens.reasoning > 0:
            table.add_row("  Reasoning", f"{tokens.reasoning:,}")
        table.add_row("Total cost", f"${tokens.cost:.4f}")

        console.print(table)

    def _print_preprocessing_stats(self, title: str, stats_list: list[dict[str, float]]) -> None:
        """Print HTML preprocessing statistics."""
        if not stats_list:
            return

        import statistics

        # Calculate aggregate stats
        tokens_before_all = [s["tokens_before"] for s in stats_list]
        tokens_after_all = [s["tokens_after"] for s in stats_list]
        reduction_pct_all = [s["reduction_pct"] for s in stats_list]

        table = Table(title=title, show_header=True)
        table.add_column("Metric")
        table.add_column("Mean", justify="right")
        table.add_column("Min", justify="right")
        table.add_column("Max", justify="right")
        table.add_column("Std Dev", justify="right")

        table.add_row(
            "Tokens before",
            f"{statistics.mean(tokens_before_all):,.0f}",
            f"{min(tokens_before_all):,.0f}",
            f"{max(tokens_before_all):,.0f}",
            f"{statistics.stdev(tokens_before_all) if len(tokens_before_all) > 1 else 0:,.0f}",
        )

        table.add_row(
            "Tokens after",
            f"{statistics.mean(tokens_after_all):,.0f}",
            f"{min(tokens_after_all):,.0f}",
            f"{max(tokens_after_all):,.0f}",
            f"{statistics.stdev(tokens_after_all) if len(tokens_after_all) > 1 else 0:,.0f}",
        )

        table.add_row(
            "Reduction %",
            f"{statistics.mean(reduction_pct_all):.1f}%",
            f"{min(reduction_pct_all):.1f}%",
            f"{max(reduction_pct_all):.1f}%",
            f"{statistics.stdev(reduction_pct_all) if len(reduction_pct_all) > 1 else 0:.1f}%",
        )

        console.print(table)


# Global stats instance for context management
_current_stats: Stats | None = None
_stats_lock = threading.Lock()


@contextmanager
def stats_context(commandline: str = ""):
    """Context manager for pipeline statistics."""
    global _current_stats

    with _stats_lock:
        if _current_stats is not None:
            raise RuntimeError("Stats context already active")
        _current_stats = Stats(commandline=commandline)

    try:
        yield _current_stats
    finally:
        with _stats_lock:
            _current_stats = None


def get_stats() -> Stats:
    """Get the current stats instance."""
    with _stats_lock:
        if _current_stats is None:
            raise RuntimeError("No active stats context")
        return _current_stats


