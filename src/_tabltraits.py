from _tabltypes import trait
from inspect import signature
from _tablsums import RowSum, EvenSum, OddSum, AltSum, AbsSum, AccSum, AccRevSum, DiagSum
from _tabltransforms import DiagRow1, DiagRow2, DiagRow3, DiagCol1, DiagCol2, DiagCol3
from _tabltransforms import TransNat0, TransNat1, TransSqrs
from _tabltabls import Triangle, Acc, AccRev, AntiDiag, Rev, Inv, InvRev, RevInv, Diffx1
from _tabltransforms import (
    BinConv, InvBinConv, RowLcm, RowGcd, RowMax,
    ColMiddle, CentralE, CentralO, ColLeft, ColRight,
)
from _tablpoly import (
    PolyRow1, PolyRow2, PolyRow3, PolyCol2, PolyCol3,
    PolyDiag, PosHalf, NegHalf, Poly,
)


# #@


def is_tabletrait(f: trait) -> bool:
    """
    Traits come in two flavors:

    (a) The 'table' type: Callable[[tabl], trow]]:
    (b) The 'generic' type: Callable[[rgen, int], trow]]

    To diffenrentiate use the function 'is_tabletrait(f)'
    that returns 'True' if 'f' is of table-type.
"""
    sig = signature(f)
    ann = list(sig.parameters.values())[0].annotation
    return ann == list[list[int]]


def RegisterTraits() -> dict[str, trait]:
    TRAITS: dict[str, trait] = {}

    def RegisterTrait(f: trait) -> None:
        TRAITS[f.__name__] = f

    # TYPE: Callable[[tabl], trow]]:

    RegisterTrait(Triangle)  # is flat; must always come first!

    RegisterTrait(Rev)
    RegisterTrait(Inv)
    RegisterTrait(RevInv)
    RegisterTrait(InvRev)

    RegisterTrait(Acc)
    # RegisterTrait(RevAcc) # rarely found
    RegisterTrait(AccRev)
    RegisterTrait(AntiDiag)
    RegisterTrait(Diffx1)

    RegisterTrait(RowSum)
    RegisterTrait(EvenSum)
    RegisterTrait(OddSum)
    RegisterTrait(AltSum)
    RegisterTrait(AbsSum)
    RegisterTrait(DiagSum)
    RegisterTrait(AccSum)
    RegisterTrait(AccRevSum)

    RegisterTrait(RowLcm)
    RegisterTrait(RowGcd)
    RegisterTrait(RowMax)

    RegisterTrait(ColMiddle)
    RegisterTrait(CentralE)
    RegisterTrait(CentralO)
    RegisterTrait(ColLeft)
    RegisterTrait(ColRight)

    RegisterTrait(BinConv)
    RegisterTrait(InvBinConv)

    RegisterTrait(TransNat0)
    RegisterTrait(TransNat1)
    RegisterTrait(TransSqrs)

    RegisterTrait(PosHalf)
    RegisterTrait(NegHalf)

    # TYPE Callable[[rgen, int], trow]]

    # RegisterTrait(DiagRow0) same as ColRight
    RegisterTrait(DiagRow1)
    RegisterTrait(DiagRow2)
    RegisterTrait(DiagRow3)
    # RegisterTrait(DiagCol0) same as ColLeft
    RegisterTrait(DiagCol1)
    RegisterTrait(DiagCol2)
    RegisterTrait(DiagCol3)

    RegisterTrait(Poly)
    # RegisterTrait(PolyRow0)
    RegisterTrait(PolyRow1)
    RegisterTrait(PolyRow2)
    RegisterTrait(PolyRow3)
    # RegisterTrait(PolyCol0) same as ColLeft
    # RegisterTrait(PolyCol1) same as RowSum
    RegisterTrait(PolyCol2)
    RegisterTrait(PolyCol3)
    RegisterTrait(PolyDiag)

    return TRAITS


