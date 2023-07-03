from functools import cache
from MoebiusInv import moebiusinv

"""Euler totient function phi, A000010,
but with offset 0 and a(0) = 0,
cardinality of numbers <= n and prime to n.


[0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10]
"""


@cache
def eulerphi(n: int) -> int:
    return sum(k * moebiusinv(n)[k] for k in range(n + 1))


if __name__ == "__main__":
    print([eulerphi(n) for n in range(10)])

    from timeit import default_timer as timer
    start = timer()
    [eulerphi(n) for n in range(1000)]
    end = timer()
    print(end - start) 
