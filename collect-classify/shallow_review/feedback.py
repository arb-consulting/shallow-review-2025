"""Human feedback import and management for classification decisions."""

import csv
import json
import logging
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .classify import add_classify_candidate
from .common import ClassifyStatus
from .data_db import data_db_locked
from .taxonomy import load_taxonomy
from .utils import normalize_url, url_hash_short

logger = logging.getLogger(__name__)


@dataclass
class FeedbackImportStats:
    """Statistics from importing feedback."""
    
    urls_parsed: int = 0
    urls_skipped: int = 0
    obsolete_csv_categories: int = 0
    added_to_classify: int = 0
    excluded_count: int = 0
    obsolete_llm_count: int = 0
    feedback_inserted: int = 0
    feedback_duplicates: int = 0
    duplicates_list: list[dict[str, str]] = field(default_factory=list)  # List of {url, action, category}
    
    def get_action_counts(self) -> dict[str, int]:
        """Get counts by action type from database."""
        # This will be populated by caller after import
        return {}


def import_feedback_from_csv(
    csv_path: Path,
    source: str,
    detect_exclusions: bool = True,
    min_shallow_review: float = 0.4,
    reclassify_obsolete_llm: bool = False,
) -> FeedbackImportStats:
    """
    Import human feedback from CSV file into classify_feedback table.
    
    Args:
        csv_path: Path to CSV file with columns URL,CATEGORY_ID,PAPER_ID,LINK_TEXT
        source: Feedback source label (e.g., "SR2025-WIP-doc")
        detect_exclusions: Auto-detect papers to exclude (not in CSV but exportable)
        min_shallow_review: Threshold for "exportable" when detecting exclusions
        reclassify_obsolete_llm: ONE-TIME flag - reset papers with obsolete LLM categories
    
    Returns:
        FeedbackImportStats with import statistics
    
    Raises:
        FileNotFoundError: If CSV file doesn't exist
        RuntimeError: If import fails
    """
    stats = FeedbackImportStats()
    timestamp = datetime.now(timezone.utc).isoformat()
    
    # Load taxonomy to validate category IDs
    logger.info("Loading taxonomy to validate category IDs...")
    taxonomy = load_taxonomy()
    valid_leaf_ids = set(taxonomy.get_all_leaf_ids())
    logger.info(f"Loaded {len(valid_leaf_ids)} valid leaf category IDs")
    
    # Read CSV and process feedback
    feedback_entries = []
    csv_urls = set()
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is line 1)
            url = row.get('URL', '').strip()
            if not url:
                stats.urls_skipped += 1
                continue
            
            # Normalize URL
            try:
                url = normalize_url(url)
            except Exception as e:
                logger.warning(f"Could not normalize URL at line {row_num}: {url[:60]} - {e}")
                stats.urls_skipped += 1
                continue
            
            # Track unique URLs (first occurrence)
            is_first_occurrence = url not in csv_urls
            csv_urls.add(url)
            
            if is_first_occurrence:
                stats.urls_parsed += 1
            
            # Get other fields
            category_id = row.get('CATEGORY_ID', '').strip()
            paper_id = row.get('PAPER_ID', '').strip() or None
            link_text = row.get('LINK_TEXT', '').strip() or None
            
            # Process based on category validity
            if category_id:
                # Check if category is valid in current taxonomy
                if category_id not in valid_leaf_ids:
                    # Obsolete category: mark for human review
                    # Only create this on first occurrence (don't duplicate for multi-category cases)
                    if is_first_occurrence:
                        stats.obsolete_csv_categories += 1
                        feedback_entries.append({
                            'url': url,
                            'url_hash_short': url_hash_short(url),
                            'feedback_source': source,
                            'feedback_timestamp': timestamp,
                            'action': 'include',
                            'human_category': None,
                            'paper_id': paper_id,
                            'link_text': link_text,
                            'notes': f'NEEDS_RECATEGORIZATION: obsolete category "{category_id}" from {csv_path.name}'
                        })
                else:
                    # Valid category: create reclassify entry (can have multiple per URL with different categories)
                    feedback_entries.append({
                        'url': url,
                        'url_hash_short': url_hash_short(url),
                        'feedback_source': source,
                        'feedback_timestamp': timestamp,
                        'action': 'reclassify',
                        'human_category': category_id,
                        'paper_id': paper_id,
                        'link_text': link_text,
                        'notes': f'Imported from {csv_path.name}'
                    })
                    # Also add include on first occurrence only
                    if is_first_occurrence:
                        feedback_entries.append({
                            'url': url,
                            'url_hash_short': url_hash_short(url),
                            'feedback_source': source,
                            'feedback_timestamp': timestamp,
                            'action': 'include',
                            'human_category': None,
                            'paper_id': paper_id,
                            'link_text': link_text,
                            'notes': f'Imported from {csv_path.name}'
                        })
            else:
                # No category: just mark as included (probably a lab category with no detailed papers)
                # Only create on first occurrence
                if is_first_occurrence:
                    feedback_entries.append({
                        'url': url,
                        'url_hash_short': url_hash_short(url),
                        'feedback_source': source,
                        'feedback_timestamp': timestamp,
                        'action': 'include',
                        'human_category': None,
                        'paper_id': paper_id,
                        'link_text': link_text,
                        'notes': f'Imported from {csv_path.name} (no category assigned)'
                    })
    
    # Add URLs to classify table if not already present
    logger.info("Checking which URLs need to be added to classify table...")
    
    # First, check which URLs are missing (inside lock)
    urls_to_add = []
    with data_db_locked() as db:
        for url in csv_urls:
            cursor = db.execute("SELECT url FROM classify WHERE url = ?", (url,))
            if not cursor.fetchone():
                urls_to_add.append(url)
    
    # Then add them (outside lock, as add_classify_candidate acquires its own lock)
    for url in urls_to_add:
        try:
            is_new = add_classify_candidate(
                url=url,
                source=f"feedback-{source}",
                source_url=None,
                collect_relevancy=None
            )
            if is_new:
                stats.added_to_classify += 1
        except Exception as e:
            logger.warning(f"Could not add {url[:60]} to classify: {e}")
    
    # Detect exclusions (exportable items NOT in CSV)
    excluded_entries = []
    reclassify_obsolete_entries = []
    
    if detect_exclusions:
        logger.info("Detecting excluded papers...")
        
        with data_db_locked() as db:
            # Get all exportable URLs with their LLM-assigned categories
            cursor = db.execute(
                """
                SELECT url, url_hash_short, data
                FROM classify
                WHERE status = 'done'
                  AND shallow_review_inclusion >= ?
                  AND ai_safety_relevance >= 0.1
                """,
                (min_shallow_review,)
            )
            exportable_rows = cursor.fetchall()
        
        # Find URLs that are exportable but not in CSV
        exportable_urls = {row['url']: row for row in exportable_rows}
        excluded_urls = set(exportable_urls.keys()) - csv_urls
        
        # Process excluded URLs
        for url in excluded_urls:
            row = exportable_urls[url]
            
            # Check if this URL has an obsolete LLM category (one-time migration behavior)
            has_obsolete_llm_category = False
            if reclassify_obsolete_llm and row['data']:
                try:
                    data = json.loads(row['data'])
                    categories = data.get('categories', [])
                    if categories:
                        llm_category_id = categories[0]['id']
                        if llm_category_id not in valid_leaf_ids:
                            has_obsolete_llm_category = True
                except (json.JSONDecodeError, KeyError, IndexError):
                    raise
            
            if has_obsolete_llm_category:
                # Special case: LLM put it in a now-deleted category
                # Use 'note' action: tracks the situation but doesn't force inclusion/exclusion
                reclassify_obsolete_entries.append({
                    'url': url,
                    'url_hash_short': row['url_hash_short'],
                    'feedback_source': source,
                    'feedback_timestamp': timestamp,
                    'action': 'note',
                    'human_category': None,
                    'paper_id': None,
                    'link_text': None,
                    'notes': f'RECLASSIFY_OBSOLETE_LLM: LLM category "{llm_category_id}" no longer exists, re-classified with current taxonomy'
                })
            else:
                # Normal case: exclude because not in CSV
                excluded_entries.append({
                    'url': url,
                    'url_hash_short': row['url_hash_short'],
                    'feedback_source': source,
                    'feedback_timestamp': timestamp,
                    'action': 'exclude',
                    'human_category': None,
                    'paper_id': None,
                    'link_text': None,
                    'notes': f'Excluded: was exportable (sr>={min_shallow_review}) but not in {csv_path.name}'
                })
        
        stats.excluded_count = len(excluded_entries)
        stats.obsolete_llm_count = len(reclassify_obsolete_entries)
        
        # Reset status to 'new' for papers with obsolete LLM categories
        if reclassify_obsolete_entries:
            logger.info("Resetting papers with obsolete LLM categories to status='new'...")
            with data_db_locked() as db:
                for entry in reclassify_obsolete_entries:
                    db.execute(
                        "UPDATE classify SET status = ? WHERE url = ?",
                        (ClassifyStatus.NEW.value, entry['url'])
                    )
    
    # Insert all feedback into database
    logger.info("Inserting feedback entries...")
    duplicates_list = []
    
    with data_db_locked() as db:
        for entry in feedback_entries + excluded_entries + reclassify_obsolete_entries:
            try:
                db.execute(
                    """
                    INSERT INTO classify_feedback 
                    (url, url_hash_short, feedback_source, feedback_timestamp, action, human_category, paper_id, link_text, notes)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        entry['url'],
                        entry['url_hash_short'],
                        entry['feedback_source'],
                        entry['feedback_timestamp'],
                        entry['action'],
                        entry['human_category'],
                        entry['paper_id'],
                        entry['link_text'],
                        entry['notes']
                    )
                )
                stats.feedback_inserted += 1
            except sqlite3.IntegrityError:
                # Duplicate entry caught by unique indexes
                # - For include/exclude/note: same url+source+action+timestamp
                # - For reclassify: same url+source+action+human_category+timestamp
                stats.feedback_duplicates += 1
                
                # Record duplicate for reporting
                dup_info = {
                    'url': entry['url'],
                    'action': entry['action'],
                    'category': entry.get('human_category'),
                }
                duplicates_list.append(dup_info)
                
                logger.debug(
                    f"Duplicate feedback: url={entry['url'][:60]}, "
                    f"action={entry['action']}, category={entry.get('human_category')}"
                )
    
    # Store duplicates in stats
    stats.duplicates_list = duplicates_list
    
    logger.info(f"Feedback import complete: {stats.feedback_inserted} inserted, {stats.feedback_duplicates} duplicates")
    
    return stats


def get_action_counts(source: str) -> dict[str, int]:
    """
    Get count of feedback entries by action type for a given source.
    
    Args:
        source: Feedback source to query
    
    Returns:
        Dictionary mapping action -> count
    """
    with data_db_locked() as db:
        cursor = db.execute(
            """
            SELECT action, COUNT(*) as count
            FROM classify_feedback
            WHERE feedback_source = ?
            GROUP BY action
            """,
            (source,)
        )
        return {row['action']: row['count'] for row in cursor.fetchall()}

