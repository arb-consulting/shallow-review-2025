import argparse
import csv
import logging
import os
import time
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
import re
import requests
from urllib.parse import urlparse
import random
import calendar

POSTS_QUERY_BY_YEAR = """
query AFPostsByYear($after: String!, $before: String!, $limit: Int!, $offset: Int!) {
  posts(input: {
    terms: {
      view: "new"
      limit: $limit
      offset: $offset
      after: $after
      before: $before
    }
  }) {
    results {
      _id
      title
      pageUrl
      baseScore
      commentCount
      postedAt
    }
  }
}
"""


def parse_datetime(dt_str: Optional[str]) -> Optional[datetime]:
    if not dt_str:
        return None
    try:
        if dt_str.endswith("Z"):
            return datetime.fromisoformat(dt_str.replace("Z", "+00:00")).astimezone(
                timezone.utc
            )
        dt = datetime.fromisoformat(dt_str)
        return (
            dt.astimezone(timezone.utc)
            if dt.tzinfo
            else dt.replace(tzinfo=timezone.utc)
        )
    except ValueError:
        m = re.match(r"^(\\d{4})-(\\d{2})-(\\d{2})", dt_str)
        if m:
            try:
                return datetime(
                    int(m.group(1)),
                    int(m.group(2)),
                    int(m.group(3)),
                    tzinfo=timezone.utc,
                )
            except (TypeError, ValueError):
                return None
        return None


def http_post_with_retries(
    url: str,
    json: Dict[str, Any],
    timeout: float = 30.0,
    max_retries: int = 6,
    backoff_base_seconds: float = 2.0,
) -> Dict[str, Any]:
    last_exc: Optional[Exception] = None
    last_status: Optional[int] = None
    last_body: Optional[str] = None
    # Minimal browser-like headers derived from target URL
    parsed = urlparse(url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    referer = origin + "/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        ),
        "Origin": origin,
        "Referer": referer,
        "Connection": "keep-alive",
    }
    # Optional: pass a session cookie if provided in environment
    cookie_env = os.environ.get("AF_LW_COOKIE")
    if cookie_env:
        headers["Cookie"] = cookie_env
    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(url, json=json, headers=headers, timeout=timeout)
            last_status = resp.status_code
            last_body = (resp.text or "")[:2000]
            if 200 <= last_status < 300:
                return resp.json()
            if last_status in (429, 500, 502, 503, 504):
                # Exponential backoff with small jitter; extra wait on 429
                base = backoff_base_seconds * (2**attempt)
                if last_status == 429:
                    base += 2.0
                time.sleep(base + random.uniform(0, 0.25))
                continue
            raise RuntimeError(f"HTTP {last_status} error from {url}: {last_body}")
        except requests.RequestException as exc:
            last_exc = exc
            time.sleep(backoff_base_seconds * (2**attempt) + random.uniform(0, 0.25))
    if last_exc:
        raise last_exc
    if last_status is not None:
        raise RuntimeError(f"HTTP {last_status} error from {url}: {last_body}")
    raise RuntimeError("Request failed without an exception (unexpected)")


def fetch_posts_page(endpoint: str, variables: Dict[str, Any]) -> Dict[str, Any]:
    body = {"query": POSTS_QUERY_BY_YEAR, "variables": variables}
    return http_post_with_retries(endpoint, json=body)


def scrape_posts(
    year: int, endpoint: str, delay_seconds: float, max_pages: int
) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    seen_ids: set = set()
    limit = 50
    total_pages = 0

    # Iterate month windows (Dec -> Jan) to avoid large offset caps
    for month in range(12, 1 - 1, -1):
        last_day = calendar.monthrange(year, month)[1]
        after = f"{year}-{month:02d}-01T00:00:00Z"
        before = f"{year}-{month:02d}-{last_day:02d}T23:59:59Z"
        logging.info("Window %s → %s", after[:10], before[:10])
        offset = 0
        while True:
            if total_pages >= max_pages:
                logging.info("Reached max-pages limit (%s); stopping.", max_pages)
                return results
            variables = {
                "after": after,
                "before": before,
                "limit": limit,
                "offset": offset,
            }
            logging.info(
                "Requesting page %s (limit=%s, offset=%s)", total_pages + 1, limit, offset
            )
            data = fetch_posts_page(endpoint, variables)
            posts = (data.get("data") or {}).get("posts") or {}
            items = posts.get("results") or []
            logging.info("Fetched %s items", len(items))
            total_pages += 1
            if not items:
                break
            for it in items:
                post_id = it.get("_id")
                if post_id in seen_ids:
                    continue
                seen_ids.add(post_id)
                created_at = it.get("postedAt") or it.get("createdAt")
                created_dt = parse_datetime(created_at) if created_at else None
                results.append(
                    {
                        "id": post_id,
                        "title": it.get("title") or "",
                        "url": it.get("pageUrl") or it.get("url"),
                        "pageUrl": it.get("pageUrl") or it.get("url"),
                        "author": "",
                        "createdAt": created_dt.isoformat()
                        if created_dt
                        else (created_at or ""),
                        "score": it.get("baseScore") if "baseScore" in it else "",
                        "commentCount": it.get("commentCount") if "commentCount" in it else "",
                        "wordCount": "",
                        "tags": "",
                        "excerpt": "",
                    }
                )
            offset += limit
            if delay_seconds > 0:
                time.sleep(delay_seconds)
    return results


def write_csv(path: str, rows: List[Dict[str, Any]]) -> None:
    fields = [
        "id",
        "title",
        "url",
        "pageUrl",
        "author",
        "createdAt",
        "score",
        "commentCount",
        "wordCount",
        "tags",
        "excerpt",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k, "") for k in fields})


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape AF/LessWrong posts into CSV.")
    parser.add_argument(
        "--site", choices=["alignment-forum", "lesswrong"], default="alignment-forum"
    )
    parser.add_argument("--year", type=int, default=2025)
    parser.add_argument("--max-pages", type=int, default=200)
    parser.add_argument("--delay", type=float, default=1.0)
    parser.add_argument("--out", type=str, default="results/1-af_raw_posts.csv")
    args = parser.parse_args()

    endpoint = (
        "https://www.lesswrong.com/graphql"
        if args.site == "lesswrong"
        else "https://www.alignmentforum.org/graphql"
    )
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    logging.info(
        "Starting scrape: site=%s endpoint=%s year=%s", args.site, endpoint, args.year
    )

    rows = scrape_posts(
        year=args.year,
        endpoint=endpoint,
        delay_seconds=args.delay,
        max_pages=args.max_pages,
    )
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    write_csv(args.out, rows)
    logging.info("Wrote %s rows to %s", len(rows), args.out)


if __name__ == "__main__":
    main()
