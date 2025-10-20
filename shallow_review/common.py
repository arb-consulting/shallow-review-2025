"""Shared types, constants, and global state for shallow-review pipeline."""

import threading
from pathlib import Path

from pydantic import BaseModel

# Paths - derived from package location, independent of pwd
ROOT_PATH = Path(__file__).parent.parent.resolve()
DATA_PATH = ROOT_PATH / "data"
PROMPTS_PATH = ROOT_PATH / "prompts"
RUNS_PATH = ROOT_PATH / "runs"

# Ensure directories exist
DATA_PATH.mkdir(exist_ok=True, parents=True)
RUNS_PATH.mkdir(exist_ok=True, parents=True)

# Global shutdown flag for graceful termination
_shutdown_event = threading.Event()


def is_shutdown_requested() -> bool:
    """Check if shutdown has been requested."""
    return _shutdown_event.is_set()


def request_shutdown() -> None:
    """Request shutdown of all threads."""
    _shutdown_event.set()


# Common base models (extend as needed)
class Item(BaseModel):
    """Base item type for pipeline objects."""

    id: str
    url: str


