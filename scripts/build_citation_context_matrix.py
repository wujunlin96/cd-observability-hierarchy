"""Build a citation-context sanity matrix for the observability manuscript.

The matrix checks whether each cited arXiv record's title/abstract contains
keywords compatible with the role assigned to that citation in the manuscript.
It is a lightweight context audit, not a substitute for human reading.
"""

from __future__ import annotations

import csv
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
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
OUT = ROOT / "results" / "citation_context_matrix.csv"


EXPECTED_ROLES: dict[str, dict[str, object]] = {
    "AlbrechtMagueijo1999VSL": {
        "role": "VSL boundary",
        "keywords": ["varying speed of light", "cosmological", "puzzles"],
    },
    "Magueijo2003VSLReview": {
        "role": "VSL review boundary",
        "keywords": ["varying speed of light", "theories"],
    },
    "Moffat2002VSLTheories": {
        "role": "VSL theory boundary",
        "keywords": ["variable speed of light", "theories"],
    },
    "Magueijo2008BimetricVSL": {
        "role": "bimetric VSL boundary",
        "keywords": ["bimetric", "varying speed of light"],
    },
    "Redigolo2012LorentzViolatingSUSY": {
        "role": "multi-speed Lorentz-violating sector boundary",
        "keywords": ["lorentz-violating", "speed of light"],
    },
    "ChashchinaSilagadze2012LightSpeedBarrier": {
        "role": "superluminal particle / light-speed-barrier boundary",
        "keywords": ["light speed", "superluminal"],
    },
    "ColladayKostelecky1998SME": {
        "role": "SME Lorentz-violation framework",
        "keywords": ["lorentz", "standard model"],
    },
    "KosteleckyRussell2011DataTablesSME": {
        "role": "SME constraint tables",
        "keywords": ["data tables", "lorentz", "cpt"],
    },
    "Bekenstein1993DisformalGeometry": {
        "role": "disformal metric boundary",
        "keywords": ["physical", "gravitational", "geometry"],
    },
    "Jacobson2008EinsteinAetherStatus": {
        "role": "Einstein-aether boundary",
        "keywords": ["einstein-aether", "gravity"],
    },
    "Glashow1998PhotonVelocityOscillations": {
        "role": "photon velocity-oscillation boundary",
        "keywords": ["photon", "velocity", "oscillations"],
    },
    "DeAngelisPain2002PhotonVelocityOscillations": {
        "role": "photon velocity-oscillation limits",
        "keywords": ["photon", "velocity", "oscillations"],
    },
    "KosteleckyMewes2004Neutrinos": {
        "role": "SME neutrino Lorentz/CPT boundary",
        "keywords": ["lorentz", "cpt", "neutrinos"],
    },
    "PaesPakvasaWeiler2005ShortcutSterile": {
        "role": "sterile active shortcut boundary",
        "keywords": ["sterile", "active", "shortcut"],
    },
    "HollenbergPaes2009ADRResonance": {
        "role": "altered-dispersion sterile resonance boundary",
        "keywords": ["active-sterile", "altered dispersion", "resonant"],
    },
    "Barenboim2019SterileADRRevisited": {
        "role": "sterile altered-dispersion boundary",
        "keywords": ["sterile", "altered dispersion"],
    },
    "LoboRomero2018SecondClockConstraints": {
        "role": "second-clock-effect boundary",
        "keywords": ["second clock", "experimental constraints"],
    },
    "HobsonLasenby2020WeylNoSecondClock": {
        "role": "Weyl second-clock boundary",
        "keywords": ["weyl", "second clock"],
    },
    "HobsonLasenby2021SecondClockNote": {
        "role": "Weyl second-clock boundary",
        "keywords": ["second clock", "weyl"],
    },
    "DereviankoPospelov2013TopologicalDMClocks": {
        "role": "topological defect clock-search boundary",
        "keywords": ["topological", "dark matter", "atomic clocks"],
    },
    "Wcislo2016OpticalClocksTopologicalDM": {
        "role": "optical clock topological-defect search",
        "keywords": ["topological", "dark matter", "optical", "clocks"],
    },
    "Roberts2017GPSDomainWallDM": {
        "role": "GPS domain-wall clock search",
        "keywords": ["domain wall", "dark matter", "atomic clocks"],
    },
    "Wcislo2018GlobalClockNetworkDM": {
        "role": "global optical-clock network search",
        "keywords": ["global network", "optical atomic clocks", "dark matter"],
    },
    "AmelinoCamelia2011RelativeLocality": {
        "role": "relative locality / deformed momentum-space boundary",
        "keywords": ["relative locality"],
    },
    "HassanRosen2011Bimetric": {
        "role": "ghost-free bimetric boundary",
        "keywords": ["bimetric", "ghost-free", "massive gravity"],
    },
    "HassanRosen2011Secondary": {
        "role": "bimetric ghost constraint boundary",
        "keywords": ["secondary constraint", "ghost", "bimetric"],
    },
    "LIGO2017GW170817GRB": {
        "role": "GW170817 multimessenger speed boundary",
        "keywords": ["gw170817", "grb 170817a", "gravitational waves"],
    },
}


