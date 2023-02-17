from functools import cache
from _tabltypes import set_attributes
from CompositionMax import compomax

"""Compositions of n with exact k parts.
[0]  1;
[1]  0,  1;
[2]  0,  1,  1;
[3]  0,  1,  2,   1;
[4]  0,  1,  4,   2,   1;
[5]  0,  1,  7,   5,   2,  1;
[6]  0,  1, 12,  11,   5,  2,  1;
[7]  0,  1, 20,  23,  12,  5,  2,  1;
[8]  0,  1, 33,  47,  27, 12,  5,  2, 1;
[9]  0,  1, 54,  94,  59, 28, 12,  5, 2, 1;
"""


@cache
def composition(n: int) -> list[int]:

    if n == 0: return [1] 

    cm = compomax(n)
    return [cm[k] - cm[k - 1] if k > 0 else 0 for k in range(n + 1) ]


@set_attributes(
    composition,
    "Composition",
    ['A048004'],
    True)
def Composition(n: int, k: int) -> int:
    return composition(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Composition, 8, True)
