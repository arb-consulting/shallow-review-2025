"""Shared types, constants, and global state for shallow-review pipeline."""

import threading
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, Field

# Paths - derived from package location, independent of pwd
ROOT_PATH = Path(__file__).parent.parent.resolve()
DATA_PATH = ROOT_PATH / "data"
PROMPTS_PATH = ROOT_PATH / "prompts"
RUNS_PATH = ROOT_PATH / "runs"
SCRAPED_PATH = DATA_PATH / "scraped"

# Ensure directories exist
DATA_PATH.mkdir(exist_ok=True, parents=True)
RUNS_PATH.mkdir(exist_ok=True, parents=True)
SCRAPED_PATH.mkdir(exist_ok=True, parents=True)

# Global shutdown flag for graceful termination
_shutdown_event = threading.Event()


def is_shutdown_requested() -> bool:
    """Check if shutdown has been requested."""
    return _shutdown_event.is_set()


def request_shutdown() -> None:
    """Request shutdown of all threads."""
    _shutdown_event.set()


# Enums
class SourceKind(str, Enum):
    """Types of collection sources."""

    CONFERENCE = "conference"
    NEWSLETTER = "newsletter"
    BLOG_AGGREGATOR = "blog_aggregator"
    RESOURCE_LIST = "resource_list"
    WORKSHOP = "workshop"
    SUMMER_SCHOOL = "summer_school"
    READING_LIST = "reading_list"
    ORGANIZATION_PAGE = "organization_page"
    PAPER_PAGE = "paper_page"  # Individual paper (no links to collect)
    BLOCKED_CONTENT = "blocked_content"  # Captcha, login wall, etc.
    OTHER = "other"


class CollectStatus(str, Enum):
    """Status of collection source processing."""

    NEW = "new"  # Not yet processed
    SCRAPE_ERROR = "scrape_error"  # Failed to scrape
    EXTRACT_ERROR = "extract_error"  # LLM extraction failed
    DONE = "done"  # Successfully completed


class ClassifyStatus(str, Enum):
    """Status of classification candidate processing."""

    NEW = "new"  # Not yet processed
    SCRAPE_ERROR = "scrape_error"  # Failed to scrape
    CLASSIFY_ERROR = "classify_error"  # LLM classification failed
    DONE = "done"  # Successfully completed


class ClassifyKind(str, Enum):
    """Content type classification (independent of AI safety/alignment relevancy).
    
    Note: All kinds can have any relevancy and inclusion scores. For example,
    a paper can have high safety relevance (0.9) but low inclusion (0.1) if not technical,
    or high relevance (0.9) and high inclusion (0.9) if presenting novel safety research.
    Use ai_safety_relevance and shallow_review_inclusion fields to determine scores.
    """

    # Research outputs
    PAPER_PUBLISHED = "paper_published"  # Peer-reviewed paper in journal/conference
    PAPER_PREPRINT = "paper_preprint"  # Preprint (arXiv, SSRN, etc.)
    BLOG_POST = "blog_post"  # Blog post or article (general blogs, personal blogs)
    LESSWRONG = "lesswrong"  # LessWrong or AI Alignment Forum post (special category)
    VIDEO = "video"  # Video, talk recording, lecture
    PODCAST = "podcast"  # Podcast episode or audio content
    CODE_TOOL = "code_tool"  # Software, library, tool, implementation
    DATASET_BENCHMARK = "dataset_benchmark"  # Dataset or benchmark release
    AGENDA_MANIFESTO = "agenda_manifesto"  # Research agenda, roadmap, manifesto
    NEWS_ANNOUNCEMENT = "news_announcement"  # News article or official announcement
    SOCIAL_MEDIA = "social_media"  # Social media post (strict criteria: major announcements only)
    COURSE_EDUCATIONAL = "course_educational"  # Course materials, tutorials, educational content
    # Non-research content
    COMMERCIAL = "commercial"  # Product/service pages, company pages
    PERSONAL_PAGE = "personal_page"  # Personal homepages, bios
    # Access issues
    BLOCKED = "blocked"  # Blocked access (captcha, login wall, paywall - content exists but inaccessible)
    ERROR_DETECTED = "error_detected"  # Content could not be accessed (429, 404, 5xx, format errors, etc.)
    OTHER = "other"  # Other content type


# Configuration objects
class RunCollectConfig(BaseModel):
    """Configuration for collect phase runs."""

    model_config = {"frozen": True}

    limit: int = Field(default=100, ge=1, description="Max sources to process")
    workers: int = Field(default=4, ge=1, le=128, description="Number of worker threads")
    relevancy_threshold: float = Field(
        default=0.3, ge=0.0, le=1.0, description="Minimum relevancy to extract links"
    )
    model: str = Field(default="claude-sonnet-4", description="LLM model to use")
    max_html_tokens: int = Field(
        default=100000, ge=1000, description="Max tokens in HTML before error"
    )


class RunClassifyConfig(BaseModel):
    """Configuration for classify phase runs."""

    model_config = {"frozen": True}

    limit: int = Field(default=100, ge=1, description="Max candidates to process")
    workers: int = Field(default=4, ge=1, le=128, description="Number of worker threads")
    min_relevancy: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Minimum collect_relevancy to process (filter)",
    )
    model: str = Field(default="claude-sonnet-4", description="LLM model to use")
    max_html_tokens: int = Field(
        default=100000, ge=1000, description="Max tokens in HTML before error"
    )


# Common base models (extend as needed)
class Item(BaseModel):
    """Base item type for pipeline objects."""

    id: str
    url: str


