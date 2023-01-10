from functools import cache
from _tabltypes import set_attributes

"""Motzkin triangle, coefficients of Motzkin polynomials.

[0] 1;
[1] 1, 0;
[2] 1, 0,  1;
[3] 1, 0,  3, 0;
[4] 1, 0,  6, 0,   2;
[5] 1, 0, 10, 0,  10, 0;
[6] 1, 0, 15, 0,  30, 0,   5;
[7] 1, 0, 21, 0,  70, 0,  35, 0;
[8] 1, 0, 28, 0, 140, 0, 140, 0,  14;
[9] 1, 0, 36, 0, 252, 0, 420, 0, 126, 0;
"""


@cache
def _motzkin(n: int) -> list[int]:
    if n == 0: return [1]
    if n == 1: return [1, 0]

    l = 0 if n % 2 else (_motzkin(n - 2)[n - 2] * 2 * (n - 1)) // (n // 2 + 1)
    row = _motzkin(n - 1) + [l]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row 


@set_attributes(
    _motzkin,
    "Motzkin-Poly",
    ['A'],
    True)
def motzkin(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _motzkin(n).copy()
    return _motzkin(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(motzkin)


''' Alternative:
from Binomial import binomial
@cache
def _motzkin(n: int) -> list[int]:

    def Catalan(n: int) -> int:
        return binomial(2 * n, n) // (n + 1)
    
    return [binomial(n, k) * Catalan(k // 2) if k % 2 == 0 else 0 for k in range(n + 1)]
'''