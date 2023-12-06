from typing import Callable
from Pascal import binomial
from math import lcm, gcd
from functools import reduce
from _tabltypes import seq, tabl, trow, rgen, tgen


"""
Note the convention:
    def RowLcm(t: trow) -> int:
    def RowLcm_(f: rgen, n: int) -> int:
called 'multidispatch on trailing underscore'.

Similar:
    def TransBinomial(T: tabl) -> trow:
    def TransBinomial_(g: rgen, size: int) -> trow:
"""

# #@


def LinMap_(g: rgen, V: seq, size: int) -> trow:
    return [sum(g(n)[k] * V(k) for k in range(n + 1)) for n in range(size)]


def LinMap(T: tabl, V: seq) -> trow:
    return [sum(T[n][k] * V(k) for k in range(n + 1)) for n in range(len(T))]


def BinMap(V: seq, size: int) -> trow:
    return [sum(binomial(n)[k] * V(k) for k in range(n + 1)) for n in range(size)]


def BinTabl_(g: rgen, size: int) -> tabl:
    return [BinMap(lambda k: g(n)[k], n + 1) for n in range(size)]


def BinTabl(T: tabl) -> tabl:
    return [BinMap(lambda k: T[n][k], n + 1) for n in range(len(T))]


def FlatBinTabl(T: tabl) -> trow:
    return [i for row in BinTabl(T) for i in row]


def BinConv(T: tabl) -> trow:
    R = [LinMap_(binomial, lambda k: T[n][k], n + 1) for n in range(len(T))]
    return [row[-1] for row in R]


def BinConv_(g: rgen, size: int) -> trow:
    T = BinTabl_(g, size)
    return [row[-1] for row in T]


def ConvTabl_(g: rgen, size: int) -> tabl:
    return [LinMap_(g, lambda k: g(n)[k], n + 1) for n in range(size)]


def Conv(T: tabl) -> tabl:
    def g(n: int) -> list[int]:
        return [T[n][k] for k in range(n + 1)]

    return [LinMap_(g, lambda k: g(n)[k], n + 1) for n in range(len(T))]


def FlatConvTabl(T: tabl) -> trow:
    return [i for row in Conv(T) for i in row]


def InvLinMap(g: rgen, V: seq, size: int) -> trow:
    return [
        sum((-1) ** (n - k) * g(n)[k] * V(k) for k in range(n + 1)) for n in range(size)
    ]


def InvConvTabl(g: rgen, size: int) -> tabl:
    return [InvLinMap(g, lambda k: g(n)[k], n + 1) for n in range(size)]


def InvBinMap(V: seq, size: int) -> trow:
    return [
        sum((-1) ** (n - k) * binomial(n)[k] * V(k) for k in range(n + 1))
        for n in range(size)
    ]


def InvBin(T: tabl) -> tabl:
    return [InvBinMap(lambda k: T[n][k], n + 1) for n in range(len(T))]


def InvBin_(g: rgen, size: int) -> tabl:
    return [InvBinMap(lambda k: g(n)[k], n + 1) for n in range(size)]


def FlatInvBinTabl(T: tabl) -> trow:
    return [i for row in InvBin(T) for i in row]


def InvBinConv(T: tabl) -> trow:
    R = [
        LinMap_(binomial, lambda k: (-1) ** (n - k) * T[n][k], n + 1)
        for n in range(len(T))
    ]
    return [row[-1] for row in R]


def InvBinConv_(g: rgen, size: int) -> trow:
    T = InvBin_(g, size)
    return [row[-1] for row in T]


def DiagRow(g: rgen, size: int, j: int) -> trow:
    return [g(j + k)[k] for k in range(size)]


def DiagRow0(g: rgen, size: int) -> trow:
    return DiagRow(g, size, 0)


def DiagRow1(g: rgen, size: int) -> trow:
    return DiagRow(g, size, 1)


def DiagRow2(g: rgen, size: int) -> trow:
    return DiagRow(g, size, 2)


def DiagRow3(g: rgen, size: int) -> trow:
    return DiagRow(g, size, 3)


