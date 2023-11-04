from typing import Callable
from itertools import accumulate
from _tabltypes import tabl, trow, tgen, rgen
from _tablinverse import InvertTabl

def flat(T: tabl) -> list[int]: 
    """Flatten table to sequence

    Args:
        T (tabl): table

    Returns:
        list[int]: sequence
    """
    if T == []: return []
    return [i for row in T for i in row] 

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


def Triangle(T: tabl) -> trow:
    return [i for row in T for i in row]


def Triangle_(g: rgen, row: int) -> trow:
    return g(row)


def Inv(T: tabl) -> trow:
    IT = InvTabl(T)
    if InvTabl(T) == []: return []
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


def Diffx(T: tabl) -> trow:
    return [(k + 1) * c for row in T for k,c in enumerate(row)]


def PrintTabls(g: tgen, size: int = 8, mdformat: bool = True) -> None:

    TABLSTRAIT: dict[str, Callable[[tabl], trow]] = {}
    def RegisterTablsTrait(f: Callable[[tabl], trow]) -> None: 
        TABLSTRAIT[f.__name__] = f

    T  = g.tab(size) 

    RegisterTablsTrait(Triangle)
    RegisterTablsTrait(Rev)
    RegisterTablsTrait(Inv)
    RegisterTablsTrait(InvRev)
    RegisterTablsTrait(RevInv)

    RegisterTablsTrait(Acc)
    RegisterTablsTrait(RevAcc)
    RegisterTablsTrait(AccRev)
    RegisterTablsTrait(AntiDiag)


    trianglename = T.id

    if mdformat:
        print("#", trianglename, ": Tables")
        print() # reqiured!
        print( "| Trait    |   Seq  |")
        print( "| :---     |  :---  |")
        for traitname, trait in TABLSTRAIT.items():
            print(f'| {traitname:<15} | {trait(T)} |')
    else:
        for traitname, trait in TABLSTRAIT.items():
            print(f'{trianglename+":"+traitname:<21} {trait(T)}')


if __name__ == "__main__":

    from Abel import Abel
    from StirlingSet import StirlingSet
    from LabeledGraphs import LabeledGraphs

    print(RevTabl(Abel.tab(6)))
    print(Rev(Abel.tab(6)))

    #PrintTabls(Abel, 4)
    #PrintTabls(StirlingSet, 6, False)
    #PrintTabls(LabeledGraphs, 6)

    #T = LabeledGraphs.tab(9)
    #print(T)
    #print(AccTabl(T))
    #print(Acc(T))
    #print(InvTabl(T))
    #print(AntiDiag(T))
