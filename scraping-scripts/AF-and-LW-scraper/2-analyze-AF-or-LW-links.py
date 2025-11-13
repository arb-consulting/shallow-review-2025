import argparse
import csv
import os
from typing import Any, Dict, List, Optional, Sequence, Tuple

from utils import dedupe_rows, parse_datetime

KEYWORDS_DEFAULT: Sequence[str] = (
    "alignment",
    "safety",
    "evals",
    "interpretability",
    "red teaming",
    "governance",
    "oversight",
    "robustness",
    "deception",
    "capabilities",
    "inner alignment",
    "outer alignment",
    "rlhf",
    "scaling",
    "specification",
)


def read_csv_rows(path: str) -> List[Dict[str, Any]]:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]


def write_csv(path: str, rows: List[Dict[str, Any]], fields: Sequence[str]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(fields))
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k, "") for k in fields})


def simple_relevance(row: Dict[str, Any], keywords: Sequence[str]) -> bool:
    title = (row.get("title") or "").lower()
    excerpt = (row.get("excerpt") or "").lower()
    tags = (row.get("tags") or "").lower()
    text = " ".join([title, excerpt, tags])
    return any(kw.lower() in text for kw in keywords)


def filter_and_curate(
    rows: List[Dict[str, Any]],
    year: int,
    keywords: Sequence[str],
    max_items: Optional[int],
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    # Normalize/clean
    norm: List[Dict[str, Any]] = []
    for r in rows:
        created = r.get("createdAt") or ""
        created_dt = parse_datetime(created)
        if created_dt and created_dt.year != year:
            continue
        norm.append(
            {
                "id": r.get("id") or r.get("_id"),
                "title": r.get("title") or "",
                "url": r.get("url") or r.get("pageUrl"),
                "pageUrl": r.get("pageUrl") or r.get("url"),
                "author": r.get("author") or r.get("user") or "",
                "createdAt": created_dt.isoformat() if created_dt else created,
                "score": r.get("score") or r.get("baseScore") or "",
                "commentCount": r.get("commentCount") or "",
                "wordCount": r.get("wordCount") or "",
                "tags": r.get("tags") or "",
                "excerpt": r.get("excerpt") or "",
            }
        )

    # Dedupe by URL/title
    norm = dedupe_rows(norm, keys=("url", "title"))

    # Filter by keywords
    filtered = [r for r in norm if simple_relevance(r, keywords)]

    # Curate a smaller subset by score/commentCount heuristics
    def score_value(x: Any) -> float:
        try:
            return float(x)
        except (TypeError, ValueError):
            return 0.0

    sorted_filtered = sorted(
        filtered,
        key=lambda r: (score_value(r.get("score")), score_value(r.get("commentCount"))),
        reverse=True,
    )
    curated = sorted_filtered[:max_items] if max_items else sorted_filtered

    return filtered, curated


def write_markdown_summary(path: str, rows: Sequence[Dict[str, Any]]) -> None:
    lines: List[str] = []
    for r in rows:
        title = r.get("title") or "(untitled)"
        url = r.get("url") or r.get("pageUrl") or ""
        author = r.get("author") or ""
        date = (r.get("createdAt") or "")[:10]
        excerpt = r.get("excerpt") or ""
        lines.append(f"- [{title}]({url}) — {author} — {date}\n  - {excerpt}")
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Filter, dedupe, and curate AF posts CSV."
    )
    parser.add_argument(
        "--in", dest="inp", type=str, default="results/1-af_raw_posts.csv"
    )
    parser.add_argument("--out-dir", type=str, default="results")
    parser.add_argument("--year", type=int, default=2025)
    parser.add_argument(
        "--keywords", type=str, nargs="*", default=list(KEYWORDS_DEFAULT)
    )
    parser.add_argument("--curated-max", type=int, default=200)
    parser.add_argument(
        "--summarize", action="store_true", help="Reserved flag; summaries optional"
    )
    parser.add_argument(
        "--site",
        type=str,
        choices=["alignment-forum", "lesswrong"],
        default=None,
        help="Output filename prefix: 'af' or 'lw'. If omitted, auto-detects from input basename ('1-lw_...').",
    )
    args = parser.parse_args()

    in_path = args.inp
    out_dir = args.out_dir
    os.makedirs(out_dir, exist_ok=True)

    # Determine output prefix: 'af' | 'lw'
    input_base = os.path.basename(in_path)
    if args.site == "lesswrong" or (
        args.site is None and input_base.startswith("1-lw_")
    ):
        prefix = "lw"
    else:
        prefix = "af"

    rows = read_csv_rows(in_path)
    filtered, curated = filter_and_curate(
        rows, year=args.year, keywords=args.keywords, max_items=args.curated_max
    )

    write_csv(
        os.path.join(out_dir, f"2-{prefix}_filtered_posts.csv"),
        filtered,
        fields=list(filtered[0].keys())
        if filtered
        else [
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
        ],
    )
    write_csv(
        os.path.join(out_dir, f"4-{prefix}_curated.csv"),
        curated,
        fields=list(curated[0].keys())
        if curated
        else [
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
        ],
    )
    write_markdown_summary(
        os.path.join(out_dir, f"3-{prefix}_summaries_and_tags.md"), curated
    )

    # Also emit a simple CSV for summaries/tags even if we didn't generate LLM summaries
    write_csv(
        os.path.join(out_dir, f"3-{prefix}_summaries_and_tags.csv"),
        [
            {
                "url": r.get("url"),
                "title": r.get("title"),
                "tags": r.get("tags") or "",
                "summary": r.get("excerpt") or "",
            }
            for r in curated
        ],
        fields=("url", "title", "tags", "summary"),
    )

    print(
        f"Wrote {len(filtered)} filtered rows and {len(curated)} curated rows to {out_dir}"
    )


if __name__ == "__main__":
    main()
