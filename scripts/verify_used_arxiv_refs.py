"""Verify that cited BibTeX entries with arXiv eprints resolve in arXiv API.

This is an existence/metadata sanity check. It does not replace full citation
context verification against paper content.
"""

from __future__ import annotations

import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "draft" / "main_observability_hierarchy.md"
BIB = next(
    (
        path
        for path in [
            ROOT / "references" / "observability_used_references.bib",
            ROOT / "paper" / "references.bib",
            ROOT / "references" / "references.bib",
        ]
        if path.exists()
    ),
    ROOT / "references" / "observability_used_references.bib",
)
USER_AGENT = "cd-observability-reference-audit/1.0 (local manuscript check)"


def parse_bib_entries(text: str) -> dict[str, dict[str, str]]:
    entries: dict[str, dict[str, str]] = {}
    for match in re.finditer(r"@\w+\{([^,]+),(.*?)(?=\n@\w+\{|\Z)", text, re.S):
        key, body = match.group(1), match.group(2)
        eprint = re.search(r"eprint\s*=\s*\{([^}]+)\}", body)
        title = re.search(r"title\s*=\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", body, re.S)
        entries[key] = {
            "eprint": eprint.group(1) if eprint else "",
            "title": " ".join(title.group(1).replace("{", "").replace("}", "").split()) if title else "",
        }
    return entries


def normalize_arxiv_id(arxiv_id: str) -> list[str]:
    base = re.sub(r"v\d+$", "", arxiv_id)
    return [base, base.split("/")[-1]]


def fetch_arxiv_titles(ids: list[str]) -> dict[str, str]:
    found: dict[str, str] = {}
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for i in range(0, len(ids), 10):
        chunk = ids[i : i + 10]
        url = "https://export.arxiv.org/api/query?id_list=" + ",".join(
            urllib.parse.quote(x, safe="/") for x in chunk
        )
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        last_error: Exception | None = None
        for attempt in range(3):
            try:
                payload = urllib.request.urlopen(request, timeout=30).read()
                break
            except (urllib.error.URLError, TimeoutError) as exc:
                last_error = exc
                if attempt == 2:
                    raise RuntimeError(f"arXiv API request failed after retries: {url}") from last_error
                time.sleep(2**attempt)
        root = ET.fromstring(payload)
        for entry in root.findall("a:entry", ns):
            arxiv_id = entry.find("a:id", ns).text.rsplit("/", 1)[-1]
            title = " ".join(entry.find("a:title", ns).text.split())
            for candidate in normalize_arxiv_id(arxiv_id):
                found[candidate] = title
    return found


def main() -> int:
    draft = DRAFT.read_text(encoding="utf-8")
    bib = BIB.read_text(encoding="utf-8")
    used = sorted(set(re.findall(r"@([A-Za-z0-9:_-]+)", draft)))
    entries = parse_bib_entries(bib)
    arxiv_ids = [entries[key]["eprint"] for key in used if entries.get(key, {}).get("eprint")]
    found = fetch_arxiv_titles(arxiv_ids)

    missing: list[str] = []
    print(f"used_citations={len(used)}")
    print(f"arxiv_eprints={len(arxiv_ids)}")
    for key in used:
        eprint = entries.get(key, {}).get("eprint", "")
        title = ""
        for candidate in normalize_arxiv_id(eprint):
            if candidate in found:
                title = found[candidate]
                break
        status = "FOUND" if title else "MISSING"
        print(f"{key}\t{eprint}\t{status}\t{title}")
        if not title:
            missing.append(key)

    if missing:
        print(f"missing_arxiv={missing}")
        return 1
    print("arxiv_reference_status=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
