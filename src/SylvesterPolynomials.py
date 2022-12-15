from functools import cache
from Binomial import binomial
from StirlingCycle import stirling_cycle
from _tabltypes import set_attributes

"""Sylvester polynomials. 
[A341101]

[0] 1;
[1] 0,   2;
[2] 0,   1,    4;
[3] 0,   2,    6,    8;
[4] 0,   6,   19,   24,   16;
[5] 0,  24,   80,  110,   80,   32;
[6] 0, 120,  418,  615,  500,  240,  64;
[7] 0, 720, 2604, 4046, 3570, 1960, 672, 128;
"""

@cache
def _sylvester(n: int) -> list[int]:
    return [sum(binomial(n, k - j) * stirling_cycle(n - k + j, j)
            for j in range(k + 1)) for k in range(n + 1)]


@set_attributes(_sylvester, "SYLVESTERPOL", False)
def sylvester(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _sylvester(n).copy()
    return _sylvester(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(sylvester)
