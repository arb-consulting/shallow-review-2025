"""Parser functions for shallow review draft documents.

Handles parsing of markdown documents with [sec:...] sections and [a:...] agendas,
extracting structured metadata and scrubbing content for LLM processing.
"""

import logging
import re
from pathlib import Path

from .draft_types import (
    DocumentItem,
    ItemType,
    OutputSectionHeader,
    Paper,
    PreparsedDocument,
)

logger = logging.getLogger(__name__)


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
    """Extract header name and level from the line containing the marker.

    The marker is at the end of the header line, so we need to search backward
    to find the start of the line, then extract the header from that line.

    Args:
        text: Full document text
        start_pos: Position of the marker (at end of header line)

    Returns:
        Tuple of (header_name, header_level)
    """
    # Find the start of the line containing the marker
    line_start = text.rfind('\n', 0, start_pos) + 1
    # Find the end of the line
    line_end = text.find('\n', start_pos)
    if line_end == -1:
        line_end = len(text)
    
    # Extract the line
    line_text = text[line_start:line_end]
    
    # Match header pattern on this line (allow leading whitespace)
    header_match = re.match(r"^\s*(#+)\s+(.+)$", line_text)
    if header_match:
        header_level = len(header_match.group(1))
        header_name = header_match.group(2).strip()
        # Unescape common Markdown escape sequences
        # Order matters: do \[ and \] first to avoid interference
        header_name = header_name.replace("\\[", "[").replace("\\]", "]")
        header_name = header_name.replace("\\_", "_")
        header_name = header_name.replace("\\*", "*")
        header_name = header_name.replace("\\#", "#")
        return header_name, header_level
    return "", 0


def parse_outputs_section(content: str) -> list[Paper | OutputSectionHeader]:
    """Parse an outputs section into papers and section headers.

    NOTE: This function is deprecated. The LLM now extracts outputs directly from
    the agenda content. This is kept for backward compatibility and testing only.

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

            header = OutputSectionHeader(
                section_name=header_name,
                header_level=header_level,
                original_md=line,
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
            link_url = url_match.group(0) if url_match else None
            
            # Extract link text from markdown [text](url) if present
            link_text = None
            md_link_match = re.match(r"\[([^\]]+)\]\([^)]+\)", paper_text)
            if md_link_match:
                link_text = md_link_match.group(1)

            paper = Paper(link_url=link_url, link_text=link_text, original_md=line)
            items.append(paper)
            i += 1
            continue

        i += 1

    return items


def parse_document(file_path: Path) -> PreparsedDocument:
    """Parse a draft markdown document into flat structure (IDs, names, levels only).

    This performs ONLY structural parsing: extracting IDs, names, header levels, and raw content.
    All metadata extraction (see_also, outputs, attributes) happens in Step 2 via LLM.

    Args:
        file_path: Path to markdown file

    Returns:
        PreparsedDocument with flat list of items (no agenda_attributes populated yet)
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
        # Extract raw content (everything between this marker and the next)
        # Skip the header line containing the current marker
        line_end = text.find('\n', start_pos)
        if line_end == -1:
            content_start = len(text)
        else:
            content_start = line_end + 1  # Start after the newline
        
        # Stop before the line containing the next marker (if any)
        # Find the start of the line containing end_pos
        if end_pos < len(text):
            line_start = text.rfind('\n', 0, end_pos)
            if line_start == -1:
                content_end = end_pos
            else:
                content_end = line_start  # Stop at the newline before next header
        else:
            content_end = end_pos
        
        content = text[content_start:content_end].strip()
        
        # Defensive: Check for empty content
        if not content:
            logger.debug(f"Empty content for {marker_type}:{marker_id}")

        # Extract header name
        header_name, detected_level = extract_header_name(text, start_pos)
        if not header_name:
            # Fallback to marker_id
            header_name = marker_id.replace("_", " ").title()
            logger.warning(
                f"No header found for {marker_type}:{marker_id}, using fallback name: {header_name}"
            )
        else:
            # Remove marker from header name (e.g., "OpenAI Safety [a:openai]" -> "OpenAI Safety")
            # After unescaping above, markers will be in the form [sec:id] or [a:id]
            # Match both forms for robustness (escaped and unescaped)
            header_name = re.sub(r'(?:\\\[|\[)(?:sec|a):[^\]]+?(?:\\\]|\])', '', header_name)
            header_name = header_name.strip()
        
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

        # Store entire content (sans header) - LLM will parse it in Step 2
        item = DocumentItem(
            id=item_id,
            name=header_name,
            header_level=header_level,
            parent_id=parent_id,
            content=content,
            item_type=item_type,
            agenda_attributes=None,  # Will be populated by LLM
        )
        items.append(item)

        # Push to stack (both sections and agendas can be parents)
        parent_stack.append((item_id, header_level))

    return PreparsedDocument(source_file=str(file_path), items=items)
