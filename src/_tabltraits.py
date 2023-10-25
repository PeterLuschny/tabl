from typing import Callable
from inspect import signature
from _tabltypes import rgen, tabl, trow
from _tablpoly import PolyRow1, PolyRow2, PolyRow3, PolyCol2, PolyCol3, PolyDiag, PosHalf, NegHalf, PosHalfTab, NegHalfTab, PolyDiagTablRow
from _tablsums import RowSum, EvenSum, OddSum, AltSum, AccSum, AccRevSum, AntiDiagSum
from _tabltransforms import DiagRow1, DiagRow2, DiagRow3, DiagCol1, DiagCol2, DiagCol3, TransSqrs, TransNat0, TransNat1 
from _tabltransforms import TransNat0Tab, TransNat1Tab, TransSqrsTab  # DiagRow1, DiagRow2, DiagRow3, DiagCol1, DiagCol2, DiagCol3, 
from _tabltransforms import BinConv, InvBinConv, RowLcm, RowGcd, RowMax, ColMiddle, ColECentral, ColOCentral, ColLeft, ColRight  
from _tabltabls import FlatTabl, FlatAccTabl, FlatRevAccTabl, FlatAccRevTabl, FlatAntiDiagTabl, FlatRevTabl, FlatInvTabl, FlatInvRevTabl, FlatRevInvTabl, FlatDiffxTabl 


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


if __name__ == "__main__":

    R = RegisterTraits() 
    count = 0
    for k in R.items() : 
        count += 1
        print(count, is_tabletrait(k[1]), k[0])
