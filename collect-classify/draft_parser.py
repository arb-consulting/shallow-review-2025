"""Parser module for shallow review draft documents.

Handles parsing of markdown documents with [sec:...] sections and [a:...] agendas,
extracting structured metadata and scrubbing content for LLM processing.
"""

import logging
import re
from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


# ============================================================================
# Constants: Orthodox Problems, Target Cases, Broad Approaches
# ============================================================================

# Orthodox Problems from "A list of core AI safety problems"
# Source: https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve
# All 13 problems listed in order:
ORTHODOX_PROBLEMS: dict[str, dict[str, str]] = {
    "value_fragile": {
        "name": "Value is fragile and hard to specify",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#1__Value_is_fragile_and_hard_to_specify",
    },
    "corrigibility_anti_natural": {
        "name": "Corrigibility is anti-natural",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#2__Corrigibility_is_anti_natural",
    },
    "pivotal_dangerous_capabilities": {
        "name": "Pivotal processes require dangerous capabilities",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#3__Pivotal_processes_require_dangerous_capabilities",
    },
    "goals_misgeneralize": {
        "name": "Goals misgeneralize out of distribution",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#4__Goals_misgeneralize_out_of_distribution",
    },
    "instrumental_convergence": {
        "name": "Instrumental convergence",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#5__Instrumental_convergence",
    },
    "pivotal_incomprehensible_plans": {
        "name": "Pivotal processes likely require incomprehensibly complex plans",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#6__Pivotal_processes_likely_require_incomprehensibly_complex_plans",
    },
    "superintelligence_fool_supervisors": {
        "name": "Superintelligence can fool human supervisors",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#7__Superintelligence_can_fool_human_supervisors",
    },
    "superintelligence_hack_software": {
        "name": "Superintelligence can hack software supervisors",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#8__Superintelligence_can_hack_software_supervisors",
    },
    "humans_not_first_class": {
        "name": "Humans cannot be first-class parties to a superintelligent value handshake",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#9__Humans_cannot_be_first_class_parties_to_a_superintelligent_value_handshake",
    },
    "humanlike_minds_not_safe": {
        "name": "Humanlike minds/goals are not necessarily safe",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#10__Humanlike_minds_goals_are_not_necessarily_safe",
    },
    "someone_else_deploys": {
        "name": "Someone else will deploy unsafe superintelligence first",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#11__Someone_else_will_deploy_unsafe_superintelligence_first",
    },
    "boxed_agi_exfiltrate": {
        "name": "A boxed AGI might exfiltrate itself by steganography, spearphishing",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#12__A_boxed_AGI_might_exfiltrate_itself_by_steganography__spearphishing",
    },
    "fair_sane_pivotal": {
        "name": "Fair, sane pivotal processes",
        "url": "https://www.alignmentforum.org/posts/mnoc3cKY3gXMrTybs/a-list-of-core-ai-safety-problems-and-how-i-hope-to-solve#13__Fair__sane_pivotal_processes",
    },
}

