from functools import cache
from tabltypes import *

"""The rising factorial, A094587. 

[0]       1
[1]       1,      1
[2]       2,      2,      1
[3]       6,      6,      3,     1
[4]      24,     24,     12,     4,     1
[5]     120,    120,     60,    20,     5,    1
[6]     720,    720,    360,   120,    30,    6,   1
[7]    5040,   5040,   2520,   840,   210,   42,   7,  1
[8]   40320,  40320,  20160,  6720,  1680,  336,  56,  8, 1
[9]  362880, 362880, 181440, 60480, 15120, 3024, 504, 72, 9, 1
"""


@cache
def _rf(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = [0] + _rf(n - 1)
    for k in range(0, n):
        row[k] += (n - k) * row[k + 1]
    return row


rising_factorial: tgen = TablGenerator(_rf, "Rising factorial", "RISFAC")


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(rising_factorial)
