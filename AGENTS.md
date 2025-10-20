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

- `docs/DEVLOG.md`: Development log with problems, solutions, lessons learned, etc.; append only, keep updated after bigger steps - do not clutter with all the details. Read only when needed.
- `docs/DATA.md`: Overview of the data types stored in the databases, parquet files, etc., including explaining all the tags or enums used, collecting data sources etc. Keep it updated.
- `README.md`: An overview for the users and other (human) developers, a brief overview.

**Instructions:**
- DO NOT create other documentation files unless instructed to do so.
- When creating novel documentation create it in docs/ and suggest an update to this file to list the new files here.
- When making extensive changes, make sure that the documentation is consistent with the code.

## Code and project structure

### Technology stack

**Platform:** Linux x64, Python>=3.11, uv for package management, ruff and mypy for linting and typechecking, GitHub private repo, pre-commit

**Core libraries:** polars, numpy, scipy, litellm, jinja2, pyyaml, rich, typer, beautifulsoup4, requests, playwright, tenacity, python-dotenv, pydantic

**Observability:** Using Helicone.ai proxy

**Instructions:**
- Use these libraries and features unless there is a new functionality required. If there is, make suggestions to the user before moving ahead.
- Use context7 MCP to look up documentation when needed, if it is available.

### LLM prompts

- Stored in YAML files under `prompts/`, split into YAML files by main task.
- Each YAML file contains system and user prompts for several subtasks, each a jinja2 templete formatted as MD.
- Most prompts ask for JSON output. Each system prompt should list the requested fields with their type, detailed description (form but also purpose) and several examples to show the desired format, level of detail, etc. Each user prompt should finish with a reminder to output JSON in MD code blocks (i.e. "```json" and "```") and an abstract example output (e.g.: ```json\n{\n  "url": <the original url string>,\n  "priority": <priority as a numebr between 0.0 and 100.0>\n}\n```)

### Library and scripts

Almost all the python code is stored under `pipeline/` module. 

Notable files:
- `__init__.py` is essentially empty.
- `common.py` contains all the *shared* type definitions, constants, pydantic dataclasses, etc. that are used across the codebase. Do NOT include those local to a single module or tied to its functionality.
- `cli.py` is the module defining the typer cli.
- `llm.py` contains initialization code for litellm and basic instrumentation tools
- `utils.py` functions such as `smart\_open()` that seamlessly opens or creates plain or compressed file (.zst), logging setup (to rich, see below), rich console object, etc.
- `stats.py` contains a global prperly mutex-locked object to record stats from all the threads, and code to print them as tables or otherwise.

**Exception:** execurable `pipeline.py` in the root folder just imports and then calls cli.py.

**Exception:** Tests in the tests/ folder.

### Tests

Do not write tests unless instructed, or when hunting for a bug that might be caught efficiently this way. This is meant to be a small project; prefer some level of defensive programming, e.g. typechecks and asserts - but do not overdo it; KISS!

### Data

- Scraped files kept as `data/scraped/<hash>.html.zst`. These should be by default scraped with playwright, with realistig user agents and other settings, waiting for a full load and scrolling a bit. 
- The scraped file metadata is stored under `data/scraped/index.sqlite`
- Other data is mostly kept in SQLite databases under `data/`. See `docs/DATA.md`.
- By default, do not store failed tasks (e.g. those that raised a general exception). Never for tasks that raised RuntimeError or similar. Example exception: Scrapes returning 400 or 4xx should be cached.
- The data output might be parquet. Always write parquets with zstandard compression, level 15.

### Logs and progress, stats, multithreading

- Log and print all the output via the rich console. Use rich progress bars on the top level.
- Every script run should create a `runs/<date\_time\_PID>.log`: file (not added to git)
- Periodically update a table with stats report while running, similar to the next item.
- At the end of every run, print tables summarizing data stats: e.g. old data items, new items, cached data, errors, tokens used, token cost, ...
- Use threadpool to multi-task. Use a global stop flag defined in `common.py` to stop threads on kill or Ctrl+C caught, check occasinally (e.g. 1/loop) in all threads.

