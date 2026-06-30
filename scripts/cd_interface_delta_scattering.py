"""Symbolic and numeric checks for the 1D C-D delta-interface model."""

from __future__ import annotations

import csv
from pathlib import Path

import sympy as sp


def symbolic_solution() -> dict[str, sp.Expr]:
    omega, C, D, lam = sp.symbols("omega C D lambda", positive=True, real=True)
    k_c = omega / C
    k_d = omega / D
    r_c, t_c, a_d = sp.symbols("r_C t_C a_D")

    equations = [
        sp.Eq(t_c, 1 + r_c),
        sp.Eq(2 * sp.I * k_c * r_c, lam * a_d / C**2),
        sp.Eq(2 * sp.I * k_d * a_d, lam * t_c / D**2),
    ]
    sol = sp.solve(equations, (r_c, t_c, a_d), simplify=True, dict=True)[0]

    alpha = sp.symbols("alpha", positive=True, real=True)
    alpha_sub = {lam: 2 * alpha * omega * sp.sqrt(C * D)}
    r_alpha = sp.simplify(sol[r_c].subs(alpha_sub))
    t_alpha = sp.simplify(sol[t_c].subs(alpha_sub))
    a_alpha = sp.simplify(sol[a_d].subs(alpha_sub))

    p_reflect = sp.simplify(r_alpha * sp.conjugate(r_alpha))
    p_transmit_c = sp.simplify(t_alpha * sp.conjugate(t_alpha))
    p_convert_total = sp.simplify(
        2 * D / C * a_alpha * sp.conjugate(a_alpha)
    )
    flux_sum = sp.simplify(p_reflect + p_transmit_c + p_convert_total)

    return {
        "r_C_lambda": sp.simplify(sol[r_c]),
        "t_C_lambda": sp.simplify(sol[t_c]),
        "a_D_lambda": sp.simplify(sol[a_d]),
        "r_C_alpha": r_alpha,
        "t_C_alpha": t_alpha,
        "a_D_alpha": a_alpha,
        "P_reflect": p_reflect,
        "P_transmit_C": p_transmit_c,
        "P_convert_total": p_convert_total,
        "flux_sum": flux_sum,
    }


def write_numeric_table() -> None:
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)
    rows = []
    for alpha in [1e-4, 1e-3, 1e-2, 0.1, 0.3, 1.0, 3.0, 10.0]:
        denom = (1.0 + alpha**2) ** 2
        p_reflect = alpha**4 / denom
        p_transmit_c = 1.0 / denom
        p_convert_total = 2.0 * alpha**2 / denom
        p_convert_forward = alpha**2 / denom
        p_two_wall_forward = p_convert_forward**2
        rows.append(
            {
                "alpha": f"{alpha:.9e}",
                "P_reflect_C": f"{p_reflect:.9e}",
                "P_transmit_C": f"{p_transmit_c:.9e}",
                "P_convert_total_D": f"{p_convert_total:.9e}",
                "P_convert_forward_D": f"{p_convert_forward:.9e}",
                "P_two_wall_forward_echo": f"{p_two_wall_forward:.9e}",
                "flux_sum": f"{p_reflect + p_transmit_c + p_convert_total:.9e}",
            }
        )

    path = out_dir / "cd_interface_delta_scattering.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(path)


def main() -> None:
    sol = symbolic_solution()
    for key, value in sol.items():
        print(f"{key} = {sp.simplify(value)}")
    write_numeric_table()


if __name__ == "__main__":
    main()
