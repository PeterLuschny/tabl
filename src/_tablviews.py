from _tabltypes import  rgen, tgen, tabl
from _tablpoly import PolyCol, PolyRow, PosHalf, NegHalf
from _tabltabls import AccTabl, RevAccTabl, AccRevTabl, RevTabl, AntiDiagTabl
from _tablsums import PrintSums
from _tabltransforms import RowLcm, RowGcd, RowMax, ColMiddle,ColECentral, ColLeft,ColRight, PrintTransforms 


# #@

def PrintTabl(t: tabl) -> None:
    print(t)


def PrintFlat(t: tabl) -> None:
    #print(flat(t))
    print(t)


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


def PrintRowArray(T: rgen, rows: int, cols: int) -> None:
    print("| DiagRow  |   Seq  |")
    print("| :---     |  :---  |")
    for j in range(rows):
        print(f'| DiagRow{j} | {[T(j + k)[k] for k in range(cols)]}|')


def PrintColArray(T: rgen, rows: int, cols: int) -> None:
    print("| DiagCol  |   Seq  |")
    print("| :---     |  :---  |")
    for j in range(cols):
        print(f'| DiagCol{j} | {[T(j + k)[j] for k in range(rows)]} |')


def PrintPolyRowArray(T: rgen, rows: int, cols: int) -> None:
    print("| PolyRow  |   Seq  |")
    print("| :---     |  :---  |")
    ########### broken? Motzkin PolyRow0, []
    for n in range(rows):
        print(f'| PolyRow{n} | {PolyRow(T, n, cols)} |')


def PrintPolyColArray(T: rgen, rows: int, cols: int) -> None:
    print("| PolyCol  |   Seq  |")
    print("| :---     |  :---  |")
    ########### broken? Motzkin PolyCol0, []
    for n in range(rows):
        print(f'| PolyCol{n} | {PolyCol(T, n, cols)} |')


def PrintFlats(t: tabl) -> None:
    print( "| Flat       |  Seq  |")
    print( "| :---       | :---  |")
    print(f'| Tabl       | {t} |')
    print(f'| RevTabl    | {RevTabl(t)} |')
    print(f'| AntiDiag   | {AntiDiagTabl(t)} |')
    print(f'| AccTabl    | {AccTabl(t)} |')
    print(f'| RevAccTabl | {RevAccTabl(t)} |')
    print(f'| AccRevTabl | {AccRevTabl(t)} |')


def PrintTrans(t: tabl) -> None:
    print( "| Trans      |   Seq  |")
    print( "| :---       |  :---  |")
    print(f'| RowLcm     | {RowLcm(t)} |')
    print(f'| RowGcd     | {RowGcd(t)} |')
    print(f'| RowMax     | {RowMax(t)} |')
    print(f'| ColMiddle  | {ColMiddle(t)} |')
    print(f'| ColCentral | {ColECentral(t)} |')
    print(f'| ColLefte   | {ColLeft(t)} |')
    print(f'| ColRight   | {ColRight(t)} |')
    
  #  print(f'| PosHalf   | {PosHalf(t)} |')
  #  print(f'| NegHalf   | {NegHalf(t)} |')
  #  print(f'| Bin       | {transbinval(t)} |')
  #  print(f'| InvBin    | {invtransbinval(t)} |')
  #  print(f'| TransSqrs | {TransSqrs(t)} |')
  #  print(f'| TransNat0 | {TransNat0(t)} |')
  #  print(f'| TransNat1 | {TransNat1(t)} |')


def PrintViews(g: tgen, rows: int = 7, verbose: bool = True) -> None:

    print("# " + g.id)
    print(g.sim)

    cols: int = rows 
    print()

    T: tabl = g.tab(rows)

    if verbose: print(g.id, "Triangle view")
    PrintRows(T)
    print()

    if verbose: print(g.id, "Triangles")
    PrintFlats(T)
    print()

    if verbose: print(g.id, "Row sums")
    PrintSums(T, g.id) 
    print()

    if verbose: print(g.id, "Transforms")
    PrintTrans(T)
    PrintTransforms(g)
    print()

    if verbose: print(g.id, "Diagonals as rows")
    PrintRowArray(g.gen, rows, cols)
    print()

    if verbose: print(g.id, "Diagonals as columns")
    PrintColArray(g.gen, rows, cols)
    print()

    if verbose: print(g.id, "Polynomial values as rows")
    PrintPolyRowArray(g.gen, rows, cols)
    print()

    if verbose: print(g.id, "Polynomial values as columns")
    PrintPolyColArray(g.gen, rows, cols)
    print()


if __name__ == "__main__":

    from Abel import Abel
    from Bell import Bell

    PrintViews(Abel, 6)
