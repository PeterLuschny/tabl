from functools import cache
from math import factorial
from sympy import Symbol, Poly
from _tabltypes import set_attributes

"""Sylvester polynomials. 
[A341101]

[0] 1;
[1] 0,   2;
[2] 0,   1,    4;
[3] 0,   2,    6,    8;
[4] 0,   6,   19,   24,   16;
[5] 0,  24,   80,  110,   80,   32;
[6] 0, 120,  418,  615,  500,  240,  64;
[7] 0, 720, 2604, 4046, 3570, 1960, 672, 128;
"""


@cache
def L(n, m, x):
    if n == 0:
        return 1
    if n == 1:
        return 1 - m - 2 * x

    return ((2 * (n  - x) - m - 1) * L(n - 1, m, x) / n 
          - (n  - x - m - 1) * L(n - 2, m, x) / n)


@cache
def _sylvester(n: int) -> list[int]:
    x = Symbol("x")
    p = (-1) ** n * factorial(n) * L(n, n, x)
    return list(reversed(Poly(p, x).all_coeffs()))


@set_attributes(_sylvester, "SYLVESTERPOL", False)
def sylvester(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _sylvester(n).copy()
    return _sylvester(n)[k]


if __name__ == "__main__":
    from _tablviews import PrintViews

    PrintViews(sylvester, 8, True)