# Target Cases from "Defining alignment research"
# Source: https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research
TARGET_CASES: dict[str, dict[str, str]] = {
    "average_case": {
        "name": "Average-case",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
    "pessimistic_case": {
        "name": "Pessimistic-case",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
    "worst_case": {
        "name": "Worst-case",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
}

# Broad Approaches from "Defining alignment research"
# Source: https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research
BROAD_APPROACHES: dict[str, dict[str, str]] = {
    "engineering": {
        "name": "Engineering",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
    "behaviorist_science": {
        "name": "Behaviorist science",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
    "cognitivist_science": {
        "name": "Cognitivist science",
        "url": "https://www.lesswrong.com/posts/67fNBeHrjdrZZNDDK/defining-alignment-research#A_better_definition_of_alignment_research",
    },
}


# ============================================================================
# Pydantic Models
# ============================================================================


class ItemType(str, Enum):
    """Type of top-level document item.

    Note: Papers and output sections are nested within agenda outputs,
    not top-level document items.
    """

    SECTION = "section"
    AGENDA = "agenda"


class Paper(BaseModel):
    """A research output (paper, blog post, etc.) in the outputs section.

    Fields from the database (classify.data JSON) are populated when available.
    """

    url: str | None = Field(default=None, description="URL if linked")
    original_md: str = Field(description="Original markdown text as read from source")

    # Database fields (from classify.data JSON)
    title: str | None = Field(default=None, description="Paper title")
    authors: list[str] = Field(default_factory=list, description="List of author names")
    author_organizations: list[str] = Field(
        default_factory=list, description="List of author organizations"
    )
    date: str | None = Field(
        default=None, description="Publication date in ISO format YYYY-MM-DD"
    )
    published_year: int | None = Field(default=None, description="Publication year as integer")
    venue: str | None = Field(default=None, description="Publication venue")
    kind: str | None = Field(
        default=None, description="Content type (e.g., 'paper_published', 'paper_preprint', 'blog_post')"
    )
    summary: str | None = Field(default=None, description="2-3 sentence summary of the work")
    key_result: str | None = Field(default=None, description="Main finding or contribution")


class OutputSectionHeader(BaseModel):
    """A subsection header within an outputs section.

    Papers following this header (until next header) are conceptually grouped under it,
    but structurally papers and headers are siblings in a flat list.
    """

    name: str = Field(description="Section header name")
    header_level: int = Field(description="Markdown header level (typically 3 or 4)")
    description: str | None = Field(default=None, description="Optional text block describing the section")
    original_md: str = Field(description="Original markdown text as read from source")


class AgendaMetadata(BaseModel):
    """Structured metadata extracted from a research agenda.

    Standard attributes have dedicated fields, non-standard ones go in other_attributes,
    and any free-form descriptive text goes in free_form_text.
    """

    # Core structured attributes (most common)
    who_edits: str | None = Field(default=None, description="Editor name (internal)")
    one_sentence_summary: str | None = None
    theory_of_change: str | None = None
    see_also: list[str] = Field(default_factory=list, description="Related agenda or section IDs")
    orthodox_problems: list[str] = Field(
        default_factory=list,
        description="List of orthodox problem IDs (keys from ORTHODOX_PROBLEMS)",
    )
    target_case: str | None = Field(
        default=None, description="Target case ID (key from TARGET_CASES)"
    )
    broad_approach: str | None = Field(
        default=None, description="Broad approach ID (key from BROAD_APPROACHES)"
    )
    some_names: list[str] = Field(default_factory=list, description="Key researchers")
    estimated_ftes: str | None = Field(default=None, description="FTE estimate or range")
    critiques: str | None = Field(
        default=None, description="Critiques as markdown text (links, descriptions, etc.)"
    )
    funded_by: str | None = Field(default=None, description="Funding sources")
    funding_in_2025: str | None = Field(default=None, description="Funding information for 2025")

    # Organization-specific attributes
    organization_structure: str | None = Field(
        default=None, description="Organization structure (e.g., 'public benefit corp', 'for-profit')"
    )
    teams: str | None = Field(
        default=None, description="Teams/divisions description in markdown"
    )
    public_alignment_agenda: str | None = Field(
        default=None, description="Public alignment agenda and/or public plan in markdown"
    )
    framework: str | None = Field(
        default=None, description="Framework link/description in markdown"
    )

    # Outputs - flat list of papers and section headers (preserving order)
    outputs: list[Paper | OutputSectionHeader] = Field(
        default_factory=list,
        description="Output sections and papers (flat list preserving order)",
    )

    # Catch-all for non-standard attributes
    other_attributes: dict[str, Any] = Field(
        default_factory=dict, description="Attributes not matching standard fields"
    )

    # Parsing quality and error detection
    parsing_issues: list[str] = Field(
        default_factory=list,
        description="Log of issues detected during parsing (missing headers, format problems, etc.)"
    )


class DocumentItem(BaseModel):
    """A single item in the flat document structure."""

    id: str = Field(description="Unique identifier (e.g., 'sec:big_labs', 'a:openai')")
    name: str = Field(description="Display name/title")
    header_level: int = Field(description="Markdown header level (1-6)")
    parent_id: str | None = Field(default=None, description="Parent item ID if nested")
    content: str | None = Field(default=None, description="Textual content right after the header (raw markdown)")
    item_type: ItemType = Field(description="Type of item")

    # Agenda-specific fields (only populated for agendas)
    agenda_metadata: AgendaMetadata | None = Field(
        default=None, description="Metadata for agendas (populated by LLM)"
    )


class ProcessedDocument(BaseModel):
    """The fully processed draft document with flat structure."""

    source_file: str
    items: list[DocumentItem] = Field(
        default_factory=list, description="Flat list of items in document order"
    )


# ============================================================================
# Text Scrubbing Functions
# ============================================================================


def scrub_markdown(text: str) -> str:
    """Clean markdown text by removing images, horizontal rules, and normalizing whitespace.

    Args:
        text: Raw markdown text

    Returns:
        Cleaned markdown text with MD-relevant whitespace preserved
    """
    # Remove image references: ![][imageN]
    text = re.sub(r"!\[\]\[image\d+\]", "", text)

    # Remove horizontal rules (--- on its own line)
    text = re.sub(r"^\s*---\s*$", "", text, flags=re.MULTILINE)

    # Remove escaped underscores in section/agenda markers
    text = re.sub(r"\\(_)", r"\1", text)

    # Normalize multiple blank lines to max 2 (preserves paragraph breaks)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove trailing whitespace from lines but preserve line breaks
    text = "\n".join(line.rstrip() for line in text.split("\n"))

    # Strip leading/trailing whitespace from whole text
    text = text.strip()

    return text


# ============================================================================
# Link Extraction Functions
# ============================================================================


def extract_links(text: str) -> list[dict[str, str | None]]:
    """Extract all HTTP(S) links from markdown text.

    Extracts both markdown-formatted links [text](url) and plain-text URLs.

    Args:
        text: Markdown text to extract links from

    Returns:
        List of dicts with 'url' and optional 'title' keys
    """
    links = []

    # Extract markdown links: [text](url)
    markdown_links = re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text)
    for match in markdown_links:
        title, url = match.groups()
        if url.startswith(("http://", "https://")):
            links.append({"url": url, "title": title})

    # Extract plain-text URLs
    # Match http(s):// followed by non-whitespace, with smart boundary detection
    url_pattern = r"https?://[^\s<>\"'\]\)]*[^\s<>\"'\]\),.\!?;:]"
    plain_urls = re.finditer(url_pattern, text)

    for match in plain_urls:
        url = match.group(0)
        # Check if this URL is already captured as a markdown link
        if not any(link["url"] == url for link in links):
            links.append({"url": url, "title": None})

    return links


def extract_all_links_from_file(file_path: Path) -> list[dict[str, str | None]]:
    """Extract all links from a markdown file.

    Args:
        file_path: Path to markdown file

    Returns:
        List of unique links found in the file (dicts with 'url' and optional 'title')
    """
    text = file_path.read_text(encoding="utf-8")
    links = extract_links(text)

    # Deduplicate by URL
    seen_urls = set()
    unique_links = []
    for link in links:
        if link["url"] not in seen_urls:
            seen_urls.add(link["url"])
            unique_links.append(link)

    return unique_links


# ============================================================================
# Document Parsing Functions
# ============================================================================


def find_markers_and_headers(text: str) -> list[tuple[str, str, int, int, int]]:
    """Find all [sec:...] and [a:...] markers and headers in document.

    Only matches markers that define sections/agendas, not those appearing
    inside markdown links or HTML anchor attributes.

    Args:
        text: Full markdown document text

    Returns:
        List of tuples: (type, id, header_level, start_pos, end_pos)
        where type is 'sec' or 'a', header_level is from markdown header (1-6)
    """
    items = []

    # Find all [sec:...] and [a:...] markers (handle both escaped \[...\] and unescaped [...])
    # Try escaped brackets first: \[(sec|a):...\]
    pattern_escaped = r"\\\[(sec|a):([^\]]+?)\\\]"
    for match in re.finditer(pattern_escaped, text):
        marker_type = match.group(1)  # 'sec' or 'a'
        marker_id = match.group(2).replace("\\", "")  # Strip any backslashes from ID
        start_pos = match.start()
        end_pos = match.end()
        
        # Skip markers inside markdown link URLs or HTML anchors (check below)
        before_marker = text[:start_pos]
        
        # Check if inside markdown link URL
        paren_depth = 0
        for i in range(len(before_marker) - 1, -1, -1):
            if before_marker[i] == ')':
                paren_depth += 1
            elif before_marker[i] == '(':
                paren_depth -= 1
                if paren_depth < 0:
                    break
        if paren_depth < 0:
            continue
        
        # Check if inside HTML anchor attribute
        brace_depth = 0
        for i in range(len(before_marker) - 1, -1, -1):
            if before_marker[i] == '}':
                brace_depth += 1
            elif before_marker[i] == '{':
                brace_depth -= 1
                if brace_depth < 0:
                    break
        if brace_depth < 0:
            continue
        
        # Find header level
        line_start = text.rfind('\n', 0, start_pos) + 1
        line_text = text[line_start:end_pos]
        header_match = re.match(r"^(#+)\s+(.+)$", line_text)
        if header_match:
            header_level = len(header_match.group(1))
        else:
            remaining_text = text[start_pos:]
            next_header_match = re.search(r"^(.*?)^(#+)\s+(.+)$", remaining_text, re.MULTILINE | re.DOTALL)
            if next_header_match:
                header_level = len(next_header_match.group(2))
            else:
                header_level = 1 if marker_type == "sec" else 2
        
        items.append((marker_type, marker_id, header_level, start_pos))
    
    # Also match unescaped brackets: [(sec|a):...]
    pattern_normal = r"\[(sec|a):([^\]]+)\]"
    for match in re.finditer(pattern_normal, text):
        marker_type = match.group(1)
        marker_id = match.group(2).replace("\\", "")
        start_pos = match.start()
        end_pos = match.end()
        
        # Skip if this would be a duplicate (already matched as escaped)
        # Check if there's a backslash before the opening bracket
        if start_pos > 0 and text[start_pos - 1] == '\\':
            continue
        
        # Skip markers inside markdown link URLs or HTML anchors
        before_marker = text[:start_pos]
        
        paren_depth = 0
        for i in range(len(before_marker) - 1, -1, -1):
            if before_marker[i] == ')':
                paren_depth += 1
            elif before_marker[i] == '(':
                paren_depth -= 1
                if paren_depth < 0:
                    break
        if paren_depth < 0:
            continue
        
        brace_depth = 0
        for i in range(len(before_marker) - 1, -1, -1):
            if before_marker[i] == '}':
                brace_depth += 1
            elif before_marker[i] == '{':
                brace_depth -= 1
                if brace_depth < 0:
                    break
        if brace_depth < 0:
            continue
        
        # Find header level
        line_start = text.rfind('\n', 0, start_pos) + 1
        line_text = text[line_start:end_pos]
        header_match = re.match(r"^(#+)\s+(.+)$", line_text)
        if header_match:
            header_level = len(header_match.group(1))
        else:
            remaining_text = text[start_pos:]
            next_header_match = re.search(r"^(.*?)^(#+)\s+(.+)$", remaining_text, re.MULTILINE | re.DOTALL)
            if next_header_match:
                header_level = len(next_header_match.group(2))
            else:
                header_level = 1 if marker_type == "sec" else 2
        
        items.append((marker_type, marker_id, header_level, start_pos))

    # Calculate end positions (start of next marker or end of document)
    result = []
    for i, (marker_type, marker_id, header_level, start_pos) in enumerate(items):
        if i + 1 < len(items):
            end_pos = items[i + 1][3]  # start_pos of next item
        else:
            end_pos = len(text)
        result.append((marker_type, marker_id, header_level, start_pos, end_pos))

    return result


def extract_header_name(text: str, start_pos: int) -> tuple[str, int]:
    """Extract header name and level from content starting at position.

    Args:
        text: Full document text
        start_pos: Start position to search from

    Returns:
        Tuple of (header_name, header_level)
    """
    remaining = text[start_pos:]
    header_match = re.search(r"^(#+)\s+(.+)$", remaining, re.MULTILINE)
    if header_match:
        header_level = len(header_match.group(1))
        header_name = header_match.group(2).strip().rstrip("\\ \t")
        # Remove escaped brackets: \[ -> [, \] -> ]
        header_name = header_name.replace("\\[", "[").replace("\\]", "]")
        return header_name, header_level
    return "", 0


def parse_outputs_section(content: str) -> list[Paper | OutputSectionHeader]:
    """Parse an outputs section into papers and section headers.

    Returns a flat list where headers and papers are siblings, preserving order.
    Headers conceptually group subsequent papers until the next header.

    Args:
        content: Markdown content of outputs section

    Returns:
        Flat list of papers and output section headers in order
    """
    items: list[Paper | OutputSectionHeader] = []
    lines = content.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()

        # Check for header (### or ####, typically level 3 or 4)
        header_match = re.match(r"^(#{3,4})\s+(.+)$", line)
        if header_match:
            header_level = len(header_match.group(1))
            header_name = header_match.group(2).strip()

            # Look ahead for description text (until next header or list item)
            description_lines = []
            i += 1
            while i < len(lines):
                next_line = lines[i].rstrip()
                # Stop at next header or list item
                if re.match(r"^#{3,4}\s+", next_line) or re.match(r"^[\*\-\+]", next_line):
                    break
                if next_line.strip():
                    description_lines.append(next_line)
                i += 1
            i -= 1  # Back up one line

            description = "\n".join(description_lines).strip() if description_lines else None
            header = OutputSectionHeader(
                name=header_name,
                header_level=header_level,
                description=description,
                original_md=line + (f"\n{description}" if description else ""),
            )
            items.append(header)
            i += 1
            continue

        # Check for list item (paper)
        list_match = re.match(r"^[\*\-\+]\s+(.+)$", line)
        if list_match:
            paper_text = list_match.group(1).strip()

            # Extract URL if present
            url_match = re.search(r"https?://[^\s<>\"'\]\)]*[^\s<>\"'\]\),.\!?;:]", paper_text)
            url = url_match.group(0) if url_match else None

            paper = Paper(url=url, original_md=line)
            items.append(paper)
            i += 1
            continue

        i += 1

    return items


def parse_document(file_path: Path) -> ProcessedDocument:
    """Parse a draft markdown document into flat structure.

    This performs basic structural parsing. The LLM extraction happens separately.

    Args:
        file_path: Path to markdown file

    Returns:
        ProcessedDocument with flat list of items (metadata fields will be populated by LLM)
    """
    text = file_path.read_text(encoding="utf-8")
    
    # Defensive: Check for empty file
    if not text.strip():
        raise ValueError(f"File {file_path} is empty")
    
    markers = find_markers_and_headers(text)
    
    # Defensive: Check for duplicate IDs
    seen_ids: set[str] = set()
    duplicate_ids: list[str] = []
    for marker_type, marker_id, _, _, _ in markers:
        item_id = f"{marker_type}:{marker_id}"
        if item_id in seen_ids:
            duplicate_ids.append(item_id)
        seen_ids.add(item_id)
    
    if duplicate_ids:
        raise ValueError(f"Duplicate item IDs found: {duplicate_ids}")

    items: list[DocumentItem] = []
    # Stack of (item_id, header_level) for tracking parent hierarchy
    parent_stack: list[tuple[str, int]] = []

    for marker_type, marker_id, header_level, start_pos, end_pos in markers:
        content = text[start_pos:end_pos]
        
        # Defensive: Check for empty content
        if not content.strip():
            logger.warning(f"Empty content for {marker_type}:{marker_id}")

        # Extract header name
        header_name, detected_level = extract_header_name(text, start_pos)
        if not header_name:
            # Fallback to marker_id
            header_name = marker_id.replace("_", " ").title()
            logger.warning(
                f"No header found for {marker_type}:{marker_id}, using fallback name: {header_name}"
            )
        if detected_level > 0:
            header_level = detected_level
        
        # Defensive: Validate header level is reasonable
        if header_level < 1 or header_level > 6:
            logger.warning(
                f"Unusual header level {header_level} for {marker_type}:{marker_id}, "
                f"name: {header_name}"
            )

        # Pop from stack until we find a parent at lower header level
        while parent_stack and parent_stack[-1][1] >= header_level:
            parent_stack.pop()

        # Determine parent_id from stack
        parent_id = parent_stack[-1][0] if parent_stack else None

        # Create item ID
        item_id = f"{marker_type}:{marker_id}"

        # Determine item type
        if marker_type == "sec":
            item_type = ItemType.SECTION
        else:
            item_type = ItemType.AGENDA

        # For agendas, parse outputs section and extract early fields
        agenda_metadata = None
        item_content = content  # Will be modified for agendas
        if marker_type == "a":
            # Extract "See also" if present
            # Look for "**See also:**" anywhere in content
            see_also = []
            see_also_pattern = r"\*\*See also:\*\*\s*(.+?)(?=\n\s*\*\*|\n\s*##|\Z)"
            see_also_match = re.search(see_also_pattern, item_content, re.MULTILINE | re.DOTALL)
            if see_also_match:
                see_also_text = see_also_match.group(1).strip()
                # Extract agenda/section IDs from the text (look for [a:...] or [sec:...] patterns)
                for match in re.finditer(r"\[(a|sec):([^\]]+)\]", see_also_text):
                    extracted_id = f"{match.group(1)}:{match.group(2)}"
                    see_also.append(extracted_id)
                # Remove the "See also" section from content to avoid duplication
                item_content = re.sub(see_also_pattern, "", item_content, flags=re.MULTILINE | re.DOTALL).strip()
            
            # Look for "Outputs in 2025:" section
            outputs_match = re.search(
                r"(?i)\*\*Outputs in 2025:\*\*\s*\n(.*?)(?=\n\s*\*\*|\n\s*##|\Z)",
                item_content,
                re.DOTALL,
            )
            if outputs_match:
                outputs_content = outputs_match.group(1)
                if not outputs_content.strip():
                    logger.warning(f"Empty outputs section for {item_id}")
                    outputs = []
                else:
                    try:
                        outputs = parse_outputs_section(outputs_content)
                        # Defensive: validate we got some items
                        if not outputs:
                            logger.warning(f"Parsed outputs section for {item_id} but got no items")
                    except Exception as e:
                        logger.warning(f"Failed to parse outputs for {item_id}: {e}")
                        outputs = []
                # Remove outputs section from content (already parsed, don't send to LLM)
                item_content = re.sub(
                    r"(?i)\*\*Outputs in 2025:\*\*\s*\n.*?(?=\n\s*\*\*|\n\s*##|\Z)",
                    "",
                    item_content,
                    flags=re.DOTALL,
                ).strip()
            else:
                outputs = []
            
            # Defensive: warn if content is very short after removing structured fields
            if len(item_content.strip()) < 50:
                logger.warning(
                    f"Content for {item_id} is very short ({len(item_content.strip())} chars) "
                    f"after removing structured fields. May indicate parsing issues."
                )

            agenda_metadata = AgendaMetadata(see_also=see_also, outputs=outputs)

        item = DocumentItem(
            id=item_id,
            name=header_name,
            header_level=header_level,
            parent_id=parent_id,
            content=item_content,
            item_type=item_type,
            agenda_metadata=agenda_metadata,
        )
        items.append(item)

        # Push to stack (both sections and agendas can be parents)
        parent_stack.append((item_id, header_level))

    return ProcessedDocument(source_file=str(file_path), items=items)