def parse_bib_entries(text: str) -> dict[str, str]:
    entries: dict[str, str] = {}
    for match in re.finditer(r"@\w+\{([^,]+),(.*?)(?=\n@\w+\{|\Z)", text, re.S):
        key, body = match.group(1), match.group(2)
        eprint = re.search(r"eprint\s*=\s*\{([^}]+)\}", body)
        if eprint:
            entries[key] = eprint.group(1)
    return entries


def normalize_arxiv_id(arxiv_id: str) -> list[str]:
    base = re.sub(r"v\d+$", "", arxiv_id)
    return [base, base.split("/")[-1]]


def fetch_records(ids: list[str]) -> dict[str, dict[str, str]]:
    records: dict[str, dict[str, str]] = {}
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for i in range(0, len(ids), 10):
        chunk = ids[i : i + 10]
        url = "https://export.arxiv.org/api/query?id_list=" + ",".join(
            urllib.parse.quote(x, safe="/") for x in chunk
        )
        root = ET.fromstring(urllib.request.urlopen(url, timeout=30).read())
        for entry in root.findall("a:entry", ns):
            arxiv_id = entry.find("a:id", ns).text.rsplit("/", 1)[-1]
            title = " ".join(entry.find("a:title", ns).text.split())
            summary = " ".join(entry.find("a:summary", ns).text.split())
            categories = " ".join(
                cat.attrib.get("term", "") for cat in entry.findall("a:category", ns)
            )
            record = {"title": title, "summary": summary, "categories": categories}
            for candidate in normalize_arxiv_id(arxiv_id):
                records[candidate] = record
    return records


def keyword_status(text: str, keywords: list[str]) -> tuple[str, str]:
    lower = text.lower()
    hits = [kw for kw in keywords if kw.lower() in lower]
    if len(hits) == len(keywords):
        return "PASS", "; ".join(hits)
    if hits:
        return "PARTIAL", "; ".join(hits)
    return "FAIL", ""


def main() -> int:
    bib_eprints = parse_bib_entries(BIB.read_text(encoding="utf-8"))
    ids = [bib_eprints[key] for key in EXPECTED_ROLES if key in bib_eprints]
    records = fetch_records(ids)
    rows = []
    failures = []
    for key, spec in EXPECTED_ROLES.items():
        eprint = bib_eprints.get(key, "")
        record = {}
        for candidate in normalize_arxiv_id(eprint):
            if candidate in records:
                record = records[candidate]
                break
        title = record.get("title", "")
        summary = record.get("summary", "")
        searchable = f"{title} {summary}"
        status, hits = keyword_status(searchable, list(spec["keywords"]))
        if status == "FAIL":
            failures.append(key)
        rows.append(
            {
                "key": key,
                "eprint": eprint,
                "role": str(spec["role"]),
                "expected_keywords": "; ".join(spec["keywords"]),
                "keyword_status": status,
                "keyword_hits": hits,
                "arxiv_title": title,
                "arxiv_categories": record.get("categories", ""),
            }
        )

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"rows={len(rows)}")
    print(f"output={OUT}")
    print(f"failures={failures}")
    if failures:
        return 1
    print("citation_context_matrix_status=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
