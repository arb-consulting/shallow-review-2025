# Code Conventions

**Ground truth for coding patterns, libraries, and conventions.**

## Technology Stack

**Platform:** Linux x64, Python ≥3.11

**Package Management:** uv (not pip)

**Linting/Typing:** ruff, mypy, pre-commit

**Core Libraries:**
- **Data**: polars, numpy, scipy
- **LLM**: litellm, jinja2, pyyaml, pydantic, tenacity
- **Web**: beautifulsoup4, requests, playwright
- **UI**: rich, typer
- **Utils**: python-dotenv, zstandard

**Observability:** Helicone.ai proxy for LLM calls

**⚠️ Do not add new libraries without explicit approval.**

## Module Structure

All code in `shallow_review/` module. Executable `pipeline.py` at root imports and calls `cli.py`.

### Notable Files

- **`common.py`**: Shared types, constants, enums, pydantic models, global state (e.g. shutdown flag). Only includes items used across multiple modules.
- **`cli.py`**: Typer CLI definition
- **`data_db.py`**: Unified database access (lazy singleton pattern)
- **`llm.py`**: Litellm initialization, retry logic, JSON extraction, token tracking
- **`utils.py`**: File I/O (`smart_open`), logging setup, console object, token counting
- **`stats.py`**: Global thread-safe stats tracking
- **`taxonomy.py`**: Classification taxonomy loader and utilities (loads `data/taxonomy.yaml`)
- **`scrape.py`**: Web scraping with playwright
- **`collect.py`**: Collection phase logic
- **`classify.py`**: Classification phase logic

## Database Access

**Single database file:** `data/data.db` (contains `scrape`, `collect`, `classify` tables)

**Pattern:** Lazy singleton with thread-safe initialization

```python
from .data_db import get_data_db

# Get connection (creates DB/tables if needed)
db = get_data_db()

# Use connection (check_same_thread=False is set)
cursor = db.execute("SELECT * FROM collect WHERE status = ?", ("new",))
db.commit()  # Explicit commits required
```

**⚠️ Important:**
- Connection is shared across threads (check_same_thread=False)
- Always call `db.commit()` explicitly after writes
- No foreign key constraints between tables
- See `docs/DATA.md` for schemas

## LLM Integration

**Setup:** Call `setup_litellm()` once at startup (lazy singleton, thread-safe)

**Disk caching:** Automatic via litellm (stored in `data/.llm_cache/`)

**Helicone observability:** Configured automatically if `HELICONE_API_KEY` env var is set
- Uses Helicone callback (`litellm.success_callback = ["helicone"]`)
- Logs all LLM requests/responses to Helicone for monitoring and analytics
- Set `HELICONE_API_KEY` in environment or `.env` file

**Usage pattern:**

```python
from .llm import get_completion, setup_litellm

# At startup
setup_litellm()

# Make LLM call with automatic retries, JSON extraction, stats tracking
result = get_completion(
    template_vars={"url": url, "html": html},
    model="claude-3-5-sonnet-20241022",
    stats_subtree="collect_tokens",  # Stats key for tracking
    response_type=MyPydanticModel,  # Validates JSON response
    system_prompt_template=prompts["task"]["system"],
    user_prompt_template=prompts["task"]["user"],
)
```

**Features:**
- Automatic retry with exponential backoff (rate limits, API errors)
- JSON extraction from markdown code blocks
- Pydantic validation of responses
- Token tracking (cache hits/misses, costs)
- Stats integration via `stats_subtree` parameter
- Graceful shutdown on budget exceeded or repeated failures

## Prompts

**Location:** `prompts/*.yaml` (one file per main task)

**Structure:**
```yaml
task_name:
  system: |
    # System prompt as jinja2 template (markdown formatted)
    ...
  user: |
    # User prompt as jinja2 template (markdown formatted)
    ...
```

**JSON output convention:**
- System prompt lists all expected JSON fields with types, descriptions, examples
- User prompt ends with: "Output JSON in markdown code block: \`\`\`json ... \`\`\`"
- Include abstract example showing expected structure

## Logging and Console

**Logging setup:**

```python
from .utils import setup_logging, console

# At startup - creates timestamped log in runs/
setup_logging()  # or setup_logging(custom_path)

# Use standard logging
import logging
logger = logging.getLogger(__name__)
logger.info("Message")
```

**Features:**
- Writes to both file (`runs/<timestamp>_<pid>.log`) and console
- File logs include timestamps, logger names, levels
- Console uses RichHandler with built-in timestamps (no redundancy)
- Rich console with colored output and tracebacks
- Tracebacks show locals (configured in RichHandler)

**Console output:**

```python
from .utils import console

# Use rich console for all output
console.print("[bold]Header[/bold]")
console.print("Normal text")

# Progress bars for long operations
from rich.progress import Progress
import logging

# Suppress INFO logging during progress to avoid clashing
root_logger = logging.getLogger()
old_level = root_logger.level
root_logger.setLevel(logging.WARNING)

try:
    with Progress() as progress:
        task = progress.add_task("Processing...", total=len(items))
        for item in items:
            # Use progress.console instead of global console
            progress.console.print("[green]✓[/green] Item processed")
            progress.update(task, advance=1)
finally:
    root_logger.setLevel(old_level)
```

**⚠️ Important:**
- Never use `print()` - always use `console.print()` or logging
- Inside progress bar context, use `progress.console.print()` to avoid display conflicts
- Temporarily suppress INFO logging during progress bars (set to WARNING or ERROR)

## Threading and Graceful Shutdown

**Pattern:** ThreadPoolExecutor with global shutdown flag

