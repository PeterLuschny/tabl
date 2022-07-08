from functools import cache
from tabltypes import *

"""The Bessel triangle, A132062. 

[0] [1]
[1] [0,      1]
[2] [0,      1,      1]
[3] [0,      3,      3,     1]
[4] [0,     15,     15,     6,     1]
[5] [0,    105,    105,    45,    10,    1]
[6] [0,    945,    945,   420,   105,   15,   1]
[7] [0,  10395,  10395,  4725,  1260,  210,  21,  1]
[8] [0, 135135, 135135, 62370, 17325, 3150, 378, 28, 1]
"""


@cache
def _bessel(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row: list[int] = _bessel(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = row[k - 1] + (2 * (n - 1) - k) * row[k]
    return row


bessel: tgen = TablGenerator(_bessel, "Bessel", "BESSEL")


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(bessel)
