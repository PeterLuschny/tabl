from functools import cache
from itertools import accumulate
from _tabltypes import set_attributes


"""Catalan triangle, Fuss-Catalan 1, A355173.

[0] [1]
[1] [0, 1]
[2] [0, 1, 2]
[3] [0, 1, 3,  5]
[4] [0, 1, 4,  9, 14]
[5] [0, 1, 5, 14, 28,  42]
[6] [0, 1, 6, 20, 48,  90, 132]
[7] [0, 1, 7, 27, 75, 165, 297, 429]
"""


@cache
def _catalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row: list[int] = _catalan(n - 1) + [_catalan(n - 1)[n - 1]]
    return list(accumulate(row))


@set_attributes(_catalan, "FUSSCATALAN1", False)
def catalan(n: int, k:int = -1) -> list[int] | int:
    if k == -1: return _catalan(n).copy()
    return _catalan(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(catalan)
