from functools import cache
from _tabltypes import MakeTriangle

"""Motzkin triangle, coefficients of Motzkin polynomials.

[0] 1
[1] 1, 0
[2] 1, 0,  1
[3] 1, 0,  3, 0
[4] 1, 0,  6, 0,   2
[5] 1, 0, 10, 0,  10, 0
[6] 1, 0, 15, 0,  30, 0,   5
[7] 1, 0, 21, 0,  70, 0,  35, 0
[8] 1, 0, 28, 0, 140, 0, 140, 0,  14
[9] 1, 0, 36, 0, 252, 0, 420, 0, 126, 0
"""


@cache
def motzkin(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]

    l = 0 if n % 2 else (motzkin(n - 2)[n - 2] * 2 * (n - 1)) // (n // 2 + 1)
    row = motzkin(n - 1) + [l]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row


@MakeTriangle(motzkin, "Motzkin", ["A359364"], False)
def Motzkin(n: int, k: int) -> int:
    return motzkin(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Motzkin)


""" Alternative:
from Binomial import Binomial
@cache
def motzkin(n: int) -> list[int]:
    def Catalan(n: int) -> int:
        return Binomial(2 * n, n) // (n + 1)
    
    return [Binomial(n, k) * Catalan(k // 2) if k % 2 == 0 else 0 for k in range(n + 1)]
"""
