from _tablsums import tabl_sum, tabl_evensum, tabl_oddsum, tabl_altsum, tabl_cumsum, tabl_revcumsum, tabl_diagsum
from _tabltransforms import flat_tabl, flat_rev, flat_diag, flat_accu, flat_revaccu, flat_accurev, row_poly, col_poly
from _tabltypes import tri, tabl

# #@

def PrintTabl(t: tabl) -> None:
    print(t)


def PrintFlat(t: tabl) -> None:
    print(flat_tabl(t))


def PrintRows(t: tabl) -> None:
    print("| trow  |  list  |")
    print("| :---  |  :---  |")
    for n, row in enumerate(t):
        print(f'| trow{n} | {row} |')


def PrintTerms(t: tabl) -> None:
    count = 0
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print(count, [n, k], term)
            count += 1


def PrintRowArray(T: tri, rows: int, cols: int) -> None:
    print("| rdiag  |   seq  |")
    print("| :---   |  :---  |")
    for j in range(rows):
        print(f'| rdiag{j} | {[T(j + k, k) for k in range(cols)]}|')


def PrintColArray(T: tri, rows: int, cols: int) -> None:
    print("| cdiag  |   seq  |")
    print("| :---   |  :---  |")
    for j in range(cols):
        print(f'| cdiag{j} | {[T(j + k, j) for k in range(rows)]} |')


def PrintRowPolyArray(T: tri, rows: int, cols: int) -> None:
    print("| rpdiag  |   seq  |")
    print("| :---    |  :---  |")
    for n in range(rows):
        print(f'| rpdiag{n} | {row_poly(T, n, cols)} |')


def PrintColPolyArray(T: tri, rows: int, cols: int) -> None:
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
    print(f'| cum      | {flat_accu(t)} |')
    print(f'| revcum   | {flat_revaccu(t)} |')
    print(f'| cumrev   | {flat_accurev(t)} |')
    print(f'| diag     | {flat_diag(t)} |')


def PrintViews(T: tri, rows: int = 7, verbose: bool = True) -> None:

    print("# " + T.id)

    cols: int = rows 
    print()

    t: tabl = T.tab(rows)

    if verbose: print(T.id, "Triangle view")
    PrintRows(t)
    print()

    if verbose: print(T.id, "Flattened seqs")
    PrintFlats(t)
    print()

    if verbose: print(T.id, "Row sums")
    PrintSums(t)
    print()

    if verbose: print(T.id, "Diagonals as rows")
    PrintRowArray(T, rows, cols)
    print()

    if verbose: print(T.id, "Diagonals as columns")
    PrintColArray(T, rows, cols)
    print()

    if verbose: print(T.id, "Polynomial values as rows")
    PrintRowPolyArray(T, rows, cols)
    print()

    if verbose: print(T.id, "Polynomial values as columns")
    PrintColPolyArray(T, rows, cols)
    print()


if __name__ == "__main__":

    from Abel import abel

    PrintViews(abel)
