from typing import Callable
from inspect import signature
from _tabltypes import rgen, tabl, trow
from _tablpoly import PolyRow1, PolyRow2, PolyRow3, PolyCol2, PolyCol3, PolyDiag, PosHalf, NegHalf, PosHalfTab, NegHalfTab, PolyDiagTablRow
from _tablsums import RowSum, EvenSum, OddSum, AltSum, AccSum, AccRevSum, AntiDiagSum
from _tabltransforms import DiagRow1, DiagRow2, DiagRow3, DiagCol1, DiagCol2, DiagCol3, TransSqrs, TransNat0, TransNat1 
from _tabltransforms import TransNat0Tab, TransNat1Tab, TransSqrsTab  # DiagRow1, DiagRow2, DiagRow3, DiagCol1, DiagCol2, DiagCol3, 
from _tabltransforms import BinConv, InvBinConv, RowLcm, RowGcd, RowMax, ColMiddle, ColECentral, ColOCentral, ColLeft, ColRight  
from _tabltabls import FlatTabl , FlatAccTabl, FlatRevAccTabl, FlatAccRevTabl, FlatAntiDiagTabl, FlatRevTabl, FlatInvTabl, FlatInvRevTabl, FlatRevInvTabl, FlatDiffxTabl 


'''
Traits come in two flavors: 
    The 'table' type:
    TYPE: Callable[[tabl], trow]]:
  
    The 'generic' type:
    TYPE: Callable[[rgen, int], trow]]

    To diffenrentiate use the function 'is_tabletrait(f)'
    that returns 'True' if 'f' is of table-type.
'''

# #@


def is_tabletrait(f: Callable):
    sig = signature(f)
    ann = list(sig.parameters.values())[0].annotation
    return ann == list[list[int]]


def RegisterTraits() -> dict[str, Callable]:
    
    TRAITS: dict[str, Callable] = {}
    def RegisterTrait(f: Callable): 
        TRAITS[f.__name__] = f

    # TYPE: Callable[[tabl], trow]]:

    RegisterTrait(FlatTabl)   # must always come first!

    RegisterTrait(FlatRevTabl)
    RegisterTrait(FlatInvTabl)
    RegisterTrait(FlatRevInvTabl)
    RegisterTrait(FlatInvRevTabl)

    RegisterTrait(FlatAccTabl)
    #RegisterTrait(FlatRevAccTabl) # rarely found
    RegisterTrait(FlatAccRevTabl)
    RegisterTrait(FlatAntiDiagTabl)
    #RegisterTrait(FlatBinTabl)    # rarely found
    #RegisterTrait(FlatInvBinTabl) # rarely found
    RegisterTrait(FlatDiffxTabl)

    RegisterTrait(RowSum)
    RegisterTrait(EvenSum)
    RegisterTrait(OddSum)
    RegisterTrait(AltSum)
    RegisterTrait(AntiDiagSum)
    RegisterTrait(AccSum)
    RegisterTrait(AccRevSum)

    RegisterTrait(RowLcm)
    RegisterTrait(RowGcd)
    RegisterTrait(RowMax)

    RegisterTrait(ColMiddle)
    RegisterTrait(ColECentral)
    RegisterTrait(ColOCentral)
    RegisterTrait(ColLeft)
    RegisterTrait(ColRight)
    
    RegisterTrait(BinConv)
    RegisterTrait(InvBinConv)

    RegisterTrait(TransNat0Tab)
    RegisterTrait(TransNat1Tab)
    RegisterTrait(TransSqrsTab)

    RegisterTrait(PosHalfTab)
    RegisterTrait(NegHalfTab)

    # TYPE Callable[[rgen, int], trow]]

    # RegisterTrait(TransNat0)
    # RegisterTrait(TransNat1)
    # RegisterTrait(TransSqrs)
    # RegisterTrait(DiagRow0) same as ColRight
    RegisterTrait(DiagRow1)
    RegisterTrait(DiagRow2)
    RegisterTrait(DiagRow3)
    # RegisterTrait(DiagCol0) same as ColLeft
    RegisterTrait(DiagCol1)
    RegisterTrait(DiagCol2)
    RegisterTrait(DiagCol3)

    RegisterTrait(PolyDiagTablRow)
    # RegisterTrait(PolyRow0)
    RegisterTrait(PolyRow1)
    RegisterTrait(PolyRow2)
    RegisterTrait(PolyRow3)
    # RegisterTrait(PolyCol0) same as ColLeft
    # RegisterTrait(PolyCol1) same as RowSum
    # Bernoulli(n,0) versus Bernoulli(n,1)!
    RegisterTrait(PolyCol2) 
    RegisterTrait(PolyCol3)
    RegisterTrait(PolyDiag)
    # RegisterTrait(PosHalf)
    # RegisterTrait(NegHalf)

    return TRAITS

