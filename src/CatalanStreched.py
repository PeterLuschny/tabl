from functools import cache
from tabltools import TablGenerator

"""The streched Catalan triangle, A053121. 

[0]   1,
[1]   0,   1,
[2]   1,   0,   1,
[3]   0,   2,   0,   1,
[4]   2,   0,   3,   0,   1,
[5]   0,   5,   0,   4,   0,   1,
[6]   5,   0,   9,   0,   5,   0,   1,
[7]   0,  14,   0,  14,   0,   6,   0,  1,
[8]  14,   0,  28,   0,  20,   0,   7,  0,  1,
[9]   0,  42,   0,  48,   0,  27,   0,  8,  0,  1.
"""


@cache
def _cas(n: int) -> list[int]:
    if n == 0:
        return [1]

    r = lambda k: _cas(n - 1)[k] if k >= 0 and k < n else 0
    row = _cas(n - 1) + [1]
    for k in range(0, n):
        row[k] = r(k - 1) + r(k + 1)
    return row


catalan_streched = TablGenerator(_cas, "Catalan streched")


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(catalan_streched)
