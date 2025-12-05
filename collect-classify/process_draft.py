#!/usr/bin/env -S uv run python
"""Process draft shallow review documents.

Provides tools to extract links and parse structured content from draft markdown documents.
"""

import json
import logging
import re
import sys
from pathlib import Path
import litellm
import typer
from jinja2 import Template
from litellm.caching.caching import Cache
from pydantic import ValidationError
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from draft_parser import (
    BROAD_APPROACHES,
    ORTHODOX_PROBLEMS,
    TARGET_CASES,
    AgendaAttributes,
    DocumentItem,
    ItemType,
    ProcessedDocument,
    extract_all_links_from_file,
    parse_document,
)

# Setup
console = Console()
logger = logging.getLogger(__name__)

# Import shallow_review modules for database access
try:
    from shallow_review.data_db import data_db_locked
    from shallow_review.utils import normalize_url
    _SHALLOW_REVIEW_AVAILABLE = True
except ImportError:
    _SHALLOW_REVIEW_AVAILABLE = False
    logger.warning("shallow_review modules not available - URL enrichment will be disabled")

# CLI app
app = typer.Typer(
    name="process-draft",
    help="Process draft shallow review documents",
    add_completion=False,
)

# LLM setup flag
_llm_setup_done = False


def setup_litellm(cache_dir: Path | None = None) -> None:
    """Set up litellm with disk-based caching.

    Args:
        cache_dir: Directory for LLM response caching
    """
    global _llm_setup_done

    if _llm_setup_done:
        return

    if cache_dir is None:
        cache_dir = Path.cwd() / ".llm_cache"

    cache_dir.mkdir(exist_ok=True, parents=True)
    litellm.cache = Cache(type="disk", disk_cache_dir=str(cache_dir))  # type: ignore[arg-type]

    _llm_setup_done = True
    logger.info(f"Litellm initialized with cache at {cache_dir}")


def setup_logging(verbose: bool = False) -> None:
    """Configure logging."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


# ============================================================================
# collect_links subcommand
# ============================================================================


@app.command()
def collect_links(
    input_file: str = typer.Argument(..., help="Path to draft markdown file"),
    output_file: str | None = typer.Option(
        None, "--output", "-o", help="Output file path (default: <input>-links.txt)"
    ),
    format: str = typer.Option(
        "txt", "--format", "-f", help="Output format: json or txt"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging"),
) -> None:
    """Extract all HTTP(S) links from a draft markdown document.

    Extracts both markdown-formatted links [text](url) and plain-text URLs.
    Uses smart boundary detection to avoid capturing trailing punctuation.
    """
    setup_logging(verbose)

    input_path = Path(input_file)
    if not input_path.exists():
        console.print(f"[red]Error: File not found: {input_file}[/red]")
        raise typer.Exit(1)

    # Determine output path
    if output_file is None:
        output_path = input_path.parent / f"{input_path.stem}-links.{format}"
    else:
        output_path = Path(output_file)

    # Extract links
    console.print(f"[cyan]Extracting links from {input_file}...[/cyan]")
    links = extract_all_links_from_file(input_path)

    console.print(f"[green]Found {len(links)} unique links[/green]")

    # Write output
    if format == "json":
        output_data = {
            "source_file": str(input_path),
            "total_links": len(links),
            "links": [link.model_dump() for link in links],
        }
        output_path.write_text(json.dumps(output_data, indent=2))
    elif format == "txt":
        # One URL per line
        lines = [link.url for link in links]
        output_path.write_text("\n".join(lines) + "\n")
    else:
        console.print(f"[red]Error: Unknown format '{format}'[/red]")
        raise typer.Exit(1)

    console.print(f"[green]Links written to {output_path}[/green]")


# ============================================================================
# parse subcommand
# ============================================================================


# LLM extraction prompt template - takes DocumentItem and returns it filled
EXTRACTION_PROMPT = Template(
    """You are extracting structured metadata from a research agenda in a shallow review document.

You will receive:
1. A DocumentItem structure (JSON) with id, name, header_level, parent_id, item_type already filled
2. The markdown content for this item in <content></content> XML tags

Your task: Return the SAME DocumentItem structure with agenda_attributes populated and parsing_issues added. Preserve id, name, header_level, parent_id, and item_type fields exactly.

**Input DocumentItem:**
```json
{{ item_json }}
```

**Markdown content to extract from:**
<content>
{{ content }}
</content>

Extract the following information from the content:

**Standard Attributes** (extract if present, look for these bold headers):
- who_edits: From "**Who edits (internal):**" - Editor name, possibly with status emoji
- one_sentence_summary: From "**One-sentence summary:**" - Brief description
- theory_of_change: From "**Theory of change:**" - How this work contributes to safety
- see_also: From "**See also:**" - Related agenda IDs (list of strings like "a:id1", "a:id2", "sec:id1"). Use the agenda list below to resolve plain text references to IDs.
- orthodox_problems: From "**Orthodox problems:**" - List of orthodox problem IDs (see table below)
- target_case: From "**Target case:**" - Target case ID (see table below)
- broad_approach: From "**Broad approach:**" - Broad approach ID (see table below)
- some_names: From "**Some names:**" - Key researchers (list)
- estimated_ftes: From "**Estimated FTEs:**" - Workforce estimate
- critiques: From "**Critiques:**" - Critiques as markdown text (links, descriptions, etc.)
- funded_by: From "**Funded by:**" - Funders (optional)
- funding_in_2025: From "**Funding in 2025:**" - Dollar amounts (optional)
- organization_structure: From "**Host org structure:**" or "**Structure:**" - Organization type (e.g., "public benefit corp", "for-profit", "research laboratory subsidiary of a for-profit")
- teams: From "**Teams:**" - Teams/divisions description in markdown (e.g. for labs)
- public_alignment_agenda: From "**Public alignment agenda:**" and/or "**Public plan:**" - Merge both if present (e.g. for labs)
- framework: From "**Framework:**" - Framework link/description in markdown (e.g. for labs)

