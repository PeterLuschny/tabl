from functools import cache
from itertools import accumulate
from _tabltypes import MakeTriangle

"""Ternary trees, Fuss-Catalan 2.


[0] [1]
[1] [0, 1]
[2] [0, 1,  3]
[3] [0, 1,  5, 12]
[4] [0, 1,  7, 25,  55]
[5] [0, 1,  9, 42, 130,  273]
[6] [0, 1, 11, 63, 245,  700, 1428]
[7] [0, 1, 13, 88, 408, 1428, 3876, 7752]
"""


@cache
def ternarytree(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row: list[int] = ternarytree(n - 1) + [ternarytree(n - 1)[n - 1]]

    return list(accumulate(accumulate(row)))


@MakeTriangle(ternarytree, "TernaryTrees", ["A355172"], False)
def TernaryTree(n: int, k: int) -> int:
    return ternarytree(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(TernaryTree)
