from functools import cache
from Binomial import binomial 
from _tabltypes import set_attributes

"""Euler secant polynomials, 
[A119879*], A081658, A153641. 

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
def _euler_sec(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = [binomial(n, k) * _euler_sec(n - k)[0] if k > 0 else 0 for k in range(n + 1)]  
    if n % 2 == 0:
        row[0] = -sum(row[2::2])
    return row


@set_attributes(_euler_sec, "EULERSECANTO", True)
def euler_sec(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _euler_sec(n).copy()
    return _euler_sec(n)[k]


def eulerS(n: int) -> int:
    return 0 if n % 2 == 1 else _euler_sec(n)[0]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(euler_sec, short=True)

    print("Bonus:")
    print([eulerS(n) for n in range(30)])

# See also: https://oeis.org/wiki/User:Peter_Luschny/SwissKnifePolynomials
