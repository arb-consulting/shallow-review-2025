"""Utility functions for file I/O, logging, and console output."""

import gzip
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import IO, Any, Literal

import zstandard as zstd
from rich.console import Console
from rich.logging import RichHandler

from .common import RUNS_PATH

# Global rich console for all output
console = Console()


def smart_open(
    path: Path | str,
    mode: Literal["rt", "wt", "rb", "wb"],
    encoding: str | None = None,
    **kwargs: Any,
) -> IO:
    """
    Open file with automatic compression detection based on extension.

    Supports:
    - .zst: Zstandard compression
    - .gz: Gzip compression
    - Others: Plain files

    Args:
        path: File path
        mode: Open mode (rt/wt for text, rb/wb for binary)
        encoding: Text encoding (for text modes)
        **kwargs: Additional args passed to open()

    Returns:
        File-like object
    """
    path = Path(path)
    is_text = "t" in mode
    is_write = "w" in mode

    if path.suffix == ".zst":
        # Zstandard compression
        base_mode = "wb" if is_write else "rb"
        fh = open(path, base_mode)

        if is_write:
            # Compression level 15 as per AGENTS.md for parquet
            cctx = zstd.ZstdCompressor(level=15)
            compressed_fh = cctx.stream_writer(fh)
        else:
            dctx = zstd.ZstdDecompressor()
            compressed_fh = dctx.stream_reader(fh)

        if is_text:
            import io

            return io.TextIOWrapper(compressed_fh, encoding=encoding or "utf-8")
        return compressed_fh

    elif path.suffix == ".gz":
        # Gzip compression
        base_mode = mode.replace("t", "")  # Remove text flag
        return gzip.open(path, base_mode, encoding=encoding if is_text else None, **kwargs)

    else:
        # Plain file
        return open(path, mode, encoding=encoding if is_text else None, **kwargs)


def setup_logging(log_file: Path | None = None) -> None:
    """
    Set up logging to file and rich console.

    Args:
        log_file: Path to log file. If None, creates timestamped file in runs/
    """
    if log_file is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        pid = os.getpid()
        log_file = RUNS_PATH / f"{timestamp}_{pid}.log"

    # Ensure parent directory exists
    log_file.parent.mkdir(exist_ok=True, parents=True)

    # Configure root logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            # File handler (plain text)
            logging.FileHandler(log_file, mode="w", encoding="utf-8"),
            # Rich console handler
            RichHandler(
                console=console,
                rich_tracebacks=True,
                tracebacks_show_locals=True,
                markup=True,
            ),
        ],
    )

    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized. Log file: {log_file}")


