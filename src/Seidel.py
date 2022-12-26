from functools import cache
from _tabltypes import set_attributes

"""Seidel triangle.

[0] [1]
[1] [0,   1]
[2] [0,   1,   1]
[3] [0,   1,   2,   2]
[4] [0,   2,   4,   5,    5]
[5] [0,   5,  10,  14,   16,   16]
[6] [0,  16,  32,  46,   56,   61,   61]
[7] [0,  61, 122, 178,  224,  256,  272,  272]
"""


@cache
def _seidel(n: int) -> list[int]:
    if n == 0:
        return [1]

    rowA: list[int] = _seidel(n - 1)
    row: list[int] = [0] + _seidel(n - 1)
    row[1] = row[n]
    for k in range(2, n + 1):
        row[k] = row[k - 1] + rowA[n - k]
    return row


@set_attributes(
    _seidel, 
    "Seidel", 
    ['A008281', 'A008282', 'A010094'], 
    False)
def seidel(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _seidel(n).copy()
    return _seidel(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(seidel)
