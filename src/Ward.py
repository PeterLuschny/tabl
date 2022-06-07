from functools import cache
from tablgenerator import TablGenerator

"""The Ward numbers A269939, A134991.

[0] [1]
[1] [0, 1]
[2] [0, 1,   3]
[3] [0, 1,  10,    15]
[4] [0, 1,  25,   105,    105]
[5] [0, 1,  56,   490,   1260,     945]
[6] [0, 1, 119,  1918,   9450,   17325,   10395]
[7] [0, 1, 246,  6825,  56980,  190575,  270270,  135135]
[8] [0, 1, 501, 22935, 302995, 1636635, 4099095, 4729725, 2027025]
"""


@cache
def _war(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = _war(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k] + (n + k - 1) * row[k - 1]
    return row


ward = TablGenerator(_war)


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(ward)
