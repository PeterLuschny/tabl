from functools import cache
from _tabltypes import set_attributes
from Binomial import binomial

"""Sierpiński's triangle, binomial(n, k) mod 2.

[0]                               1
[1]                              1, 1
[2]                            1, 0, 1
[3]                           1, 1, 1, 1
[4]                         1, 0, 0, 0, 1
[5]                        1, 1, 0, 0, 1, 1
[6]                      1, 0, 1, 0, 1, 0, 1
[7]                     1, 1, 1, 1, 1, 1, 1, 1
[8]                   1, 0, 0, 0, 0, 0, 0, 0, 1
[9]                  1, 1, 0, 0, 0, 0, 0, 0, 1, 1
"""


@cache
def sierpinski(n: int) -> list[int]:
    b = binomial(n)
    return [b[k] % 2 for k in range(n + 1)]


@set_attributes(
    sierpinski,
    "Sierpinski",
    ["A047999", "A090971", "A114700", "A143200", "A166282"],
    True,
)
def Sierpinski(n: int, k: int) -> int:
    return sierpinski(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Sierpinski)
