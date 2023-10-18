from functools import cache
from _tabltypes import set_attributes

"""Compositions of n into at most k parts.

[0] 1;
[1] 0, 1;
[2] 0, 1,  2;
[3] 0, 1,  3,   4;
[4] 0, 1,  5,   7,   8;
[5] 0, 1,  8,  13,  15,  16;
[6] 0, 1, 13,  24,  29,  31,  32;
[7] 0, 1, 21,  44,  56,  61,  63,  64;
[8] 0, 1, 34,  81, 108, 120, 125, 127, 128;
[9] 0, 1, 55, 149, 208, 236, 248, 253, 255, 256;
"""


@cache
def compomax(n: int) -> list[int]:
    @cache
    def t(n: int, k: int) -> int:
        if n == 0 or k == 1:
            return 1
        return sum(t(n - j, k) for j in range(1, min(n, k) + 1))

    return [t(n, k) for k in range(n + 1)]


@set_attributes(compomax, "CompositionMax", ["A126198"], False)
def CompoMax(n: int, k: int) -> int:
    return compomax(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(CompoMax, 8, True)