**Global shutdown flag:**

```python
from .common import is_shutdown_requested, request_shutdown

# Check periodically in long-running loops
for item in items:
    if is_shutdown_requested():
        logger.info("Shutdown requested, exiting")
        break
    # ... process item ...
```

**Signal handling:**

```python
import signal
from .common import request_shutdown

def signal_handler(sig, frame):
    console.print("\n[yellow]Shutdown requested (Ctrl+C)[/yellow]")
    request_shutdown()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
```

**Thread pool usage:**

```python
from concurrent.futures import ThreadPoolExecutor
from .common import is_shutdown_requested

with ThreadPoolExecutor(max_workers=workers) as executor:
    futures = []
    for item in items:
        if is_shutdown_requested():
            break
        future = executor.submit(process_func, item)
        futures.append(future)
    
    # Wait for completion
    for future in futures:
        if is_shutdown_requested():
            break
        future.result()  # or use as_completed()
```

## Statistics Tracking

**Pattern:** Global thread-safe singleton

```python
from .stats import get_stats

# Get global stats object
stats = get_stats()

# Update stats (always use lock)
with stats.lock:
    stats.collect_sources.new.add(url)
    stats.collect_tokens.update(
        cache_read=100,
        uncached=500,
        cost=0.002
    )

# Print summary at end
stats.print_summary()

# Save to JSON
stats.save_to_file(output_path)
```

**CountStats pattern:**
- Uses sets of IDs to avoid double-counting
- Tracks: `new`, `cached`, `errors` (dict with error messages)
- Access via: `stats.collect_sources.new.add(url)`

**TokenStats pattern:**
- Tracks: `cache_read`, `cache_write`, `uncached`, `reasoning`, `output`, `cost`
- Update via: `stats.collect_tokens.update(cache_read=100, cost=0.002)`

## File Handling

**Compressed files:** Use `smart_open()` for automatic compression handling

```python
from .utils import smart_open
from pathlib import Path

# Reads/writes .zst, .gz automatically, plain files otherwise
with smart_open(path, "rt") as f:
    content = f.read()

with smart_open(path, "wt") as f:
    f.write(content)
```

**Scraped HTML storage:**
- Location: `data/scraped/<url_hash>.html.zst`
- Compression: Zstandard level 15 (default in scrape.py)
- Access via: `get_scrape_path(url)` or `open_scraped(url, mode)`

**Parquet files:**
- Always use zstandard compression level 15:
  ```python
  df.write_parquet(path, compression="zstd", compression_level=15)
  ```

## Error Handling

**Philosophy:** Fail visibly rather than masking errors

**Formatting:** Use `format_error()` from utils for consistent error messages

```python
from .utils import format_error

try:
    # ... operation ...
except Exception as e:
    error_msg = format_error(e, levels=2)  # 2 levels of traceback
    logger.error(f"Failed: {error_msg}")
    # Store in DB, stats, etc.
```

**Caching failed operations:**
- **Do cache:** HTTP 4xx errors (except transient ones)
- **Don't cache:** General exceptions, RuntimeError, API errors

**Retries:** 
- Configured in `llm.py` via tenacity
- Retries: rate limits, API errors, validation errors (with cache bypass)
- No retry: budget exceeded, shutdown requested

**Timeouts:**
- Scraping: 60 seconds (playwright `timeout=60000`)
- LLM calls: 120 seconds (litellm `timeout=120.0`)
- Prevents indefinite hangs

**Stats update failures:**
- Stats updates wrapped in try/except to not fail main operations
- Failures logged as warnings rather than silently swallowed
- Pattern: `except RuntimeError as stat_err: logger.warning(f"Failed to update stats: {stat_err}")`

## Coding Principles

1. **KISS** - Simple, readable code. This is a small research project.
2. **No premature optimization** - Use indexes, but don't over-engineer.
3. **Defensive programming** - Type hints, asserts where useful, but don't overdo it.
4. **No tests by default** - Only write tests when explicitly instructed or debugging.
5. **Fail visibly** - Don't mask errors; let them propagate with good error messages.
6. **Shared state in common.py** - Don't duplicate constants/types across modules.
7. **Thread-safe singletons** - Use lock + lazy init pattern (see `data_db.py`, `llm.py`).
8. **Explicit is better** - No magic; be clear about side effects.

## Token Counting

**Approximation via tiktoken:**

```python
from .utils import estimate_tokens

# Approximate token count for LLM context
token_count = estimate_tokens(text, model="gpt-4")
```

**Actual tracking:** Done automatically by `get_completion()` and stored in stats.

## Data Integrity

**Database writes:**
- Update status column atomically with data
- Use ISO 8601 timestamps with timezone (UTC)
- Store complex data in JSON columns
- Always commit explicitly

**Scrape caching:**
- Write HTML atomically (temp file + rename)
- Update DB metadata in same transaction
- Hash is computed from URL only

**Transactions:**
- Used for atomic scrape operations (file + DB)
- Not used for LLM operations (idempotent via caching)

## Common Patterns

**Processing pipeline:**
1. Get items with status='new' from DB
2. Check shutdown flag in loop
3. For each item:
   - Call processing function (scrape, compute_collect, compute_classify)
   - Update stats with lock
   - Update DB status and commit
   - Log progress
4. Print summary at end

**Configuration objects:**
- Defined in `common.py` as Pydantic models
- Examples: `RunCollectConfig`, `RunClassifyConfig`
- Passed from CLI to processing functions
- Immutable during run

**Path handling:**
- All paths derived from `ROOT_PATH` in `common.py`
- Paths are absolute, independent of current working directory
- Use `Path` objects, not strings

