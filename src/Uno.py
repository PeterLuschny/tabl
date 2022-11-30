from functools import cache
from tabltypes import set_attributes

"""Uno, the all 1's triangle, A000012.

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
def _uno(n: int) -> list[int]:
    if n == 0:
        return [1]

    return _uno(n - 1) + [1]


@set_attributes(_uno, "UNOPERTUTTIS", True)
def uno(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _uno(n).copy()
    return _uno(n)[k]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(uno)
