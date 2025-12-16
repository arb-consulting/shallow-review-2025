#!/usr/bin/env python3
"""Add LaTeX-style tags to markdown headers."""

import re
from pathlib import Path


def make_tag(header_text: str) -> str:
    """Convert header text to a tag format.
    
    Strip, preserve case, replace spaces and non-alnum with underscores.
    """
    # Strip whitespace
    text = header_text.strip()
    # Replace non-alphanumeric with underscores
    text = re.sub(r'[^a-zA-Z0-9]+', '_', text)
    # Remove only leading underscores
    text = text.lstrip('_')
    return text


def process_line(line: str) -> str:
    """Process a single line, adding or updating tags to headers."""
    # Match headers: capture the hashes, spaces, and the header text (with optional existing tag)
    match = re.match(r'^(#{1,3})\s+(.+?)(\s*\\?\[(?:sec|a):[^\]]+\])?\s*$', line)
    
    if not match:
        return line
    
    hashes, header_text, existing_tag = match.groups()
    
    # Determine tag type based on header level
    level = len(hashes)
    if level <= 2:  # # or ##
        tag_type = 'sec'
    else:  # ###
        tag_type = 'a'
    
    # Create the tag (preserving case)
    tag_name = make_tag(header_text)
    tag = f' \\[{tag_type}:{tag_name}\\]'
    
    # Always update/replace the tag to ensure case is correct
    return f'{hashes} {header_text}{tag}\n'


def main():
    """Process the markdown file."""
    input_file = Path('/home/dev/proj/shallow-review/main-pipeline/data/2025-12-16-draft-post-review/source.md')
    
    # Read the file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Process each line
    processed_lines = [process_line(line) for line in lines]
    
    # Write back to the file
    with open(input_file, 'w', encoding='utf-8') as f:
        f.writelines(processed_lines)
    
    print(f'✓ Processed {input_file}')
    print(f'  Total lines: {len(lines)}')
    print(f'  Headers modified: {sum(1 for old, new in zip(lines, processed_lines) if old != new)}')


if __name__ == '__main__':
    main()

