from functools import cache
from _tabltypes import MakeTriangle

"""Gaussian coefficient for q = 2.

[0]  1;
[1]  1,   1;
[2]  1,   3,    1;
[3]  1,   7,    7,     1;
[4]  1,  15,   35,    15,     1;
[5]  1,  31,  155,   155,    31,    1;
[6]  1,  63,  651,  1395,   651,   63,   1;
[7]  1, 127, 2667, 11811, 11811, 2667, 127, 1;
"""


@cache
def gaussq2(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = gaussq2(n - 1)
    pow: list[int] = [1] + gaussq2(n - 1)
    p = 2
    for k in range(1, n):
        pow[k] = row[k - 1] + p * row[k]
        p *= 2
    return pow


@MakeTriangle(gaussq2, "Gaussq2", ["A022166"], True)
def Gaussq2(n: int, k: int) -> int:
    return gaussq2(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Gaussq2, 8, True)
