from functools import cache
from _tabltypes import set_attributes
from Binomial import binomial

"""Lozanic numbers. 
[A034851]


[0]  1;
[1]  1,  1;
[2]  1,  1,  1;
[3]  1,  2,  2,  1;
[4]  1,  2,  4,  2,  1;
[5]  1,  3,  6,  6,  3,  1;
[6]  1,  3,  9, 10,  9,  3,  1;
[7]  1,  4, 12, 19, 19, 12,  4,  1;
[8]  1,  4, 16, 28, 38, 28, 16,  4,  1;
[9]  1,  5, 20, 44, 66, 66, 44, 20,  5,  1;
"""

@cache
def _lozanic(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] =  [1] + _lozanic(n - 1)  
    for k in range(1, n):
        row[k] += row[k + 1]

    if n % 2 != 0:
        return row

    for k in range(1, n, 2):
        row[k] -= binomial(n // 2 - 1, (k - 1) // 2)

    return row


@set_attributes(_lozanic, "LOZANICTRIAN", True)
def lozanic(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _lozanic(n).copy()
    return _lozanic(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(lozanic)
