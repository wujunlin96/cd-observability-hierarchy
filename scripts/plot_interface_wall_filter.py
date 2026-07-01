"""Generate an SVG plot for finite-wall C-D interface coherence filtering.

This script deliberately uses only the Python standard library so the figure is
reproducible in minimal environments.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path
from xml.sax.saxutils import escape


WIDTH = 860
HEIGHT = 560
LEFT = 92
RIGHT = 30
TOP = 62
BOTTOM = 78

X_MIN = 1e-3
X_MAX = 30.0
Y_MIN = 1e-5
Y_MAX = 1.4


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def sx(x: float) -> float:
    log_min = math.log10(X_MIN)
    log_max = math.log10(X_MAX)
    return LEFT + (math.log10(x) - log_min) / (log_max - log_min) * (WIDTH - LEFT - RIGHT)


def sy(y: float) -> float:
    log_min = math.log10(Y_MIN)
    log_max = math.log10(Y_MAX)
    return HEIGHT - BOTTOM - (math.log10(y) - log_min) / (log_max - log_min) * (
        HEIGHT - TOP - BOTTOM
    )


def polyline(points: list[tuple[float, float]], color: str, dashed: bool = False) -> str:
    coords = " ".join(f"{sx(x):.1f},{sy(y):.1f}" for x, y in points if x > 0 and y > 0)
    dash = ' stroke-dasharray="9 7"' if dashed else ""
    return (
        f'<polyline points="{coords}" fill="none" stroke="{color}" '
        f'stroke-width="3"{dash} stroke-linejoin="round" stroke-linecap="round" />'
    )


def marker_points(points: list[tuple[float, float]], color: str) -> str:
    out = []
    for x, y in points:
        out.append(
            f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="4.2" '
            f'fill="white" stroke="{color}" stroke-width="2" />'
        )
    return "\n".join(out)


def text(x: float, y: float, body: str, size: int = 14, anchor: str = "middle") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial, sans-serif" '
        f'font-size="{size}" text-anchor="{anchor}" fill="#222">{escape(body)}</text>'
    )


def line(x1: float, y1: float, x2: float, y2: float, color: str, width: float = 1.0) -> str:
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{color}" stroke-width="{width:.1f}" />'
    )


def build_axes() -> list[str]:
    items: list[str] = []
    x0, x1 = LEFT, WIDTH - RIGHT
    y0, y1 = TOP, HEIGHT - BOTTOM

    items.append(f'<rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="white" />')
    items.append(line(x0, y1, x1, y1, "#222", 1.4))
    items.append(line(x0, y0, x0, y1, "#222", 1.4))

    x_ticks = [1e-3, 1e-2, 1e-1, 1, 10]
    y_ticks = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]

    for tick in x_ticks:
        x = sx(tick)
        items.append(line(x, y0, x, y1, "#e5e5e5", 0.8))
        items.append(line(x, y1, x, y1 + 6, "#222", 1.0))
        label = f"1e{int(math.log10(tick))}" if tick != 1 else "1"
        items.append(text(x, y1 + 25, label, 12))

    for tick in y_ticks:
        y = sy(tick)
        items.append(line(x0, y, x1, y, "#e5e5e5", 0.8))
        items.append(line(x0 - 6, y, x0, y, "#222", 1.0))
        label = f"1e{int(math.log10(tick))}" if tick != 1 else "1"
        items.append(text(x0 - 12, y + 4, label, 12, "end"))

    items.append(text(WIDTH / 2, 34, "Finite C-D interface as a momentum filter", 18))
    items.append(text(WIDTH / 2, HEIGHT - 24, "dimensionless wall thickness zeta = omega L_w / C", 14))
    items.append(
        '<text x="24" y="300" font-family="Arial, sans-serif" font-size="14" '
        'text-anchor="middle" fill="#222" transform="rotate(-90 24 300)">'
        "P_forward / P_delta,forward</text>"
    )

    x_coh = sx(2.0)
    items.append(
        f'<line x1="{x_coh:.1f}" y1="{y0:.1f}" x2="{x_coh:.1f}" y2="{y1:.1f}" '
        'stroke="#555" stroke-width="1.4" stroke-dasharray="4 6" />'
    )
    items.append(
        f'<text x="{x_coh + 9:.1f}" y="{sy(0.03):.1f}" font-family="Arial, sans-serif" '
        'font-size="12" fill="#333" transform="rotate(-90 '
        f'{x_coh + 9:.1f} {sy(0.03):.1f})">D/C=2 coherence: |k_C-k_D| L_w ~= 1</text>'
    )
    return items


def main() -> None:
    rows = load_rows(Path("results/cd_finite_wall_transfer_scan.csv"))
    target_d = 2.0
    target_alpha = 0.1
    colors = {"square": "#1f77b4", "sech2": "#d62728"}
    small_split_d = math.sqrt(1.0 + 1e-3)

    svg: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">'
    ]
    svg.extend(build_axes())

    legend_y = 84
    for i, profile in enumerate(["square", "sech2"]):
        subset = [
            r
            for r in rows
            if r["profile"] == profile
            and abs(float(r["D_over_C"]) - target_d) < 1e-9
            and abs(float(r["alpha_integrated"]) - target_alpha) < 1e-12
        ]
        subset.sort(key=lambda r: float(r["zeta_omega_Lw_over_C"]))
        numeric = [
            (float(r["zeta_omega_Lw_over_C"]), float(r["forward_over_delta"]))
            for r in subset
        ]
        born = [
            (float(r["zeta_omega_Lw_over_C"]), float(r["born_forward_over_delta"]))
            for r in subset
        ]
        color = colors[profile]
        svg.append(polyline(numeric, color, dashed=False))
        svg.append(marker_points(numeric, color))
        svg.append(polyline(born, color, dashed=True))

        y = legend_y + i * 44
        x = 530
        label = "square wall" if profile == "square" else "smooth sech^2 wall"
        svg.append(line(x, y, x + 44, y, color, 3.0))
        svg.append(text(x + 54, y + 4, f"{label}: transfer matrix", 12, "start"))
        svg.append(
            f'<line x1="{x:.1f}" y1="{y + 18:.1f}" x2="{x + 44:.1f}" y2="{y + 18:.1f}" '
            f'stroke="{color}" stroke-width="2.4" stroke-dasharray="8 6" />'
        )
        svg.append(text(x + 54, y + 22, f"{label}: Born filter", 12, "start"))

    small_subset = [
        r
        for r in rows
        if r["profile"] == "sech2"
        and abs(float(r["D_over_C"]) - small_split_d) < 1e-9
        and abs(float(r["alpha_integrated"]) - target_alpha) < 1e-12
    ]
    small_subset.sort(key=lambda r: float(r["zeta_omega_Lw_over_C"]))
    small_numeric = [
        (float(r["zeta_omega_Lw_over_C"]), float(r["forward_over_delta"]))
        for r in small_subset
    ]
    small_born = [
        (float(r["zeta_omega_Lw_over_C"]), float(r["born_forward_over_delta"]))
        for r in small_subset
    ]
    small_color = "#2ca02c"
    svg.append(polyline(small_numeric, small_color, dashed=False))
    svg.append(marker_points(small_numeric, small_color))
    svg.append(polyline(small_born, small_color, dashed=True))
    x = 530
    y = legend_y + 2 * 44
    svg.append(line(x, y, x + 44, y, small_color, 3.0))
    svg.append(text(x + 54, y + 4, "smooth wall, xi=1e-3: transfer matrix", 12, "start"))
    svg.append(
        f'<line x1="{x:.1f}" y1="{y + 18:.1f}" x2="{x + 44:.1f}" y2="{y + 18:.1f}" '
        f'stroke="{small_color}" stroke-width="2.4" stroke-dasharray="8 6" />'
    )
    svg.append(text(x + 54, y + 22, "smooth wall, xi=1e-3: Born filter", 12, "start"))

    svg.append("</svg>")

    out_dir = Path("figures")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "interface_wall_filter.svg"
    out_path.write_text("\n".join(svg), encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()
