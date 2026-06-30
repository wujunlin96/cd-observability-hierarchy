"""Order-of-magnitude estimates for macroscopic C-D routes.

This script is intentionally simple. It does not assert a model is viable;
it gives scale targets for clock-holonomy and defect/interface ideas.
"""

from __future__ import annotations

import csv
from pathlib import Path

C = 299_792_458.0  # m/s


def delay_factor(xi: float) -> float:
    """Magnitude of |1 - C/D| for D/C = sqrt(1 + xi)."""
    if xi <= -1:
        raise ValueError("xi must be greater than -1")
    return abs(1.0 - 1.0 / (1.0 + xi) ** 0.5)


def length_for_delay(delta_t_s: float, xi: float) -> float:
    """D-segment length needed for a C-D travel-time offset delta_t."""
    f = delay_factor(xi)
    if f == 0:
        return float("inf")
    return C * delta_t_s / f


def main() -> None:
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)

    clock_rows = []
    for label, freq_hz in [
        ("gps_clock_10MHz", 1.0e7),
        ("microwave_clock_9GHz", 9.192631770e9),
        ("optical_clock_4e14Hz", 4.0e14),
        ("optical_clock_1e15Hz", 1.0e15),
        ("rb87_compton", 1.963e25),
    ]:
        one_rad_s = 1.0 / (2.0 * 3.141592653589793 * freq_hz)
        clock_rows.append(
            {
                "clock": label,
                "frequency_hz": f"{freq_hz:.9e}",
                "delta_tau_for_1_rad_s": f"{one_rad_s:.9e}",
                "delta_tau_for_0p01_rad_s": f"{0.01 * one_rad_s:.9e}",
            }
        )

    with (out_dir / "cd_macro_clock_holonomy_scales.csv").open(
        "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=clock_rows[0].keys())
        writer.writeheader()
        writer.writerows(clock_rows)

    delay_rows = []
    for delay_label, dt in [
        ("1_ns", 1e-9),
        ("1_us", 1e-6),
        ("1_ms", 1e-3),
        ("1_s", 1.0),
    ]:
        for xi in [1.0, 1e-3, 1e-6, 1e-9]:
            delay_rows.append(
                {
                    "target_delay": delay_label,
                    "delta_t_s": f"{dt:.9e}",
                    "xi": f"{xi:.9e}",
                    "D_over_C": f"{(1.0 + xi) ** 0.5:.9e}",
                    "required_D_segment_m": f"{length_for_delay(dt, xi):.9e}",
                    "required_D_segment_km": f"{length_for_delay(dt, xi)/1000.0:.9e}",
                }
            )

    with (out_dir / "cd_macro_defect_delay_scales.csv").open(
        "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=delay_rows[0].keys())
        writer.writeheader()
        writer.writerows(delay_rows)

    wall_rows = []
    v_dm = 300_000.0  # m/s
    for duration_label, duration_s in [
        ("1_s", 1.0),
        ("1_min", 60.0),
        ("1_hour", 3600.0),
        ("1_day", 86400.0),
    ]:
        wall_rows.append(
            {
                "crossing_duration": duration_label,
                "duration_s": f"{duration_s:.9e}",
                "assumed_wall_speed_m_s": f"{v_dm:.9e}",
                "wall_thickness_m": f"{v_dm * duration_s:.9e}",
                "wall_thickness_km": f"{v_dm * duration_s / 1000.0:.9e}",
            }
        )

    with (out_dir / "cd_macro_wall_crossing_scales.csv").open(
        "w", newline="", encoding="utf-8"
    ) as f:
        writer = csv.DictWriter(f, fieldnames=wall_rows[0].keys())
        writer.writeheader()
        writer.writerows(wall_rows)

    for path in [
        "cd_macro_clock_holonomy_scales.csv",
        "cd_macro_defect_delay_scales.csv",
        "cd_macro_wall_crossing_scales.csv",
    ]:
        print(out_dir / path)


if __name__ == "__main__":
    main()
