from functools import cache
from itertools import accumulate
from _tabltypes import set_attributes
from Partition import _partnum_exact

"""Partition numbers at most.

[0] 1
[1] 0, 1
[2] 0, 1, 2
[3] 0, 1, 2,  3
[4] 0, 1, 3,  4,  5
[5] 0, 1, 3,  5,  6,  7
[6] 0, 1, 4,  7,  9, 10, 11
[7] 0, 1, 4,  8, 11, 13, 14, 15
[8] 0, 1, 5, 10, 15, 18, 20, 21, 22
[9] 0, 1, 5, 12, 18, 23, 26, 28, 29, 30
"""


@cache
def _partnum_max(n: int) -> list[int]:
    return list(accumulate(_partnum_exact(n)))


@set_attributes(
    _partnum_max, 
    "PartitionMax", 
    ['A008284', 'A058398', 'A072233'], 
    False)
def partnum_max(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _partnum_max(n).copy()
    return _partnum_max(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(partnum_max)