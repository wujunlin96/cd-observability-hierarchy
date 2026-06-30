"""Generate a PNG version of the finite-wall interface figure.

The LaTeX preprint package should not depend on SVG support.  This script uses
Pillow, which is available in the local environment, and reads the same CSV as
the standard-library SVG plot.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1720
HEIGHT = 1120
SCALE = 2
LEFT = 184
RIGHT = 60
TOP = 124
BOTTOM = 156
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


def font(size: int) -> ImageFont.ImageFont:
    for name in ["arial.ttf", "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def dashed_line(draw: ImageDraw.ImageDraw, xy: tuple[float, float, float, float], fill: str, width: int) -> None:
    x1, y1, x2, y2 = xy
    length = math.hypot(x2 - x1, y2 - y1)
    if length == 0:
        return
    dash = 18
    gap = 14
    dx = (x2 - x1) / length
    dy = (y2 - y1) / length
    pos = 0.0
    while pos < length:
        end = min(pos + dash, length)
        draw.line(
            (x1 + dx * pos, y1 + dy * pos, x1 + dx * end, y1 + dy * end),
            fill=fill,
            width=width,
        )
        pos += dash + gap


def draw_polyline(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[float, float]],
    color: str,
    width: int = 5,
    dashed: bool = False,
) -> None:
    mapped = [
        (sx(x), sy(y))
        for x, y in points
        if X_MIN <= x <= X_MAX and Y_MIN <= y <= Y_MAX
    ]
    for a, b in zip(mapped, mapped[1:]):
        if dashed:
            dashed_line(draw, (*a, *b), color, width)
        else:
            draw.line((*a, *b), fill=color, width=width)


def draw_markers(draw: ImageDraw.ImageDraw, points: list[tuple[float, float]], color: str) -> None:
    r = 8
    for x, y in points:
        if not (X_MIN <= x <= X_MAX and Y_MIN <= y <= Y_MAX):
            continue
        cx, cy = sx(x), sy(y)
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="white", outline=color, width=4)


def centered(draw: ImageDraw.ImageDraw, xy: tuple[float, float], text: str, fnt: ImageFont.ImageFont, fill: str = "#222") -> None:
    box = draw.textbbox((0, 0), text, font=fnt)
    draw.text((xy[0] - (box[2] - box[0]) / 2, xy[1] - (box[3] - box[1]) / 2), text, font=fnt, fill=fill)


def main() -> None:
    rows = load_rows(Path("results/cd_finite_wall_transfer_scan.csv"))
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)
    f12 = font(24)
    f14 = font(28)
    f18 = font(36)

    x0, x1 = LEFT, WIDTH - RIGHT
    y0, y1 = TOP, HEIGHT - BOTTOM
    draw.line((x0, y1, x1, y1), fill="#222", width=3)
    draw.line((x0, y0, x0, y1), fill="#222", width=3)

    for tick in [1e-3, 1e-2, 1e-1, 1, 10]:
        x = sx(tick)
        draw.line((x, y0, x, y1), fill="#e5e5e5", width=2)
        draw.line((x, y1, x, y1 + 12), fill="#222", width=2)
        centered(draw, (x, y1 + 48), f"1e{int(math.log10(tick))}" if tick != 1 else "1", f12)

    for tick in [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]:
        y = sy(tick)
        draw.line((x0, y, x1, y), fill="#e5e5e5", width=2)
        draw.line((x0 - 12, y, x0, y), fill="#222", width=2)
        label = f"1e{int(math.log10(tick))}" if tick != 1 else "1"
        box = draw.textbbox((0, 0), label, font=f12)
        draw.text((x0 - 24 - (box[2] - box[0]), y - (box[3] - box[1]) / 2), label, font=f12, fill="#222")

    centered(draw, (WIDTH / 2, 68), "Finite C-D interface as a momentum filter (D/C=2, alpha_int=0.1)", f18)
    centered(draw, (WIDTH / 2, HEIGHT - 50), "wall thickness zeta = omega L_w / C", f14)
    ylabel = Image.new("RGBA", (560, 54), (255, 255, 255, 0))
    ydraw = ImageDraw.Draw(ylabel)
    centered(ydraw, (280, 27), "P_forward / P_delta,forward", f14)
    img.paste(ylabel.rotate(90, expand=True), (26, 332), ylabel.rotate(90, expand=True))

    x_coh = sx(2.0)
    dashed_line(draw, (x_coh, y0, x_coh, y1), "#555", 3)
    draw.text((x_coh + 18, sy(0.03) - 10), "|k_C-k_D| L_w ~= 1", font=f12, fill="#333")

    colors = {"square": "#1f77b4", "sech2": "#d62728"}
    for i, profile in enumerate(["square", "sech2"]):
        subset = [
            r
            for r in rows
            if r["profile"] == profile
            and abs(float(r["D_over_C"]) - 2.0) < 1e-9
            and abs(float(r["alpha_integrated"]) - 0.1) < 1e-12
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
        draw_polyline(draw, numeric, color, width=6, dashed=False)
        draw_markers(draw, numeric, color)
        draw_polyline(draw, born, color, width=5, dashed=True)

        y = 690 + i * 88
        x = 310
        label = "square wall" if profile == "square" else "smooth sech^2 wall"
        draw.line((x, y, x + 88, y), fill=color, width=6)
        draw.text((x + 108, y - 16), f"{label}: transfer matrix", font=f12, fill="#222")
        dashed_line(draw, (x, y + 36, x + 88, y + 36), color, 5)
        draw.text((x + 108, y + 20), f"{label}: Born filter", font=f12, fill="#222")

    out = Path("figures/interface_wall_filter.png")
    img.resize((WIDTH // SCALE, HEIGHT // SCALE), Image.Resampling.LANCZOS).save(out)
    print(out)


if __name__ == "__main__":
    main()
