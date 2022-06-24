from functools import cache
from tabltools import TablGenerator

"""Ternary trees, unsigned A109956, A001764. 

[0]     1
[1]     1,     1
[2]     3,     4,     1
[3]    12,    18,     7,     1
[4]    55,    88,    42,    10,    1
[5]   273,   455,   245,    75,   13,    1
[6]  1428,  2448,  1428,   510,  117,   16,   1
[7]  7752, 13566,  8379,  3325,  910,  168,  19,  1
[8] 43263, 76912, 49588, 21252, 6578, 1472, 228, 22, 1
"""


@cache
def _ttr(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = _ttr(n - 1) + [1]
    z = 3 * n * (3 * n - 1) * (3 * n - 2)
    for k in range(n):
        u = (n - k) * (k + 2 * n) * (k + 2 * n + 1)
        row[k] = (row[k] * z) // u
    return row


ternary_tree = TablGenerator(_ttr)


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(ternary_tree)
