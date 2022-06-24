from typing import Callable


def TablGenerator(g: Callable[[int], list[int]]):
    def T(n, k=None):
        if n < 0:
            return [g(k) for k in range(-n)]
        if k == None:
            return g(n)
        return g(n)[k]

    return T


def isTablGenerator(
    T: Callable[[int, int | None], int | list[int] | list[list[int]]]
    ) -> bool:
    return (
        isinstance(T, Callable)
        and isinstance(T(0), list)
        and isinstance(T(0, None), list)
        and isinstance(T(0, 0), int)
        and isinstance(T(0)[0], int)
        and isinstance(T(-1)[0], list)
        and isinstance(T(-1)[0][0], int)
    )

def poly(T, n, x):
    row = T(n)
    return sum(c * x ** k for (k, c) in enumerate(row))


def row_poly(T, n, len):
    return [poly(T, n, k) for k in range(len)]


def col_poly(T, n, len):
    return [poly(T, k, n) for k in range(len)]
