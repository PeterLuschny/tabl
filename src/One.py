from functools import cache
from _tabltypes import set_attributes

"""Uno, the all 1's triangle.

[0]  1
[1]  1,  1
[2]  1,  1,  1
[3]  1,  1,  1,  1
[4]  1,  1,  1,  1,  1
[5]  1,  1,  1,  1,  1,  1
[6]  1,  1,  1,  1,  1,  1,  1
[7]  1,  1,  1,  1,  1,  1,  1,  1
[8]  1,  1,  1,  1,  1,  1,  1,  1,  1
"""


@cache
def _one(n: int) -> list[int]:
    if n == 0:
        return [1]

    return _one(n - 1) + [1]


@set_attributes(
    _one, 
    "One", 
    ['A000012', 'A008836', 'A014077'], 
    True)
def one(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _one(n).copy()
    return _one(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(one)
