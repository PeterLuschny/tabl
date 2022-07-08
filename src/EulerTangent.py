from functools import cache
from Binomial import binomial
from tabltypes import *

"""The Euler tangent polynomials, A162660, A350972, A155585, A009006, A000182. 

[0]    0;
[1]    1,     0;
[2]    0,     2,     0;
[3]   -2,     0,     3,   0;
[4]    0,    -8,     0,   4,    0;
[5]   16,     0,   -20,   0,    5,    0;
[6]    0,    96,     0, -40,    0,    6,    0;
[7] -272,     0,   336,   0,  -70,    0,    7,  0;
[8]    0, -2176,     0, 896,    0, -112,    0,  8,  0;
[9] 7936,     0, -9792,   0, 2016,    0, -168,  0,  9,  0;
"""


@cache
def _euler_tan(n: int) -> list[int]:

    row: list[int] = [binomial(n, k) * _euler_tan(n - k)[0] if k > 0 else 0 for k in range(n + 1)]  # type: ignore

    if n % 2 == 1:
        row[0] = -sum(row[2::2]) + 1
    return row


euler_tan: tgen = TablGenerator(_euler_tan, "Euler tangent", "EULTAN")


def eulerT(n) -> int:
    return 0 if n % 2 == 0 else _euler_tan(n)[0]


####################################################################
# See also: https://oeis.org/wiki/User:Peter_Luschny/SwissKnifePolynomials

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(euler_tan, short=True)

    print([eulerT(n) for n in range(100)])
