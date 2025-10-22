"""Utility functions for file I/O, logging, and console output."""

import gzip
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import IO, Any, Iterable, Literal

import numpy as np
import zstandard as zstd
from rich.console import Console
from rich.logging import RichHandler

from .common import RUNS_PATH

# Global rich console for all output
console = Console()

# Token counting - use tiktoken for approximation
try:
    import tiktoken

    _tiktoken_available = True
except ImportError:
    _tiktoken_available = False


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

    # Create handlers with different formats
    # File handler: includes timestamp
    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    )

    # Rich console handler: RichHandler adds its own timestamp, so format excludes it
    rich_handler = RichHandler(
        console=console,
        rich_tracebacks=True,
        tracebacks_show_locals=True,
        markup=True,
    )
    rich_handler.setFormatter(logging.Formatter("%(name)s: %(message)s"))

    # Configure root logger
    logging.basicConfig(
        level=logging.INFO,
        handlers=[file_handler, rich_handler],
    )

    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized. Log file: {log_file}")


def format_error(e: Exception, levels: int = 2) -> str:
    """
    Format exception with limited traceback depth.

    Args:
        e: Exception to format
        levels: Number of traceback levels to include (default: 2)

    Returns:
        Formatted error string with traceback
    """
    import traceback

    # Get the traceback
    tb = traceback.extract_tb(e.__traceback__)

    # Take only the last N levels
    tb_limited = tb[-levels:] if len(tb) > levels else tb

    # Format the traceback
    lines = []
    for frame in tb_limited:
        lines.append(f"  File \"{frame.filename}\", line {frame.lineno}, in {frame.name}")
        if frame.line:
            lines.append(f"    {frame.line}")

    # Add the exception message
    lines.append(f"{type(e).__name__}: {str(e)}")

    return "\n".join(lines)


def count_tokens(text: str, model: str = "gpt-4") -> int:
    """
    Count approximate tokens in text for a given model.

    Uses tiktoken for accurate counting. Falls back to character-based estimate
    if tiktoken is not available.

    Args:
        text: Text to count tokens for
        model: Model name (e.g., "gpt-4", "claude-sonnet-4")

    Returns:
        Approximate token count
    """
    if not _tiktoken_available:
        # Fallback: rough estimate (1 token ≈ 4 characters for English)
        return len(text) // 4

    # Map model names to tiktoken encodings
    # Claude models use similar tokenization to GPT-4
    if "claude" in model.lower() or "sonnet" in model.lower():
        encoding_name = "cl100k_base"  # GPT-4/Claude approximation
    elif "gpt-4" in model.lower():
        encoding_name = "cl100k_base"
    elif "gpt-3.5" in model.lower():
        encoding_name = "cl100k_base"
    else:
        # Default to GPT-4 encoding
        encoding_name = "cl100k_base"

    try:
        encoding = tiktoken.get_encoding(encoding_name)
        return len(encoding.encode(text))
    except Exception:
        # Fallback on any error
        return len(text) // 4


def preprocess_html(html: str, model: str = "gpt-4") -> tuple[str, dict[str, int]]:
    """
    Preprocess HTML for LLM consumption by removing unnecessary elements.

    Removes completely:
    - <script> tags and content
    - <style> tags and content
    - <link> tags and content
    - <noscript> tags and content
    - <svg> tags and content
    - HTML comments (via BeautifulSoup)
    - Base64-encoded images (data: URIs in src/href attributes)
    
    Unwraps (removes tag but keeps content):
    - <div> tags
    - <span> tags
    
    Strips attributes:
    - Keeps only href on <a>, src/alt on <img>
    - Removes all other attributes (data-*, id, class, style, etc.)
    
    Cleans whitespace:
    - Collapses excessive newlines and spaces

    Args:
        html: Raw HTML content
        model: Model name for token counting

    Returns:
        Tuple of (cleaned_html, stats) where stats contains:
        - tokens_before: Token count before cleaning
        - tokens_after: Token count after cleaning
        - tokens_saved: Tokens saved by cleaning
        - reduction_pct: Percentage reduction
    """
    from bs4 import BeautifulSoup, Comment
    import re

    # Count tokens before
    tokens_before = count_tokens(html, model)

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    # Remove script tags
    for script in soup.find_all("script"):
        script.decompose()

    # Remove style tags
    for style in soup.find_all("style"):
        style.decompose()

    # Remove link tags (stylesheets, fonts, etc.)
    for link in soup.find_all("link"):
        link.decompose()

    # Remove noscript tags
    for noscript in soup.find_all("noscript"):
        noscript.decompose()

    # Remove svg tags
    for svg in soup.find_all("svg"):
        svg.decompose()

    # Remove HTML comments (via BeautifulSoup, not regex)
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Remove base64 images (data: URIs) and clean up attributes
    # Define which attributes to keep per tag
    attributes_to_keep = {
        "a": ["href"],
        "img": ["src", "alt"],
    }

    for tag in soup.find_all(True):  # Find all tags
        # Handle base64 in src/href first
        if tag.has_attr("src") and tag["src"].startswith("data:"):
            tag["src"] = "[base64-image-removed]"
        if tag.has_attr("href") and tag["href"].startswith("data:"):
            tag["href"] = "[base64-data-removed]"

        # Remove all attributes except those we want to keep
        tag_name = tag.name
        keep_attrs = attributes_to_keep.get(tag_name, [])
        
        # Get list of attrs to remove (can't modify dict during iteration)
        attrs_to_remove = [attr for attr in tag.attrs if attr not in keep_attrs]
        
        for attr in attrs_to_remove:
            del tag[attr]

    # Unwrap div and span tags (remove tag but keep contents)
    for div in soup.find_all("div"):
        div.unwrap()
    for span in soup.find_all("span"):
        span.unwrap()

    # Get cleaned HTML
    cleaned_html = str(soup)

    # Remove excessive whitespace
    cleaned_html = re.sub(r"\n\s*\n+", "\n\n", cleaned_html)
    cleaned_html = re.sub(r"[ \t]+", " ", cleaned_html)

    # Count tokens after
    tokens_after = count_tokens(cleaned_html, model)
    tokens_saved = tokens_before - tokens_after
    reduction_pct = (tokens_saved / tokens_before * 100) if tokens_before > 0 else 0

    stats = {
        "tokens_before": tokens_before,
        "tokens_after": tokens_after,
        "tokens_saved": tokens_saved,
        "reduction_pct": reduction_pct,
    }

    return cleaned_html, stats


