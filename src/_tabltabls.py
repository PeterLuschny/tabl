"""
This module provides various functions to manipulate and transform triangular tables (tabl).
Functions:
    AntiDiagTabl(T: tabl) -> tabl:
        Return the table of (upward) anti-diagonals.
    AccTabl(T: tabl) -> tabl:
        Return the table with accumulated sums of each row.
    RevTabl(T: tabl) -> tabl:
        Return the table with each row reversed.
    InvTabl(T: tabl) -> tabl:
        Return the inverted table.
    InvRevTabl(T: tabl) -> tabl:
        Return the inverted and reversed table.
    RevAccTabl(T: tabl) -> tabl:
        Return the table with each row reversed and then accumulated.
    AccRevTabl(T: tabl) -> tabl:
        Return the table with each row accumulated and then reversed.
    AltSignTabl(T: tabl) -> tabl:
        Return the table with alternating signs applied to each element.
    Diffx1(T: tabl) -> trow:
        Return a flattened table with each element multiplied by its 1-based index.
    Diffx1Tabl(T: tabl) -> tabl:
        Return the table with each element multiplied by its 1-based index.
    Diffx0(T: tabl) -> trow:
        Return a flattened table with each element multiplied by its 0-based index.
    Diffx0Tabl(T: tabl) -> tabl:
        Return the table with each element multiplied by its 0-based index.
    Triangle(T: tabl) -> trow:
        Return a flattened table.
    Triangle_(g: rgen, row: int) -> trow:
        Generate a row of the table using the provided generator function.
    Inv(T: tabl) -> trow:
        Return a flattened inverted table.
    Rev(T: tabl) -> trow:
        Return a flattened reversed table.
    InvRev(T: tabl) -> trow:
        Return a flattened inverted and reversed table.
    RevInv(T: tabl) -> trow:
        Return a flattened reversed and inverted table.
    AntiDiag(T: tabl) -> trow:
        Return a flattened table of (upward) anti-diagonals.
    Acc(T: tabl) -> trow:
        Return a flattened table with accumulated sums of each row.
    RevAcc(T: tabl) -> trow:
        Return a flattened table with each row reversed and then accumulated.
    AccRev(T: tabl) -> trow:
        Return a flattened table with each row accumulated and then reversed.
    AltSign(T: tabl) -> trow:
        Return a flattened table with alternating signs applied to each element.
    PrintTabls(g: tgen, size: int = 8, mdformat: bool = True) -> None:
        Print various traits of the table generated by the provided generator function.
Usage:
    This module can be used to manipulate and transform triangular tables 
    for various mathematical and computational purposes.
"""

from typing import Callable
from itertools import accumulate
from _tabltypes import tabl, trow, tgen, rgen
from _tablinverse import InvertTabl


# #@


def AntiDiagTabl(T: tabl) -> tabl:
    """Return the table of (upward) anti-diagonals."""
    return [[T[n - k - 1][k]
            for k in range((n + 1) // 2)]
            for n in range(1, len(T) + 1)]


def AccTabl(T: tabl) -> tabl:
    return [list(accumulate(row)) for row in T]


def RevTabl(T: tabl) -> tabl:
    return [list(reversed(row)) for row in T]


def InvTabl(T: tabl) -> tabl:
    return InvertTabl(T)


def InvRevTabl(T: tabl) -> tabl:
    return InvertTabl(RevTabl(T))


def RevAccTabl(T: tabl) -> tabl:
    return RevTabl(AccTabl(T))


def AccRevTabl(T: tabl) -> tabl:
    return AccTabl(RevTabl(T))


def AltSignTabl(T: tabl) -> tabl:
    return [[(-1)**k * T[n][k]
            for k in range(n + 1)]
            for n in range(len(T))]


def Diffx1(T: tabl) -> trow:  # flat tabl
    return [(k + 1) * c for row in T for k, c in enumerate(row)]


def Diffx1Tabl(T: tabl) -> tabl:
    return [[(k + 1) * c for k, c in enumerate(row)] for row in T]


def Diffx0(T: tabl) -> trow:  # flat tabl
    return [k * c for row in T for k, c in enumerate(row)]


def Diffx0Tabl(T: tabl) -> tabl:
    return [[k * c for k, c in enumerate(row)] for row in T]


def Triangle(T: tabl) -> trow:
    return [i for row in T for i in row]


def Triangle_(g: rgen, row: int) -> trow:
    return g(row)


def Inv(T: tabl) -> trow:
    IT = InvTabl(T)
    if InvTabl(T) == []:
        return []
    return [i for row in IT for i in row]


def Rev(T: tabl) -> trow:
    return [i for row in RevTabl(T) for i in row]


def InvRev(T: tabl) -> trow:
    return [i for row in InvTabl(RevTabl(T)) for i in row]


def RevInv(T: tabl) -> trow:
    IT = InvTabl(T)
    return [i for row in RevTabl(IT) for i in row]


def AntiDiag(T: tabl) -> trow:
    return [i for row in AntiDiagTabl(T) for i in row]


def Acc(T: tabl) -> trow:
    return [i for row in AccTabl(T) for i in row]


def RevAcc(T: tabl) -> trow:
    return [i for row in RevAccTabl(T) for i in row]


def AccRev(T: tabl) -> trow:
    return [i for row in AccRevTabl(T) for i in row]


def AltSign(T: tabl) -> trow:
    return [i for row in AltSignTabl(T) for i in row]


def PrintTabls(g: tgen, size: int = 8, mdformat: bool = True) -> None:

    TABLSTRAIT: dict[str, Callable[[tabl], trow]] = {}

    def RegisterTablsTrait(f: Callable[[tabl], trow]) -> None:
        TABLSTRAIT[f.__name__] = f

    T = g.tab(size)

    RegisterTablsTrait(Triangle)
    RegisterTablsTrait(Rev)
    RegisterTablsTrait(Inv)
    RegisterTablsTrait(InvRev)
    RegisterTablsTrait(RevInv)

    RegisterTablsTrait(Acc)
    RegisterTablsTrait(RevAcc)
    RegisterTablsTrait(AccRev)
    RegisterTablsTrait(AntiDiag)
    RegisterTablsTrait(Diffx0)

    trianglename = g.id

    if mdformat:
        print("#", trianglename, ": Tables")
        print()  # reqiured!
        print("| Trait    |   Seq  |")
        print("| :---     |  :---  |")
        for traitname, trait in TABLSTRAIT.items():
            print(f'| {traitname:<15} | {trait(T)} |')
    else:
        for traitname, trait in TABLSTRAIT.items():
            print(f'{trianglename+":"+traitname:<21} {trait(T)}')


if __name__ == "__main__":

    from Abel import Abel
    # from StirlingSet import StirlingSet
    # from LabeledGraphs import LabeledGraphs

    T = Abel.tab(8)
    A = AltSignTabl(T)
    print(T)
    print(A)

    # print(RevTabl(Abel.tab(6)))
    # print(Rev(Abel.tab(6)))

    # print(RevTabl(Abel.tab(6)))
    # print(Rev(Abel.tab(6)))

    # PrintTabls(Abel, 6)
    # PrintTabls(StirlingSet, 6, False)
    # PrintTabls(LabeledGraphs, 6)

    # T = LabeledGraphs.tab(9)
    # print(T)
    # print(AccTabl(T))
    # print(Acc(T))
    # print(InvTabl(T))
    # print(AntiDiag(T))
