from functools import cache
from _tabltypes import MakeTriangle

"""Zarankiewicz triangle.

[0]  1;
[1]  2,  4;
[2]  4,  8,  16;
[3]  6, 12,  24,  36;
[4]  9, 18,  36,  54,  81;
[5] 12, 24,  48,  72, 108, 144;
[6] 16, 32,  64,  96, 144, 192, 256;
[7] 20, 40,  80, 120, 180, 240, 320, 400;
[8] 25, 50, 100, 150, 225, 300, 400, 500, 625;
"""


@cache
def zarankiewicz(n: int) -> list[int]:
    def s(n: int): return (1 + n // 2) * (1 + (n + 1) // 2)

    sn = s(n)
    return [sn * s(k) for k in range(n + 1)]


@MakeTriangle(
    zarankiewicz,
    "Zarankiewicz",
    ["A298368"],
    False,
)
def Zarankiewicz(n: int, k: int) -> int:
    return zarankiewicz(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Zarankiewicz)
