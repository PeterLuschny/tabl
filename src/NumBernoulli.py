from Genocchi import genocchi
from fractions import Fraction as frac

"""Bernoulli numbers A164555/A027642
"""

# #@


def Bernoulli(n: int) -> frac:
    if n < 2:
        return frac(1, n + 1)
    if n % 2 == 1:
        return frac(0, 1)
    g = genocchi(n // 2 - 1)[-1]
    f = frac(g, 2 ** (n + 1) - 2)
    return -f if n % 4 == 0 else f


if __name__ == "__main__":
    print([Bernoulli(n) for n in range(10)])

    from timeit import default_timer as timer

    start = timer()
    [Bernoulli(n) for n in range(1000)]
    end = timer()
    print(end - start)
