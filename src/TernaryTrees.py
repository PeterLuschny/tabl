from functools import cache
from itertools import accumulate
from tabltypes import set_name

"""Ternary trees, Fuss-Catalan 2, A355172.

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
def _ternary_tree(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row: list[int] = _ternary_tree(n - 1) + [_ternary_tree(n - 1)[n - 1]]
    return list(accumulate(accumulate(row)))


@set_name(_ternary_tree, "TERNARYTREES")
def ternary_tree(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _ternary_tree(n).copy()
    return _ternary_tree(n)[k]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(ternary_tree)
