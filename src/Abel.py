from functools import cache
from cachetools import cached, LRUCache
from tabltools import TablGenerator
from Binomial import binomial


"""The coefficients of Abel poynomials

[0] [1]
[1] [0,        1]
[2] [0,       -2,       1]
[3] [0,        9,      -6,       1]
[4] [0,      -64,      48,     -12,      1]
[5] [0,      625,    -500,     150,    -20,      1]
[6] [0,    -7776,    6480,   -2160,    360,    -30,    1]
[7] [0,   117649, -100842,   36015,  -6860,    735,  -42,   1]
[8] [0, -2097152, 1835008, -688128, 143360, -17920, 1344, -56, 1]
"""


@cache
def a(n):
    return (-n - 1) ** n

ncache = LRUCache(maxsize=1001)

@cached(ncache)
def _abe(N: int) -> list[int]:

    if N == 0:
        return [1]

    item = ncache.get(N, None)
    while item is not None:
        _abe(N - 1)

    def T(n, k):
        return k ** n if k == 0 else sum(
            binomial(n - 1, j) * _abe(n - j - 1)[k - 1] * a(j) 
            for j in range(n - k + 1) )

    return [T(N, k) for k in range(N + 1)]


abel = TablGenerator(_abe)

####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(abel, short=True)
