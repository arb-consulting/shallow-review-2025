#!/usr/bin/env python3
"""
Filter arXiv papers to only those with specified authors.
Fetches paper metadata and checks if any listed author matches.
"""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
import re
import unicodedata
from typing import List, Set
import sys

def normalize_name(name: str) -> str:
    """
    Normalize a name for matching:
    - Remove diacritics
    - Convert to lowercase
    - Remove extra whitespace
    """
    # Decompose unicode characters and remove combining marks (diacritics)
    name = ''.join(
        c for c in unicodedata.normalize('NFD', name)
        if unicodedata.category(c) != 'Mn'
    )
    # Lowercase and normalize whitespace
    name = ' '.join(name.lower().split())
    return name

def extract_name_parts(name: str) -> dict:
    """
    Extract first name, last name, and initials from a full name.
    Returns dict with 'first', 'last', 'first_initial', 'normalized'
    """
    parts = name.strip().split()
    if not parts:
        return {}

    result = {
        'first': parts[0] if len(parts) > 0 else '',
        'last': parts[-1] if len(parts) > 0 else '',
        'first_initial': parts[0][0] if len(parts) > 0 and parts[0] else '',
        'normalized': normalize_name(name),
        'original': name
    }
    return result

def names_match(target_name: str, paper_author: str) -> bool:
    """
    Check if target_name matches paper_author with robust matching.

    Matching strategies (in order of preference):
    1. Full name match (normalized)
    2. Last name + first initial match
    3. Last name match (if target has only last name)
    """
    target = extract_name_parts(target_name)
    author = extract_name_parts(paper_author)

    if not target or not author:
        return False

    # Strategy 1: Full normalized name match
    if target['normalized'] == author['normalized']:
        return True

    # Strategy 2: Last name + first initial (e.g., "A. Liu" matches "Andy Liu")
    target_last_norm = normalize_name(target['last'])
    author_last_norm = normalize_name(author['last'])

    if target_last_norm == author_last_norm:
        # If first names are present, check if initials match
        if target['first'] and author['first']:
            if normalize_name(target['first_initial']) == normalize_name(author['first_initial']):
                return True
        else:
            # If one name has only last name, that's a match
            return True

    return False

def check_if_author_in_list(paper_authors: List[str], target_authors: List[str]) -> tuple:
    """
    Check if any paper author matches any target author.
    Returns (matched: bool, matching_author: str or None)
    """
    for paper_author in paper_authors:
        for target_author in target_authors:
            if names_match(target_author, paper_author):
                return True, target_author
    return False, None

def fetch_paper_metadata(arxiv_id: str) -> dict:
    """
    Fetch metadata for a single arXiv paper.
    Returns dict with 'title', 'authors' (list), 'abstract', 'url'
    """
    # Extract arXiv ID from URL if needed
    if 'arxiv.org' in arxiv_id:
        # Extract ID from URL like https://arxiv.org/abs/2411.00472v1
        match = re.search(r'(\d+\.\d+)(v\d+)?', arxiv_id)
        if match:
            arxiv_id = match.group(1)

    # Query arXiv API by ID
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"

    try:
        with urllib.request.urlopen(url) as response:
            xml_data = response.read()

        root = ET.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}

        entry = root.find('atom:entry', ns)
        if entry is None:
            return None

        # Extract title
        title_elem = entry.find('atom:title', ns)
        title = title_elem.text.strip() if title_elem is not None else ''

        # Extract authors
        authors = []
        for author_elem in entry.findall('atom:author', ns):
            name_elem = author_elem.find('atom:name', ns)
            if name_elem is not None:
                authors.append(name_elem.text.strip())

        # Extract abstract
        summary_elem = entry.find('atom:summary', ns)
        abstract = summary_elem.text.strip() if summary_elem is not None else ''

        # Extract URL
        id_elem = entry.find('atom:id', ns)
        url = id_elem.text.strip() if id_elem is not None else ''

        return {
            'title': title,
            'authors': authors,
            'abstract': abstract,
            'url': url
        }

    except Exception as e:
        print(f"Error fetching {arxiv_id}: {e}", file=sys.stderr)
        return None

def read_lines(filepath: str) -> List[str]:
    """Read non-empty lines from a file."""
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    """Main function."""
    if len(sys.argv) != 3:
        print("Usage: python filter_papers_by_authors.py <urls_file> <names_file>")
        print("Output will be written to <urls_file>-filtered.txt")
        sys.exit(1)

    urls_file = sys.argv[1]
    names_file = sys.argv[2]
    output_file = f"{urls_file.rsplit('.', 1)[0]}-filtered.txt"

    print(f"Reading URLs from: {urls_file}")
    print(f"Reading author names from: {names_file}")
    print(f"Output will be written to: {output_file}\n")

    # Read input files
    urls = read_lines(urls_file)
    target_authors = read_lines(names_file)

    print(f"Found {len(urls)} URLs")
    print(f"Found {len(target_authors)} target authors:")
    for author in target_authors:
        print(f"  - {author}")
    print()

    # Filter papers
    filtered_urls = []
    matched_count = 0

    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] Checking {url}...", end=' ', flush=True)

        # Fetch metadata
        metadata = fetch_paper_metadata(url)

        if metadata is None:
            print("❌ Failed to fetch")
            continue

        # Check if any target author is in the paper's author list
        is_match, matching_author = check_if_author_in_list(metadata['authors'], target_authors)

        if is_match:
            print(f"✓ Match: {matching_author}")
            filtered_urls.append(url)
            matched_count += 1
        else:
            print("✗ No match")

        # Rate limiting - be nice to arXiv API (max 1 request per 3 seconds)
        if i < len(urls):
            time.sleep(3)

    # Write filtered results
    with open(output_file, 'w') as f:
        for url in filtered_urls:
            f.write(url + '\n')

    print(f"\n{'='*60}")
    print(f"Filtered {len(urls)} papers down to {matched_count} papers")
    print(f"Results saved to: {output_file}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
