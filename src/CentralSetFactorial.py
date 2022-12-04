from functools import cache
from _tabltypes import set_attributes

"""Central set factorial numbers, A269945 (see also A008957, A036969).

[0] [1]
[1] [0, 1]
[2] [0, 1,    1]
[3] [0, 1,    5,      1]
[4] [0, 1,   21,     14,      1]
[5] [0, 1,   85,    147,     30,     1]
[6] [0, 1,  341,   1408,    627,    55,    1]
[7] [0, 1, 1365,  13013,  11440,  2002,   91,   1]
[8] [0, 1, 5461, 118482, 196053, 61490, 5278, 140,  1]
"""


@cache
def _cs_factorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row: list[int] = _cs_factorial(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = k ** 2 * row[k] + row[k - 1]
    return row


@set_attributes(_cs_factorial, "CENTRFACTSET", True)
def cs_factorial(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _cs_factorial(n).copy()
    return _cs_factorial(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(cs_factorial)
