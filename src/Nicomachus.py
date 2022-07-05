from functools import cache
from tabltools import TablGenerator

"""Nicomachus triangle, A036561

[0] [  1]
[1] [  2,   3]
[2] [  4,   6,   9]
[3] [  8,  12,  18,  27]
[4] [ 16,  24,  36,  54,  81]
[5] [ 32,  48,  72, 108, 162, 243]
[6] [ 64,  96, 144, 216, 324, 486,  729]
[7] [128, 192, 288, 432, 648, 972, 1458, 2187]
"""


@cache
def _nico(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = _nico(n - 1) + [3 * _nico(n - 1)[n - 1]]
    for k in range(0, n):
        row[k] *= 2
    return row


nicomachus = TablGenerator(_nico, "Nicomachus", "NICOMA")


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(nicomachus)
