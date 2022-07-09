# #@

from tabltypes import tgen, trow


def poly(T: tgen, n: int, x: int) -> int:
    row: trow = T(n)
    return sum(c * x ** k for (k, c) in enumerate(row))


def row_poly(T: tgen, n: int, leng: int) -> trow:
    return [poly(T, n, k) for k in range(leng)]


def col_poly(T: tgen, n: int, leng: int) -> trow:
    return [poly(T, k, n) for k in range(leng)]
