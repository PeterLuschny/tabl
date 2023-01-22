from _tabltypes import tri, tabl
from _tablsums import tabl_sum, tabl_evensum, tabl_oddsum, tabl_altsum, tabl_accsum, tabl_revaccsum, tabl_accrevsum, tabl_diagsum
from _tabltransforms import flat_tabl, flat_rev, flat_diag, row_poly,  col_poly, middle, central, left_side, right_side, pos_half, neg_half,  flat_acc, flat_revacc, flat_accrev, tabllcm, tablgcd, tablmax,  transbinval, invtransbinval, transsqrs,transnat0, transnat1 

# #@

def PrintTabl(t: tabl) -> None:
    print(t)


def PrintFlat(t: tabl) -> None:
    print(flat_tabl(t))


def PrintRows(t: tabl) -> None:
    print("|  Row   |  Seq   |")
    print("| :---   |  :---  |")
    for n, row in enumerate(t):
        print(f'| Row{n} | {row} |')


def PrintTerms(t: tabl) -> None:
    count = 0
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print(count, [n, k], term)
            count += 1


def PrintRowArray(T: tri, rows: int, cols: int) -> None:
    print("| DiagRow  |   Seq  |")
    print("| :---     |  :---  |")
    for j in range(rows):
        print(f'| DiagRow{j} | {[T(j + k, k) for k in range(cols)]}|')


def PrintColArray(T: tri, rows: int, cols: int) -> None:
    print("| DiagCol  |   Seq  |")
    print("| :---     |  :---  |")
    for j in range(cols):
        print(f'| DiagCol{j} | {[T(j + k, j) for k in range(rows)]} |')


def PrintPolyRowArray(T: tri, rows: int, cols: int) -> None:
    print("| PolyRow  |   Seq  |")
    print("| :---     |  :---  |")
    for n in range(rows):
        print(f'| PolyRow{n} | {row_poly(T, n, cols)} |')


def PrintPolyColArray(T: tri, rows: int, cols: int) -> None:
    print("| PolyCol  |   Seq  |")
    print("| :---     |  :---  |")
    for n in range(rows):
        print(f'| PolyCol{n} | {col_poly(T, n, cols)} |')


def PrintSums(t: tabl) -> None:
    print( "| Sum       |   Seq  |")
    print( "| :---      |  :---  |")
    print(f'| Sum       | {tabl_sum(t)} |')
    print(f'| EvenSum   | {tabl_evensum(t)} |')
    print(f'| OddSum    | {tabl_oddsum(t)} |')
    print(f'| AltSum    | {tabl_altsum(t)} |')
    print(f'| AccSum    | {tabl_accsum(t)} |')
    print(f'| AccRevSum | {tabl_accrevsum(t)} |')
    print(f'| RevAccSum | {tabl_revaccsum(t)} |')
    print(f'| DiagSum   | {tabl_diagsum(t)} |')


def PrintFlats(t: tabl) -> None:
    print( "| Flat      |  Seq  |")
    print( "| :---      | :---  |")
    print(f'| Triangle  | {flat_tabl(t)} |')
    print(f'| TriRev    | {flat_rev(t)} |')
    print(f'| TriAcc    | {flat_acc(t)} |')
    print(f'| TriRevAcc | {flat_revacc(t)} |')
    print(f'| TriAccRev | {flat_accrev(t)} |')
    print(f'| TriDiag   | {flat_diag(t)} |')


def PrintTrans(t: tabl) -> None:
    print( "| Trans     |   Seq  |")
    print( "| :---      |  :---  |")
    print(f'| RowLcm    | {tabllcm(t)} |')
    print(f'| RowGcd    | {tablgcd(t)} |')
    print(f'| RowMax    | {tablmax(t)} |')
    print(f'| Middle    | {middle(t)} |')
    print(f'| Central   | {central(t)} |')
    print(f'| LeftSide  | {left_side(t)} |')
    print(f'| RightSide | {right_side(t)} |')
    print(f'| PosHalf   | {pos_half(t)} |')
    print(f'| NegHalf   | {neg_half(t)} |')
    print(f'| Bin       | {transbinval(t)} |')
    print(f'| InvBin    | {invtransbinval(t)} |')
    print(f'| TransSqrs | {transsqrs(t)} |')
    print(f'| TransNat0 | {transnat0(t)} |')
    print(f'| TransNat1 | {transnat1(t)} |')


def PrintViews(T: tri, rows: int = 7, verbose: bool = True) -> None:

    print("# " + T.id)
    print(T.sim)

    cols: int = rows 
    print()

    t: tabl = T.tab(rows)

    if verbose: print(T.id, "Triangle view")
    PrintRows(t)
    print()

    if verbose: print(T.id, "Flattened triangles")
    PrintFlats(t)
    print()

    if verbose: print(T.id, "Row sums")
    PrintSums(t)
    print()

    if verbose: print(T.id, "Transforms")
    PrintTrans(t)
    print()

    if verbose: print(T.id, "Diagonals as rows")
    PrintRowArray(T, rows, cols)
    print()

    if verbose: print(T.id, "Diagonals as columns")
    PrintColArray(T, rows, cols)
    print()

    if verbose: print(T.id, "Polynomial values as rows")
    PrintPolyRowArray(T, rows, cols)
    print()

    if verbose: print(T.id, "Polynomial values as columns")
    PrintPolyColArray(T, rows, cols)
    print()


if __name__ == "__main__":

    from Abel import abel
    from Bell import bell

    PrintViews(abel, 9)
