from functools import cache
from tabltypes import set_name

"""von Neumann ordinals (kind of), A002262.

[0] [0]
[1] [0,  1]
[2] [0,  1,  2]
[3] [0,  1,  2,  3]
[4] [0,  1,  2,  3,  4]
[5] [0,  1,  2,  3,  4,  5]
[6] [0,  1,  2,  3,  4,  5,  6]
[7] [0,  1,  2,  3,  4,  5,  6,  7]
"""


@cache
def _ordinals(n: int) -> list[int]:
    if n == 0:
        return [0]

    return _ordinals(n - 1) + [n]


@set_name(_ordinals, "ORDINALNUMBR")
def ordinals(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _ordinals(n).copy()
    return _ordinals(n)[k]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(ordinals)
