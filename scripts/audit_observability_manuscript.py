"""Structural integrity checks for the C-D observability manuscript.

This is not a scientific peer review. It verifies local consistency between the
Markdown draft, BibTeX database, figures, generated CSV results, and a key
reported finite-wall flux-conservation number.
"""

from __future__ import annotations

import csv
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
FINITE_WALL_CSV = ROOT / "results" / "cd_finite_wall_transfer_scan.csv"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def bib_keys(text: str) -> set[str]:
    return set(re.findall(r"@\w+\{([^,]+),", text))


def manuscript_cites(text: str) -> set[str]:
    return set(re.findall(r"@([A-Za-z0-9:_-]+)", text))


def markdown_figures(text: str) -> list[str]:
    return re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)


def literal_paths(text: str) -> set[str]:
    roots = "scripts|results|figures|notes|references|draft|submission|paper"
    candidates = set(re.findall(rf"`((?:{roots})/[^`]+)`", text))
    candidates |= set(re.findall(rf"`((?:{roots})\\[^`]+)`", text))
    return candidates


def artifact_candidates(literal: str) -> list[Path]:
    normalized = literal.replace("\\", "/")
    candidates = [(ROOT / normalized).resolve()]
    package_prefix = "submission/arxiv_cd_observability/"
    if normalized.startswith(package_prefix):
        candidates.append((ROOT / "paper" / normalized[len(package_prefix) :]).resolve())
    public_package_prefix = "paper/"
    if normalized.startswith(public_package_prefix):
        candidates.append(
            (ROOT / "submission" / "arxiv_cd_observability" / normalized[len(public_package_prefix) :]).resolve()
        )
    return candidates


def max_flux_error(path: Path) -> float:
    with path.open(encoding="utf-8", newline="") as f:
        return max(float(row["flux_error"]) for row in csv.DictReader(f))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    draft = read(DRAFT)
    bib = read(BIB)

    missing_cites = sorted(manuscript_cites(draft) - bib_keys(bib))
    if missing_cites:
        errors.append(f"missing citation keys: {missing_cites}")

    for fig in markdown_figures(draft):
        fig_path = (DRAFT.parent / fig).resolve()
        if not fig_path.exists():
            errors.append(f"missing figure link target: {fig} -> {fig_path}")

    for literal in sorted(literal_paths(draft)):
        candidates = artifact_candidates(literal)
        if not any(path.exists() for path in candidates):
            errors.append(
                "missing literal artifact path: "
                f"{literal} -> {', '.join(str(path) for path in candidates)}"
            )

    if FINITE_WALL_CSV.exists():
        mx = max_flux_error(FINITE_WALL_CSV)
        reported = re.search(
            r"maximum flux-conservation error is (?:below )?(?:\\\(|\$)?([0-9.]+)\\times10\^\{?(-?[0-9]+)\}?(?:\\\)|\$)?",
            draft,
        )
        if reported:
            mantissa = float(reported.group(1))
            exponent = int(reported.group(2))
            reported_value = mantissa * 10**exponent
            if mx > reported_value:
                errors.append(
                    f"reported flux bound {reported_value:.3e} is below current max {mx:.3e}"
                )
        else:
            warnings.append("no parseable reported finite-wall flux-conservation bound found")
    else:
        errors.append(f"missing finite-wall CSV: {FINITE_WALL_CSV}")

    print(f"draft={DRAFT}")
    print(f"citations={len(manuscript_cites(draft))}")
    print(f"figures={len(markdown_figures(draft))}")
    print(f"literal_artifact_paths={len(literal_paths(draft))}")
    if FINITE_WALL_CSV.exists():
        print(f"finite_wall_max_flux_error={max_flux_error(FINITE_WALL_CSV):.15e}")
    if warnings:
        print("WARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    if errors:
        print("ERRORS:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("audit_status=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
