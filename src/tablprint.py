from tabltools import row_poly, col_poly
from tablsums import PrintSums
from tabltypes import tgen, tabl

# #@


def PrintTabl(t: tabl) -> None:
    print(t)


def PrintRows(t: tabl) -> None:
    for n, row in enumerate(t):
        print([n], row)


def PrintTerms(t: tabl) -> None:
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print([n, k], term)


def PrintRowArray(F: tgen, rows: int, cols: int) -> None:
    for j in range(rows):
        print([F(j + k, k) for k in range(cols)])


def PrintColArray(F: tgen, rows: int, cols: int) -> None:
    for j in range(cols):
        print([F(j + k, j) for k in range(rows)])


def PrintRowPolyArray(T: tgen, rows: int, cols: int) -> None:
    for n in range(rows):
        print(row_poly(T, n, cols))


def PrintColPolyArray(T: tgen, rows: int, cols: int) -> None:
    for n in range(rows):
        print(col_poly(T, n, cols))


def PrintViews(T: tgen, rows: int = 7, cono: int | None = None, verbose: bool = True) -> None:
    print("_" * 48)
    print(T.name)

    cols: int = rows if cono is None else cono
    print()

    t: tabl = T(-rows)

    if verbose: print("Triangle view")
    PrintRows(t)
    print()

    if verbose: print("Row sums: all, even, odd, alternating")
    PrintSums(t)
    print()

    if verbose: print("Diagonals as rows")
    PrintRowArray(T, rows, cols)
    print()

    if verbose: print("Diagonals as columns")
    PrintColArray(T, rows, cols)
    print()

    if verbose: print("Polynomial values as rows")
    PrintRowPolyArray(T, rows, cols)
    print()

    if verbose: print("Polynomial values as columns")
    PrintColPolyArray(T, rows, cols)
    print()