def one_line_histogram(
    data: Iterable[float],
    bins: int = 10,
    field_width: int = 6,
    show_min: bool = True,
    show_max: bool = True,
    show_mean: bool = True,
    show_sd: bool = True,
    show_count: bool = True,
    show_histogram: bool = True,
    use_color: bool = True,
) -> str:
    """
    Create a one-line histogram visualization with statistics.

    Args:
        data: Iterable of numbers to visualize
        bins: Number of bins for histogram (default: 10)
        field_width: Minimum width for min/max value fields (default: 6)
        show_min: Include minimum value (default: True)
        show_max: Include maximum value (default: True)
        show_mean: Include mean value (default: True)
        show_sd: Include standard deviation (default: True)
        show_count: Include item count (default: True)
        show_histogram: Include histogram visualization (default: True)
        use_color: Use rich color markup (default: True)

    Returns:
        Formatted one-line string with histogram and statistics
        Format: "<min> <histogram> <max> | mean=<mean> sd=<sd> <n> items"
        Min is right-aligned, max is left-aligned.

    Example:
        >>> data = [1.2, 3.4, 2.1, 5.6, 4.3, 2.8, 3.9, 4.1, 2.5, 3.7]
        >>> print(one_line_histogram(data))
        1.20 ▁▃▂▅█▄▆▇▃▅ 5.60 | mean=3.36 sd=1.24 10 items
    """
    # Convert to numpy array for efficient computation
    values = np.array(list(data), dtype=float)
    
    if len(values) == 0:
        return "[empty dataset]"
    
    # Calculate statistics
    min_val = float(np.min(values))
    max_val = float(np.max(values))
    mean_val = float(np.mean(values))
    sd_val = float(np.std(values))
    count = len(values)
    
    # Build output parts
    parts = []
    
    # Min value (right-aligned)
    if show_min:
        min_str = f"{min_val:{field_width}.2f}"
        if use_color:
            min_str = f"[cyan]{min_str}[/cyan]"
        parts.append(min_str)
    
    # Histogram
    if show_histogram:
        # Create histogram bins
        hist_counts, bin_edges = np.histogram(values, bins=bins)
        
        # Handle edge case: all values are the same
        if hist_counts.max() == 0:
            hist_str = "█" * bins
        else:
            # Map counts to block characters
            block_chars = "▁▂▃▄▅▆▇█"
            hist_str = ''.join(
                block_chars[min(int(x / hist_counts.max() * 7), 7)]
                for x in hist_counts
            )
        
        if use_color:
            hist_str = f"[yellow]{hist_str}[/yellow]"
        parts.append(hist_str)
    
    # Max value (left-aligned)
    if show_max:
        max_str = f"{max_val:<{field_width}.2f}"
        if use_color:
            max_str = f"[magenta]{max_str}[/magenta]"
        parts.append(max_str)
    
    # Statistics section
    stats_parts = []
    
    if show_mean:
        mean_str = f"mean={mean_val:{field_width}.2f}"
        if use_color:
            mean_str = f"[green]{mean_str}[/green]"
        stats_parts.append(mean_str)
    
    if show_sd:
        sd_str = f"sd={sd_val:{field_width}.2f}"
        if use_color:
            sd_str = f"[blue]{sd_str}[/blue]"
        stats_parts.append(sd_str)
    
    if show_count:
        count_str = f"{count} items"
        if use_color:
            count_str = f"[dim]{count_str}[/dim]"
        stats_parts.append(count_str)
    
    # Combine parts
    result = " ".join(parts)
    
    if stats_parts:
        result += " | " + " ".join(stats_parts)
    
    return result


