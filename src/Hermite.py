from functools import cache
from tabltools import TablGenerator

"""The coefficients of the Hermite polynomials, A099174, A066325. 

[0] [1]
[1] [0, 1]
[2] [1, 0, 1]
[3] [0, 3, 0, 1]
[4] [3, 0, 6, 0, 1]
[5] [0, 15, 0, 10, 0, 1]
[6] [15, 0, 45, 0, 15, 0, 1]
[7] [0, 105, 0, 105, 0, 21, 0, 1]
"""


@cache
def _her(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = _her(n - 1) + [0]
    for k in range(1, n):
        row[k] = _her(n - 1)[k - 1] + (k + 1) * row[k + 1]
    row[0] = _her(n - 1)[1]
    row[n] = 1
    return row


hermite = TablGenerator(_her)


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(hermite)
