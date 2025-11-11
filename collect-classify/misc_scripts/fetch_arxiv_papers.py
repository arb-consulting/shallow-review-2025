#!/usr/bin/env python3
"""
Fetch arXiv papers from specified authors between Nov 2024 and Nov 2025.
"""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
from typing import List, Set

# arXiv API endpoint
ARXIV_API = "http://export.arxiv.org/api/query"

# Date range: Nov 2024 to Nov 2025
START_DATE = "202411010000"
END_DATE = "202511062359"

def read_authors(filepath: str) -> List[str]:
    """Read author names from file."""
    with open(filepath, 'r') as f:
        authors = [line.strip() for line in f if line.strip()]
    return authors

def format_author_query(author_name: str) -> str:
    """
    Format author name for arXiv query.
    Convert "First Last" to "last" for the au: field.
    """
    parts = author_name.split()
    if len(parts) >= 2:
        # Use last name for search
        return parts[-1].lower().replace(' ', '_')
    return author_name.lower().replace(' ', '_')

def fetch_arxiv_papers(author_name: str) -> List[str]:
    """
    Fetch arXiv papers for a given author within the date range.
    Returns list of abstract URLs.
    """
    author_query = format_author_query(author_name)

    # Build query: author AND date range
    search_query = f"au:{author_query}+AND+submittedDate:[{START_DATE}+TO+{END_DATE}]"

    # Set max results high to get all papers (arXiv default is 10)
    params = {
        'search_query': search_query,
        'start': 0,
        'max_results': 1000  # Should be enough for one author in one year
    }

    url = f"{ARXIV_API}?{urllib.parse.urlencode(params, safe=':+[]')}"

    print(f"Querying for {author_name} ({author_query})...", flush=True)

    try:
        with urllib.request.urlopen(url) as response:
            xml_data = response.read()

        # Parse XML response
        root = ET.fromstring(xml_data)

        # Atom namespace
        ns = {'atom': 'http://www.w3.org/2005/Atom'}

        # Extract abstract URLs from <id> elements in each <entry>
        urls = []
        for entry in root.findall('atom:entry', ns):
            id_elem = entry.find('atom:id', ns)
            if id_elem is not None:
                url = id_elem.text.strip()
                # Convert to https
                url = url.replace('http://', 'https://')
                urls.append(url)

        print(f"  Found {len(urls)} papers for {author_name}", flush=True)
        return urls

    except Exception as e:
        print(f"  Error fetching papers for {author_name}: {e}", flush=True)
        return []

def main():
    """Main function."""
    authors_file = "data/various_sources/even-more-names-from-gavin.txt"

    print(f"Reading authors from {authors_file}...\n")
    authors = read_authors(authors_file)

    print(f"Found {len(authors)} authors")
    print(f"Date range: Nov 2024 to Nov 2025\n")

    all_urls: Set[str] = set()

    for author in authors:
        urls = fetch_arxiv_papers(author)
        all_urls.update(urls)
        # Be nice to arXiv API - rate limit
        time.sleep(3)

    print(f"\n{'='*60}")
    print(f"Total unique papers found: {len(all_urls)}")
    print(f"{'='*60}\n")

    # Sort URLs for consistent output
    sorted_urls = sorted(all_urls)

    for url in sorted_urls:
        print(url)

    # Also save to file
    output_file = "data/arxiv_papers_even_more_gavin_authors.txt"
    with open(output_file, 'w') as f:
        for url in sorted_urls:
            f.write(url + '\n')

    print(f"\nURLs saved to {output_file}")

if __name__ == "__main__":
    main()
