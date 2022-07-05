from functools import cache
from tabltools import TablGenerator

"""The central cycle factorial numbers, A269940, A259456

[0] [1]
[1] [0,   1]
[2] [0,   2,      3]
[3] [0,   6,     20,     15]
[4] [0,  24,    130,    210,    105]
[5] [0,  120,   924,   2380,   2520,    945]
[6] [0,  720,  7308,  26432,  44100,  34650,  10395]
[7] [0, 5040, 64224, 303660, 705320, 866250, 540540, 135135]
"""


@cache
def _ccf(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = _ccf(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n + k - 1) * (row[k] + row[k - 1])

    return row


cc_factorial = TablGenerator(_ccf, "Central cycle factorials", "CYCFAC")

####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(cc_factorial)
