from functools import cache
from _tabltypes import set_attributes

"""Fubini triangle, 
[A019538, A090582, A131689*, A278075].

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
def _fubini(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return _fubini(n - 1)[k] if k <= n - 1 else 0

    row: list[int] = [0] + _fubini(n - 1)
    for k in range(1, n + 1):
        row[k] = k * (r(k - 1) + r(k))
    return row


@set_attributes(_fubini, "FUBINITRIANG", False)
def fubini(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _fubini(n).copy()
    return _fubini(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(fubini)
