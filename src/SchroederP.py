from functools import cache
from _tabltypes import MakeTriangle

"""Schroeder bilateral paths.


[0]     1;
[1]     2,     1;
[2]     6,     6,     1;
[3]    20,    30,    12,     1;
[4]    70,   140,    90,    20,     1;
[5]   252,   630,   560,   210,    30,    1;
[6]   924,  2772,  3150,  1680,   420,   42,    1;
[7]  3432, 12012, 16632, 11550,  4200,  756,   56,  1;
[8] 12870, 51480, 84084, 72072, 34650, 9240, 1260, 72, 1;
"""


@cache
def schroederpaths(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = schroederpaths(n - 1) + [1]

    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * (2 * n - k)) // k
    row[0] = (row[0] * (4 * n - 2)) // n

    return row


@MakeTriangle(schroederpaths, "SchroederP", ["A104684", "A063007"], True)
def SchroederPaths(n: int, k: int) -> int:
    return schroederpaths(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(SchroederPaths)
