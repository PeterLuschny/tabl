from functools import cache
from tablgenerator import TablGenerator

"""The Seidel triangle, A008281 or A008280. 

[0] [1]
[1] [0,   1]
[2] [0,   1,   1]
[3] [0,   1,   2,   2]
[4] [0,   2,   4,   5,    5]
[5] [0,   5,  10,  14,   16,   16]
[6] [0,  16,  32,  46,   56,   61,   61]
[7] [0,  61, 122, 178,  224,  256,  272,  272]

Seidel boustrophedon:
[0] [ 1]
[1] [ 0,  1]
[2] [ 1,  1,   0]
[3] [ 0,  1,   2,   2]
[4] [ 5,  5,   4,   2,   0]
[5] [ 0,  5,  10,  14,  16,  16]
[6] [61, 61,  56,  46,  32,  16,   0]
[7] [ 0, 61, 122, 178, 224, 256, 272, 272]
"""


@cache
def _sei(n: int) -> list[int]:
    if n == 0:
        return [1]

    rowA = _sei(n - 1)
    row = [0] + _sei(n - 1)
    row[1] = row[n]
    for k in range(2, n + 1):
        row[k] = row[k - 1] + rowA[n - k]
    return row


def _seibou(n: int) -> list[int]:
    return _sei(n) if n % 2 else _sei(n)[::-1]


seidel = TablGenerator(_sei)

seidel_boust = TablGenerator(_seibou)

####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(seidel)
    TablTest(seidel_boust)