**Available Agendas and Sections** (use these IDs in see_also):
{% for item in agenda_list %}
- {{ item.id }}: {{ item.name }}
{% endfor %}

**Orthodox Problems** (use IDs from this table):
{% for problem_id, problem_info in orthodox_problems.items() %}
- {{ problem_id }}: {{ problem_info.name }}
{% endfor %}

**Target Cases** (use IDs from this table):
{% for case_id, case_info in target_cases.items() %}
- {{ case_id }}: {{ case_info.name }}
{% endfor %}

**Broad Approaches** (use IDs from this table):
{% for approach_id, approach_info in broad_approaches.items() %}
- {{ approach_id }}: {{ approach_info.name }}
{% endfor %}

**Outputs** (extract from "**Outputs in 2025:**" or "**Outputs:**" section if present):
- Extract all output items (papers, blog posts, etc.) as a flat list
- For items with URLs: Extract the URL and preserve the original markdown
- For items without URLs: Set url=null and preserve the original markdown in original_md
- For subsection headers (e.g., "### Interpretability at pretrain-time"): Create OutputSectionHeader items with name, header_level, and original_md
- Ignore the header depth - just preserve the structure and order
- Leave title, authors, date, venue, kind, summary, key_result as null (they will be enriched from database later)

**Other Attributes**: Any attributes with **Attribute Name:** format that don't match the standard ones above.

**Parsing Issues**: Detect and report any issues with the content or parsing:
- Source document issues: missing headers, wrong sec:/a: markers, formatting problems
- Content issues: empty/minimal content, mismatched titles, wrong company/org info
- Parsing issues: confusion about structure, ambiguous attributions, etc.
If everything looks correct and complete, return an empty list.

**EXAMPLES:**

Example 1 - Lab/Organization (a:openai):

Input DocumentItem:
```json
{
  "id": "a:openai",
  "name": "OpenAI Safety",
  "header_level": 2,
  "parent_id": "sec:big_labs",
  "content": null,
  "item_type": "agenda",
  "agenda_attributes": null,
  "parsing_issues": []
}
```

