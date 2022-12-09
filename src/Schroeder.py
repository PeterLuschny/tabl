from functools import cache
from _tabltypes import set_attributes

"""Schroeder triangle, 
['A033877 ', 'A080245 ', 'A080247 ', 'A122538*'].


[0] [1]
[1] [0,     1]
[2] [0,     2,     1]
[3] [0,     6,     4,     1]
[4] [0,    22,    16,     6,    1]
[5] [0,    90,    68,    30,    8,    1]
[6] [0,   394,   304,   146,   48,   10,   1]
[7] [0,  1806,  1412,   714,  264,   70,  12,   1]
[8] [0,  8558,  6752,  3534, 1408,  430,  96,  14,  1]
[9] [0, 41586, 33028, 17718, 7432, 2490, 652, 126, 16, 1]
"""


@cache
def _schroeder(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row: list[int] = _schroeder(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + row[k + 1]
    return row


@set_attributes(_schroeder, "SCHROEDERTRI", True)
def schroeder(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _schroeder(n).copy()
    return _schroeder(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(schroeder)
