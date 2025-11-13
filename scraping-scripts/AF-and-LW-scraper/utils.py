import time
import math
import random
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple
from datetime import datetime, timezone

import json as _json
import re

try:
    from typing import TypedDict
except ImportError:  # Python <3.8 fallback
    TypedDict = dict  # type: ignore

try:
    import requests  # lightweight dep, common in most envs
except Exception:  # pragma: no cover
    requests = None  # type: ignore


def sleep_with_jitter(seconds: float) -> None:
    """Sleep for given seconds plus a small random jitter to avoid thundering herds."""
    if seconds <= 0:
        return
    jitter = min(0.25, seconds * 0.1)
    time.sleep(seconds + random.uniform(0, jitter))


def rate_limit_min_interval(min_interval_seconds: float) -> Callable[[], None]:
    """
    Create a simple rate limiter that ensures at least min_interval_seconds between calls.
    Usage:
        limiter = rate_limit_min_interval(0.8)
        # before each network request:
        limiter()
    """
    last_time = 0.0

    def _limit() -> None:
        nonlocal last_time
        now = time.monotonic()
        elapsed = now - last_time
        if elapsed < min_interval_seconds:
            time.sleep(min_interval_seconds - elapsed)
        last_time = time.monotonic()

    return _limit


def http_post_with_retries(
    url: str,
    json: Dict[str, Any],
    headers: Optional[Dict[str, str]] = None,
    timeout: float = 30.0,
    max_retries: int = 5,
    backoff_base_seconds: float = 1.0,
) -> Dict[str, Any]:
    """
    POST JSON with exponential backoff and simple retry policy.
    Returns decoded JSON dict. Raises on final failure.
    """
    if requests is None:
        raise RuntimeError("requests is not available; install it to enable HTTP calls")

    # default headers
    req_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if headers:
        req_headers.update(headers)

    last_exc: Optional[Exception] = None
    last_status: Optional[int] = None
    last_body: Optional[str] = None
    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(url, json=json, headers=req_headers, timeout=timeout)
            status = resp.status_code
            # remember last response details
            last_status = status
            try:
                last_body = resp.text[:2000]
            except Exception:
                last_body = "<unreadable body>"
            if status >= 200 and status < 300:
                return resp.json()
            # Retry on 429/5xx
            if status in (429, 500, 502, 503, 504):
                delay = backoff_base_seconds * (2**attempt)
                sleep_with_jitter(delay)
                continue
            # Non-retryable
            raise RuntimeError(f"HTTP {status} error from {url}: {last_body}")
        except Exception as exc:  # network errors, timeouts, etc.
            last_exc = exc
            delay = backoff_base_seconds * (2**attempt)
            sleep_with_jitter(delay)
    # Exhausted
    if last_exc:
        raise last_exc
    if last_status is not None:
        raise RuntimeError(f"HTTP {last_status} error from {url}: {last_body}")
    raise RuntimeError(
        "http_post_with_retries failed without an exception (unexpected)"
    )


def parse_datetime(dt_str: str) -> Optional[datetime]:
    """
    Parse ISO-ish datetime strings, including 'Z' suffix. Returns timezone-aware UTC datetime if possible.
    """
    if not dt_str:
        return None
    try:
        # Handle common Zulu suffix
        if dt_str.endswith("Z"):
            return datetime.fromisoformat(dt_str.replace("Z", "+00:00")).astimezone(
                timezone.utc
            )
        # Try ISO directly
        dt = datetime.fromisoformat(dt_str)
        # If naive, assume UTC
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        # Fallback: loose regex for yyyy-mm-dd
        m = re.match(r"^(\\d{4})-(\\d{2})-(\\d{2})", dt_str)
        if m:
            try:
                return datetime(
                    int(m.group(1)),
                    int(m.group(2)),
                    int(m.group(3)),
                    tzinfo=timezone.utc,
                )
            except Exception:
                return None
        return None


def clean_markdown(text: Optional[str]) -> str:
    """
    Very small markdown cleaner for excerpts/titles; strips control chars and condenses whitespace.
    """
    if not text:
        return ""
    # Remove control characters
    text = re.sub(r"[\\x00-\\x1f\\x7f]", " ", text)
    # Collapse whitespace
    text = re.sub(r"\\s+", " ", text).strip()
    return text


def dedupe_rows(
    rows: List[Dict[str, Any]], keys: Sequence[str]
) -> List[Dict[str, Any]]:
    """
    Dedupe list of dict rows by a set of key fields (first occurrence wins).
    """
    seen: set = set()
    result: List[Dict[str, Any]] = []
    for row in rows:
        key_tuple = tuple(row.get(k) for k in keys)
        if key_tuple in seen:
            continue
        seen.add(key_tuple)
        result.append(row)
    return result


def pick_latest_by_suffix(candidates: Sequence[str]) -> Optional[str]:
    """
    Given filenames that may include numeric suffixes like '-3', return the path with the highest suffix.
    If none have a numeric suffix, return the last in provided order that exists.
    """
    best_path: Optional[str] = None
    best_num = -1
    for path in candidates:
        m = re.search(r"-(\\d+)\\.[A-Za-z0-9]+$", path)
        num = int(m.group(1)) if m else -1
        if num > best_num:
            best_num = num
            best_path = path
    return best_path
