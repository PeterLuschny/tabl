from functools import cache
from _tabltypes import set_attributes

"""Pascal triangle, binomial coefficients, A007318.

[0]   1;
[1]   1,   1;
[2]   1,   2,   1;
[3]   1,   3,   3,   1;
[4]   1,   4,   6,   4,   1;
[5]   1,   5,  10,  10,   5,   1;
[6]   1,   6,  15,  20,  15,   6,   1;
[7]   1,   7,  21,  35,  35,  21,   7,   1;
[8]   1,   8,  28,  56,  70,  56,  28,   8,   1;
[9]   1,   9,  36,  84, 126, 126,  84,  36,   9,   1;
"""


@cache
def _binomial(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = [1] + _binomial(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    return row


@set_attributes(_binomial, "BINOMIALCOEF", True)
def binomial(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _binomial(n).copy()
    return _binomial(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(binomial)