def DiagCol(g: rgen, size: int, j: int) -> trow:
    return [g(j + k)[j] for k in range(size)]


def DiagCol0(g: rgen, size: int) -> trow:
    return DiagCol(g, size, 0)


def DiagCol1(g: rgen, size: int) -> trow:
    return DiagCol(g, size, 1)


def DiagCol2(g: rgen, size: int) -> trow:
    return DiagCol(g, size, 2)


def DiagCol3(g: rgen, size: int) -> trow:
    return DiagCol(g, size, 3)


# Note our convention to exclude 0 and 1.
def Lcm_(g: rgen, row: int) -> int:
    Z = [v for v in g(row) if v not in [-1, 0, 1]]
    return lcm(*Z) if Z != [] else 1


def TabLcm_(g: rgen, size: int) -> trow:
    return [Lcm_(g, row) for row in range(size)]


def Lcm(t: trow) -> int:
    Z = [v for v in t if v not in [-1, 0, 1]]
    return lcm(*Z) if Z != [] else 1


def RowLcm(T: tabl) -> trow:
    return [Lcm(row) for row in T]


def RowLcm_(g: rgen, size: int) -> trow:
    return [Lcm_(g, row) for row in range(size)]


# Note our convention to exclude 0 and 1.
def Gcd_(g: rgen, row: int) -> int:
    Z = [v for v in g(row) if v not in [-1, 0, 1]]
    return gcd(*Z) if Z != [] else 1


def RowGcd_(g: rgen, size: int) -> trow:
    return [Gcd_(g, row) for row in range(size)]


def Gcd(r: trow) -> int:
    Z = [v for v in r if v not in [-1, 0, 1]]
    return gcd(*Z) if Z != [] else 1


