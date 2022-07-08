from functools import cache
from tabltypes import *
from Binomial import binomial

"""The unsigned coefficients of Abel polynomials, A061356

[0] [1]
[1] [0,        1]
[2] [0,        2,       1]
[3] [0,        9,       6,       1]
[4] [0,       64,      48,      12,      1]
[5] [0,      625,     500,     150,     20,      1]
[6] [0,     7776,    6480,    2160,    360,     30,    1]
[7] [0,   117649,  100842,   36015,   6860,    735,   42,   1]
[8] [0,  2097152, 1835008,  688128, 143360,  17920, 1344,  56, 1]
"""

@cache
def _abe(n: int) -> list[int]:

    if n == 0:
        return [1]

    return [binomial(n - 1, k - 1) * n ** (n - k) if k > 0 else 0 for k in range(n + 1)]


abel: tgen = TablGenerator(_abe, "Abel", "ABELPO")

####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(abel) 
