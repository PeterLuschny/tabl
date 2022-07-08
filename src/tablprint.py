from tabltools import row_poly, col_poly
from tablsums import PrintSums

#@

def PrintTabl(T, k=None) -> None:
    t: list[list[int]] = T if k == None else T(-k)
    print(t)


def PrintRows(T, k=None) -> None:
    t: list[list[int]] = T if k == None else T(-k)
    for n, row in enumerate(t):
        print([n], row)


def PrintTerms(T, k=None) -> None:
    t: list[list[int]] = T if k == None else T(-k)
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print([n, k], term)


def PrintRowArray(F, rows, cols) -> None:
    for j in range(rows):
        print([F(j + k, k) for k in range(cols)])


def PrintColArray(F, rows, cols) -> None:
    for j in range(cols):
        print([F(j + k, j) for k in range(rows)])


def PrintRowPolyArray(T, rows, cols) -> None:
    for n in range(rows):
        print(row_poly(T, n, cols))


def PrintColPolyArray(T, rows, cols) -> None:
    for n in range(rows):
        print(col_poly(T, n, cols))


def PrintViews(T, rows: int=7, cono: int | None=None, verbose=True) -> None:
    print("_" * 48)
    print(T.name)

    cols: int = rows if cono == None else cono
    print()

    Tabl: list[list[int]] = T(-rows)
    if verbose: print("Triangle view")
    PrintRows(Tabl)
    print()

    if verbose: print("Row sums: all, even, odd, alternating")
    PrintSums(Tabl)
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

