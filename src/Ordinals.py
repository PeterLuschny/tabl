from functools import cache
from _tabltypes import set_attributes

"""von Neumann ordinals (kind of), 
['A002260 ', 'A002262*', 'A004736 ', 'A025581 ', 'A025646 ', 
'A025650 ', 'A025651 ', 'A025659 ', 'A025660 ', 'A025661 ', 
'A025668 ', 'A025669 ', 'A025670 ', 'A025674 ', 'A025675 ', 
'A025676 ', 'A025677 ', 'A025681 ', 'A025682 ', 'A025683 ', 
'A025690 ', 'A025691 ', 'A122200 ', 'A136261 ', 'A140756 ', 
'A163351 ', 'A166352 ', 'A189768 ', 'A194905 ', 'A194908 ', 
'A298486 ', 'A330238 ']


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
