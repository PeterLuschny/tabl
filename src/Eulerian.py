from functools import cache
from tabltools import TablGenerator

"""The Eulerian triangle, A173018. 

[0]  1,
[1]  1,    0,
[2]  1,    1,     0,
[3]  1,    4,     1,      0,
[4]  1,   11,    11,      1,      0,
[5]  1,   26,    66,     26,      1,    0,
[6]  1,   57,   302,    302,     57,    1,   0,
[7]  1,  120,  1191,   2416,   1191,  120,   1,  0,
[8]  1,  247,  4293,  15619,  15619, 4293, 247,  1,  0
"""


@cache
def _eur(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = _eur(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n - k) * row[k - 1] + (k + 1) * row[k]
    return row


eulerian = TablGenerator(_eur)


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(eulerian)
