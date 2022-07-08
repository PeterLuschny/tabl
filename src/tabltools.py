#@


def poly(T, n, x) -> int:
    row: list[int] = T(n)
    return sum(c * x ** k for (k, c) in enumerate(row))


def row_poly(T, n, len) -> list[int]:
    return [poly(T, n, k) for k in range(len)]


def col_poly(T, n, len) -> list[int]:
    return [poly(T, k, n) for k in range(len)]
