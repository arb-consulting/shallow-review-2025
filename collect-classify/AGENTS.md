# Data pipeline and research project

These are the instructions for AI coding and research assistants.

**General instructions:**
- You may use shell commands such as ls, pwd, mv, cp, head, etc. Never remove files you have not created.
- Never run other commands yourself. In particular: no running scripts, tests, package managemet, git commands, external tools. Suggest the commands to the developer (me).
- Be very succinct in explaining what you did after making changes - write a emphasized short summary, and then list anything that I might find non-obvious or surprising: problems, caveats, creative solutions, possible issues, etc.; still keep to the major ones.
- Assume I am an experienced senior developer and a mathematician and treat me as such. Tell me when you think something is a mistake. Do NOT praise my solutions and rahter offer impassive and objective view. Assume I am not a native speaker and offer better formulations or grammar corrections, but do so sparingly.
- In many cases, it will be beneficial to discuss the high-level plan and ask questions to clarify the context before plunging into editing files and taking actions, espacially beginning a new conversation or task; ask at your liberty when you need information (but not for asking itself).
- Do not try to handle every error. The tasks should rather fail visibly than mask an error. 
- Write simple and readable code, this is a small, agile research project.
- Performance is not an issue for now: Do use database indexes etc. and principled solutions, but do not reach for more complex solutions or code in the name of performance (nor for abstract generality).
- Above all: KISS 

## Documentation

**Ground truth documents** (keep updated when making changes):

- `docs/DATA.md`: **Ground truth** for all database schemas, data structures, file formats, enums, and constants. Keep fully synchronized with code.
- `docs/CODE.md`: **Ground truth** for coding conventions, libraries, patterns, and implementation details. Reference this to avoid duplicating functionality.
- `docs/COLLECT.md`: Collection phase process, logic, requirements, observations, and design decisions. Do NOT repeat DB schemas (reference DATA.md) or coding patterns (reference CODE.md).
- `docs/CLASSIFY.md`: Classification phase process, logic, requirements, observations, and design decisions. Do NOT repeat DB schemas (reference DATA.md) or coding patterns (reference CODE.md).
- `docs/SCRAPE.md`: Minimal scraping infrastructure documentation. Do NOT repeat DB schemas (reference DATA.md).
- `docs/DEVLOG.md`: Development log with major problems, solutions, lessons learned, and design decisions. Append-only, updated after significant changes. Do not clutter with minor details.
- `README.md`: Brief overview for users and developers, cli usage, etc.

**Instructions:**
- **DO NOT create other documentation files** unless explicitly instructed to do so.
- When making database or data structure changes, update `docs/DATA.md` first.
- When adding/changing coding patterns or libraries, update `docs/CODE.md`.
- When making process changes, update the relevant process doc (COLLECT.md, CLASSIFY.md, or SCRAPE.md).
- After significant milestones, append to `docs/DEVLOG.md`.
- Never duplicate: schemas live in DATA.md only, coding patterns in CODE.md only.

## Quick Reference

For detailed coding conventions, see `docs/CODE.md`. Key points:

**Platform:** Linux x64, Python>=3.11, uv for package management, ruff and mypy for linting and typechecking, GitHub private repo, pre-commit

**Core libraries:** polars, numpy, scipy, litellm, jinja2, pyyaml, rich, typer, beautifulsoup4, requests, playwright, tenacity, python-dotenv, pydantic

**Module structure:** Code in `shallow_review/`, executable `pipeline.py` at root. See CODE.md for notable files.

**Database:** Single `data/data.db` with lazy singleton access via `get_data_db()`. See DATA.md for schemas.

**Logging:** Via rich console and timestamped files in `runs/`. Never use `print()`.

**Threading:** ThreadPoolExecutor with global shutdown flag (`is_shutdown_requested()`). Check flag periodically in loops.

**Stats:** Global thread-safe singleton via `get_stats()`. Always use lock when updating.

**LLM calls:** Via `get_completion()` with automatic retries, caching, JSON extraction, stats tracking.

**Prompts:** YAML files in `prompts/`, jinja2 templates, request JSON output in markdown code blocks.

**Tests:** Don't write unless explicitly instructed. Prefer defensive programming (asserts, type hints).

**Data caching:** Scrapes in `data/scraped/<hash>.html.zst` (zstd level 15). Parquet with zstd level 15.

## Code and project structure

### Technology stack

**Observability:** Using Helicone.ai callback for LLM monitoring - automatically configured if `HELICONE_API_KEY` env var is set

**Instructions:**
- Use these libraries and features unless there is a new functionality required. If there is, make suggestions to the user before moving ahead.
- Use context7 MCP to look up documentation when needed, if it is available.

### LLM prompts

- Stored in YAML files under `prompts/`, split into YAML files by main task.
- Each YAML file contains system and user prompts for several subtasks, each a jinja2 template formatted as MD.
- Most prompts ask for JSON output. Each system prompt should list the requested fields with their type, detailed description (form but also purpose) and several examples to show the desired format, level of detail, etc. Each user prompt should finish with a reminder to output JSON in MD code blocks (i.e. "```json" and "```") and an abstract example output (e.g.: ```json\n{\n  "url": <the original url string>,\n  "priority": <priority as a number between 0.0 and 100.0>\n}\n```)

### Library and scripts

Almost all the python code is stored under `shallow_review/` module. 

Notable files:
- `common.py` contains all the *shared* type definitions, constants, pydantic dataclasses, etc. that are used across the codebase. Do NOT include those local to a single module or tied to its functionality.
- `cli.py` is the module defining the typer cli.
- `data_db.py` contains the unified database access (lazy singleton pattern).
- `llm.py` contains initialization code for litellm and basic instrumentation tools
- `utils.py` functions such as `smart_open()` that seamlessly opens or creates plain or compressed file (.zst), logging setup (to rich, see below), rich console object, etc.
- `stats.py` contains a global properly mutex-locked object to record stats from all the threads, and code to print them as tables or otherwise.

**Exception:** executable `pipeline.py` in the root folder just imports and then calls cli.py.

**Exception:** Tests in the tests/ folder.

**Details:** See `docs/CODE.md` for detailed patterns and conventions.

### Tests

Do not write tests unless instructed, or when hunting for a bug that might be caught efficiently this way. This is meant to be a small project; prefer some level of defensive programming, e.g. typechecks and asserts - but do not overdo it; KISS!

### Data

- Scraped files kept as `data/scraped/<hash>.html.zst`. These should be by default scraped with playwright, with realistic user agents and other settings, waiting for a full load and scrolling a bit. 
- The scraped file metadata and all intermediate and final result recors are stored in `data/data.db`. See `docs/DATA.md`.
- By default, do not store failed tasks (e.g. those that raised a general exception). Never for tasks that raised RuntimeError or similar. Example exception: Scrapes returning 400 or 4xx should be cached.
- The data output might be parquet. Always write parquets with zstandard compression, level 15.

### Logs and progress, stats, multithreading

- Log and print all the output via the rich console. Use rich progress bars on the top level.
- Every script run should create a `runs/<date_time_PID>.log` file (not added to git)
- Periodically update a table with stats report while running, similar to the next item.
- At the end of every run, print tables summarizing data stats: e.g. old data items, new items, cached data, errors, tokens used, token cost, ...
- Use threadpool to multi-task. Use a global stop flag defined in `common.py` to stop threads on kill or Ctrl+C caught, check occasionally (e.g. 1/loop) in all threads.

