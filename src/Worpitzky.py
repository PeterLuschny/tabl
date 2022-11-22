from functools import cache
from tabltypes import tabl, tstruct

"""Worpitzky triangle, A028246.

[0]  1;
[1]  1,   1;
[2]  1,   3,    2;
[3]  1,   7,   12,     6;
[4]  1,  15,   50,    60,     24;
[5]  1,  31,  180,   390,    360,    120;
[6]  1,  63,  602,  2100,   3360,   2520,    720;
[7]  1, 127, 1932, 10206,  25200,  31920,  20160,   5040;
[8]  1, 255, 6050, 46620, 166824, 317520, 332640, 181440, 40320;
"""


@cache
def _worpitzky(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = _worpitzky(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k - 1] + (k + 1) * row[k]
    return row


@tstruct(_worpitzky, "WORPITZKYNUM")
def worpitzky(size: int) -> tabl: 
    return [_worpitzky(j) for j in range(size)]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(worpitzky)
