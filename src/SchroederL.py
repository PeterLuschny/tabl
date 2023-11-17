from functools import cache
from _tabltypes import MakeTriangle

"""Little Schroeder triangle.
[0]      1;
[1]      1,      1;
[2]      3,      4,      1;
[3]     11,     17,      7,     1;
[4]     45,     76,     40,    10,     1;
[5]    197,    353,    216,    72,    13,     1;
[6]    903,   1688,   1345,   458,   113,    16,    1;
[7]   4279,   8257,   6039,  2745,   829,   163,   19,   1;
[8]  20793,  41128,  31864, 15932,  5558,  1356,  222,  22,  1;
[9] 103049, 207905, 168584, 90776, 35318, 10070, 2066, 290, 25, 1;
"""


@cache
def schroederl(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    arow = schroederl(n - 1) + [0]
    row = schroederl(n - 1) + [1]

    row[0] = row[0] + 2 * row[1]
    for k in range(1, n):
        row[k] = arow[k - 1] + 3 * arow[k] + 2 * arow[k + 1]

    return row


@MakeTriangle(schroederl, "SchroederL", ["A172094"], True)
def SchroederL(n: int, k: int) -> int:
    return schroederl(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(SchroederL)
