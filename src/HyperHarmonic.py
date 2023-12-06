from functools import cache
from _tabltypes import MakeTriangle

"""The hyperharmonic numbers.

[0]    1;
[1]    1,     1;
[2]    2,     3,    1;
[3]    6,    11,    5,    1;
[4]   24,    50,   26,    7,   1;
[5]  120,   274,  154,   47,   9,   1;
[6]  720,  1764, 1044,  342,  74,  11,  1;
[7] 5040, 13068, 8028, 2754, 638, 107, 13, 1;
"""


@cache
def hyperharmonic(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = hyperharmonic(n - 1) + [1]

    for m in range(n - 1, 0, -1):
        row[m] = (n - m + 1) * row[m] + row[m - 1]
    row[0] *= n

    return row


@MakeTriangle(hyperharmonic, "HyperHarmonic", ["A165675", "A093905", "A105954", "A165674"], True)
def HyperHarmonic(n: int, k: int) -> int:
    return hyperharmonic(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(HyperHarmonic)
