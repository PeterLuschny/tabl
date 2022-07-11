from typing import Literal
from tablsums import tabl_sum, tabl_evensum, tabl_oddsum, tabl_altsum, tabl_cumsum, tabl_revcumsum, tabl_diagsum
from tabltransform import flat_tabl, flat_rev, flat_diag, flat_cum, flat_revcum, flat_cumrev, row_poly, col_poly
from tabltypes import tgen, tabl

# #@

def PrintTabl(t: tabl) -> None:
    print(t)


def PrintRows(t: tabl) -> None:
    print("| trow  |  list  |")
    print("| :---  |  :---  |")
    for n, row in enumerate(t):
        print(f'| trow{n} | {row} |')


def PrintTerms(t: tabl) -> None:
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print([n, k], term)


def PrintRowArray(T: tgen, rows: int, cols: int) -> None:
    print("| rdiag  |   seq  |")
    print("| :---   |  :---  |")
    for j in range(rows):
        print(f'| rdiag{j} | {[T.val(j + k, k) for k in range(cols)]}|')


def PrintColArray(T: tgen, rows: int, cols: int) -> None:
    print("| cdiag  |   seq  |")
    print("| :---   |  :---  |")
    for j in range(cols):
        print(f'| cdiag{j} | {[T.val(j + k, j) for k in range(rows)]} |')


def PrintRowPolyArray(T: tgen, rows: int, cols: int) -> None:
    print("| rpdiag  |   seq  |")
    print("| :---    |  :---  |")
    for n in range(rows):
        print(f'| rpdiag{n} | {row_poly(T, n, cols)} |')


def PrintColPolyArray(T: tgen, rows: int, cols: int) -> None:
    print("| cpdiag  |   seq  |")
    print("| :---    |  :---  |")
    for n in range(rows):
        print(f'| cpdiag{n} | {col_poly(T, n, cols)} |')


def PrintSums(t: tabl) -> None:
    print("| sum       |   seq  |")
    print("| :---      |  :---  |")
    print(f'| sum       | {tabl_sum(t)} |')
    print(f'| evensum   | {tabl_evensum(t)} |')
    print(f'| oddsum    | {tabl_oddsum(t)} |')
    print(f'| altsum    | {tabl_altsum(t)} |')
    print(f'| diagsum   | {tabl_diagsum(t)} |')
    print(f'| cumsum    | {tabl_cumsum(t)} |')
    print(f'| revcumsum | {tabl_revcumsum(t)} |')


def PrintFlats(t: tabl) -> None:
    print("| flat      |   seq  |")
    print("| :---      |  :---  |")
    print(f'| tabl     | {flat_tabl(t)} |')
    print(f'| rev      | {flat_rev(t)} |')
    print(f'| cum      | {flat_cum(t)} |')
    print(f'| revcum   | {flat_revcum(t)} |')
    print(f'| cumrev   | {flat_cumrev(t)} |')
    print(f'| diag     | {flat_diag(t)} |')


def PrintViews(T: tgen, rows: int = 7, cono: int | None = None, 
    verbose: bool = True) -> None:

    print("# " + T.__name__)

    cols: int = rows if cono is None else cono
    print()

    t: tabl = T(rows)

    if verbose: print("Triangle view")
    PrintRows(t)
    print()

    if verbose: print("Flattened seqs")
    PrintFlats(t)
    print()

    if verbose: print("Row sums")
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

"""
import contextlib
from tabl import tabl_fun
def SaveTables() -> None:
    path: Literal['tables.md'] = 'tables.md'

    with open(path, 'w+') as dest:
        with contextlib.redirect_stdout(dest):
            for fun in tabl_fun:
                PrintViews(fun)
"""

####################################################################

if __name__ == "__main__":
    from tabltypes import tvals
    from Abel import abel

    PrintViews(abel)
    # SaveTables()
