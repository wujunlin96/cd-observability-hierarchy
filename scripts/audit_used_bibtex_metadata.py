"""Audit metadata completeness for references cited by the main draft."""

from __future__ import annotations

import csv
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
USED_BIB = ROOT / "references" / "observability_used_references.bib"
OUT = ROOT / "results" / "used_bibtex_metadata_audit.csv"


def parse_entries(text: str) -> dict[str, dict[str, str]]:
    entries: dict[str, dict[str, str]] = {}
    for match in re.finditer(r"@\w+\{([^,]+),(.*?)(?=\n@\w+\{|\Z)", text, re.S):
        key, body = match.group(1), match.group(2)
        fields: dict[str, str] = {}
        for field in [
            "author",
            "title",
            "journal",
            "volume",
            "number",
            "pages",
            "year",
            "doi",
            "eprint",
        ]:
            found = re.search(field + r"\s*=\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", body, re.S)
            fields[field] = (
                " ".join(found.group(1).replace("{", "").replace("}", "").split())
                if found
                else ""
            )
        entries[key] = fields
    return entries


def crossref_suggestion(title: str) -> dict[str, str]:
    if not title:
        return {}
    params = urllib.parse.urlencode({"query.title": title, "rows": "1"})
    url = f"https://api.crossref.org/works?{params}"
    try:
        data = json.loads(
            urllib.request.urlopen(
                urllib.request.Request(url, headers={"User-Agent": "cd-observability-audit/1.0"}),
                timeout=20,
            ).read()
        )
    except Exception:
        return {}
    items = data.get("message", {}).get("items", [])
    if not items:
        return {}
    item = items[0]
    return {
        "crossref_title": " ".join(item.get("title", [""])[0].split()),
        "crossref_container": " ".join(item.get("container-title", [""])[0].split()),
        "crossref_volume": str(item.get("volume", "")),
        "crossref_page": str(item.get("page", "")),
        "crossref_doi": str(item.get("DOI", "")),
        "crossref_score": str(item.get("score", "")),
    }


def main() -> int:
    entries = parse_entries(USED_BIB.read_text(encoding="utf-8"))
    rows: list[dict[str, str]] = []
    incomplete: list[str] = []
    for key, fields in entries.items():
        missing = [
            field
            for field in ["journal", "volume", "pages", "doi"]
            if not fields.get(field)
        ]
        status = "PASS" if not missing else "INCOMPLETE"
        suggestion = crossref_suggestion(fields.get("title", "")) if missing else {}
        if missing:
            incomplete.append(key)
        rows.append(
            {
                "key": key,
                "status": status,
                "missing_fields": "; ".join(missing),
                "title": fields.get("title", ""),
                "year": fields.get("year", ""),
                "eprint": fields.get("eprint", ""),
                "journal": fields.get("journal", ""),
                "volume": fields.get("volume", ""),
                "pages": fields.get("pages", ""),
                "doi": fields.get("doi", ""),
                **suggestion,
            }
        )

    OUT.parent.mkdir(exist_ok=True)
    fieldnames = [
        "key",
        "status",
        "missing_fields",
        "title",
        "year",
        "eprint",
        "journal",
        "volume",
        "pages",
        "doi",
        "crossref_title",
        "crossref_container",
        "crossref_volume",
        "crossref_page",
        "crossref_doi",
        "crossref_score",
    ]
    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"entries={len(rows)}")
    print(f"incomplete={len(incomplete)}")
    print(f"output={OUT}")
    print(f"incomplete_keys={incomplete}")
    if incomplete:
        return 1
    print("used_bibtex_metadata_status=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
