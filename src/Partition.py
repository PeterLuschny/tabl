from functools import cache
from itertools import accumulate
from _tabltypes import set_attributes

"""Partition numbers (Euler's table), see also A026820, A000041.

[0] 1
[1] 0, 1
[2] 0, 1, 1
[3] 0, 1, 1, 1
[4] 0, 1, 2, 1, 1
[5] 0, 1, 2, 2, 1, 1
[6] 0, 1, 3, 3, 2, 1, 1
[7] 0, 1, 3, 4, 3, 2, 1, 1
[8] 0, 1, 4, 5, 5, 3, 2, 1, 1
[9] 0, 1, 4, 7, 6, 5, 3, 2, 1, 1
"""

# sim = ['A008284', 'A058398', 'A072233']

@cache
def _part(n: int, k: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return 1 if n == 0 else 0

    return _part(n - 1, k - 1) + _part(n - k, k)


@cache
def _partnum_exact(n: int) -> list[int]:
    return [_part(n, k) for k in range(n + 1)]


@set_attributes(
    _partnum_exact, 
    "Partition", 
    ['A008284', 'A058398', 'A072233'], 
    True)
def partnum_exact(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _partnum_exact(n).copy()
    return _partnum_exact(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(partnum_exact)
