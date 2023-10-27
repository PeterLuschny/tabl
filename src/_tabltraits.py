from typing import Callable
from inspect import signature
from _tablpoly import PolyRow1, PolyRow2, PolyRow3, PolyCol2, PolyCol3, PolyDiag, PosHalfTabl, NegHalfTabl, PolyDiagRow
from _tablsums import RowSum, EvenSum, OddSum, AltSum, AccSum, AccRevSum, AntiDiagSum
from _tabltransforms import DiagRow1, DiagRow2, DiagRow3, DiagCol1, DiagCol2, DiagCol3
from _tabltransforms import TransNat0Tabl, TransNat1Tabl, TransSqrsTabl  
from _tabltransforms import BinConv, InvBinConv, RowLcm, RowGcd, RowMax, ColMiddle, ColECentral, ColOCentral, ColLeft, ColRight  
from _tabltabls import FlatTabl, FlatAccTabl, FlatAccRevTabl, FlatAntiDiagTabl, FlatRevTabl, FlatInvTabl, FlatInvRevTabl, FlatRevInvTabl, FlatDiffxTabl 


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

    RegisterTrait(TransNat0Tabl)
    RegisterTrait(TransNat1Tabl)
    RegisterTrait(TransSqrsTabl)

    RegisterTrait(PosHalfTabl)
    RegisterTrait(NegHalfTabl)

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

    RegisterTrait(PolyDiagRow)
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


def Formulas() -> dict[str, str]:
    FORMULA: dict[str, str] = {}

    FORMULA['Tabl']         = 'T(n, k), 0 &le; k &le; n'
    FORMULA['FlatTabl']     = 'T(n, k), 0 &le; k &le; n'
    FORMULA['RevTabl']      = 'T(n, n - k), 0 &le; k &le; n'
    FORMULA['InvTabl']      = 'T<sup>-1</sup>(n, k), 0 &le; k &le; n'
    FORMULA['RevInvTabl']   = 'T<sup>-1</sup>(n, n - k), 0 &le; k &le; n'
    FORMULA['InvRevTabl']   = '(T(n, n - k))<sup>-1</sup>, 0 &le; k &le; n'
    FORMULA['AccTabl']      = 'see docs'
    FORMULA['RevAccTabl']   = 'see docs'
    FORMULA['AccRevTabl']   = 'see docs'
    FORMULA['AntiDiagTabl'] = 'see docs'
    FORMULA['BinTabl']      = 'see docs'
    FORMULA['InvBinTabl']   = 'see docs'
    FORMULA['DiffxTabl']    = 'T(n, k) (k+1)'
    FORMULA['RowSum']       = '&sum;<sub> k=0..n </sub> T(n, k)'
    FORMULA['EvenSum']      = '&sum;<sub> k=0..n </sub> T(n, k) even(k)'
    FORMULA['OddSum']       = '&sum;<sub> k=0..n </sub> T(n, k) odd(k)'
    FORMULA['AltSum']       = '&sum;<sub> k=0..n </sub> T(n, k) (-1)^k'
    FORMULA['AntiDiagSum']  = '&sum;<sub> k=0..n // 2 </sub> T(n - k, k)'
    FORMULA['AccSum']       = '&sum;<sub> k=0..n </sub>&sum;<sub> j=0..k </sub> T(n, j)'
    FORMULA['AccRevSum']    = '&sum;<sub> k=0..n </sub>&sum;<sub> j=0..k </sub> T(n, n - j)'
    FORMULA['RowLcm']       = 'Lcm<sub> k=0..n </sub> | T(n, k) | &gt; 1'
    FORMULA['RowGcd']       = 'Gcd<sub> k=0..n </sub> | T(n, k) | &gt; 1'
    FORMULA['RowMax']       = 'Max<sub> k=0..n </sub> | T(n, k) |'
    FORMULA['ColMiddle']    = 'T(n, n // 2)'
    FORMULA['ColECentral']  = 'T(2 n, n)'
    FORMULA['ColOCentral']  = 'T(2 n + 1, n)'
    FORMULA['ColLeft']      = 'T(n, 0)'
    FORMULA['ColRight']     = 'T(n, n)'
    FORMULA['BinConv']      = '&sum;<sub> k=0..n </sub> C(n, k) T(n, k)'
    FORMULA['InvBinConv']   = '&sum;<sub> k=0..n </sub> C(n, k) T(n, n - k) (-1)^k'
    FORMULA['TransSqrsTabl']  = '&sum;<sub> k=0..n </sub> T(n, k) k^2'
    FORMULA['TransNat0Tabl']  = '&sum;<sub> k=0..n </sub> T(n, k) k'
    FORMULA['TransNat1Tabl']  = '&sum;<sub> k=0..n </sub> T(n, k) (k + 1)^k'
    FORMULA['DiagRow1']     = 'T(n + 1, n)'
    FORMULA['DiagRow2']     = 'T(n + 2, n)'
    FORMULA['DiagRow3']     = 'T(n + 3, n)'
    FORMULA['DiagCol1']     = 'T(n + 1, 1)'
    FORMULA['DiagCol2']     = 'T(n + 2, 2)'
    FORMULA['DiagCol3']     = 'T(n + 3, 3)'
    FORMULA['PolyTabl']     = 'see docs'
    FORMULA['PolyRow1']     = '&sum;<sub> k=0..1 </sub>T(1, k) n^k'
    FORMULA['PolyRow2']     = '&sum;<sub> k=0..2 </sub>T(2, k) n^k'
    FORMULA['PolyRow3']     = '&sum;<sub> k=0..3 </sub>T(3, k) n^k'
    FORMULA['PolyCol2']     = '&sum;<sub> k=0..n </sub>T(n, k) 2^k'
    FORMULA['PolyCol3']     = '&sum;<sub> k=0..n </sub>T(n, k) 3^k'
    FORMULA['PolyDiag']     = '&sum;<sub> k=0..n </sub>T(n, k) n^k'
    FORMULA['PolyDiagRow']  = 'see docs'
    FORMULA['PosHalfTabl']  = '&sum;<sub> k=0..n </sub>2^n T(n, k) (1/2)^k'
    FORMULA['NegHalfTabl']  = '&sum;<sub> k=0..n </sub>(-2)^n T(n, k) (-1/2)^k'

    return FORMULA


if __name__ == "__main__":

    R = RegisterTraits() 
    count = 0
    for k in R.items() : 
        count += 1
        print(count, is_tabletrait(k[1]), k[0])
