from functools import cache
from _tabltypes import set_attributes

"""Coefficients of Chebyshev T(n, x) polynomials.
[A039991, A053120, A081265]

[0]   1;
[1]   0,  1;
[2]  -1,  0,   2;
[3]   0, -3,   0,    4;
[4]   1,  0,  -8,    0,    8;
[5]   0,  5,   0,  -20,    0,    16;
[6]  -1,  0,  18,    0,  -48,     0    32;
[7]   0, -7,   0,   56,    0,  -112     0,   64;
[8]   1,  0, -32,    0,  160,     0  -256,    0,  128;
[9]   0,  9,   0, -120,    0,   432     0, -576,    0,  256;
"""


@cache
def _chebyshevT(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    rov: list[int] = _chebyshevT(n - 2)
    row: list[int] = [0] + _chebyshevT(n - 1) 
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] =  2 * row[k] - rov[k]
    return row


@set_attributes(_chebyshevT, "CHEBYSHEVTPO", True)
def chebyshevT(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _chebyshevT(n).copy()
    return _chebyshevT(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(chebyshevT)