def GcdReducedRow(r: trow) -> trow:
    Z = [v for v in r if v not in [-1, 0, 1]]
    cd = gcd(*Z) if Z != [] else 1
    return [v // cd if v not in [-1, 0, 1] else v for v in r]


def GcdReduced(T: tabl) -> tabl:
    return [GcdReducedRow(row) for row in T]


def RowGcd(T: tabl) -> trow:
    return [Gcd(row) for row in T]


# Note our convention to use the abs value.
def Max_(g: rgen, row: int) -> int:
    absf = [abs(t) for t in g(row)]
    return reduce(max, absf)


def Max(r: trow) -> int:
    absrow = [abs(n) for n in r]
    return reduce(max, absrow)


def RowMax_(g: rgen, size: int) -> trow:
    return [Max_(g, row) for row in range(size)]


def RowMax(T: tabl) -> trow:
    return [Max(row) for row in T]


################################################


def Trans_(g: rgen, V: Callable[[int], int], size: int) -> trow:
    return [sum(g(n)[k] * V(k) for k in range(n + 1)) for n in range(size)]


def Trans(T: tabl, V: Callable[[int], int]) -> trow:
    return [sum(T[n][k] * V(k) for k in range(n + 1)) for n in range(len(T))]


def TransSqrs_(g: rgen, size: int) -> trow:
    return Trans_(g, lambda k: k * k, size)


def TransSqrs(T: tabl) -> trow:
    return Trans(T, lambda k: k * k)


def TransNat0_(g: rgen, size: int) -> trow:
    return Trans_(g, lambda k: k, size)


def TransNat0(T: tabl) -> trow:
    return Trans(T, lambda k: k)


def TransNat1_(g: rgen, size: int) -> trow:
    return Trans_(g, lambda k: k + 1, size)


def TransNat1(T: tabl) -> trow:
    return Trans(T, lambda k: k + 1)


def ColMiddle(T: tabl) -> trow:
    return [row[n // 2] for n, row in enumerate(T)]


def CentralE(T: tabl) -> trow:
    return [row[n // 2] for n, row in enumerate(T) if n % 2 == 0]


def CentralO(T: tabl) -> trow:
    return [row[n // 2] for n, row in enumerate(T) if n % 2 == 1]


def ColLeft(T: tabl) -> trow:
    return [row[0] for row in T]


def ColRight(T: tabl) -> trow:
    return [row[-1] for row in T]


# def Det(t: tabl) -> trow:
#    return list(accumulate(ColRight(t), operator.mul))


def PrintTransforms(t: tgen, size: int = 8, mdformat: bool = True) -> None:
    TRANSTRAIT: dict[str, Callable[[t.gen, int], trow]] = {}

    def RegisterTransTrait(f: Callable[[t.gen, int], trow]) -> None:
        TRANSTRAIT[f.__name__] = f

    RegisterTransTrait(TransSqrs_)
    RegisterTransTrait(TransNat0_)
    RegisterTransTrait(TransNat1_)

    RegisterTransTrait(DiagRow0)
    RegisterTransTrait(DiagRow1)
    RegisterTransTrait(DiagRow2)
    RegisterTransTrait(DiagRow3)

    RegisterTransTrait(DiagCol0)
    RegisterTransTrait(DiagCol1)
    RegisterTransTrait(DiagCol2)
    RegisterTransTrait(DiagCol3)

    trianglename = t.id
    gen = t.gen
    if mdformat:
        print("#", trianglename, ": Transforms")
        print("| Trait     |   Seq  |")
        print("| :---      |  :---  |")
        for traitname, trait in TRANSTRAIT.items():
            print(f"| {traitname:<8} | {trait(gen, size)} |")
        print()
    else:
        for traitname, trait in TRANSTRAIT.items():
            print(f'{trianglename + ":" + traitname:<14} {trait(gen, size)}')


def PrintMiscTraits(T: tabl, trianglename: str, mdformat: bool = True) -> None:
    MISCTRAIT: dict[str, Callable[[tabl], trow]] = {}

    def RegisterMiscTrait(f: Callable[[tabl], trow]) -> None:
        MISCTRAIT[f.__name__] = f

    RegisterMiscTrait(RowLcm)
    RegisterMiscTrait(RowGcd)
    RegisterMiscTrait(RowMax)

    RegisterMiscTrait(ColMiddle)
    RegisterMiscTrait(CentralE)
    RegisterMiscTrait(ColLeft)
    RegisterMiscTrait(ColRight)

    RegisterMiscTrait(BinConv)
    RegisterMiscTrait(InvBinConv)

    if mdformat:
        print("#", trianglename, ": Transforms")
        print("| Trait        |   Seq  |")
        print("| :---         |  :---  |")
        for traitname, trait in MISCTRAIT.items():
            print(f"| {traitname:<12} | {trait(T)} |")
        print()
    else:
        for traitname, trait in MISCTRAIT.items():
            print(f'{trianglename + ":" + traitname:<18} {trait(T)}')


if __name__ == "__main__":
    from tabl import tabl_fun

    def ReduceAll() -> None:
        for fun in tabl_fun:
            t = fun.tab(9)
            r = GcdReduced(t)
            if t[3:] != r[3:]:
                print(fun.id)
                print(t)
                print(r)
                print()

    # ReduceAll()

    """
    from Abel import Abel, abel
    from Bell import Bell, bell
    from StirlingCyc import StirlingCycle
    from CompositionMax import CompoMax

    T = Abel.tab(9)
    print(T)

    #PrintTransforms(Abel)
    #PrintTransforms(CompoMax, 7, False)

    #PrintMiscTraits(Abel.tab(8), Abel.id)
    #PrintMiscTraits(CompoMax.tab(8), CompoMax.id, False)

    print("BinConv    ", BinConv(T))
    #print(BinConv_(abel, 6))

    print("InvBinConv ", InvBinConv(T))
    #print(InvBinConv_(abel, 6))

    #print(BinTabl_(abel, 6))
    print("BinTabl    ", BinTabl(T))

    #print(InvBinTabl_(abel, 6))
    print("BinTabl    ", InvBinTabl(T))

    # print(FlatBinTabl(Abel.tab(6)))

    #print(ConvTabl_(abel, 6))
    print("ConvTabl    ", ConvTabl(T))

    print("InvConvTabl", InvConvTabl(abel, 6))

    """
