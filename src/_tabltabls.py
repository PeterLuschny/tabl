from typing import Callable
from itertools import accumulate
from _tabltypes import tabl, trow, tgen
from _tablinverse import InverseTabl

def flat(t: tabl) -> list[int]: 
    """Flatten table to sequence

    Args:
        t (tabl): table

    Returns:
        list[int]: sequence
    """
    if t == []: return []
    return [i for row in t for i in row] 

# #@


def AntiDiagTabl(t: tabl) -> tabl:
    """Return the table of (upward) anti-diagonals."""
    return [[t[n - k - 1][k] 
             for k in range((n + 1) // 2)] 
             for n in range(1, len(t) + 1)]


def AccTabl(t: tabl) -> tabl:
    return [list(accumulate(row)) for row in t]


def RevTabl(t: tabl) -> tabl:
    return [list(reversed(row)) for row in t]


def InvTabl(t: tabl) -> tabl:
    return InverseTabl(t)


def InvRevTabl(t: tabl) -> tabl:
    return InverseTabl(RevTabl(t))


def RevAccTabl(t: tabl) -> tabl:
    return RevTabl(AccTabl(t))


def AccRevTabl(t: tabl) -> tabl:
    return AccTabl(RevTabl(t))


def FlatTabl(t: tabl) -> trow:
    return [i for row in t for i in row]


def FlatInvTabl(t: tabl) -> trow:
    return [i for row in InvTabl(t) for i in row]


def FlatRevTabl(t: tabl) -> trow:
    return [i for row in RevTabl(t) for i in row]


def FlatInvRevTabl(t: tabl) -> trow:
    return [i for row in InvTabl(RevTabl(t)) for i in row]


def FlatRevInvTabl(t: tabl) -> trow:
    return [i for row in RevTabl(InvTabl(t)) for i in row]


def FlatAntiDiagTabl(t: tabl) -> trow:
    return [i for row in AntiDiagTabl(t) for i in row]


def FlatAccTabl(t: tabl) -> trow:
    return [i for row in AccTabl(t) for i in row]


def FlatRevAccTabl(t: tabl) -> trow:
    return [i for row in RevAccTabl(t) for i in row]


def FlatAccRevTabl(t: tabl) -> trow:
    return [i for row in AccRevTabl(t) for i in row]


def FlatDiffxTabl(t: tabl) -> trow:
    return [(k + 1) * c for row in t for k,c in enumerate(row)]


def PrintTabls(t: tgen, size: int = 8, mdformat: bool = True) -> None:

    TABLSTRAIT: dict[str, Callable[[tabl], trow]] = {}
    def RegisterTablsTrait(f: Callable[[tabl], trow]) -> None: 
        TABLSTRAIT[f.__name__] = f

    T  = t.tab(size) 

    RegisterTablsTrait(FlatTabl)
    RegisterTablsTrait(FlatRevTabl)
    RegisterTablsTrait(FlatInvTabl)
    RegisterTablsTrait(FlatInvRevTabl)
    RegisterTablsTrait(FlatRevInvTabl)

    RegisterTablsTrait(FlatAccTabl)
    RegisterTablsTrait(FlatRevAccTabl)
    RegisterTablsTrait(FlatAccRevTabl)
    RegisterTablsTrait(FlatAntiDiagTabl)


    trianglename = t.id

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

    #PrintTabls(Abel, 4)
    #PrintTabls(StirlingSet, 6, False)
    #PrintTabls(LabeledGraphs, 6)

    T = LabeledGraphs.tab(9)
    print(T)
    print(AccTabl(T))
    print(FlatAccTabl(T))
    #print(InvTabl(T))
    #print(AntiDiagTabl(T))
