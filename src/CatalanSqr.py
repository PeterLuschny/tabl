from functools import cache
from _tabltypes import MakeTriangle

"""The Riordan square of the Catalan numbers in the sense of A321620.

[0]    1;
[1]    1,     1;
[2]    2,     3,     1;
[3]    5,     9,     5,    1;
[4]   14,    28,    20,    7,    1;
[5]   42,    90,    75,   35,    9,    1;
[6]  132,   297,   275,  154,   54,   11,   1;
[7]  429,  1001,  1001,  637,  273,   77,  13,   1;
[8] 1430,  3432,  3640, 2548, 1260,  440, 104,  15,  1;
[9] 4862, 11934, 13260, 9996, 5508, 2244, 663, 135, 17, 1;
"""


@cache
def catalansqr(n: int) -> list[int]:
    if n == 0:
        return [1]

    pow = catalansqr(n - 1) + [0]
    row = pow.copy()
    row[0] += row[1]
    row[n] = 1

    for k in range(n - 1, 0, -1):
        row[k] = pow[k - 1] + 2 * pow[k] + pow[k + 1]

    return row


@MakeTriangle(catalansqr, "CatalanSqr", ["A039599", "A050155"], True)
def CatalanSqr(n: int, k: int) -> int:
    return catalansqr(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(CatalanSqr)
