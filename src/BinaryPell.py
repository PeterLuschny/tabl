from functools import cache
from _tabltypes import MakeTriangle

"""Binary Pell triangle

[0] [  1]
[1] [  2,    1]
[2] [  4,    4,    1]
[3] [  8,   12,    6,    1]
[4] [ 16,   32,   24,    8,    1]
[5] [ 32,   80,   80,   40,   10,   1]
[6] [ 64,  192,  240,  160,   60,  12,   1]
[7] [128,  448,  672,  560,  280,  84,  14,  1]
[8] [256, 1024, 1792, 1792, 1120, 448, 112, 16, 1]
"""


@cache
def binarypell(n):
    
    if n == 0: return [1]
    arow = binarypell(n-1) 
    row = arow + [1]   
    for k in range(n-1, 0, -1):
        row[k] = arow[k - 1] + 2 * arow[k]
    row[0] = 2 * arow[0]    
    return row


@MakeTriangle(binarypell, "BinaryPell", ["A038207"], True)
def BinaryPell(n: int, k: int) -> int:
    return binarypell(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(BinaryPell)
