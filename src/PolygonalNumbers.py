from functools import cache
from tabltypes import tabl, tstruct

"""Polygonal numbers, A139600

[0 ] Nonnegatives . A001477: 0,  1,  2,  3,  4,   5,   6,   7, ...
[1 ] Triangulars .. A000217: 0,  1,  3,  6, 10,  15,  21,  28, ...
[2 ] Squares ...... A000290: 0,  1,  4,  9, 16,  25,  36,  49, ...
[3 ] Pentagonals .. A000326: 0,  1,  5, 12, 22,  35,  51,  70, ...
[4 ] Hexagonals ... A000384: 0,  1,  6, 15, 28,  45,  66,  91, ...
[5 ] Heptagonals .. A000566: 0,  1,  7, 18, 34,  55,  81, 112, ...
[6 ] Octagonals ... A000567: 0,  1,  8, 21, 40,  65,  96, 133, ...
[7 ] 9-gonals ..... A001106: 0,  1,  9, 24, 46,  75, 111, 154, ...
[8 ] 10-gonals .... A001107: 0,  1, 10, 27, 52,  85, 126, 175, ...
[9 ] 11-gonals .... A051682: 0,  1, 11, 30, 58,  95, 141, 196, ...
[10] 12-gonals .... A051624: 0,  1, 12, 33, 64, 105, 156, 217, ...

Triangle view:
[0] [0]
[1] [0, 1]
[2] [0, 1, 2]
[3] [0, 1, 3,  3]
[4] [0, 1, 4,  6,  4]
[5] [0, 1, 5,  9, 10,  5]
[6] [0, 1, 6, 12, 16, 15,  6]
[7] [0, 1, 7, 15, 22, 25, 21, 7]
"""


@cache
def _polygonal(n: int) -> list[int]:
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]

    rov: list[int] = _polygonal(n - 2)
    row: list[int] = _polygonal(n - 1) + [n]
    row[n - 1] += row[n - 2]
    for k in range(2, n - 1):
        row[k] += row[k] - rov[k]
    return row


@tstruct(_polygonal, "POLYGONALNUM")
def polygonal(size: int) -> tabl: 
    return [_polygonal(j) for j in range(size)]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(polygonal)
