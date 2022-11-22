from functools import cache
from tabltypes import tabl, tstruct

"""Delannoy triangle, A008288.

[0] [1]
[1] [1,  1]
[2] [1,  3,   1]
[3] [1,  5,   5,   1]
[4] [1,  7,  13,   7,   1]
[5] [1,  9,  25,  25,   9,   1]
[6] [1, 11,  41,  63,  41,  11,   1]
[7] [1, 13,  61, 129, 129,  61,  13,   1]
[8] [1, 15,  85, 231, 321, 231,  85,  15,  1]
[9] [1, 17, 113, 377, 681, 681, 377, 113, 17, 1]
"""


@cache
def _delannoy(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    rowA: list[int] = _delannoy(n - 2)
    row: list[int] = _delannoy(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + rowA[k - 1]
    return row


@tstruct(_delannoy, "DELANNOYTRIA")
def delannoy(size: int) -> tabl: 
    return [_delannoy(j) for j in range(size)]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(delannoy)
