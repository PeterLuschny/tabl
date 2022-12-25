from functools import cache
from _tabltypes import set_attributes

"""Stirling set B-type.


[0]     1;
[1]     1,     1;
[2]     3,     4,     1;
[3]    11,    19,     9,     1;
[4]    49,   104,    70,    16,    1;
[5]   257,   641,   550,   190,   25,   1;
[6]  1539,  4380,  4531,  2080,  425,  36,  1;
[7] 10299, 32803, 39515, 22491, 6265, 833, 49, 1;
"""

# sim = ['A154602']

@cache
def _stirling_setB(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    pow: list[int] = _stirling_setB(n - 1)
    row: list[int] = _stirling_setB(n - 1) + [1]

    row[0] += 2 * row[1]
    
    for k in range(1, n - 1):
        row[k] = 2 * (k + 1) * pow[k + 1] + (2 * k + 1) * pow[k] + pow[k - 1]

    row[n - 1] = (2 * n - 1) * pow[n - 1] + pow[n - 2]
    return row


@set_attributes(
    _stirling_setB, 
    "StirlingSetB", 
    ['A154602'], 
    True)
def stirling_setB(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _stirling_setB(n).copy()
    return _stirling_setB(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(stirling_setB)
