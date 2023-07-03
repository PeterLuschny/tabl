from functools import cache
from MoebiusMat import moebiusmat

"""Moebius function, A008683, but with offset 0 and mu(0) = 0.

[0, 1, -1, -1, 0, -1, 1, -1, 0, 0]
"""


@cache
def moebius(n: int) -> int:
    if n == 1: return 1
    if n == 2: return -1
    return -sum(moebius(k) for k, i in enumerate(moebiusmat(n)[: n - 1]) if i != 0)


if __name__ == "__main__":
    print([moebius(n) for n in range(10)])

    from timeit import default_timer as timer
    start = timer()
    [moebius(n) for n in range(1000)]
    end = timer()
    print(end - start) 
