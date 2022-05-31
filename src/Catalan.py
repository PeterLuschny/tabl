from functools import cache
from tablgenerator import TablGenerator

"""The Catalan triangle, A009766. 

[0] [1]
[1] [1, 1]
[2] [1, 2, 2]
[3] [1, 3, 5, 5]
[4] [1, 4, 9, 14, 14]
[5] [1, 5, 14, 28, 42, 42]
[6] [1, 6, 20, 48, 90, 132, 132]
[7] [1, 7, 27, 75, 165, 297, 429, 429]
[8] [1, 8, 35, 110, 275, 572, 1001, 1430, 1430]
[9] [1, 9, 44, 154, 429, 1001, 2002, 3432, 4862, 4862]
"""


@cache
def _ca(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = _ca(n - 1) + [0]
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row


catalan = TablGenerator(_ca)


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(catalan)