Content:
<content>
**See also:** iterative alignment, safeguards, personas.
**Host org structure**: public benefit corp
**Teams**: Alignment, Safety Systems (Interpretability, Safety Oversight, Pretraining Safety)
**Public alignment agenda:** [None](https://openai.com/safety). Barak [offers](https://lesswrong.com) personal views.
**Public plan**: [Preparedness Framework](https://cdn.openai.com/pdf/preparedness-framework.pdf)
**Critiques:** [Stein-Perlman](https://ailabwatch.org/companies/openai)
**Some names:** Johannes Heidecke, Boaz Barak
**Funded by:** Microsoft, AWS, Oracle
**Outputs in 2025:**
* Their System Cards contain safety work.
* [https://alignment.openai.com/](https://alignment.openai.com/)
</content>

Output DocumentItem (only non-default values shown):
```json
{
  "id": "a:openai",
  "name": "OpenAI Safety",
  "header_level": 2,
  "parent_id": "sec:big_labs",
  "content": null,
  "item_type": "agenda",
  "agenda_attributes": {
    "see_also": ["sec:iterative_alignment", "a:anthropic_safeguards", "a:psych_personas"],
    "some_names": ["Johannes Heidecke", "Boaz Barak"],
    "critiques": "[Stein-Perlman](https://ailabwatch.org/companies/openai)",
    "funded_by": "Microsoft, AWS, Oracle",
    "organization_structure": "public benefit corp",
    "teams": "Alignment, Safety Systems (Interpretability, Safety Oversight, Pretraining Safety)",
    "public_alignment_agenda": "[None](https://openai.com/safety). Barak [offers](https://lesswrong.com) personal views. **Public plan**: [Preparedness Framework](https://cdn.openai.com/pdf/preparedness-framework.pdf)",
    "outputs": [
      {"original_md": "* Their System Cards contain safety work."},
      {"url": "https://alignment.openai.com/", "original_md": "* [https://alignment.openai.com/](https://alignment.openai.com/)"}
    ]
  },
  "parsing_issues": []
}
```

Example 2 - Research Agenda (sec:iterative_alignment):

Input DocumentItem:
```json
{
  "id": "sec:iterative_alignment",
  "name": "Iterative alignment",
  "header_level": 2,
  "parent_id": null,
  "content": null,
  "item_type": "section",
  "agenda_attributes": null,
  "parsing_issues": []
}
```

Content:
<content>
**Who edits (internal):** Stag✅
**One-sentence summary:** nudging base models by optimising their output.
**Theory of change:** LLMs don't seem very dangerous and might scale to AGI, assume alignment is a superficial feature.
**See also:** [character training](#character-training-[a:psych_personas])
**Orthodox problems:** this agenda implicitly questions this framing.
**Target case:** optimistic-case
**Broad approach:** engineering
**Some names:** post-training teams at most labs.
**Estimated FTEs:** 1200+
**Funded by:** most of the industry
**Outputs:** Subdivided as follows:

### Iterative alignment at pretrain-time
* [**Towards Cognitively-Faithful Models**](https://arxiv.org/abs/2509.04445)

### Iterative alignment at post-train-time
* [**RLHS: Mitigating Misalignment**](https://arxiv.org/abs/2501.08617)
</content>

Output DocumentItem (only non-default values shown):
```json
{
  "id": "sec:iterative_alignment",
  "name": "Iterative alignment",
  "header_level": 2,
  "parent_id": null,
  "content": null,
  "item_type": "section",
  "agenda_attributes": {
    "who_edits": "Stag✅",
    "one_sentence_summary": "nudging base models by optimising their output.",
    "theory_of_change": "LLMs don't seem very dangerous and might scale to AGI, assume alignment is a superficial feature.",
    "see_also": ["a:psych_personas"],
    "target_case": "average_case",
    "broad_approach": "engineering",
    "some_names": ["post-training teams at most labs"],
    "estimated_ftes": "1200+",
    "funded_by": "most of the industry",
    "outputs": [
      {
        "name": "Iterative alignment at pretrain-time",
        "header_level": 3,
        "original_md": "### Iterative alignment at pretrain-time"
      },
      {
        "url": "https://arxiv.org/abs/2509.04445",
        "original_md": "* [**Towards Cognitively-Faithful Models**](https://arxiv.org/abs/2509.04445)"
      },
      {
        "name": "Iterative alignment at post-train-time",
        "header_level": 3,
        "original_md": "### Iterative alignment at post-train-time"
      },
      {
        "url": "https://arxiv.org/abs/2501.08617",
        "original_md": "* [**RLHS: Mitigating Misalignment**](https://arxiv.org/abs/2501.08617)"
      }
    ]
  },
  "parsing_issues": ["Orthodox problems field says 'this agenda implicitly questions this framing' - unclear which problems this relates to"]
}
```

Note in examples:
- **Omit default values**: Fields with defaults (null, [], {}) can be omitted from output for brevity. The examples above show only non-default values.
- Extract text EXACTLY as written, preserving markdown formatting
- For "see_also": resolve external links to agenda IDs when possible (e.g., "character training" with link to [a:psych_personas] becomes "a:psych_personas")
- For "target_case": map "optimistic-case" to "average_case" (closest match)
- For organization/labs: focus on teams, funders, structure, public plans
- For research agendas: focus on theory of change, orthodox problems, target case, broad approach
- Merge "Public alignment agenda" and "Public plan" fields into single "public_alignment_agenda"
- For "outputs": Extract all items from "**Outputs in 2025:**" or "**Outputs:**" section
  - URLs go in "url" field, preserve full markdown in "original_md"
  - Items without URLs: omit "url" field (defaults to null), include "original_md"
  - Subsection headers: OutputSectionHeader with "name", "header_level", "original_md" (omit description if not present)
  - Preserve order and structure, leave database fields (title, authors, etc.) as null (can be omitted)

IMPORTANT: 
- Return valid JSON only. Do not use backslash escapes except for standard JSON escapes (\\n, \\t, \\", \\\\).
- Preserve markdown formatting exactly as written in the source.
- **Omit fields with default values** (null, [], {}) for brevity - they will be filled in automatically.

Respond with a complete DocumentItem JSON object (example with ALL fields shown):
```json
{
  "id": "a:openai",  // MUST match input exactly
  "name": "OpenAI Safety",  // MUST match input exactly
  "header_level": 2,  // MUST match input exactly
  "parent_id": "sec:big_labs",  // MUST match input exactly
  "content": null,  // ALWAYS null
  "item_type": "agenda",  // MUST match input exactly
  "agenda_attributes": {
    // Only include fields with non-default values:
    "who_edits": "Name✅",
    "one_sentence_summary": "Brief description",
    "see_also": ["a:id1", "sec:id2"],
    "some_names": ["Name1", "Name2"],
    "funded_by": "Company A, Company B",
    "outputs": [
      {
        "url": "https://arxiv.org/abs/1234.5678",
        "original_md": "* [**Paper Title**](https://arxiv.org/abs/1234.5678)"
      }
    ]
    // Omit: orthodox_problems (empty), target_case (null), teams (null), etc.
  },
  "parsing_issues": []  // Last field, can be omitted if empty
}
```
"""
)


def _should_retry(exception):
    """Determine if we should retry on this exception."""
    if isinstance(exception, KeyboardInterrupt):
        return False
    from openai import APIError, RateLimitError

    return isinstance(exception, (RateLimitError, APIError, ValidationError))


@retry(
    retry=retry_if_exception(_should_retry),
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=2, min=4, max=64),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)


def clean_agenda_content(content: str) -> str:
    """Remove structured fields from content, keeping only unstructured prose.
    
    After LLM extraction, we remove all the "**Field Name:** value" patterns
    since they're now in structured fields. This keeps only unstructured text
    that doesn't fit into any specific field.
    
    Args:
        content: Original agenda content
        
    Returns:
        Cleaned content with only unstructured prose
    """
    if not content:
        return ""
    
    # Split by paragraphs (double newline)
    paragraphs = re.split(r'\n\n+', content)
    cleaned_paragraphs = []
    
    for para in paragraphs:
        # Skip empty paragraphs
        if not para.strip():
            continue
            
        # Skip marker lines like [a:openai] or [sec:...]
        if re.match(r'^\s*\\?\[(?:a|sec):[^\]]+\\?\]\s*$', para.strip()):
            logger.debug(f"Skipping marker line: {para.strip()[:50]}")
            continue
        
        # Skip paragraphs that start with a structured field marker "**Field:**" or "**Field**:"
        # This includes the entire paragraph (field name + value)
        # Handle both formats: **Field**: (colon outside) and **Field:** (colon inside bold)
        stripped = para.strip()
        if re.match(r'^\s*\*\*[^*]+(:\*\*|\*\*:)\s*', stripped):
            logger.debug(f"Skipping structured field: {stripped[:80]}")
            continue
        
        # Skip header markers that might be at the end (e.g., "## Next Section")
        if re.match(r'^\s*#+\s+', para.strip()):
            logger.debug(f"Skipping header: {para.strip()[:50]}")
            continue
        
        # Keep this paragraph - it's unstructured content
        logger.debug(f"Keeping paragraph: {para.strip()[:80]}")
        cleaned_paragraphs.append(para.strip())
    
    # Join paragraphs with double newline
    cleaned = '\n\n'.join(cleaned_paragraphs)
    
    logger.debug(f"Cleaned content length: {len(cleaned)} (from {len(content)})")
    return cleaned


def extract_agenda_attributes(
    item: DocumentItem,
    content: str,
    agenda_list: list[dict[str, str]],
) -> DocumentItem:
    """Extract structured metadata from agenda content using Claude Haiku.

    Takes a DocumentItem with structural fields (id, name, header_level, parent_id)
    and content separately. Returns the same DocumentItem with agenda_attributes populated.

    Args:
        item: DocumentItem with id, name, header_level, parent_id filled (content should be None)
        content: Markdown content to extract from
        agenda_list: List of all agendas/sections for see_also resolution (dicts with 'id' and 'name')

    Returns:
        DocumentItem with agenda_attributes populated (and parsing_issues added)
    """
    from litellm import completion

    # Defensive checks
    if item.content is not None:
        logger.warning(f"Item {item.id} has non-null content field, should be null for extraction")
    
    if not content or not content.strip():
        logger.warning(f"Empty content for {item.id}, returning item with empty attributes")
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append("Empty content provided for extraction")
        return item

    if not agenda_list:
        logger.warning(f"Empty agenda_list for {item.id}, see_also resolution may fail")

    # Create input item JSON (without content field for prompt)
    item_for_prompt = item.model_copy()
    item_for_prompt.content = None  # Ensure content is None
    item_json = item_for_prompt.model_dump_json(indent=2, exclude_none=False)

    # Render prompt with item structure and content
    try:
        prompt = EXTRACTION_PROMPT.render(
            item_json=item_json,
            content=content,
            orthodox_problems=ORTHODOX_PROBLEMS,
            target_cases=TARGET_CASES,
            broad_approaches=BROAD_APPROACHES,
            agenda_list=agenda_list,
        )
    except Exception as e:
        logger.error(f"Failed to render prompt for {item.id}: {e}")
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append(f"Prompt rendering failed: {str(e)}")
        return item

    # Call LLM
    try:
        response = completion(
            model="claude-haiku-4-5",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=8000,  # Increased for full DocumentItem output
            temperature=0.0,
        )
    except Exception as e:
        logger.error(f"LLM call failed for {item.id}: {e}")
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append(f"LLM call failed: {str(e)}")
        return item

    # Extract response
    if not response or not response.choices or not response.choices[0].message:
        logger.error(f"Invalid LLM response for {item.id}")
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append("Invalid LLM response structure")
        return item

    response_text = response.choices[0].message.content
    if not response_text:
        logger.error(f"Empty LLM response for {item.id}")
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append("Empty LLM response")
        return item

    # Parse JSON from response (handle markdown code blocks)
    json_match = re.search(r"```(?:json)?\s*\n(.*?)\n```", response_text, re.DOTALL)
    if json_match:
        json_text = json_match.group(1)
    else:
        json_text = response_text
    
    # Fix common JSON escape issues from LLM output
    def fix_json_escapes(text: str) -> str:
        """Fix invalid backslash escapes in JSON text."""
        result = text.replace('\\', '\\\\')  # Escape all backslashes
        # Now unescape the valid JSON escapes (they're now double-escaped)
        result = result.replace('\\\\n', '\\n')
        result = result.replace('\\\\t', '\\t')
        result = result.replace('\\\\r', '\\r')
        result = result.replace('\\\\f', '\\f')
        result = result.replace('\\\\b', '\\b')
        result = result.replace('\\\\/', '\\/')
        result = result.replace('\\\\"', '\\"')
        result = result.replace('\\\\\\\\', '\\\\')  # Fix double-escaped backslashes
        return result
    
    json_text = fix_json_escapes(json_text)

    # Parse as DocumentItem
    try:
        returned_item = DocumentItem.model_validate_json(json_text)
    except (json.JSONDecodeError, ValidationError) as e:
        logger.error(f"Failed to parse JSON for {item.id}: {e}")
        logger.debug(f"Response text: {response_text[:500]}")
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append(f"JSON parsing failed: {str(e)}")
        return item
    
    # Validate structural fields are unchanged
    validation_errors = []
    if returned_item.id != item.id:
        validation_errors.append(f"ID mismatch: expected {item.id}, got {returned_item.id}")
    if returned_item.name != item.name:
        validation_errors.append(f"Name mismatch: expected {item.name}, got {returned_item.name}")
    if returned_item.header_level != item.header_level:
        validation_errors.append(f"Header level mismatch: expected {item.header_level}, got {returned_item.header_level}")
    if returned_item.parent_id != item.parent_id:
        validation_errors.append(f"Parent ID mismatch: expected {item.parent_id}, got {returned_item.parent_id}")
    if returned_item.item_type != item.item_type:
        validation_errors.append(f"Item type mismatch: expected {item.item_type}, got {returned_item.item_type}")
    if returned_item.content is not None:
        validation_errors.append(f"Content should be null, got: {returned_item.content[:50] if returned_item.content else 'None'}...")
    
    if validation_errors:
        logger.error(f"LLM changed structural fields for {item.id}: {validation_errors}")
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.extend(validation_errors)
        return item

    # Validate agenda_attributes content
    if not returned_item.agenda_attributes:
        logger.warning(f"LLM didn't populate agenda_attributes for {item.id}")
        item.agenda_attributes = AgendaAttributes()
        item.parsing_issues.append("LLM response missing agenda_attributes")
        return item
    
    attrs = returned_item.agenda_attributes
    
    # Validate see_also IDs exist in agenda_list
    valid_agenda_ids = {a["id"] for a in agenda_list}
    if attrs.see_also:
        invalid_see_also = set(attrs.see_also) - valid_agenda_ids
        if invalid_see_also:
            logger.warning(
                f"Invalid see_also IDs for {item.id}: {invalid_see_also}. "
                f"Valid IDs: {sorted(valid_agenda_ids)[:10]}..."
            )
            returned_item.parsing_issues.append(
                f"Invalid see_also IDs: {sorted(invalid_see_also)}"
            )

    # Validate orthodox_problems IDs
    if attrs.orthodox_problems:
        invalid_problems = [p for p in attrs.orthodox_problems if p not in ORTHODOX_PROBLEMS]
        if invalid_problems:
            logger.warning(
                f"Invalid orthodox_problem IDs for {item.id}: {invalid_problems}"
            )
            returned_item.parsing_issues.append(
                f"Invalid orthodox_problem IDs: {invalid_problems}"
            )

    # Validate target_case ID
    if attrs.target_case and attrs.target_case not in TARGET_CASES:
        logger.warning(
            f"Invalid target_case ID for {item.id}: {attrs.target_case}"
        )
        returned_item.parsing_issues.append(f"Invalid target_case ID: {attrs.target_case}")

    # Validate broad_approach ID
    if attrs.broad_approach and attrs.broad_approach not in BROAD_APPROACHES:
        logger.warning(
            f"Invalid broad_approach ID for {item.id}: {attrs.broad_approach}"
        )
        returned_item.parsing_issues.append(f"Invalid broad_approach ID: {attrs.broad_approach}")

    # Success - return the filled item
    return returned_item


# ============================================================================
# Paper Enrichment Functions
# ============================================================================


def enrich_papers_from_db(doc: ProcessedDocument, verbose: bool = False) -> tuple[int, int]:
    """Enrich Paper objects with data from classify database and add missing papers.
    
    Args:
        doc: ProcessedDocument with parsed papers
        verbose: If True, show detailed list of missing URLs
        
    Returns:
        Tuple of (enriched_count, added_count) - papers enriched and papers added to DB
    """
    if not _SHALLOW_REVIEW_AVAILABLE:
        logger.warning("shallow_review modules not available - skipping paper enrichment")
        return (0, 0)
    
    from draft_parser import Paper
    
    # Collect all paper URLs from all agendas
    paper_urls: set[str] = set()
    papers_by_url: dict[str, list[Paper]] = {}
    
    for item in doc.items:
        if item.agenda_attributes and item.agenda_attributes.outputs:
            for output in item.agenda_attributes.outputs:
                if isinstance(output, Paper) and output.url:
                    paper_urls.add(output.url)
                    if output.url not in papers_by_url:
                        papers_by_url[output.url] = []
                    papers_by_url[output.url].append(output)
    
    if not paper_urls:
        return (0, 0)
    
    enriched_count = 0
    added_count = 0
    missing_urls: list[tuple[str, str]] = []  # (original_url, normalized_url)
    
    # Look up papers in database
    with data_db_locked() as db:
        for url in paper_urls:
            normalized = normalize_url(url)
            
            # Try normalized URL first, then original
            row = db.execute(
                "SELECT data FROM classify WHERE url = ? OR url = ?",
                (normalized, url)
            ).fetchone()
            
            if row and row["data"]:
                # Enrich all Paper objects with this URL
                try:
                    data = json.loads(row["data"])
                    for paper in papers_by_url[url]:
                        paper.title = data.get("title")
                        paper.authors = data.get("authors", [])
                        paper.author_organizations = data.get("author_organizations", [])
                        paper.date = data.get("date")
                        paper.published_year = data.get("published_year")
                        paper.venue = data.get("venue")
                        paper.kind = data.get("kind")
                        paper.summary = data.get("summary")
                        paper.key_result = data.get("key_result")
                        enriched_count += 1
                except (json.JSONDecodeError, KeyError) as e:
                    logger.warning(f"Failed to parse classify data for {url}: {e}")
            else:
                # Paper not in database - add it
                missing_urls.append((url, normalized))
    
    # Add missing papers to classify table
    if missing_urls:
        from shallow_review.classify import add_classify_candidate
        
        console.print(f"[yellow]Found {len(missing_urls)} papers not in database, adding to classify table...[/yellow]")
        for original_url, normalized_url in missing_urls:
            try:
                is_new = add_classify_candidate(
                    url=normalized_url,
                    source="draft_parser",
                    source_url=None,
                    collect_relevancy=None,
                )
                if is_new:
                    added_count += 1
                    logger.info(f"Added missing paper to classify: {normalized_url}")
                    if original_url != normalized_url:
                        logger.debug(f"  (normalized from: {original_url})")
                else:
                    # Race condition - was added between check and add
                    logger.debug(f"Paper already exists (race condition): {normalized_url}")
            except Exception as e:
                logger.error(f"Failed to add paper {normalized_url} to classify: {e}")
                console.print(f"[red]Error: Failed to add {normalized_url}: {e}[/red]")
        
        # Warn about all missing papers
        console.print(
            f"[yellow]Warning: {len(missing_urls)} paper URLs not found in database "
            f"({added_count} added, {len(missing_urls) - added_count} already existed or failed)[/yellow]"
        )
        if verbose:
            for original_url, normalized_url in missing_urls[:10]:  # Show first 10
                display_url = normalized_url if original_url == normalized_url else f"{original_url} → {normalized_url}"
                console.print(f"  [dim]- {display_url}[/dim]")
            if len(missing_urls) > 10:
                console.print(f"  [dim]... and {len(missing_urls) - 10} more[/dim]")
    
    return (enriched_count, added_count)


# ============================================================================
# Validation Functions
# ============================================================================


def validate_document_structure(
    doc: ProcessedDocument, llm_processed_agenda_ids: set[str] | None = None
) -> tuple[list[str], list[str]]:
    """Validate document structure and return (errors, warnings).

    Checks:
    - Header levels make sense (agendas exactly one level below their containing section)
    - Section levels increase by at most one
    - No nested agendas
    - No strange tags in names (e.g. no other `[`)
    - All LLM-processed agendas have reasonable amount of fields (at least 5)

    Args:
        doc: ProcessedDocument to validate
        llm_processed_agenda_ids: Set of agenda IDs that were LLM-processed (for field count check)

    Returns:
        Tuple of (errors, warnings) lists
    """
    if llm_processed_agenda_ids is None:
        llm_processed_agenda_ids = set()
    errors: list[str] = []
    warnings: list[str] = []

    # Build a map of item_id -> DocumentItem for quick lookup
    items_by_id: dict[str, DocumentItem] = {item.id: item for item in doc.items}

    # Track section hierarchy
    section_stack: list[DocumentItem] = []

    for item in doc.items:
        # Check for strange tags in names
        if "[" in item.name and not re.search(r"\[(?:sec|a):[^\]]+\]", item.name):
            errors.append(
                f"Item '{item.name}' ({item.id}) contains unexpected '[' tag in name"
            )

        if item.item_type == ItemType.SECTION:
            # Validate section header level progression
            if section_stack:
                parent_section = section_stack[-1]
                level_diff = item.header_level - parent_section.header_level
                if level_diff > 1:
                    errors.append(
                        f"Section '{item.name}' ({item.id}) jumps by {level_diff} levels "
                        f"from parent '{parent_section.name}' ({parent_section.id})"
                    )
                elif level_diff < 0:
                    # This is fine, it's a sibling or uncle
                    pass

            # Update stack: pop until we find a parent at lower level
            while section_stack and section_stack[-1].header_level >= item.header_level:
                section_stack.pop()

            section_stack.append(item)

        elif item.item_type == ItemType.AGENDA:
            # Validate agenda is exactly one level below its containing section
            # Use parent_id to find the actual parent (which should be a section)
            if not item.parent_id:
                errors.append(
                    f"Agenda '{item.name}' ({item.id}) has no parent section"
                )
            else:
                parent = items_by_id.get(item.parent_id)
                if not parent:
                    errors.append(
                        f"Agenda '{item.name}' ({item.id}) has invalid parent_id: {item.parent_id}"
                    )
                elif parent.item_type != ItemType.SECTION:
                    errors.append(
                        f"Agenda '{item.name}' ({item.id}) has parent '{parent.name}' ({parent.id}) "
                        f"which is not a section"
                    )
                else:
                    expected_level = parent.header_level + 1
                    if item.header_level != expected_level:
                        errors.append(
                            f"Agenda '{item.name}' ({item.id}) has level {item.header_level}, "
                            f"expected {expected_level} (one level below section '{parent.name}')"
                        )

            # Check for nested agendas (agenda as parent of another agenda)
            if item.parent_id and items_by_id.get(item.parent_id):
                parent = items_by_id[item.parent_id]
                if parent.item_type == ItemType.AGENDA:
                    errors.append(
                        f"Agenda '{item.name}' ({item.id}) is nested under another agenda "
                        f"'{parent.name}' ({parent.id})"
                    )

            # Check agenda has reasonable amount of fields (at least 5 non-empty)
            # Only check for agendas that were LLM-processed
            if item.agenda_attributes and item.id in llm_processed_agenda_ids:
                field_count = sum(
                    [
                        1 if item.agenda_attributes.who_edits else 0,
                        1 if item.agenda_attributes.one_sentence_summary else 0,
                        1 if item.agenda_attributes.theory_of_change else 0,
                        1 if item.agenda_attributes.see_also else 0,
                        1 if item.agenda_attributes.orthodox_problems else 0,
                        1 if item.agenda_attributes.target_case else 0,
                        1 if item.agenda_attributes.broad_approach else 0,
                        1 if item.agenda_attributes.some_names else 0,
                        1 if item.agenda_attributes.estimated_ftes else 0,
                        1 if item.agenda_attributes.critiques else 0,
                        1 if item.agenda_attributes.funded_by else 0,
                        1 if item.agenda_attributes.funding_in_2025 else 0,
                        1 if item.agenda_attributes.organization_structure else 0,
                        1 if item.agenda_attributes.teams else 0,
                        1 if item.agenda_attributes.public_alignment_agenda else 0,
                        1 if item.agenda_attributes.framework else 0,
                        1 if item.agenda_attributes.outputs else 0,
                        1 if item.agenda_attributes.other_attributes else 0,
                    ]
                )
                if field_count < 5:
                    warnings.append(
                        f"Agenda '{item.name}' ({item.id}) has only {field_count} fields "
                        f"(expected at least 5)"
                    )
                
                # Validate see_also IDs reference valid items
                if item.agenda_attributes.see_also:
                    valid_ids = set(items_by_id.keys())
                    invalid_refs = [
                        ref for ref in item.agenda_attributes.see_also
                        if ref not in valid_ids
                    ]
                    if invalid_refs:
                        errors.append(
                            f"Agenda '{item.name}' ({item.id}) has invalid see_also references: "
                            f"{invalid_refs}"
                        )
                    
                    # Check for duplicate see_also entries
                    if len(item.agenda_attributes.see_also) != len(set(item.agenda_attributes.see_also)):
                        duplicates = [
                            ref for ref in set(item.agenda_attributes.see_also)
                            if item.agenda_attributes.see_also.count(ref) > 1
                        ]
                        warnings.append(
                            f"Agenda '{item.name}' ({item.id}) has duplicate see_also entries: "
                            f"{duplicates}"
                        )
                
                # Validate outputs URLs are valid if present
                if item.agenda_attributes.outputs:
                    from draft_parser import Paper
                    for output in item.agenda_attributes.outputs:
                        if isinstance(output, Paper) and output.url:
                            if not output.url.startswith(("http://", "https://")):
                                warnings.append(
                                    f"Agenda '{item.name}' ({item.id}) has invalid output URL: "
                                    f"{output.url}"
                                )
    
    # Warn about agendas not LLM-processed
    all_agenda_ids = {item.id for item in doc.items if item.item_type == ItemType.AGENDA}
    unprocessed_count = len(all_agenda_ids - llm_processed_agenda_ids)
    if unprocessed_count > 0:
        warnings.append(
            f"{unprocessed_count} agenda(s) were not LLM-processed (skipped due to --limit or processing error)"
        )

    return errors, warnings


@app.command()
def parse(
    input_file: str = typer.Argument(..., help="Path to draft markdown file"),
    output_file: str | None = typer.Option(
        None, "--output", "-o", help="Output JSON file path (default: <input>-parsed.json)"
    ),
    cache_dir: str | None = typer.Option(
        None, "--cache-dir", help="LLM cache directory (default: .llm_cache)"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging"),
    limit: int | None = typer.Option(
        None, "--limit", "-n", help="Limit LLM extraction to first N agendas (full document is always parsed)"
    ),
) -> None:
    """Parse a draft document into structured JSON using Claude Haiku.

    Step 1: Parses the document structure (sections [sec:...] and agendas [a:...])
    Step 2: Uses Claude Haiku to extract structured metadata from each agenda.
    """
    setup_logging(verbose)

    input_path = Path(input_file)
    if not input_path.exists():
        console.print(f"[red]Error: File not found: {input_file}[/red]")
        raise typer.Exit(1)

    # Setup LLM
    cache_path = Path(cache_dir) if cache_dir else None
    setup_litellm(cache_path)

    # Determine output path
    if output_file is None:
        output_path = input_path.parent / f"{input_path.stem}-parsed.json"
    else:
        output_path = Path(output_file)

    # ========================================================================
    # Step 1: Parse document structure
    # ========================================================================
    console.print(f"[cyan]Step 1: Parsing document structure from {input_file}...[/cyan]")
    doc = parse_document(input_path)

    # Count all sections and agendas (always parse full document)
    all_agenda_items = [item for item in doc.items if item.item_type == ItemType.AGENDA]
    total_sections = len([i for i in doc.items if i.item_type == ItemType.SECTION])
    total_agendas = len(all_agenda_items)
    
    console.print(
        f"[green]Found {total_sections} sections with {total_agendas} agendas[/green]"
    )
    
    # Apply limit only to LLM processing (not document parsing)
    if limit is not None:
        agenda_items = all_agenda_items[:limit]
        console.print(
            f"[yellow]Limiting LLM processing to first {limit} agendas (out of {total_agendas})[/yellow]"
        )
    else:
        agenda_items = all_agenda_items

    # Build agenda list for LLM (for see_also resolution)
    agenda_list = [
        {"id": item.id, "name": item.name}
        for item in doc.items
        if item.item_type in (ItemType.SECTION, ItemType.AGENDA)
    ]

    # ========================================================================
    # Step 2: Extract metadata with LLM
    # ========================================================================
    console.print("[cyan]Step 2: Extracting metadata with Claude Haiku...[/cyan]")

    # Track which agendas were LLM-processed
    llm_processed_agenda_ids: set[str] = set()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(f"Processing {len(agenda_items)} agendas...", total=len(agenda_items))

        for idx, item in enumerate(agenda_items):
            progress.update(
                task, description=f"Processing {item.id}...", advance=0
            )

            # Extract attributes with LLM
            try:
                # Scrub content before passing to LLM
                from draft_parser import scrub_markdown
                content_for_llm = scrub_markdown(item.content or "")
                
                # Create input item with content=None
                item_for_llm = item.model_copy()
                item_for_llm.content = None
                
                # Call LLM extraction (returns filled DocumentItem)
                filled_item = extract_agenda_attributes(
                    item_for_llm,
                    content_for_llm,
                    agenda_list,
                )
                
                # Replace item in list with filled version
                # Find original item in doc.items and replace
                for doc_idx, doc_item in enumerate(doc.items):
                    if doc_item.id == item.id:
                        doc.items[doc_idx] = filled_item
                        break
                
                # Update reference for next iterations
                agenda_items[idx] = filled_item
                
                # Mark as LLM-processed
                llm_processed_agenda_ids.add(filled_item.id)

            except Exception as e:
                logger.error(f"Failed to extract attributes for {item.id}: {e}")
                console.print(
                    f"[yellow]Warning: Failed to extract {item.id}: {e}[/yellow]"
                )
                item.parsing_issues.append(f"Extraction failed: {str(e)}")

            progress.update(task, advance=1)

    # ========================================================================
    # Step 3: Enrich papers from database
    # ========================================================================
    console.print("[cyan]Step 3: Enriching papers from database...[/cyan]")
    enriched_count, added_count = enrich_papers_from_db(doc, verbose=verbose)
    console.print(
        f"[green]Enriched {enriched_count} papers, added {added_count} new papers to classify table[/green]"
    )

    # ========================================================================
    # Step 4: Validate structure
    # ========================================================================
    console.print("[cyan]Step 3: Validating parsed document...[/cyan]")
    errors, warnings = validate_document_structure(doc, llm_processed_agenda_ids)

    # Add LLM-detected parsing issues to warnings
    for item in doc.items:
        if item.agenda_attributes and item.agenda_attributes.parsing_issues:
            for issue in item.agenda_attributes.parsing_issues:
                warnings.append(f"{item.id}: {issue}")

    # Display errors and warnings
    if errors:
        console.print(f"\n[red]Errors found ({len(errors)}):[/red]")
        for error in errors:
            console.print(f"  [red]ERROR:[/red] {error}")

    if warnings:
        console.print(f"\n[yellow]Warnings found ({len(warnings)}):[/yellow]")
        for warning in warnings:
            console.print(f"  [yellow]WARNING:[/yellow] {warning}")

    if not errors and not warnings:
        console.print("[green]No errors or warnings found![/green]")

    # Convert PreparsedDocument to ProcessedDocument for output
    processed_doc = ProcessedDocument(
        source_file=doc.source_file,
        items=doc.items
    )

    # Write output
    output_data = processed_doc.model_dump()
    output_path.write_text(json.dumps(output_data, indent=2, default=str))

    console.print(f"\n[green]Parsed document written to {output_path}[/green]")

    # Exit with error code if errors found
    if errors:
        console.print(f"\n[red]Parsing completed with {len(errors)} errors[/red]")
        raise typer.Exit(1)


# ============================================================================
# Helper functions for format command
# ============================================================================


def shorten_title(title: str, max_length: int = 40) -> str:
    """Shorten a title to max_length, cutting at last word and adding '...'."""
    if len(title) <= max_length:
        return title

    # Cut at max_length and find last space
    truncated = title[:max_length]
    last_space = truncated.rfind(' ')

    if last_space > 0:
        # Cut at last word boundary
        return truncated[:last_space] + "..."
    else:
        # No space found, just truncate
        return truncated + "..."


def get_url_title_from_db(url: str) -> str | None:
    """Look up URL in database and return title if found.

    Args:
        url: URL to look up

    Returns:
        Title string if found in database, None otherwise
    """
    if not _SHALLOW_REVIEW_AVAILABLE:
        return None

    try:
        # Normalize URL for lookup
        normalized = normalize_url(url)

        # Check classify table first (has more metadata)
        with data_db_locked() as db:
            row = db.execute(
                "SELECT data FROM classify WHERE url = ? OR url = ?",
                (url, normalized)
            ).fetchone()

            if row and row["data"]:
                data = json.loads(row["data"])
                return data.get("title")

            # Fallback to scrape table
            row = db.execute(
                "SELECT data FROM scrape WHERE url = ? OR url = ?",
                (url, normalized)
            ).fetchone()

            if row and row["data"]:
                data = json.loads(row["data"])
                return data.get("title")

        return None
    except Exception as e:
        logger.debug(f"Failed to look up URL {url}: {e}")
        return None


def format_url_link(url: str) -> str:
    """Format a URL as markdown link with title from database if available.

    Args:
        url: URL to format

    Returns:
        Markdown link string: [title](url) if title found, else just url
    """
    title = get_url_title_from_db(url)

    if title:
        # Shorten title if needed
        title = shorten_title(title, max_length=40)
        return f"[{title}]({url})"
    else:
        # No title found, just return URL
        return url


def format_see_also_item(item: str) -> str:
    """Format a see_also item - either a a:/sec: reference or a URL.

    Args:
        item: A see_also reference (e.g., "a:interpretability" or "https://...")

    Returns:
        Formatted markdown string
    """
    # Check if it's a URL
    if item.startswith(("http://", "https://")):
        # Format as URL with DB lookup
        return format_url_link(item)
    else:
        # It's a category/section reference - return as-is
        return item


# ============================================================================
# format subcommand
# ============================================================================


@app.command()
def format(
    input_file: str = typer.Argument(..., help="Path to parsed JSON file"),
    output_file: str | None = typer.Option(
        None, "--output", "-o", help="Output markdown file path (default: <input>-formatted.md)"
    ),
    template_file: str | None = typer.Option(
        None, "--template", "-t", help="Path to Jinja2 markdown template (default: draft_template.md)"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging"),
) -> None:
    """Format a parsed JSON file into a nicely formatted markdown document.

    Takes the JSON output from the parse command and applies a Jinja2 template
    to generate a human-readable markdown document with all agendas and attributes.
    """
    setup_logging(verbose)

    input_path = Path(input_file)
    if not input_path.exists():
        console.print(f"[red]Error: File not found: {input_file}[/red]")
        raise typer.Exit(1)

    # Determine template path
    if template_file is None:
        template_path = Path(__file__).parent / "draft_template.md"
    else:
        template_path = Path(template_file)

    if not template_path.exists():
        console.print(f"[red]Error: Template not found: {template_path}[/red]")
        raise typer.Exit(1)

    # Determine output path
    if output_file is None:
        output_path = input_path.parent / f"{input_path.stem}-formatted.md"
    else:
        output_path = Path(output_file)

    console.print(f"[cyan]Loading parsed data from {input_file}...[/cyan]")

    # Load parsed JSON
    try:
        data = json.loads(input_path.read_text())
    except json.JSONDecodeError as e:
        console.print(f"[red]Error: Invalid JSON in {input_file}: {e}[/red]")
        raise typer.Exit(1)

    # Load template
    console.print(f"[cyan]Applying template {template_path}...[/cyan]")
    template_text = template_path.read_text()
    template = Template(template_text)

    # Render template with helper functions
    try:
        rendered = template.render(
            **data,
            format_url=format_url_link,  # Make helper available to template
            shorten_title=shorten_title,
            format_see_also=format_see_also_item,
        )
    except Exception as e:
        console.print(f"[red]Error: Template rendering failed: {e}[/red]")
        if verbose:
            logger.exception("Template rendering error")
        raise typer.Exit(1)

    # Write output
    output_path.write_text(rendered)

    console.print(f"[green]Formatted document written to {output_path}[/green]")
    console.print(f"[dim]Sections: {len(data.get('sections', []))}, " +
                  f"Agendas: {sum(len(s.get('agendas', [])) for s in data.get('sections', []))}[/dim]")


# ============================================================================
# Main entry point
# ============================================================================


def main() -> None:
    """Entry point for CLI."""
    try:
        app()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        if logger.isEnabledFor(logging.DEBUG):
            logger.exception("Unhandled exception")
        sys.exit(1)


if __name__ == "__main__":
    main()