def Formulas() -> dict[str, str]:
    FORMULA: dict[str, str] = {}

    FORMULA["Triangle"] = "T(n, k), 0 &le; k &le; n"
    FORMULA["Rev"] = "T(n, n - k), 0 &le; k &le; n"
    FORMULA["Inv"] = "T<sup>-1</sup>(n, k), 0 &le; k &le; n"
    FORMULA["RevInv"] = "T<sup>-1</sup>(n, n - k), 0 &le; k &le; n"
    FORMULA["InvRev"] = "(T(n, n - k))<sup>-1</sup>, 0 &le; k &le; n"
    FORMULA["Acc"] = "see docs"
    FORMULA["RevAcc"] = "see docs"
    FORMULA["AccRev"] = "see docs"
    FORMULA["AntiDiag"] = "see docs"
    FORMULA["Diffx1"] = "T(n, k) (k+1)"
    FORMULA["RowSum"] = "&sum;<sub> k=0..n </sub> T(n, k)"
    FORMULA["EvenSum"] = "&sum;<sub> k=0..n </sub> T(n, k) even(k)"
    FORMULA["OddSum"] = "&sum;<sub> k=0..n </sub> T(n, k) odd(k)"
    FORMULA["AltSum"] = "&sum;<sub> k=0..n </sub> T(n, k) (-1)^k"
    FORMULA["AbsSum"] = "&sum;<sub> k=0..n </sub> | T(n, k) |"
    FORMULA["DiagSum"] = "&sum;<sub> k=0..n // 2 </sub> T(n - k, k)"
    FORMULA["AccSum"] = "&sum;<sub> k=0..n </sub>&sum;<sub> j=0..k </sub> T(n, j)"
    FORMULA["AccRevSum"] = "&sum;<sub> k=0..n </sub>&sum;<sub> j=0..k </sub> T(n, n - j)"
    FORMULA["RowLcm"] = "Lcm<sub> k=0..n </sub> | T(n, k) | &gt; 1"
    FORMULA["RowGcd"] = "Gcd<sub> k=0..n </sub> | T(n, k) | &gt; 1"
    FORMULA["RowMax"] = "Max<sub> k=0..n </sub> | T(n, k) |"
    FORMULA["ColMiddle"] = "T(n, n // 2)"
    FORMULA["CentralE"] = "T(2 n, n)"
    FORMULA["CentralO"] = "T(2 n + 1, n)"
    FORMULA["ColLeft"] = "T(n, 0)"
    FORMULA["ColRight"] = "T(n, n)"
    FORMULA["BinConv"] = "&sum;<sub> k=0..n </sub> C(n, k) T(n, k)"
    FORMULA["InvBinConv"] = "&sum;<sub> k=0..n </sub> C(n, k) T(n, n - k) (-1)^k"
    FORMULA["TransSqrs"] = "&sum;<sub> k=0..n </sub> T(n, k) k^2"
    FORMULA["TransNat0"] = "&sum;<sub> k=0..n </sub> T(n, k) k"
    FORMULA["TransNat1"] = "&sum;<sub> k=0..n </sub> T(n, k) (k + 1)"
    FORMULA["DiagRow1"] = "T(n + 1, n)"
    FORMULA["DiagRow2"] = "T(n + 2, n)"
    FORMULA["DiagRow3"] = "T(n + 3, n)"
    FORMULA["DiagCol1"] = "T(n + 1, 1)"
    FORMULA["DiagCol2"] = "T(n + 2, 2)"
    FORMULA["DiagCol3"] = "T(n + 3, 3)"
    FORMULA["Poly"] = "see docs"
    FORMULA["PolyRow1"] = "&sum;<sub> k=0..1 </sub>T(1, k) n^k"
    FORMULA["PolyRow2"] = "&sum;<sub> k=0..2 </sub>T(2, k) n^k"
    FORMULA["PolyRow3"] = "&sum;<sub> k=0..3 </sub>T(3, k) n^k"
    FORMULA["PolyCol2"] = "&sum;<sub> k=0..n </sub>T(n, k) 2^k"
    FORMULA["PolyCol3"] = "&sum;<sub> k=0..n </sub>T(n, k) 3^k"
    FORMULA["PolyDiag"] = "&sum;<sub> k=0..n </sub>T(n, k) n^k"
    FORMULA["PosHalf"] = "&sum;<sub> k=0..n </sub>2^n T(n, k) (1/2)^k"
    FORMULA["NegHalf"] = "&sum;<sub> k=0..n </sub>(-2)^n T(n, k) (-1/2)^k"

    return FORMULA


if __name__ == "__main__":
    R = RegisterTraits()
    count = 0
    for k in R.items():
        count += 1
        print(count, is_tabletrait(k[1]), k[0])
