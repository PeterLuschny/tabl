from typing import Callable
from Binomial import binomial
from math import lcm, gcd
from functools import reduce
from _tabltypes import seq, tabl, trow, rgen, tgen


'''
Note the convention:
    def RowLcm(t: trow) -> int:
    def RowLcm_(f: rgen, n: int) -> int:
called 'multidispatch on trailing underscore'.

Similar:
    def TransBinomial(T: tabl) -> trow:
    def TransBinomial_(g: rgen, size: int) -> trow:
'''

# #@


def LinMap_(g: rgen, V: seq, size: int) -> trow:
    return [sum(g(n)[k] * V(k) for k in range(n + 1)) for n in range(size)]


def LinMap(M: tabl, V: seq) -> trow:
    return [sum(M[n][k] * V(k) for k in range(n + 1)) for n in range(len(M))]


def BinMap(V: seq, size: int) -> trow:
    return [sum(binomial(n)[k] * V(k) for k in range(n + 1)) for n in range(size)]


def BinTabl_(g: rgen, size: int) -> tabl:
    return [BinMap(lambda k: g(n)[k], n + 1) for n in range(size)]


def BinTabl(M: tabl) -> tabl:
    return [BinMap(lambda k: M[n][k], n + 1) for n in range(len(M))]


def FlatBinTabl(t: tabl) -> trow:
    return [i for row in BinTabl(t) for i in row]


def BinConv(T: tabl) -> trow:
    R = [LinMap_(binomial, lambda k: T[n][k], n + 1) for n in range(len(T))]
    return [row[-1] for row in R]


def BinConv_(g: rgen, size: int) -> trow:
    T = BinTabl_(g, size)
    return [row[-1] for row in T]


def ConvTabl_(g: rgen, size: int) -> tabl:
    return [LinMap_(g, lambda k: g(n)[k], n + 1) for n in range(size)]


def ConvTabl(t: tabl) -> tabl:
    def g(n: int) ->list[int]: return [t[n][k] for k in range(n + 1)]
    return [LinMap_(g, lambda k: g(n)[k], n + 1) for n in range(len(t))]


def FlatConvTabl(t: tabl) -> trow:
    return [i for row in ConvTabl(t) for i in row]


def InvLinMap(g: rgen, V: seq, size: int) -> trow:
    return [sum((-1) ** (n - k) * g(n)[k] * V(k) for k in range(n + 1))
               for n in range(size) ]


def InvConvTabl(g: rgen, size: int) -> tabl:
    return [InvLinMap(g, lambda k: g(n)[k], n + 1) for n in range(size)]


def InvBinMap(V: seq, size: int) -> trow:
    return [sum((-1) ** (n - k) * binomial(n)[k] * V(k) 
               for k in range(n + 1)) for n in range(size)]


def InvBinTabl(M: tabl) -> tabl:
    return [InvBinMap(lambda k: M[n][k], n + 1) for n in range(len(M))]


def InvBinTabl_(g: rgen, size: int) -> tabl: 
    return [InvBinMap(lambda k: g(n)[k], n + 1) for n in range(size)]


def FlatInvBinTabl(t: tabl) -> trow:
    return [i for row in InvBinTabl(t) for i in row]


def InvBinConv(T: tabl) -> trow:
    R = [LinMap_(binomial, lambda k: (-1) ** (n - k) * T[n][k], n + 1) for n in range(len(T))]
    return [row[-1] for row in R]


def InvBinConv_(g: rgen, size: int) -> trow:
    T = InvBinTabl_(g, size)
    return [row[-1] for row in T]


def DiagRow(g: rgen, size: int, j: int) -> trow:
    return [g(j + k)[k] for k in range(size)]

def DiagRow0(g: rgen, size: int) -> trow: return DiagRow(g, size, 0)
def DiagRow1(g: rgen, size: int) -> trow: return DiagRow(g, size, 1)
def DiagRow2(g: rgen, size: int) -> trow: return DiagRow(g, size, 2)
def DiagRow3(g: rgen, size: int) -> trow: return DiagRow(g, size, 3)


def DiagCol(g: rgen, size: int, j: int) -> trow:
    return [g(j + k)[j] for k in range(size)]

def DiagCol0(g: rgen, size: int) -> trow: return DiagCol(g, size, 0)
def DiagCol1(g: rgen, size: int) -> trow: return DiagCol(g, size, 1)
def DiagCol2(g: rgen, size: int) -> trow: return DiagCol(g, size, 2)
def DiagCol3(g: rgen, size: int) -> trow: return DiagCol(g, size, 3)


# Note our convention to exclude 0 and 1.
def Lcm_(g: rgen, row: int) -> int:
    Z = [v for v in g(row) if not v in [-1, 0, 1]]
    return lcm(*Z) if Z != [] else 1


