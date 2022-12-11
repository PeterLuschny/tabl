from functools import cache
from _tabltypes import set_attributes

"""Coefficients of Chebyshev S(n, x) = U(n, x/2) polynomials.
['A049310*', 'A053119', 'A112552', 'A168561']


[0]  1;
[1]  0,  1;
[2] -1,  0,   1;
[3]  0, -2,   0,   1;
[4]  1,  0,  -3,   0,  1;
[5]  0,  3,   0,  -4,  0,  1;
[6] -1,  0,   6,   0, -5,  0,  1;
[7]  0, -4,   0,  10,  0, -6,  0,   1;
[8]  1,  0, -10,   0, 15,  0, -7,   0, 1;
[9]  0,  5,   0, -20,  0,  21,  0, -8, 0, 1;
"""


@cache
def _chebyshevS(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    rov: list[int] = _chebyshevS(n - 2)
    row: list[int] = [0] + _chebyshevS(n - 1)
    for k in range(0, n - 1):
        row[k] -= rov[k]
    return row


@set_attributes(_chebyshevS, "CHEBYSHEVSPO", True)
def chebyshevS(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _chebyshevS(n).copy()
    return _chebyshevS(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(chebyshevS)
