from functools import cache
from tabltools import TablGenerator

"""The Motzkin triangle, A009766.

[0]    1;
[1]    1,    1;
[2]    2,    2,    1;
[3]    4,    5,    3,    1;
[4]    9,   12,    9,    4,   1;
[5]   21,   30,   25,   14,   5,   1;
[6]   51,   76,   69,   44,  20,   6,   1;
[7]  127,  196,  189,  133,  70,  27,   7,  1;
[8]  323,  512,  518,  392, 230, 104,  35,  8, 1;
[9]  835, 1353, 1422, 1140, 726, 369, 147, 44, 9, 1.
"""


@cache
def _mot(n: int) -> list[int]:
    if n == 0:
        return [1]

    r = lambda k: _mot(n - 1)[k] if k >= 0 and k < n else 0
    row = _mot(n - 1) + [1]
    for k in range(0, n):
        row[k] += r(k - 1) + r(k + 1)
    return row


motzkin = TablGenerator(_mot)


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(motzkin)
