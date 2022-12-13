from functools import cache
from _tabltypes import set_attributes

"""von Neumann ordinals (kind of), 
[A002260, A002262*, A004736, A025581]


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


@set_attributes(_ordinals, "ORDINALNUMBR", False)
def ordinals(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _ordinals(n).copy()
    return _ordinals(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(ordinals)
