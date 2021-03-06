from functools import cache
from tabltypes import tabl, tvals

"""The all 1's triangle, A000012.

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


@tvals(_uno, "UNOALL")
def uno(size: int) -> tabl: 
    return [_uno(j) for j in range(size)]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(uno)
