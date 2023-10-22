from typing import Callable
from _tabltypes import rgen, tgen, tabl, trow
from _tablpoly import PolyRow0, PolyRow1, PolyRow2, PolyRow3, PolyCol0, PolyCol1, PolyCol2, PolyCol3, PolyDiag, PosHalf, NegHalf, PolyTabl
from _tablsums import RowSum, EvenSum, OddSum, AltSum, AccSum, AccRevSum, AntiDiagSum
from _tabltabls import FlatTabl, FlatAccTabl, FlatRevAccTabl, FlatAccRevTabl, FlatAntiDiagTabl, FlatRevTabl, FlatInvTabl, FlatInvRevTabl, FlatRevInvTabl, FlatDiffxTabl 
from _tabltransforms import FlatBinTabl, FlatInvBinTabl, BinConv, InvBinConv,  RowLcm, RowGcd, RowMax, DiagRow0, DiagRow1, DiagRow2, DiagRow3, DiagCol0, DiagCol1, DiagCol2, DiagCol3, TransSqrs, TransNat0, TransNat1, ColMiddle, ColECentral, ColOCentral, ColLeft, ColRight 


# #@


TRAIT: dict[str, Callable[[tabl], trow]] = {}
def RegisterTrait(f: Callable[[tabl], trow]) -> None: 
    TRAIT[f.__name__] = f

TRAIT2: dict[str, Callable[[rgen, int], trow]] = {}
def RegisterTrait2(f: Callable[[rgen, int], trow]) -> None:
    TRAIT2[f.__name__] = f

def RegisterTraits() -> None:

    RegisterTrait(FlatTabl)   # must always come first!

    #RegisterTrait(FlatRevTabl)
    #RegisterTrait(FlatInvTabl)
    #RegisterTrait(FlatRevInvTabl)
    #RegisterTrait(FlatInvRevTabl)

    #RegisterTrait(FlatAccTabl)
    #RegisterTrait(FlatRevAccTabl) # rarely found
    #RegisterTrait(FlatAccRevTabl)
    #RegisterTrait(FlatAntiDiagTabl)
    #RegisterTrait(FlatBinTabl)    # rarely found
    #RegisterTrait(FlatInvBinTabl) # rarely found
    #RegisterTrait(FlatDiffxTabl)

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

#  -------------------------------------------

    RegisterTrait2(TransNat0)
    RegisterTrait2(TransNat1)
    RegisterTrait2(TransSqrs)
    # RegisterTrait2(DiagRow0) same as ColRight
    RegisterTrait2(DiagRow1)
    RegisterTrait2(DiagRow2)
    RegisterTrait2(DiagRow3)
    # RegisterTrait2(DiagCol0) same as ColLeft
    RegisterTrait2(DiagCol1)
    RegisterTrait2(DiagCol2)
    RegisterTrait2(DiagCol3)

    RegisterTrait2(PolyTabl)
    # RegisterTrait2(PolyRow0)
    RegisterTrait2(PolyRow1)
    RegisterTrait2(PolyRow2)
    RegisterTrait2(PolyRow3)
    # RegisterTrait2(PolyCol0) same as ColLeft
    # RegisterTrait2(PolyCol1) same as RowSum
    RegisterTrait2(PolyCol2) 
    RegisterTrait2(PolyCol3)
    RegisterTrait2(PolyDiag)
    RegisterTrait2(PosHalf)
    RegisterTrait2(NegHalf)


'''
for fun in tabl_fun:
        PrintTraits(fun, 20, True)

for traitname, hits in HITS.items():
    print(f'| {hits} | {traitname:<16} |')


[ 0]  6  FlatDiffx
[ 1]  7  RevAccTabl
[ 2] 11  AccRevTabl
[ 3] 12  InvRevTabl
[ 4] 13  AccTabl
[ 5] 14  RowLcm
[ 6] 15  Poly
#------------------- 
[ 7] 19  TransSqrs
[ 8] 22  RevInvTabl
[ 9] 28  AntiDiagTabl
[10] 28  PolyDiag
[11] 29  ColMiddle
[12] 29  InvTabl
[13] 32  AccSum
[14] 32  BinConv
[15] 32  InvBinConv
[16] 34  AccRevSum
[17] 34  TransNat1
[18] 35  PolyRow3
[19] 36  PolyCol3
[20] 40  AntiDiagSum
[21] 40  TransNat0
[22] 42  OddSum
[23] 45  EvenSum
[24] 45  RowMax
[25] 46  NegHalf
[26] 47  PosHalf
[27] 48  PolyCol2
[28] 51  ColCentral
[29] 53  RowGcd
[30] 54  RevTabl
[31] 55  DiagRow3
[32] 57  AltSum
[33] 58  DiagCol3
[34] 60  DiagCol2
[35] 61  DiagRow2
[36] 65  DiagCol1
[37] 65  PolyRow2
[38] 66  DiagRow1
--
[39] 67  ColLeft
[40] 67  ColRight
[41] 67  * DiagCol0
[42] 67  * DiagRow0
[43] 67  Tabl
[44] 67  * PolyCol0
[45] 67  * PolyCol1
[46] 67  * PolyRow0
[47] 67  PolyRow1
[48] 67  RowSum

DiagCol0 = PolyCol0 = ColLeft
DiagRow0 = PolyRow0 = ColRight
RowSum   = PolyCol1

'''
