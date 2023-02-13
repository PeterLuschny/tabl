from functools import cache
from _tabltypes import set_attributes

"""Genocchi triangle.

[0] [     1]
[1] [     1,      1]
[2] [     2,      3,      3]
[3] [     8,     14,     17,     17]
[4] [    56,    104,    138,    155,    155]
[5] [   608,   1160,   1608,   1918,   2073,   2073]  
[6] [  9440,  18272,  25944,  32008,  36154,  38227,  38227]
[7] [198272, 387104, 557664, 702280, 814888, 891342, 929569, 929569]
"""


@cache
def genocchi(n: int) -> list[int]:

    if n == 0: return [1]

    row: list[int] = [0] + genocchi(n - 1) + [0]

    for k in range(n, 0, -1):
        row[k] += row[k + 1]

    for k in range(2, n + 2):
        row[k] += row[k - 1]

    return row[1:]


@set_attributes(
    genocchi, 
    "Genocchi", 
    ['A297703'], 
    False)
def Genocchi(n: int, k: int) -> int: 
    return genocchi(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Genocchi)
