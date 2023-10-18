from functools import cache
from _tabltypes import set_attributes

"""Bessel2 triangle.

[0] 1
[1] 1, 0
[2] 1, 0,  1
[3] 1, 0,  3, 0
[4] 1, 0,  6, 0,   3
[5] 1, 0, 10, 0,  15, 0
[6] 1, 0, 15, 0,  45, 0,   15
[7] 1, 0, 21, 0, 105, 0,  105, 0
[8] 1, 0, 28, 0, 210, 0,  420, 0, 105
[9] 1, 0, 36, 0, 378, 0, 1260, 0, 945, 0
"""


@cache
def bessel2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]

    row = bessel2(n - 1) + [0]
    row[n] = 0 if n % 2 else row[n - 2]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row


@set_attributes(
    bessel2,
    "Bessel2",
    ["A359760", "A073278", "A066325", "A099174", "A111924", "A144299", "A104556"],
    False,
)
def Bessel2(n: int, k: int) -> int:
    return bessel2(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Bessel2)
