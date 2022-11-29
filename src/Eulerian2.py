from functools import cache
from tabltypes import set_name

"""Eulerian2 triangle, A340556.

[0] 1;
[1] 0, 1;
[2] 0, 1,   2;
[3] 0, 1,   8,     6;
[4] 0, 1,  22,    58,     24;
[5] 0, 1,  52,   328,    444,    120;
[6] 0, 1, 114,  1452,   4400,   3708,    720;
[7] 0, 1, 240,  5610,  32120,  58140,  33984,  5040;
[8] 0, 1, 494, 19950, 195800, 644020, 785304, 341136, 40320;
"""


@cache
def _eulerian2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row: list[int] = _eulerian2(n - 1) + [0]
    for k in range(n, 1, -1):
        row[k] = (2 * n - k) * row[k - 1] + k * row[k]
    return row


@set_name(_eulerian2, "EULERIANORD2")
def eulerian2(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _eulerian2(n).copy()
    return _eulerian2(n)[k]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(eulerian2)

# See also http://luschny.de/math/oeis/A340556.html
