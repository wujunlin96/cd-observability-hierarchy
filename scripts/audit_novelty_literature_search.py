"""Run a reproducible novelty-neighbor literature search.

The goal is not to prove priority. It is to find obvious collisions with the
current C-D observability framing and to document which neighboring literatures
already cover parts of the construction.
"""

from __future__ import annotations

import csv
import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_CSV = ROOT / "results" / "novelty_literature_search.csv"
OUT_JSON = ROOT / "results" / "novelty_literature_search.json"


QUERIES = [
    {
        "label": "exact_title_collision",
        "text": '"C-D Observability Hierarchy" "Multi-Sector Speed Constants"',
        "purpose": "direct collision with the current title/framing",
    },
    {
        "label": "observability_hidden_speed",
        "text": '"hidden sector" "speed of light" observability Lorentz',
        "purpose": "papers treating hidden speed constants as observables",
    },
    {
        "label": "multi_sector_limiting_speed",
        "text": '"different limiting speeds" sectors Lorentz',
        "purpose": "multi-speed sector and Lorentz-violation overlap",
    },
    {
        "label": "relative_calibration_holonomy",
        "text": '"relative calibration" holonomy Lorentz sector',
        "purpose": "relative-sector calibration or holonomy collision",
    },
    {
        "label": "hidden_cone_portal",
        "text": '"hidden sector" "different speed" portal Lorentz',
        "purpose": "portal models with hidden cone mismatch",
    },
    {
        "label": "interface_echo_speed",
        "text": '"interface" "different speed" hidden sector echo',
        "purpose": "defect/interface conversion or echo overlap",
    },
    {
        "label": "disformal_lorentz_hidden",
        "text": 'disformal "Lorentz violation" "hidden sector"',
        "purpose": "disformal/aether boundary",
    },
    {
        "label": "neutrino_altered_dispersion",
        "text": '"altered dispersion" sterile neutrino Lorentz',
        "purpose": "neutrino/ADR boundary for portal escape routes",
    },
]


def get_url(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "CDNoveltyAudit/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def arxiv_query(text: str, max_results: int = 8) -> list[dict[str, str]]:
    # arXiv supports quoted phrases in all: queries. Spaces are encoded by urlencode.
    query = f"all:{text}"
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "relevance",
            "sortOrder": "descending",
        }
    )
    url = "https://export.arxiv.org/api/query?" + params
    xml = get_url(url)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml)
    rows: list[dict[str, str]] = []
    for entry in root.findall("atom:entry", ns):
        title = " ".join((entry.findtext("atom:title", default="", namespaces=ns)).split())
        summary = " ".join((entry.findtext("atom:summary", default="", namespaces=ns)).split())
        arxiv_id = entry.findtext("atom:id", default="", namespaces=ns).rsplit("/", 1)[-1]
        published = entry.findtext("atom:published", default="", namespaces=ns)[:10]
        authors = [
            author.findtext("atom:name", default="", namespaces=ns)
            for author in entry.findall("atom:author", ns)
        ]
        rows.append(
            {
                "database": "arxiv",
                "id": arxiv_id,
                "title": title,
                "year": published[:4],
                "published": published,
                "authors": "; ".join(authors[:6]),
                "venue": "arXiv",
                "url": f"https://arxiv.org/abs/{arxiv_id}",
                "abstract": summary,
            }
        )
    return rows


def semantic_scholar_query(text: str, max_results: int = 8) -> list[dict[str, str]]:
    params = urllib.parse.urlencode(
        {
            "query": text,
            "limit": max_results,
            "fields": "title,year,authors,abstract,venue,url,externalIds,citationCount",
        }
    )
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + params
    try:
        data = json.loads(get_url(url))
    except Exception as exc:  # network throttling should not kill the audit
        return [
            {
                "database": "semantic_scholar",
                "id": "ERROR",
                "title": f"Semantic Scholar query failed: {exc}",
                "year": "",
                "published": "",
                "authors": "",
                "venue": "",
                "url": "",
                "abstract": "",
            }
        ]
    rows: list[dict[str, str]] = []
    for item in data.get("data", []):
        authors = [a.get("name", "") for a in item.get("authors", [])]
        ext = item.get("externalIds") or {}
        paper_id = ext.get("ArXiv") or ext.get("DOI") or item.get("paperId", "")
        rows.append(
            {
                "database": "semantic_scholar",
                "id": paper_id,
                "title": item.get("title", ""),
                "year": str(item.get("year") or ""),
                "published": str(item.get("year") or ""),
                "authors": "; ".join(authors[:6]),
                "venue": item.get("venue", ""),
                "url": item.get("url", ""),
                "abstract": item.get("abstract") or "",
                "citation_count": str(item.get("citationCount") or 0),
            }
        )
    return rows


