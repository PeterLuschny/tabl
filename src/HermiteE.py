from functools import cache
from _tabltypes import set_attributes

"""(Probabilist's) Hermite polynomials He, unsigned coefficients. 

[0] [ 1]
[1] [ 0,   1]
[2] [ 1,   0,  1]
[3] [ 0,   3,  0,   1]
[4] [ 3,   0,  6,   0,  1]
[5] [ 0,  15,  0,  10,  0,  1]
[6] [15,   0, 45,   0, 15,  0, 1]
[7] [ 0, 105,  0, 105,  0, 21, 0, 1]
"""


@cache
def hermiteE(n: int) -> list[int]:
    row: list[int] = [0] * (n + 1) 
    row[n] = 1
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (n - k)  
    return row


@set_attributes(
    hermiteE, 
    "HermiteE", 
    ['A066325', 'A073278', 'A099174'], 
    True)
def HermiteE(n: int, k: int) -> int: 
    return hermiteE(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(HermiteE)
