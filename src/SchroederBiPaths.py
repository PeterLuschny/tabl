from functools import cache
from tabltypes import set_name

"""Schroeder bilateral paths, A104684 (see also A063007).

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
def _bilatpath(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = _bilatpath(n - 1) + [1]
    
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * (2 * n - k)) // k
    row[0] = (row[0] * (4 * n - 2)) // n
    return row


@set_name(_bilatpath, "SCHBILATERAL")
def bilatpath(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _bilatpath(n).copy()
    return _bilatpath(n)[k]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(bilatpath)
