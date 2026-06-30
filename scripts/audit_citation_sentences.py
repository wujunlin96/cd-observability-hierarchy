"""Audit citation-bearing manuscript sentences against source roles.

This check is stronger than verifying that citation keys exist. It extracts
each sentence or table row containing a citation, assigns each cited key an
expected source role, fetches arXiv title/abstract metadata when available,
and checks that both the manuscript context and the source metadata are
compatible with that role.

It is still not a substitute for a final human reading of the full papers.
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
OUT = ROOT / "results" / "citation_sentence_audit.csv"


ROLE_SPECS: dict[str, dict[str, object]] = {
    "Redigolo2012LorentzViolatingSUSY": {
        "role": "multi-speed Lorentz-violating sector boundary",
        "source_keywords": ["lorentz-violating", "speed of light"],
        "context_any": ["different limiting speed", "multi-speed", "multiple speed"],
    },
    "ChashchinaSilagadze2012LightSpeedBarrier": {
        "role": "superluminal particle / critical-speed boundary",
        "source_keywords": ["light speed", "superluminal"],
        "context_any": ["superluminal", "critical speed", "different limiting speed"],
    },
    "AlbrechtMagueijo1999VSL": {
        "role": "VSL cosmology boundary",
        "source_keywords": ["varying speed of light", "cosmological", "puzzles"],
        "context_any": ["varying-speed", "visible light speed", "cosmological"],
    },
    "Magueijo2003VSLReview": {
        "role": "VSL review boundary",
        "source_keywords": ["varying speed of light", "theories"],
        "context_any": ["varying-speed", "visible light speed", "cosmological"],
    },
    "Moffat2002VSLTheories": {
        "role": "VSL theory boundary",
        "source_keywords": ["variable speed of light", "theories"],
        "context_any": ["varying-speed", "visible light speed", "cosmological"],
    },
    "Magueijo2008BimetricVSL": {
        "role": "bimetric VSL boundary",
        "source_keywords": ["bimetric", "varying speed of light"],
        "context_any": ["bimetric", "varying-speed", "visible light speed"],
    },
    "ColladayKostelecky1998SME": {
        "role": "SME Lorentz-violation framework",
        "source_keywords": ["lorentz", "standard model"],
        "context_any": ["standard-model extension", "sme", "lorentz"],
    },
    "KosteleckyRussell2011DataTablesSME": {
        "role": "SME constraint tables",
        "source_keywords": ["data tables", "lorentz", "cpt"],
        "context_any": ["standard-model extension", "sme", "constraint", "bounded"],
    },
    "Bekenstein1993DisformalGeometry": {
        "role": "disformal metric boundary",
        "source_keywords": ["physical", "gravitational", "geometry"],
        "context_any": ["disformal", "physical/gravitational", "metric"],
    },
    "Jacobson2008EinsteinAetherStatus": {
        "role": "Einstein-aether boundary",
        "source_keywords": ["einstein-aether", "gravity"],
        "context_any": ["aether", "preferred", "timelike"],
    },
    "Glashow1998PhotonVelocityOscillations": {
        "role": "photon velocity-oscillation boundary",
        "source_keywords": ["photon", "velocity", "oscillations"],
        "context_any": ["photon", "velocity oscillation", "velocity eigenstate"],
    },
    "DeAngelisPain2002PhotonVelocityOscillations": {
        "role": "photon velocity-oscillation limits",
        "source_keywords": ["photon", "velocity", "oscillations"],
        "context_any": ["photon", "bounded", "limits", "velocity oscillation"],
    },
    "KosteleckyMewes2004Neutrinos": {
        "role": "SME neutrino Lorentz/CPT boundary",
        "source_keywords": ["lorentz", "cpt", "neutrinos"],
        "context_any": ["neutrino", "sme", "lorentz", "cpt"],
    },
    "PaesPakvasaWeiler2005ShortcutSterile": {
        "role": "sterile active shortcut boundary",
        "source_keywords": ["sterile", "active", "shortcut"],
        "context_any": ["sterile", "shortcut"],
    },
    "HollenbergPaes2009ADRResonance": {
        "role": "altered-dispersion sterile resonance boundary",
        "source_keywords": ["active-sterile", "altered dispersion", "resonant"],
        "context_any": ["altered-dispersion", "resonant", "sterile"],
    },
    "Barenboim2019SterileADRRevisited": {
        "role": "sterile altered-dispersion boundary",
        "source_keywords": ["sterile", "altered dispersion"],
        "context_any": ["altered-dispersion", "sterile"],
    },
    "LoboRomero2018SecondClockConstraints": {
        "role": "second-clock-effect boundary",
        "source_keywords": ["second clock", "experimental constraints"],
        "context_any": ["second-clock", "weyl", "clock"],
    },
    "HobsonLasenby2020WeylNoSecondClock": {
        "role": "Weyl second-clock boundary",
        "source_keywords": ["weyl", "second clock"],
        "context_any": ["weyl", "second-clock", "clock"],
    },
    "HobsonLasenby2021SecondClockNote": {
        "role": "Weyl second-clock boundary",
        "source_keywords": ["second clock", "weyl"],
        "context_any": ["weyl", "second-clock", "clock"],
    },
    "DereviankoPospelov2013TopologicalDMClocks": {
        "role": "topological defect clock-search boundary",
        "source_keywords": ["topological", "dark matter", "atomic clocks"],
        "context_any": ["topological", "clock", "frequency shifts"],
    },
    "Wcislo2016OpticalClocksTopologicalDM": {
        "role": "optical clock topological-defect search",
        "source_keywords": ["topological", "dark matter", "optical", "clocks"],
        "context_any": ["topological", "clock", "frequency shifts"],
    },
    "Roberts2017GPSDomainWallDM": {
        "role": "GPS domain-wall clock search",
        "source_keywords": ["domain wall", "dark matter", "atomic clocks"],
        "context_any": ["domain wall", "clock", "frequency shifts", "topological"],
    },
    "Wcislo2018GlobalClockNetworkDM": {
        "role": "global optical-clock network search",
        "source_keywords": ["global network", "optical atomic clocks", "dark matter"],
        "context_any": ["global", "clock", "frequency shifts", "topological"],
    },
    "AmelinoCamelia2011RelativeLocality": {
        "role": "relative locality / deformed momentum-space boundary",
        "source_keywords": ["relative locality"],
        "context_any": ["relative locality", "momentum-space", "boost kinematics"],
    },
    "HassanRosen2011Bimetric": {
        "role": "ghost-free bimetric boundary",
        "source_keywords": ["bimetric", "ghost-free", "massive gravity"],
        "context_any": ["bimetric", "ghost", "spin-2", "multimetric"],
    },
    "HassanRosen2011Secondary": {
        "role": "bimetric ghost constraint boundary",
        "source_keywords": ["secondary constraint", "ghost", "bimetric"],
        "context_any": ["bimetric", "ghost", "spin-2", "multimetric"],
    },
    "LIGO2017GW170817GRB": {
        "role": "GW170817 multimessenger speed boundary",
        "source_keywords": ["gw170817", "grb 170817a", "gravitational waves"],
        "context_any": ["gw170817", "grb170817a", "gravity-light", "speed"],
    },
}


def parse_bib_entries(text: str) -> dict[str, dict[str, str]]:
    entries: dict[str, dict[str, str]] = {}
    for match in re.finditer(r"@\w+\{([^,]+),(.*?)(?=\n@\w+\{|\Z)", text, re.S):
        key, body = match.group(1), match.group(2)
        fields: dict[str, str] = {}
        for field in ["eprint", "title", "doi", "journal", "year"]:
            found = re.search(field + r"\s*=\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", body, re.S)
            fields[field] = (
                " ".join(found.group(1).replace("{", "").replace("}", "").split())
                if found
                else ""
            )
        entries[key] = fields
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
            record = {"title": title, "summary": summary}
            for candidate in normalize_arxiv_id(arxiv_id):
                records[candidate] = record
    return records


def citation_contexts(markdown: str) -> list[dict[str, object]]:
    contexts: list[dict[str, object]] = []
    for line_no, line in enumerate(markdown.splitlines(), start=1):
        if "@" not in line:
            continue
        if line.lstrip().startswith("|"):
            candidates = [line.strip()]
        else:
            candidates = re.split(r"(?<=[.!?])\s+(?=[A-Z])", line.strip())
        for context in candidates:
            keys = re.findall(r"@([A-Za-z0-9:_-]+)", context)
            if keys:
                contexts.append({"line": line_no, "context": context, "keys": keys})
    return contexts


def keyword_hits(text: str, keywords: list[str]) -> list[str]:
    lower = text.lower().replace("--", "-")
    return [kw for kw in keywords if kw.lower() in lower]


def main() -> int:
    draft = DRAFT.read_text(encoding="utf-8")
    bib_entries = parse_bib_entries(BIB.read_text(encoding="utf-8"))
    used = sorted(set(re.findall(r"@([A-Za-z0-9:_-]+)", draft)))
    arxiv_ids = [
        bib_entries[key]["eprint"]
        for key in used
        if bib_entries.get(key, {}).get("eprint")
    ]
    records = fetch_records(arxiv_ids)

    rows: list[dict[str, str]] = []
    failures: list[str] = []
    for context in citation_contexts(draft):
        manuscript_context = str(context["context"])
        for key in context["keys"]:
            spec = ROLE_SPECS.get(key)
            if spec is None:
                rows.append(
                    {
                        "line": str(context["line"]),
                        "key": key,
                        "role": "MISSING_ROLE_SPEC",
                        "context_status": "FAIL",
                        "source_status": "FAIL",
                        "overall_status": "FAIL",
                        "context_hits": "",
                        "source_hits": "",
                        "manuscript_context": manuscript_context,
                        "source_title": bib_entries.get(key, {}).get("title", ""),
                    }
                )
                failures.append(key)
                continue

            context_hits = keyword_hits(manuscript_context, list(spec["context_any"]))
            context_status = "PASS" if context_hits else "FAIL"
            record = {}
            for candidate in normalize_arxiv_id(bib_entries.get(key, {}).get("eprint", "")):
                if candidate in records:
                    record = records[candidate]
                    break
            source_text = f"{record.get('title', '')} {record.get('summary', '')}"
            source_hits = keyword_hits(source_text, list(spec["source_keywords"]))
            if len(source_hits) == len(spec["source_keywords"]):
                source_status = "PASS"
            elif source_hits:
                source_status = "PARTIAL"
            else:
                source_status = "FAIL"

            overall_status = "PASS" if context_status == "PASS" and source_status in {"PASS", "PARTIAL"} else "FAIL"
            if overall_status == "FAIL":
                failures.append(key)
            rows.append(
                {
                    "line": str(context["line"]),
                    "key": key,
                    "role": str(spec["role"]),
                    "context_status": context_status,
                    "source_status": source_status,
                    "overall_status": overall_status,
                    "context_hits": "; ".join(context_hits),
                    "source_hits": "; ".join(source_hits),
                    "manuscript_context": manuscript_context,
                    "source_title": record.get("title", bib_entries.get(key, {}).get("title", "")),
                }
            )

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"contexts={len(citation_contexts(draft))}")
    print(f"citation_occurrences={len(rows)}")
    print(f"output={OUT}")
    print(f"failures={sorted(set(failures))}")
    if failures:
        return 1
    print("citation_sentence_audit_status=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
