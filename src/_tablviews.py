from _tabltypes import rgen, tgen, tabl
from _tabltypes import InvTable, RevTable, RevInvTable, InvRevTable
from _tablpoly import PolyCol, PolyRow, PosHalf, NegHalf
from _tabltabls import AccTabl, RevAccTabl, AccRevTabl, RevTabl, AntiDiagTabl, Diffx1Tabl
from _tablsums import PrintSums
from _tabltransforms import (
    ColMiddle,
    CentralE,
    ColLeft,
    ColRight,
    RowLcm,
    RowGcd,
    RowMax,
    CentralO,
    BinConv,
    InvBinConv,
    TransSqrs, 
    TransNat0, 
    TransNat1,
)


# #@


def flat(t: tabl) -> list[int]:
    """Flatten table to sequence

    Args:
        t (tabl): table

    Returns:
        list[int]: sequence
    """
    if t == []:
        return []
    return [i for row in t for i in row]


def PrintTabl(t: tabl) -> None:
    for row in t:
        print(row)


def PrintFlat(t: tabl) -> None:
    print([i for r in t for i in r])


def PrintRows(t: tabl) -> None:
    print("|  Row   |  Seq   |")
    print("| :---   |  :---  |")
    for n, row in enumerate(t):
        print(f"| Row{n} | {row} |")


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
        print(f"| DiagRow{j} | {[T(j + k)[k] for k in range(cols)]}|")


def PrintColArray(T: rgen, rows: int, cols: int) -> None:
    print("| DiagCol  |   Seq  |")
    print("| :---     |  :---  |")
    for j in range(cols):
        print(f"| DiagCol{j} | {[T(j + k)[j] for k in range(rows)]} |")


def PrintPolyRowArray(T: rgen, rows: int, cols: int) -> None:
    print("| PolyRow  |   Seq  |")
    print("| :---     |  :---  |")
    for n in range(rows):
        print(f"| PolyRow{n} | {PolyRow(T, cols, n)} |")


def PrintPolyColArray(T: rgen, rows: int, cols: int) -> None:
    print("| PolyCol  |   Seq  |")
    print("| :---     |  :---  |")
    for n in range(rows):
        print(f"| PolyCol{n} | {PolyCol(T, cols, n)} |")


def PrintFlats(t: tabl) -> None:
    print("| Flat       |  Seq  |")
    print("| :---       | :---  |")
    print(f"| Triangle   | {t} |")
    print(f"| RevTabl    | {RevTabl(t)} |")
    print(f"| AntiDiag   | {AntiDiagTabl(t)} |")
    print(f"| AccTabl    | {AccTabl(t)} |")
    print(f"| RevAccTabl | {RevAccTabl(t)} |")
    print(f"| AccRevTabl | {AccRevTabl(t)} |")
    print(f"| DiffxTabl  | {Diffx1Tabl(t)} |")


def PrintTrans(t: tabl) -> None:
    print("| Trans      |   Seq  |")
    print("| :---       |  :---  |")
    print(f"| RowLcm     | {RowLcm(t)} |")
    print(f"| RowGcd     | {RowGcd(t)} |")
    print(f"| RowMax     | {RowMax(t)} |")
    print(f"| CentralE   | {CentralE(t)} |")
    print(f"| CentralO   | {CentralO(t)} |")
    print(f"| ColMiddle  | {ColMiddle(t)} |")
    print(f"| ColLeft    | {ColLeft(t)} |")
    print(f"| ColRight   | {ColRight(t)} |")
    print(f"| BinConv    | {BinConv(t)} |")
    print(f"| InvBinConv | {InvBinConv(t)} |")
    print(f"| TransSqrs  | {TransSqrs(t)} |")
    print(f"| TransNat0  | {TransNat0(t)} |")
    print(f"| TransNat1  | {TransNat1(t)} |")
    print(f"| PosHalf    | {PosHalf(t)} |")
    print(f"| NegHalf    | {NegHalf(t)} |")


def PrintViews(g: tgen, rows: int = 7, verbose: bool = True) -> None:
    print("# " + g.id)
    print(g.sim)

    cols: int = rows
    print()

    T: tabl = g.tab(rows)

    if verbose:
        print(g.id, "Triangle view")
        print()
    PrintRows(T)
    print()

    if verbose:
        print(g.id, "Triangles\n")
    PrintFlats(T)
    print()

    if verbose:
        print(g.id, "Row sums\n")
    PrintSums(T, g.id)
    print()

    if verbose:
        print(g.id, "Transforms\n")
    PrintTrans(T)
    print()

    if verbose:
        print(g.id, "Diagonals as rows\n")
    PrintRowArray(g.gen, rows, cols)
    print()

    if verbose:
        print(g.id, "Diagonals as columns\n")
    PrintColArray(g.gen, rows, cols)
    print()

    if verbose:
        print(g.id, "Polynomial values as rows\n")
    PrintPolyRowArray(g.gen, rows, cols)
    print()

    if verbose:
        print(g.id, "Polynomial values as columns\n")
    PrintPolyColArray(g.gen, rows, cols)
    print()


def PrintProfile(fun: tgen, dim: int = 10) -> None:
    tim: int = dim + dim

    PrintViews(fun, dim)

    V = InvTable(fun, tim)
    if V is not None:
        PrintViews(V, dim)

    r = RevTable(fun, tim)
    PrintViews(r, dim)

    r = RevInvTable(fun, tim)
    if r is not None:
        PrintViews(r, dim)

    r = InvRevTable(fun, tim)
    if r is not None:
        PrintViews(r, dim)


if __name__ == "__main__":
    from Abel import Abel
    from Bell import Bell

    # PrintViews(Abel, 6)
    PrintProfile(Abel)
