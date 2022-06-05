from functools import cache
from Binomial import binomial
from tablgenerator import TablGenerator

"""The Euler secant polynomials, A119879, A081658, A153641. 

[0] [   1]
[1] [   0,     1]
[2] [  -1,     0,     1]
[3] [   0,    -3,     0,   1]
[4] [   5,     0,    -6,   0,   1]
[5] [   0,    25,     0, -10,   0,   1]
[6] [ -61,     0,    75,   0, -15,   0,   1]
[7] [   0,  -427,     0, 175,   0, -21,   0,  1]
[8] [1385,     0, -1708,   0, 350,   0, -28,  0,  1]
"""


@cache
def _esec(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [binomial(n, k) * _esec(n - k)[0] if k > 0 else 0 for k in range(n + 1)]
    if n % 2 == 0:
        row[0] = -sum(row)
    return row


euler_sec = TablGenerator(_esec)


def euler(n):
    return 0 if n % 2 == 1 else _esec(n)[0]


####################################################################
# See also: https://oeis.org/wiki/User:Peter_Luschny/SwissKnifePolynomials

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(euler_sec, True)

    print([euler(n) for n in range(100)])