def RegisterGenericTraits() -> dict[str, Callable[[rgen, int], trow]]:
    
    TABLES: dict[str, Callable[[rgen, int], trow]] = {}
    def RegisterGenericTrait(f: Callable[[rgen, int], trow]): 
        TABLES[f.__name__] = f

    RegisterGenericTrait(TransNat0)
    RegisterGenericTrait(TransNat1)
    RegisterGenericTrait(TransSqrs)
    # RegisterGenericTrait(DiagRow0) same as ColRight
    RegisterGenericTrait(DiagRow1)
    RegisterGenericTrait(DiagRow2)
    RegisterGenericTrait(DiagRow3)
    # RegisterGenericTrait(DiagCol0) same as ColLeft
    RegisterGenericTrait(DiagCol1)
    RegisterGenericTrait(DiagCol2)
    RegisterGenericTrait(DiagCol3)

    RegisterGenericTrait(PolyDiagTablRow)
    # RegisterGenericTrait(PolyRow0)
    RegisterGenericTrait(PolyRow1)
    RegisterGenericTrait(PolyRow2)
    RegisterGenericTrait(PolyRow3)
    # RegisterGenericTrait(PolyCol0) same as ColLeft
    # RegisterGenericTrait(PolyCol1) same as RowSum
    # Bernoulli(n,0) versus Bernoulli(n,1)!
    RegisterGenericTrait(PolyCol2) 
    RegisterGenericTrait(PolyCol3)
    RegisterGenericTrait(PolyDiag)
    RegisterGenericTrait(PosHalf)
    RegisterGenericTrait(NegHalf)

    return TABLES


def RegisterTableTraits() -> dict[str, Callable[[tabl], trow]]:

    TRAITS: dict[str, Callable[[tabl], trow]] = {}
    def RegisterTableTrait(f: Callable[[tabl], trow]): 
        TRAITS[f.__name__] = f

    RegisterTableTrait(FlatTabl)   # must always come first!

    #RegisterTableTrait(FlatRevTabl)
    #RegisterTableTrait(FlatInvTabl)
    #RegisterTableTrait(FlatRevInvTabl)
    #RegisterTableTrait(FlatInvRevTabl)

    #RegisterTableTrait(FlatAccTabl)
    #RegisterTableTrait(FlatRevAccTabl) # rarely found
    #RegisterTableTrait(FlatAccRevTabl)
    #RegisterTableTrait(FlatAntiDiagTabl)
    #RegisterTableTrait(FlatBinTabl)    # rarely found
    #RegisterTableTrait(FlatInvBinTabl) # rarely found
    #RegisterTableTrait(FlatDiffxTabl)

    RegisterTableTrait(RowSum)
    RegisterTableTrait(EvenSum)
    RegisterTableTrait(OddSum)
    RegisterTableTrait(AltSum)
    RegisterTableTrait(AntiDiagSum)
    RegisterTableTrait(AccSum)
    RegisterTableTrait(AccRevSum)

    RegisterTableTrait(RowLcm)
    RegisterTableTrait(RowGcd)
    RegisterTableTrait(RowMax)

    RegisterTableTrait(ColMiddle)
    RegisterTableTrait(ColECentral)
    RegisterTableTrait(ColOCentral)
    RegisterTableTrait(ColLeft)
    RegisterTableTrait(ColRight)
    
    RegisterTableTrait(BinConv)
    RegisterTableTrait(InvBinConv)

    RegisterTableTrait(TransNat0Tab)
    RegisterTableTrait(TransNat1Tab)
    RegisterTableTrait(TransSqrsTab)

    RegisterTableTrait(PosHalfTab)
    RegisterTableTrait(NegHalfTab)

    return TRAITS


if __name__ == "__main__":

    #T = RegisterTableTraits()
    #G = RegisterGenericTraits()
    #for k in T.items() : print(is_tabletrait(k[1]), k[0])
    #for k in G.items() : print(is_tabletrait(k[1]), k[0])

    R = RegisterTraits() 
    count = 0
    for k in R.items() : 
        count += 1
        print(count, is_tabletrait(k[1]), k[0])
