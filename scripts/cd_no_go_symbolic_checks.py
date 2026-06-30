"""Symbolic sanity checks for the C-D no-go hierarchy.

Checks:
1. Linear maps V -> V commuting with Lorentz algebra are scalar.
2. Quadratic equivariant maps Sym^2(V) -> V have dimension 0.
3. Cubic equivariant maps Sym^3(V) -> V have dimension 1, matching x^2 x.
"""

from __future__ import annotations

import itertools

import sympy as sp


def lorentz_generators() -> list[sp.Matrix]:
    zero = sp.zeros(4)

    def mat(entries: list[tuple[int, int, int]]) -> sp.Matrix:
        m = sp.zeros(4)
        for i, j, value in entries:
            m[i, j] = value
        return m

    jx = mat([(2, 3, -1), (3, 2, 1)])
    jy = mat([(1, 3, 1), (3, 1, -1)])
    jz = mat([(1, 2, -1), (2, 1, 1)])
    kx = mat([(0, 1, 1), (1, 0, 1)])
    ky = mat([(0, 2, 1), (2, 0, 1)])
    kz = mat([(0, 3, 1), (3, 0, 1)])
    return [jx, jy, jz, kx, ky, kz]


def linear_commutant_dimension() -> tuple[int, list[sp.Expr], list[sp.Symbol]]:
    variables = sp.symbols("a0:16")
    a = sp.Matrix(4, 4, variables)
    equations: list[sp.Expr] = []
    for g in lorentz_generators():
        comm = g * a - a * g
        equations.extend(list(comm))
    matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    nullspace = matrix.nullspace()
    return len(nullspace), nullspace, list(variables)


def symmetric_tuples(rank: int) -> list[tuple[int, ...]]:
    return list(itertools.combinations_with_replacement(range(4), rank))


def equivariant_map_dimension(rank: int) -> tuple[int, list[sp.Matrix], list[sp.Symbol]]:
    lower = symmetric_tuples(rank)
    variables = sp.symbols(f"t0:{4 * len(lower)}")
    index = {
        (mu, tup): variables[mu * len(lower) + i]
        for mu in range(4)
        for i, tup in enumerate(lower)
    }

    def coeff(mu: int, indices: tuple[int, ...]) -> sp.Symbol:
        return index[(mu, tuple(sorted(indices)))]

    equations: list[sp.Expr] = []
    for g in lorentz_generators():
        for mu in range(4):
            for inds in lower:
                expr = sum(g[mu, a] * coeff(a, inds) for a in range(4))
                for slot in range(rank):
                    expr -= sum(
                        g[a, inds[slot]]
                        * coeff(mu, inds[:slot] + (a,) + inds[slot + 1 :])
                        for a in range(4)
                    )
                equations.append(sp.expand(expr))

    matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    nullspace = matrix.nullspace()
    return len(nullspace), nullspace, list(variables)


def cubic_candidate_residual() -> list[sp.Expr]:
    eta = sp.diag(1, -1, -1, -1)
    lower = symmetric_tuples(3)

    def c(mu: int, inds: tuple[int, int, int]) -> sp.Expr:
        nu, rho, sigma = inds
        return sp.Rational(1, 3) * (
            (1 if mu == nu else 0) * eta[rho, sigma]
            + (1 if mu == rho else 0) * eta[nu, sigma]
            + (1 if mu == sigma else 0) * eta[nu, rho]
        )

    residuals: list[sp.Expr] = []
    for g in lorentz_generators():
        for mu in range(4):
            for inds in lower:
                expr = sum(g[mu, a] * c(a, inds) for a in range(4))
                for slot in range(3):
                    expr -= sum(
                        g[a, inds[slot]]
                        * c(mu, inds[:slot] + (a,) + inds[slot + 1 :])
                        for a in range(4)
                    )
                residuals.append(sp.simplify(expr))
    return residuals


def main() -> None:
    linear_dim, linear_basis, linear_vars = linear_commutant_dimension()
    print("linear_commutant_dim =", linear_dim)
    print("linear_basis_vector =", linear_basis[0].T if linear_basis else None)

    quad_dim, _, _ = equivariant_map_dimension(rank=2)
    print("quadratic_equivariant_dim =", quad_dim)

    cubic_dim, _, _ = equivariant_map_dimension(rank=3)
    print("cubic_equivariant_dim =", cubic_dim)
    print("cubic_x2x_residual_zero =", all(r == 0 for r in cubic_candidate_residual()))


if __name__ == "__main__":
    main()
