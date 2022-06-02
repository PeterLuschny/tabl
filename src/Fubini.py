from functools import cache
from tablgenerator import TablGenerator

"""The Fubini triangle, A131689. 

[0]  1;
[1]  0,  1;
[2]  0,  1,    2;
[3]  0,  1,    6,     6;
[4]  0,  1,   14,    36,    24;
[5]  0,  1,   30,   150,   240,    120;
[6]  0,  1,   62,   540,  1560,   1800,    720;
[7]  0,  1,  126,  1806,  8400,  16800,  15120,  5040;
[8]  0,  1,  254,  5796, 40824, 126000, 191520, 141120, 40320;
"""


@cache
def _fu(n: int) -> list[int]:
    if n == 0:
        return [1]

    r = lambda k: _fu(n - 1)[k] if k <= n - 1 else 0
    row = [0] + _fu(n - 1)
    for k in range(1, n + 1):
        row[k] = k * (r(k - 1) + r(k))
    return row


fubini = TablGenerator(_fu)


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(fubini)
