from functools import cache
from _tabltypes import set_attributes


"""Narayana triangle, 
[A001263, A090181*, A131198].


[0]  1;
[1]  0,  1;
[2]  0,  1,   1;
[3]  0,  1,   3,    1;
[4]  0,  1,   6,    6,     1;
[5]  0,  1,  10,   20,    10,     1;
[6]  0,  1,  15,   50,    50,    15,     1;
[7]  0,  1,  21,  105,   175,   105,    21,    1;
[8]  0,  1,  28,  196,   490,   490,   196,   28,   1;
[9]  0,  1,  36,  336,  1176,  1764,  1176,  336,  36,  1;
"""


@cache
def _narayana(n: int) -> list[int]:
    if n < 3:
        return ([1], [0, 1], [0, 1, 1])[n]

    a: list[int] = _narayana(n - 2) + [0, 0]
    row: list[int] = _narayana(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = (
            (row[k] + row[k - 1]) * (2 * n - 1)
            - (a[k] - 2 * a[k - 1] + a[k - 2]) * (n - 2)
        ) // (n + 1)
    return row


@set_attributes(_narayana, "NARAYANATRIA", True)
def narayana(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _narayana(n).copy()
    return _narayana(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(narayana)
