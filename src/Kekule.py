from functools import cache
from DistLattices import dist_latt
from _tabltypes import MakeTriangle

"""Kekule triangle.

  [0] 1;
  [1] 1,  1;
  [2] 1,  2,  1;
  [3] 1,  3,  3,  1;
  [4] 1,  5,  6,  4,  1;
  [5] 1,  8, 14, 10,  5,  1;
  [6] 1, 13, 31, 30, 15,  6, 1;
  [7] 1, 21, 70, 85, 55, 21, 7, 1;
"""

@cache
def kekule(n: int) -> list[int]:
    return [dist_latt(n - k, k) for k in range(n + 1)]


@MakeTriangle(kekule, "Kekule", ["A050446", "A050447"], False)
def Kekule(n: int, k: int) -> int:
    return kekule(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Kekule)
    #for n in range(9): print(kekule(n))

"""
    # A050446
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 3, 6, 10, 15, 21, 28, 36, 45]
    [1, 5, 14, 30, 55, 91, 140, 204, 285]
    [1, 8, 31, 85, 190, 371, 658, 1086, 1695]
    [1, 13, 70, 246, 671, 1547, 3164, 5916, 10317]
    [1, 21, 157, 707, 2353, 6405, 15106, 31998, 62349]
    [1, 34, 353, 2037, 8272, 26585, 72302, 173502, 377739]
    [1, 55, 793, 5864, 29056, 110254, 345775, 940005, 2286648]
    [1, 89, 1782, 16886, 102091, 457379, 1654092, 5094220, 13846117]
"""
