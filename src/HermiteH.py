from functools import cache
from _tabltypes import set_attributes

"""(Physicist's) Hermite polynomials, unsigned coefficients. 

[0]     1;
[1]     0,     2;
[2]     2,     0,      4;
[3]     0,    12,      0,      8;
[4]    12,     0,     48,      0,     16;
[5]     0,   120,      0,    160,      0,    32;
[6]  120,      0,    720,      0,    480,     0,     64;
[7]     0,  1680,      0,   3360,      0,  1344,      0,   128;
[8]  1680,     0,  13440,      0,  13440,     0,   3584,     0,   256;
[9]     0, 30240,      0,  80640,      0, 48384,      0,  9216,     0,  512;
"""


@cache
def hermiteh(n: int) -> list[int]:

    row: list[int] = [0] * (n + 1); 
    row[n] = 2 ** n
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (2 * (n - k))  
    return row


@set_attributes(
    hermiteh, 
    "HermiteH", 
    ['A060821'], 
    False)
def HermiteH(n: int, k: int) -> int: 
    return hermiteh(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(HermiteH)
