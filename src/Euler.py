from functools import cache
from tabltypes import tabl, tvals

"""The Euler triangle, A247453, A109449.

0:      1
1:     -1      1
2:      1     -2      1
3:     -2      3     -3      1
4:      5     -8      6     -4      1
5:    -16     25    -20     10     -5     1
6:     61    -96     75    -40     15    -6     1
7:   -272    427   -336    175    -70    21    -7    1
8:   1385  -2176   1708   -896    350  -112    28   -8   1
9:  -7936  12465  -9792   5124  -2016   630  -168   36  -9   1
"""


@cache
def _euler(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = _euler(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * n) // (k)
    row[0] = -sum((-1) ** (j // 2) * row[j] for j in range(n, 0, -2))

    return row


@tvals(_euler, "EULNUM")
def euler(size: int) -> tabl: 
    return [_euler(j) for j in range(size)]


def euler_num(n: int) -> int:
    return _euler(n)[0]

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(euler)

    print("Bonus:")
    print([euler_num(n) for n in range(30)])

# See also: https://oeis.org/wiki/User:Peter_Luschny/SwissKnifePolynomials
