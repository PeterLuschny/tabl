from functools import cache
from tabltools import TablGenerator

"""Stirling set numbers, A048993.

[0]  1
[1]  0, 1
[2]  0, 1,   1
[3]  0, 1,   3,    1
[4]  0, 1,   7,    6,    1
[5]  0, 1,  15,   25,   10,    1
[6]  0, 1,  31,   90,   65,   15,    1
[7]  0, 1,  63,  301,  350,  140,   21,   1
[8]  0, 1, 127,  966, 1701, 1050,  266,  28,  1
[9]  0, 1, 255, 3025, 7770, 6951, 2646, 462, 36, 1
"""


@cache
def _sts(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [0] + _sts(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row


stirling_set = TablGenerator(_sts)


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(stirling_set)
