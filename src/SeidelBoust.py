from functools import cache
from _tabltypes import set_attributes
from Seidel import _seidel


"""Seidel boustrophedon:

[0] [ 1]
[1] [ 0,  1]
[2] [ 1,  1,   0]
[3] [ 0,  1,   2,   2]
[4] [ 5,  5,   4,   2,   0]
[5] [ 0,  5,  10,  14,  16,  16]
[6] [61, 61,  56,  46,  32,  16,   0]
[7] [ 0, 61, 122, 178, 224, 256, 272, 272]
"""

# #@
# sim = ['A008280', 'A108040', 'A236935', 'A239005']


def _seidel_boust(n: int) -> list[int]:
    return _seidel(n) if n % 2 else _seidel(n)[::-1]


@set_attributes(
    _seidel_boust, 
    "SeidelBoust", 
    ['A008280', 'A108040', 'A236935', 'A239005'], 
    False)
def seidel_boust(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _seidel_boust(n).copy()
    return _seidel_boust(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(seidel_boust)