def crossref_query(text: str, max_results: int = 8) -> list[dict[str, str]]:
    params = urllib.parse.urlencode({"query.bibliographic": text, "rows": max_results})
    url = "https://api.crossref.org/works?" + params
    try:
        data = json.loads(get_url(url))
    except Exception as exc:
        return [
            {
                "database": "crossref",
                "id": "ERROR",
                "title": f"Crossref query failed: {exc}",
                "year": "",
                "published": "",
                "authors": "",
                "venue": "",
                "url": "",
                "abstract": "",
            }
        ]
    rows: list[dict[str, str]] = []
    for item in data.get("message", {}).get("items", []):
        title = " ".join((item.get("title") or [""])[0].split())
        container = " ".join((item.get("container-title") or [""])[0].split())
        author_names = []
        for author in item.get("author", [])[:6]:
            given = author.get("given", "")
            family = author.get("family", "")
            author_names.append(" ".join(x for x in [given, family] if x))
        year = ""
        date_parts = (item.get("published-print") or item.get("published-online") or item.get("issued") or {}).get("date-parts") or []
        if date_parts and date_parts[0]:
            year = str(date_parts[0][0])
        doi = item.get("DOI", "")
        rows.append(
            {
                "database": "crossref",
                "id": doi,
                "title": title,
                "year": year,
                "published": year,
                "authors": "; ".join(author_names),
                "venue": container,
                "url": "https://doi.org/" + doi if doi else item.get("URL", ""),
                "abstract": item.get("abstract", ""),
                "citation_count": "",
            }
        )
    return rows


def openalex_query(text: str, max_results: int = 8) -> list[dict[str, str]]:
    params = urllib.parse.urlencode({"search": text, "per-page": max_results})
    url = "https://api.openalex.org/works?" + params
    try:
        data = json.loads(get_url(url))
    except Exception as exc:
        return [
            {
                "database": "openalex",
                "id": "ERROR",
                "title": f"OpenAlex query failed: {exc}",
                "year": "",
                "published": "",
                "authors": "",
                "venue": "",
                "url": "",
                "abstract": "",
            }
        ]
    rows: list[dict[str, str]] = []
    for item in data.get("results", []):
        authors = [
            auth.get("author", {}).get("display_name", "")
            for auth in item.get("authorships", [])[:6]
        ]
        primary = item.get("primary_location") or {}
        source = primary.get("source") or {}
        doi = (item.get("doi") or "").replace("https://doi.org/", "")
        rows.append(
            {
                "database": "openalex",
                "id": doi or item.get("id", ""),
                "title": item.get("title", "") or item.get("display_name", ""),
                "year": str(item.get("publication_year") or ""),
                "published": str(item.get("publication_date") or item.get("publication_year") or ""),
                "authors": "; ".join(authors),
                "venue": source.get("display_name", ""),
                "url": item.get("doi") or item.get("id", ""),
                "abstract": "",
                "citation_count": str(item.get("cited_by_count") or 0),
            }
        )
    return rows


def collision_score(record: dict[str, str]) -> tuple[str, str]:
    text = (record.get("title", "") + " " + record.get("abstract", "")).lower()
    score = 0
    reasons: list[str] = []
    for term in ["observability", "hidden sector", "limiting speed", "speed of light", "lorentz"]:
        if term in text:
            score += 1
            reasons.append(term)
    if "calibration" in text or "holonomy" in text:
        score += 2
        reasons.append("calibration/holonomy")
    if "interface" in text or "defect" in text or "echo" in text:
        score += 1
        reasons.append("interface/defect/echo")
    if "standard-model extension" in text or "sme" in text:
        score += 1
        reasons.append("SME")
    if score >= 5:
        level = "high"
    elif score >= 3:
        level = "medium"
    elif score >= 1:
        level = "low"
    else:
        level = "none"
    return level, "; ".join(reasons)


def main() -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    all_rows: list[dict[str, str]] = []
    run_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for item in QUERIES:
        query_rows = []
        query_rows.extend(arxiv_query(item["text"]))
        time.sleep(1.0)
        query_rows.extend(openalex_query(item["text"]))
        time.sleep(1.0)
        query_rows.extend(crossref_query(item["text"]))
        time.sleep(1.0)
        query_rows.extend(semantic_scholar_query(item["text"]))
        time.sleep(1.0)
        for record in query_rows:
            level, reasons = collision_score(record)
            all_rows.append(
                {
                    "run_at_utc": run_at,
                    "query_label": item["label"],
                    "query_text": item["text"],
                    "query_purpose": item["purpose"],
                    "database": record.get("database", ""),
                    "id": record.get("id", ""),
                    "title": record.get("title", ""),
                    "year": record.get("year", ""),
                    "published": record.get("published", ""),
                    "authors": record.get("authors", ""),
                    "venue": record.get("venue", ""),
                    "url": record.get("url", ""),
                    "citation_count": record.get("citation_count", ""),
                    "collision_level": level,
                    "collision_reasons": reasons,
                    "abstract": record.get("abstract", ""),
                }
            )
    fields = [
        "run_at_utc",
        "query_label",
        "query_text",
        "query_purpose",
        "database",
        "id",
        "title",
        "year",
        "published",
        "authors",
        "venue",
        "url",
        "citation_count",
        "collision_level",
        "collision_reasons",
        "abstract",
    ]
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_rows)
    OUT_JSON.write_text(json.dumps(all_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    by_query: dict[str, int] = {}
    high_or_medium = 0
    for row in all_rows:
        by_query[row["query_label"]] = by_query.get(row["query_label"], 0) + 1
        if row["collision_level"] in {"high", "medium"}:
            high_or_medium += 1
    print(f"rows={len(all_rows)}")
    print(f"high_or_medium_collision_candidates={high_or_medium}")
    for label, count in by_query.items():
        print(f"{label}={count}")
    print(OUT_CSV)
    print(OUT_JSON)


if __name__ == "__main__":
    main()
