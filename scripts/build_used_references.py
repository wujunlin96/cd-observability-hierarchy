"""Build a BibTeX file containing only references cited by the main draft."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "draft" / "main_observability_hierarchy.md"
BIB = next(
    (
        path
        for path in [
            ROOT / "references" / "references.bib",
            ROOT / "paper" / "references.bib",
            ROOT / "references" / "observability_used_references.bib",
        ]
        if path.exists()
    ),
    ROOT / "references" / "references.bib",
)
OUT = ROOT / "references" / "observability_used_references.bib"


def parse_entries(text: str) -> dict[str, str]:
    entries: dict[str, str] = {}
    for match in re.finditer(r"(@\w+\{([^,]+),.*?)(?=\n@\w+\{|\Z)", text, re.S):
        entries[match.group(2)] = match.group(1).rstrip() + "\n"
    return entries


def main() -> int:
    draft = DRAFT.read_text(encoding="utf-8")
    used = sorted(set(re.findall(r"@([A-Za-z0-9:_-]+)", draft)))
    entries = parse_entries(BIB.read_text(encoding="utf-8"))
    missing = [key for key in used if key not in entries]
    if missing:
        print(f"missing_used_keys={missing}")
        return 1

    unused = sorted(set(entries) - set(used))
    OUT.write_text("\n".join(entries[key] for key in used), encoding="utf-8")
    print(f"used_entries={len(used)}")
    print(f"source_entries={len(entries)}")
    print(f"unused_source_entries={len(unused)}")
    print(f"output={OUT}")
    print("used_references_status=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