def TabLcm_(g: rgen, size: int) -> trow:
    return [Lcm_(g, row) for row in range(size)]


def Lcm(t: trow) -> int:
    Z = [v for v in t if not v in [-1, 0, 1]]
    return lcm(*Z) if Z != [] else 1


def RowLcm(t: tabl) -> trow:
    return [Lcm(row) for row in t]


# Note our convention to exclude 0 and 1.
def Gcd_(g: rgen, row: int) -> int:
    Z = [v for v in g(row) if not v in [-1, 0, 1]]
    return gcd(*Z) if Z != [] else 1


def RowGcd_(g: rgen, size: int) -> trow:
    return [Gcd_(g, row) for row in range(size)]


def Gcd(t: trow) -> int:
    Z = [v for v in t if not v in [-1, 0, 1]]
    return gcd(*Z) if Z != [] else 1


def GcdReducedRow(t: trow) -> trow:
    Z = [v for v in t if not v in [-1, 0, 1]]
    cd = gcd(*Z) if Z != [] else 1
    return [v // cd if not v in [-1, 0, 1] else v for v in t]


def GcdReduced(t: tabl) -> tabl:
    return [GcdReducedRow(row) for row in t]


def RowGcd(t: tabl) -> trow:
    return [Gcd(row) for row in t]


# Note our convention to use the abs value.
def Max_(g: rgen, row: int) -> int:
    absf =[abs(t) for t in g(row)]
    return reduce(max, absf) 


def RowMax_(g: rgen, size: int) -> trow:
    return [Max_(g, row) for row in range(size)]


def Max(t: trow) -> int:
    absrow = [abs(n) for n in t]
    return reduce(max, absrow) 


def RowMax(t: tabl) -> trow:
    return [Max(row) for row in t]


################################################


def Trans(g: rgen, V: Callable[[int], int], size: int) -> trow:
    return [sum(g(n)[k] * V(k) for k in range(n + 1)) 
            for n in range(size)]


def TransSqrs(f: rgen, size: int) -> trow: 
    return Trans(f, lambda k: k * k, size)


def TransNat0(f: rgen, size: int) -> trow: 
    return Trans(f, lambda k: k, size)


def TransNat1(f: rgen, size: int) -> trow: 
    return Trans(f, lambda k: k + 1, size)


def trans(T: tabl, V: Callable[[int], int]) -> trow:
    return [sum(T[n][k] * V(k) for k in range(n + 1)) 
            for n in range(len(T))]


def transsqrs(T: tabl) -> trow: 
    return trans(T, lambda k: k * k)


def transnat0(T: tabl) -> trow: 
    return trans(T, lambda k: k)


def transnat1(T: tabl) -> trow: 
    return trans(T, lambda k: k + 1)


def ColMiddle(t: tabl) -> trow:
    return [row[n // 2] for n, row in enumerate(t)]


def ColECentral(t: tabl) -> trow:
    return [row[n // 2] for n, row in enumerate(t) if n % 2 == 0]


def ColOCentral(t: tabl) -> trow:
    return [row[n // 2] for n, row in enumerate(t) if n % 2 == 1]


def ColLeft(t: tabl) -> trow:
    return [row[0] for row in t]


def ColRight(t: tabl)  -> trow:
    return [row[-1] for row in t]


#def Det(t: tabl) -> trow:
#    return list(accumulate(ColRight(t), operator.mul))


def PrintTransforms(t: tgen, size: int = 8, mdformat: bool = True) -> None:

    TRANSTRAIT: dict[str, Callable[[t.gen, int], trow]] = {}
    def RegisterTransTrait(f: Callable[[t.gen, int], trow]) -> None: 
        TRANSTRAIT[f.__name__] = f

    RegisterTransTrait(TransSqrs)
    RegisterTransTrait(TransNat0)
    RegisterTransTrait(TransNat1)

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
        print( "| Trait     |   Seq  |")
        print( "| :---      |  :---  |")
        for traitname, trait in TRANSTRAIT.items():
            print(f'| {traitname:<8} | {trait(gen, size)} |')
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
    RegisterMiscTrait(ColECentral)
    RegisterMiscTrait(ColLeft)
    RegisterMiscTrait(ColRight)

    RegisterMiscTrait(BinConv)
    RegisterMiscTrait(InvBinConv)

    if mdformat:
        print("#", trianglename, ": Transforms")
        print( "| Trait        |   Seq  |")
        print( "| :---         |  :---  |")
        for traitname, trait in MISCTRAIT.items():
            print(f'| {traitname:<12} | {trait(T)} |')
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

    from Abel import Abel, abel
    from Bell import Bell, bell
    from StirlingCyc import StirlingCycle
    from CompositionMax import CompoMax

    
    '''
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

    '''
