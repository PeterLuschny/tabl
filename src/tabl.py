from functools import cache, reduce
from itertools import accumulate
from math import lcm, gcd, factorial
from sys import setrecursionlimit, set_int_max_str_digits
from typing import Callable, TypeAlias
import contextlib
import csv
import requests
import gzip
from fractions import Fraction as frac
from sympy import Matrix, Rational
from pathlib import Path

path = Path(__file__).parent
reldatapath = "data/oeis_data.csv"
datapath = (path / reldatapath).resolve()
reloeispath = "data/oeis.csv"
oeispath = (path / reloeispath).resolve()
relstrippedpath = "data/stripped"
strippedpath = (path / relstrippedpath).resolve()
relcsvpath = "data/csv"
csvpath = (path / relcsvpath).resolve()
allcsvfile = "data/allcsv.csv"
allcsvpath = (path / allcsvfile).resolve()
relhtmlpath = "data/html"
htmlpath = (path / relhtmlpath).resolve()
relmdpath = "data/md"
mdpath = (path / relmdpath).resolve()


def GetDataPath() -> Path:
    return datapath


def GetCsvPath() -> Path:
    return csvpath


def GetAllCsvPath() -> Path:
    return allcsvpath


def GetHtmlPath() -> Path:
    return htmlpath


def GetMdPath() -> Path:
    return mdpath


setrecursionlimit(3000)
set_int_max_str_digits(5000)


def isintegerinv(T: list[list[int] | list[Rational]]) -> bool:
    for row in T:
        for k in row:
            if type(k) == Rational:
                return False
    return True


def InverseTriangle(r, dim: int) -> list[list[int]]:
    M = [[r(n)[k] if k <= n else 0 for k in range(dim)] for n in range(dim)]
    try:
        I = Matrix(M) ** -1
    except:
        # print("Not invertible")
        return []
    T = [[I[n, k] for k in range(n + 1)] for n in range(dim)]
    if not isintegerinv(T):
        # print("Inverse not integer matrix")
        return []
    return T


def InverseTabl(T: list[list[int]]) -> list[list[int]]:
    M = [[T[n][k] if k <= n else 0 for k in range(len(T))] for n in range(len(T))]
    try:
        I = Matrix(M) ** -1
    except:
        # print("Not invertible")
        return []
    t = [[I[n, k] for k in range(n + 1)] for n in range(len(M))]
    if not isintegerinv(t):
        # print("Inverse not integer matrix")
        return []
    return t


"""Type: table row"""
trow: TypeAlias = list[int]
"""Type: table"""
tabl: TypeAlias = list[list[int]]
"""Type: sequence generator"""
seq: TypeAlias = Callable[[int], int]
"""Type: row generator"""
rgen: TypeAlias = Callable[[int], trow]
"""Type: table generator"""
tgen: TypeAlias = Callable[[int, int], int]
"""Type: triangle"""
tri: TypeAlias = Callable[[int, int], int]


def inversion_wrapper(T: tgen, size: int) -> tgen | None:
    t = T.inv(size)
    if t == []:
        return None

    def psgen(n: int) -> trow:
        return list(t[n])

    @set_attributes(psgen, T.id + ":Inv", [], True)
    def Psgen(n: int, k: int) -> int:
        return psgen(n)[k]

    return Psgen


def reversion_wrapper(T: tgen, size: int) -> tgen:
    t = T.rev(size)

    def rsgen(n: int) -> trow:
        return list(t[n])

    @set_attributes(rsgen, T.id + ":Rev", [], True)
    def Rsgen(n: int, k: int) -> int:
        return rsgen(n)[k]

    return Rsgen


def revinv_wrapper(T: tgen, size: int) -> tgen | None:
    I = inversion_wrapper(T, size)
    if I == None:
        return None
    J = reversion_wrapper(I, size)

    def rigen(n: int) -> trow:
        return list(J.gen(n))

    @set_attributes(rigen, J.id, [], True)
    def Rigen(n: int, k: int) -> int:
        return rigen(n)[k]

    return Rigen


def invrev_wrapper(T: tgen, size: int) -> tgen | None:
    R = reversion_wrapper(T, size)
    S = inversion_wrapper(R, size)
    if S == None:
        return None

    def tigen(n: int) -> trow:
        return list(S.gen(n))

    @set_attributes(tigen, S.id, [], True)
    def Tigen(n: int, k: int) -> int:
        return tigen(n)[k]

    return Tigen


def SubTriangle(g: rgen, N: int, K: int, size: int) -> tabl:
    return [[g(n)[k] for k in range(K, K - N + n + 1)] for n in range(N, N + size)]


def AbsSubTriangle(g: rgen, N: int, K: int, size: int) -> tabl:
    return [[abs(g(n)[k]) for k in range(K, K - N + n + 1)] for n in range(N, N + size)]


def set_attributes(
    gen: rgen, id: str, sim: list[str], vert: bool = False
) -> Callable[..., Callable[[int, int], int]]:
    def maketab(size: int) -> tabl:
        return [list(gen(n)) for n in range(size)]

    def makerev(size: int) -> tabl:
        return [list(reversed(gen(n))) for n in range(size)]

    def makemat(size: int) -> tabl:
        return [[gen(n)[k] if k <= n else 0 for k in range(size)] for n in range(size)]

    def makeflat(size: int) -> list[int]:
        return [gen(n)[k] for n in range(size) for k in range(n + 1)]

    def makeinv(size: int) -> tabl:
        if not vert:
            return []
        return InverseTriangle(gen, size)

    def makerevinv(size: int) -> tabl:
        if not vert:
            return []
        I = InverseTriangle(gen, size)
        if I == []:
            return []
        return [[I[n][n - k] for k in range(n + 1)] for n in range(size)]

    def makeinvrev(size: int) -> tabl:
        R = [list(reversed(gen(n))) for n in range(size)]
        M = [[R[n][k] if k <= n else 0 for k in range(size)] for n in range(size)]
        return InverseTabl(M)

    def sub(N: int, K: int) -> Callable[[int], tabl]:
        def gsub(size: int) -> tabl:
            return [
                [gen(n)[k] for k in range(K, K - N + n + 1)] for n in range(N, N + size)
            ]

        return gsub

    def abssub(N: int, K: int) -> Callable[[int], tabl]:
        def gabssub(size: int) -> tabl:
            return [
                [abs(gen(n)[k]) for k in range(K, K - N + n + 1)]
                for n in range(N, N + size)
            ]

        return gabssub

    def wrapper(f: Callable[[int, int], int]) -> Callable[[int, int], int]:
        f.tab = maketab
        f.rev = makerev
        f.mat = makemat
        f.inv = makeinv
        f.flat = makeflat
        f.revinv = makerevinv
        f.invrev = makeinvrev
        f.sub = sub
        f.abssub = abssub
        f.sim = sim
        f.id = id
        f.gen = gen
        return f

    return wrapper


def AntiDiagTabl(t: tabl) -> tabl:
    """Return the table of (upward) anti-diagonals."""
    return [
        [t[n - k - 1][k] for k in range((n + 1) // 2)] for n in range(1, len(t) + 1)
    ]


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
    return [(k + 1) * c for row in t for k, c in enumerate(row)]


def PrintTabls(t: tgen, size: int = 8, mdformat: bool = True) -> None:
    TABLSTRAIT: dict[str, Callable[[tabl], trow]] = {}

    def RegisterTablsTrait(f: Callable[[tabl], trow]) -> None:
        TABLSTRAIT[f.__name__] = f

    T = t.tab(size)
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
        print("| Trait    |   Seq  |")
        print("| :---     |  :---  |")
        for traitname, trait in TABLSTRAIT.items():
            print(f"| {traitname:<15} | {trait(T)} |")
    else:
        for traitname, trait in TABLSTRAIT.items():
            print(f'{trianglename+":"+traitname:<21} {trait(T)}')


def Poly(g: rgen, n: int, x: int) -> int:
    row = g(n)
    return sum(c * (x**j) for (j, c) in enumerate(row))


def PolyRow(g: rgen, size: int, row: int) -> trow:
    return [Poly(g, row, k) for k in range(size)]


def PolyRow0(g: rgen, size: int) -> trow:
    return PolyRow(g, size, 0)


def PolyRow1(g: rgen, size: int) -> trow:
    return PolyRow(g, size, 1)


def PolyRow2(g: rgen, size: int) -> trow:
    return PolyRow(g, size, 2)


def PolyRow3(g: rgen, size: int) -> trow:
    return PolyRow(g, size, 3)


def PolyCol(g: rgen, size: int, col: int) -> trow:
    return [Poly(g, k, col) for k in range(size)]


def PolyCol0(g: rgen, size: int) -> trow:
    return PolyCol(g, size, 0)


def PolyCol1(g: rgen, size: int) -> trow:
    return PolyCol(g, size, 1)


def PolyCol2(g: rgen, size: int) -> trow:
    return PolyCol(g, size, 2)


def PolyCol3(g: rgen, size: int) -> trow:
    return PolyCol(g, size, 3)


def PolyDiag(g: rgen, size: int) -> trow:
    return [Poly(g, n, n) for n in range(size)]


def antidiag_poly(g: rgen, n: int) -> trow:
    return [Poly(g, n - k, k) for k in range(n + 1)]


def PolyDiagTabl(g: rgen, size: int) -> tabl:
    return [antidiag_poly(g, n) for n in range(size)]


def PolyTabl(g: rgen, size: int) -> trow:
    return [i for row in PolyDiagTabl(g, size) for i in row]


def PolyFrac(T: tabl, x: frac) -> list[frac | int]:
    return [sum(c * (x**k) for (k, c) in enumerate(row)) for row in T]


def PosHalf(g: rgen, size: int) -> trow:
    T = [g(n) for n in range(size)]
    R = PolyFrac(T, frac(1, 2))
    return [((2**n) * r).numerator for n, r in enumerate(R)]


def NegHalf(g: rgen, size: int) -> trow:
    T = [g(n) for n in range(size)]
    R = PolyFrac(T, frac(-1, 2))
    return [(((-2) ** n) * r).numerator for n, r in enumerate(R)]


def PrintPolys(t: tgen, size: int = 8, mdformat: bool = True) -> None:
    POLYTRAIT: dict[str, Callable[[t.gen, int], trow]] = {}

    def RegisterPolyTrait(f: Callable[[t.gen, int], trow]) -> None:
        POLYTRAIT[f.__name__] = f

    RegisterPolyTrait(PolyTabl)
    RegisterPolyTrait(PolyRow0)
    RegisterPolyTrait(PolyRow1)
    RegisterPolyTrait(PolyRow2)
    RegisterPolyTrait(PolyRow3)
    RegisterPolyTrait(PolyCol0)
    RegisterPolyTrait(PolyCol1)
    RegisterPolyTrait(PolyCol2)
    RegisterPolyTrait(PolyCol3)

    RegisterPolyTrait(PolyDiag)
    RegisterPolyTrait(PosHalf)
    RegisterPolyTrait(NegHalf)
    trianglename = t.id
    gen = t.gen
    if mdformat:
        print("#", trianglename, ": Polynomial values")
        print("| Trait    |   Seq  |")
        print("| :---     |  :---  |")
        for traitname, trait in POLYTRAIT.items():
            print(f"| {traitname:<8} | {trait(gen, size)} |")
        print()
    else:
        for traitname, trait in POLYTRAIT.items():
            print(f'{trianglename+":"+traitname:<14} {trait(gen, size)}')


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
    def g(n: int) -> list[int]:
        return [t[n][k] for k in range(n + 1)]

    return [LinMap_(g, lambda k: g(n)[k], n + 1) for n in range(len(t))]


def FlatConvTabl(t: tabl) -> trow:
    return [i for row in ConvTabl(t) for i in row]


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


def InvBinTabl(M: tabl) -> tabl:
    return [InvBinMap(lambda k: M[n][k], n + 1) for n in range(len(M))]


def InvBinTabl_(g: rgen, size: int) -> tabl:
    return [InvBinMap(lambda k: g(n)[k], n + 1) for n in range(size)]


def FlatInvBinTabl(t: tabl) -> trow:
    return [i for row in InvBinTabl(t) for i in row]


def InvBinConv(T: tabl) -> trow:
    R = [
        LinMap_(binomial, lambda k: (-1) ** (n - k) * T[n][k], n + 1)
        for n in range(len(T))
    ]
    return [row[-1] for row in R]


def InvBinConv_(g: rgen, size: int) -> trow:
    T = InvBinTabl_(g, size)
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


def Max_(g: rgen, row: int) -> int:
    absf = [abs(t) for t in g(row)]
    return reduce(max, absf)


def RowMax_(g: rgen, size: int) -> trow:
    return [Max_(g, row) for row in range(size)]


def Max(t: trow) -> int:
    absrow = [abs(n) for n in t]
    return reduce(max, absrow)


def RowMax(t: tabl) -> trow:
    return [Max(row) for row in t]


def Trans(g: rgen, V: Callable[[int], int], size: int) -> trow:
    return [sum(g(n)[k] * V(k) for k in range(n + 1)) for n in range(size)]


def TransSqrs(f: rgen, size: int) -> trow:
    return Trans(f, lambda k: k * k, size)


def TransNat0(f: rgen, size: int) -> trow:
    return Trans(f, lambda k: k, size)


def TransNat1(f: rgen, size: int) -> trow:
    return Trans(f, lambda k: k + 1, size)


def trans(T: tabl, V: Callable[[int], int]) -> trow:
    return [sum(T[n][k] * V(k) for k in range(n + 1)) for n in range(len(T))]


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


def ColRight(t: tabl) -> trow:
    return [row[-1] for row in t]


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
    RegisterMiscTrait(ColECentral)
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


def even_sum(r: trow) -> int:
    return sum(r[::2])


def even_sum_(g: rgen, index: int) -> int:
    return even_sum(g(index))


def odd_sum(r: trow) -> int:
    return sum(r[1::2])


def odd_sum_(g: rgen, index: int) -> int:
    return odd_sum(g(index))


def antidiag_sum(r: trow) -> int:
    return sum(r)


def antidiag_sum_(g: rgen, n: int) -> int:
    return sum([g(n - k)[k] for k in range((n + 2) // 2)])


def acc_sum(r: trow) -> int:
    return sum(accumulate(r))


def acc_sum_(g: rgen, index: int) -> int:
    return acc_sum(g(index))


def accrev_sum(r: trow) -> int:
    return sum(accumulate(reversed(r)))


def accrev_sum_(g: rgen, index: int) -> int:
    return acc_sum(g(index))


def alt_sum(r: trow) -> int:
    return even_sum(r) - odd_sum(r)


def alt_sum_(g: rgen, index: int) -> int:
    return alt_sum(g(index))


def RowSum(t: tabl) -> trow:
    return [sum(row) for row in t]


def RowSum_(g: rgen, size: int) -> trow:
    return [sum(g(n)) for n in range(size)]


def EvenSum(t: tabl) -> trow:
    return [even_sum(row) for row in t]


def EvenSum_(g: rgen, size: int) -> trow:
    return [even_sum(g(n)) for n in range(size)]


def OddSum(t: tabl) -> trow:
    return [odd_sum(row) for row in t]


def OddSum_(g: rgen, size: int) -> trow:
    return [odd_sum(g(n)) for n in range(size)]


def AltSum(t: tabl) -> trow:
    return [alt_sum(row) for row in t]


def AltSum_(g: rgen, size: int) -> trow:
    return [alt_sum(g(n)) for n in range(size)]


def AccSum(t: tabl) -> trow:
    return [acc_sum(row) for row in t]


def AccSum_(g: rgen, size: int) -> trow:
    return [acc_sum(g(n)) for n in range(size)]


def AccRevSum(t: tabl) -> trow:
    return [accrev_sum(row) for row in t]


def AccRevSum_(g: rgen, size: int) -> trow:
    return [accrev_sum(g(n)) for n in range(size)]


def AntiDiagSum(t: tabl) -> trow:
    def row(n: int) -> list[int]:
        return [t[n - k - 1][k] for k in range((n + 1) // 2)]

    return [sum(row(n)) for n in range(1, len(t) + 1)]


def AntiDiagSum_(g: rgen, size: int) -> trow:
    return [antidiag_sum_(g, n) for n in range(size)]


def PrintSums(T: tabl, trianglename: str, mdformat: bool = True) -> None:
    SUMTRAIT: dict[str, Callable[[tabl], trow]] = {}

    def RegisterSumTrait(f: Callable[[tabl], trow]) -> None:
        SUMTRAIT[f.__name__] = f

    RegisterSumTrait(RowSum)
    RegisterSumTrait(EvenSum)
    RegisterSumTrait(OddSum)
    RegisterSumTrait(AltSum)
    RegisterSumTrait(AccSum)
    RegisterSumTrait(AccRevSum)
    RegisterSumTrait(AntiDiagSum)
    if mdformat:
        # print("#", trianglename, ": Sums")
        print("| Trait        |   Seq  |")
        print("| :---         |  :---  |")
        for traitname, trait in SUMTRAIT.items():
            print(f"| {traitname:<12} | {trait(T)} |")
    else:
        for traitname, trait in SUMTRAIT.items():
            print(f'{trianglename + ":" + traitname:<18} {trait(T)}')


def PrintTabl(t: tabl) -> None:
    print(t)


def PrintFlat(t: tabl) -> None:
    # print(flat(t))
    print(t)


def PrintRows(t: tabl) -> None:
    print("|  Row   |  Seq   |")
    print("| :---   |  :---  |")
    for n, row in enumerate(t):
        print(f"| Row{n} | {row} |")


def PrintTerms(t: tabl) -> None:
    count = 0
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print(count, [n, k], term)
            count += 1


def PrintRowArray(T: rgen, rows: int, cols: int) -> None:
    print("| DiagRow  |   Seq  |")
    print("| :---     |  :---  |")
    for j in range(rows):
        print(f"| DiagRow{j} | {[T(j + k)[k] for k in range(cols)]}|")


def PrintColArray(T: rgen, rows: int, cols: int) -> None:
    print("| DiagCol  |   Seq  |")
    print("| :---     |  :---  |")
    for j in range(cols):
        print(f"| DiagCol{j} | {[T(j + k)[j] for k in range(rows)]} |")


def PrintPolyRowArray(T: rgen, rows: int, cols: int) -> None:
    print("| PolyRow  |   Seq  |")
    print("| :---     |  :---  |")
    for n in range(rows):
        print(f"| PolyRow{n} | {PolyRow(T, cols, n)} |")


def PrintPolyColArray(T: rgen, rows: int, cols: int) -> None:
    print("| PolyCol  |   Seq  |")
    print("| :---     |  :---  |")
    for n in range(rows):
        print(f"| PolyCol{n} | {PolyCol(T, cols, n)} |")


def PrintFlats(t: tabl) -> None:
    print("| Flat       |  Seq  |")
    print("| :---       | :---  |")
    print(f"| Tabl       | {t} |")
    print(f"| RevTabl    | {RevTabl(t)} |")
    print(f"| AntiDiag   | {AntiDiagTabl(t)} |")
    print(f"| AccTabl    | {AccTabl(t)} |")
    print(f"| RevAccTabl | {RevAccTabl(t)} |")
    print(f"| AccRevTabl | {AccRevTabl(t)} |")


def PrintTrans(t: tabl) -> None:
    print("| Trans      |   Seq  |")
    print("| :---       |  :---  |")
    print(f"| RowLcm     | {RowLcm(t)} |")
    print(f"| RowGcd     | {RowGcd(t)} |")
    print(f"| RowMax     | {RowMax(t)} |")
    print(f"| ColMiddle  | {ColMiddle(t)} |")
    print(f"| ColECenter | {ColECentral(t)} |")
    print(f"| ColOCenter | {ColOCentral(t)} |")
    print(f"| ColLeft    | {ColLeft(t)} |")
    print(f"| ColRight   | {ColRight(t)} |")
    print(f"| TransSqrs  | {transsqrs(t)} |")
    print(f"| TransNat0  | {transnat0(t)} |")
    print(f"| TransNat1  | {transnat1(t)} |")


def PrintViews(g: tgen, rows: int = 7, verbose: bool = True) -> None:
    print("# " + g.id)
    print(g.sim)
    cols: int = rows
    print()
    T: tabl = g.tab(rows)
    if verbose:
        print(g.id, "Triangle view")
    PrintRows(T)
    print()
    if verbose:
        print(g.id, "Triangles")
    PrintFlats(T)
    print()
    if verbose:
        print(g.id, "Row sums")
    PrintSums(T, g.id)
    print()
    if verbose:
        print(g.id, "Transforms")
    PrintTrans(T)
    print()
    if verbose:
        print(g.id, "Diagonals as rows")
    PrintRowArray(g.gen, rows, cols)
    print()
    if verbose:
        print(g.id, "Diagonals as columns")
    PrintColArray(g.gen, rows, cols)
    print()
    if verbose:
        print(g.id, "Polynomial values as rows")
    PrintPolyRowArray(g.gen, rows, cols)
    print()
    if verbose:
        print(g.id, "Polynomial values as columns")
    PrintPolyColArray(g.gen, rows, cols)
    print()


def Profile(T: tgen, hor: int = 10) -> dict[str, list[int]]:
    d: dict[str, list[int]] = {}
    t: tabl = T.tab(hor)
    ver: int = hor // 2
    # Triangle flattened
    d["Triangle"] = flat(T.tab(6))
    # Row sums
    d["RowSum"] = RowSum(t)
    d["EvenSum"] = EvenSum(t)
    d["OddSum"] = OddSum(t)
    d["AltSum"] = AltSum(t)
    d["AccSum"] = AccSum(t)
    d["AccRevSum"] = AccRevSum(t)
    d["AntiDiagSum"] = AntiDiagSum(t)
    # DiagsAsRowArray
    rows: int = ver
    cols: int = hor
    for j in range(rows):
        d["DiagRow" + str(j)] = [T.gen(j + k)[k] for k in range(cols)]
    # DiagsAsColArray
    rows = hor
    cols = ver
    for j in range(cols):
        d["DiagCol" + str(j)] = [T.gen(j + k)[j] for k in range(rows)]
    # RowPolyArray
    rows = ver
    cols = hor
    for j in range(rows):
        d["PolyRow" + str(j)] = PolyRow(T.gen, j, cols)
    # ColPolyArray
    rows = ver
    cols = hor
    for j in range(rows):
        if j == 1:
            continue
        d["PolyCol" + str(j)] = PolyCol(T.gen, j, cols)
    return d


counter: int = 0


def PrintProfile(T: tgen, dim: int, format: str) -> None:
    d: dict[str, list[int]] = Profile(T, dim)
    if format == "twolines":
        for seq in d.items():
            print(f"{T.id}:{seq[0]}\n{seq[1]}")
    if format == "oneline":
        print(T.id)
        for seq in d.items():
            print(f"{seq[0]}, {seq[1]}")
        print()
    if format == "nonames":
        global counter
        for seq in d.items():
            counter += 1
            print(seq[1])


def PrintExtendedProfile(T: tgen, dim: int, format: str) -> None:
    tim: int = dim + dim // 2
    PrintProfile(T, dim, format)
    I = inversion_wrapper(T, tim)
    if I != None:
        PrintProfile(I, dim, format)
    R = reversion_wrapper(T, tim)
    PrintProfile(R, dim, format)
    r = revinv_wrapper(T, tim)
    if r != None:
        PrintProfile(r, dim, format)
    r = invrev_wrapper(T, tim)
    if r != None:
        PrintProfile(r, dim, format)
    if format == "nonames":
        global counter
        print(counter, "sequences generated.")


@cache
def abel(n: int) -> list[int]:
    if n == 0:
        return [1]
    b = binomial(n - 1)
    return [b[k - 1] * n ** (n - k) if k > 0 else 0 for k in range(n + 1)]


@set_attributes(abel, "Abel", ["A061356", "A137452", "A139526"], True)
def Abel(n: int, k: int) -> int:
    return abel(n)[k]


@cache
def F(n: int) -> int:
    return factorial(n) ** 3 * ((n + 1) * (n + 1) * (n + 2))


@cache
def baxter(n: int) -> list[int]:
    if n == 0:
        return [1]
    return [0] + [(2 * F(n - 1)) // (F(k - 1) * F(n - k)) for k in range(1, n + 1)]


@set_attributes(baxter, "Baxter", ["A359363", "A056939"], False)
def Baxter(n: int, k: int) -> int:
    return baxter(n)[k]


@cache
def bell(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [bell(n - 1)[n - 1]] + bell(n - 1)
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row


@set_attributes(bell, "Bell", ["A011971", "A011972", "A123346"], False)
def Bell(n: int, k: int) -> int:
    return bell(n)[k]


@cache
def bessel(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = bessel(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = row[k - 1] + (2 * (n - 1) - k) * row[k]
    return row


@set_attributes(bessel, "Bessel", ["A001497", "A001498", "A122850", "A132062"], True)
def Bessel(n: int, k: int) -> int:
    return bessel(n)[k]


@cache
def bessel2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]
    row = bessel2(n - 1) + [0]
    row[n] = 0 if n % 2 else row[n - 2]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row


@set_attributes(
    bessel2,
    "Bessel2",
    ["A359760", "A073278", "A066325", "A099174", "A111924", "A144299", "A104556"],
    False,
)
def Bessel2(n: int, k: int) -> int:
    return bessel2(n)[k]


@cache
def binomial(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [1] + binomial(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    return row


@set_attributes(
    binomial,
    "Binomial",
    [
        "A007318",
        "A074909",
        "A108086",
        "A117440",
        "A118433",
        "A130595",
        "A135278",
        "A154926",
    ],
    True,
)
def Binomial(n: int, k: int) -> int:
    return binomial(n)[k]


@cache
def catalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    pow: list[int] = catalan(n - 1) + [0]
    row: list[int] = pow.copy()
    for k in range(n - 1, 0, -1):
        row[k] = pow[k - 1] + 2 * pow[k] + pow[k + 1]
    row[n] = 1
    return row


@set_attributes(catalan, "Catalan", ["A128899", "A039598"], True)
def Catalan(n: int, k: int) -> int:
    return catalan(n)[k]


@cache
def catalan_aer(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return catalan_aer(n - 1)[k] if k >= 0 and k < n else 0

    row: list[int] = catalan_aer(n - 1) + [1]
    for k in range(0, n):
        row[k] = r(k - 1) + r(k + 1)
    return row


@set_attributes(
    catalan_aer, "CatalanAer", ["A052173", "A053121", "A112554", "A322378"], True
)
def CatalanAer(n: int, k: int) -> int:
    return catalan_aer(n)[k]


@cache
def catalansqr(n: int) -> list[int]:
    if n == 0:
        return [1]
    pow = catalansqr(n - 1) + [0]
    row = pow.copy()
    row[0] += row[1]
    row[n] = 1
    for k in range(n - 1, 0, -1):
        row[k] = pow[k - 1] + 2 * pow[k] + pow[k + 1]
    return row


@set_attributes(catalansqr, "CatalanSqr", ["A039599", "A050155"], True)
def CatalanSqr(n: int, k: int) -> int:
    return catalansqr(n)[k]


@cache
def central_cycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = central_cycle(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n + k - 1) * (row[k] + row[k - 1])
    return row


@set_attributes(central_cycle, "CentralCycle", ["A111999", "A259456", "A269940"], False)
def CentralCycle(n: int, k: int) -> int:
    return central_cycle(n)[k]


@cache
def central_set(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = central_set(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = k**2 * row[k] + row[k - 1]
    return row


@set_attributes(central_set, "CentralSet", ["A008957", "A036969", "A269945"], True)
def CentralSet(n: int, k: int) -> int:
    return central_set(n)[k]


@cache
def chebyshevS(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    rov: list[int] = chebyshevS(n - 2)
    row: list[int] = [0] + chebyshevS(n - 1)
    for k in range(0, n - 1):
        row[k] -= rov[k]
    return row


@set_attributes(
    chebyshevS, "ChebyshevS", ["A049310", "A053119", "A112552", "A168561"], True
)
def ChebyshevS(n: int, k: int) -> int:
    return chebyshevS(n)[k]


@cache
def chebyshevT(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    rov: list[int] = chebyshevT(n - 2)
    row: list[int] = [0] + chebyshevT(n - 1)
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] = 2 * row[k] - rov[k]
    return row


@set_attributes(chebyshevT, "ChebyshevT", ["A039991", "A053120", "A081265"], True)
def ChebyshevT(n: int, k: int) -> int:
    return chebyshevT(n)[k]


@cache
def chebyshevU(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 2]
    rov: list[int] = chebyshevU(n - 2)
    row: list[int] = [0] + chebyshevU(n - 1)
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] = 2 * row[k] - rov[k]
    return row


@set_attributes(chebyshevU, "ChebyshevU", ["A053117", "A053118", "A115322"], True)
def ChebyshevU(n: int, k: int) -> int:
    return chebyshevU(n)[k]


@cache
def ctree(n: int) -> list[int]:
    if n % 2 == 1:
        return [1] * (n + 1)
    return [1, 0] * (n // 2) + [1]


@set_attributes(ctree, "ChristTree", ["A106465", "A106470"], True)
def Ctree(n: int, k: int) -> int:
    return ctree(n)[k]


@cache
def composition(n: int) -> list[int]:
    if n == 0:
        return [1]
    cm = compomax(n)
    return [cm[k] - cm[k - 1] if k > 0 else 0 for k in range(n + 1)]


@set_attributes(composition, "Composition", ["A048004"], True)
def Composition(n: int, k: int) -> int:
    return composition(n)[k]


@cache
def compomax(n: int) -> list[int]:
    @cache
    def t(n: int, k: int) -> int:
        if n == 0 or k == 1:
            return 1
        return sum(t(n - j, k) for j in range(1, min(n, k) + 1))

    return [t(n, k) for k in range(n + 1)]


@set_attributes(compomax, "CompositionMax", ["A126198"], False)
def CompoMax(n: int, k: int) -> int:
    return compomax(n)[k]


@cache
def delannoy(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    rov: list[int] = delannoy(n - 2)
    row: list[int] = delannoy(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + rov[k - 1]
    return row


@set_attributes(delannoy, "Delannoy", ["A008288"], True)
def Delannoy(n: int, k: int) -> int:
    return delannoy(n)[k]


@cache
def euler(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = euler(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * n) // (k)
    row[0] = -sum((-1) ** (j // 2) * row[j] for j in range(n, 0, -2))
    return row


@set_attributes(euler, "Euler", ["A109449", "A247453"], True)
def Euler(n: int, k: int) -> int:
    return euler(n)[k]


def euler_num(n: int) -> int:
    return euler(n)[0]


@cache
def eulerian(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = eulerian(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n - k) * row[k - 1] + (k + 1) * row[k]
    return row


@set_attributes(eulerian, "Eulerian", ["A008292", "A123125", "A173018"], False)
def Eulerian(n: int, k: int) -> int:
    return eulerian(n)[k]


@cache
def eulerian2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = eulerian2(n - 1) + [0]
    for k in range(n, 1, -1):
        row[k] = (2 * n - k) * row[k - 1] + k * row[k]
    return row


@set_attributes(
    eulerian2, "Eulerian2", ["A008517", "A112007", "A163936", "A340556"], False
)
def Eulerian2(n: int, k: int) -> int:
    return eulerian2(n)[k]


@cache
def eulerianB(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = eulerianB(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = (2 * (n - k) + 1) * row[k - 1] + (2 * k + 1) * row[k]
    return row


@set_attributes(eulerianB, "EulerianB", ["A060187", "A138076"], True)
def EulerianB(n: int, k: int) -> int:
    return eulerianB(n)[k]


@cache
def euler_sec(n: int) -> list[int]:
    if n == 0:
        return [1]
    b = binomial(n)
    row = [b[k] * euler_sec(n - k)[0] if k > 0 else 0 for k in range(n + 1)]
    if n % 2 == 0:
        row[0] = -sum(row[2::2])
    return row


@set_attributes(euler_sec, "EulerSec", ["A119879", "A081658", "A153641"], True)
def EulerSec(n: int, k: int) -> int:
    return euler_sec(n)[k]


def eulerS(n: int) -> int:
    return 0 if n % 2 == 1 else euler_sec(n)[0]


@cache
def euler_tan(n: int) -> list[int]:
    b = binomial(n)
    row = [b[k] * euler_tan(n - k)[0] if k > 0 else 0 for k in range(n + 1)]
    if n % 2 == 1:
        row[0] = -sum(row[2::2]) + 1
    return row


@set_attributes(
    euler_tan,
    "EulerTan",
    ["A162660", "A350972", "A155585", "A009006", "A000182"],
    False,
)
def EulerTan(n: int, k: int) -> int:
    return euler_tan(n)[k]


def eulerT(n: int) -> int:
    return 0 if n % 2 == 0 else euler_tan(n)[0]


@cache
def falling_factorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    r: list[int] = falling_factorial(n - 1)
    row: list[int] = [n * r[k] for k in range(-1, n)]
    row[0] = 1
    return row


@set_attributes(
    falling_factorial,
    "FallingFact",
    ["A008279", "A068424", "A094587", "A173333", "A181511"],
    False,
)
def FallingFactorial(n: int, k: int) -> int:
    return falling_factorial(n)[k]


@cache
def fibonacci(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = fibonacci(n - 1) + [1]
    s: int = row[1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1]
    row[0] = s
    return row


@set_attributes(fibonacci, "Fibonacci", ["A105809", "A228074", "A354267"], False)
def Fibonacci(n: int, k: int) -> int:
    return fibonacci(n)[k]


@cache
def fubini(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return fubini(n - 1)[k] if k <= n - 1 else 0

    row: list[int] = [0] + fubini(n - 1)
    for k in range(1, n + 1):
        row[k] = k * (r(k - 1) + r(k))
    return row


@set_attributes(fubini, "Fubini", ["A019538", "A090582", "A131689", "A278075"], False)
def Fubini(n: int, k: int) -> int:
    return fubini(n)[k]


@cache
def fuss_catalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = fuss_catalan(n - 1) + [fuss_catalan(n - 1)[n - 1]]
    return list(accumulate(row))


@set_attributes(fuss_catalan, "FussCatalan", ["A030237", "A054445", "A355173"], False)
def FussCatalan(n: int, k: int) -> int:
    return fuss_catalan(n)[k]


@cache
def gaussq2(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = gaussq2(n - 1)
    pow: list[int] = [1] + gaussq2(n - 1)
    p = 2
    for k in range(1, n):
        pow[k] = row[k - 1] + p * row[k]
        p *= 2
    return pow


@set_attributes(gaussq2, "Gaussq2", ["A022166"], True)
def Gaussq2(n: int, k: int) -> int:
    return gaussq2(n)[k]


@cache
def genocchi(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + genocchi(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] += row[k + 1]
    for k in range(2, n + 2):
        row[k] += row[k - 1]
    return row[1:]


@set_attributes(genocchi, "Genocchi", ["A297703"], False)
def Genocchi(n: int, k: int) -> int:
    return genocchi(n)[k]


@cache
def harmonic(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = harmonic(n - 1) + [1]
    sav: int = row[1]
    for k in range(n - 1, 0, -1):
        row[k] = (n - 1) * row[k] + row[k - 1]
    row[1] += sav
    return row


@set_attributes(harmonic, "Harmonic", ["A109822", "A358694"], True)
def Harmonic(n: int, k: int) -> int:
    return harmonic(n)[k]


@cache
def hermiteE(n: int) -> list[int]:
    row: list[int] = [0] * (n + 1)
    row[n] = 1
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (n - k)
    return row


@set_attributes(hermiteE, "HermiteE", ["A066325", "A073278", "A099174"], True)
def HermiteE(n: int, k: int) -> int:
    return hermiteE(n)[k]


@cache
def hermiteH(n: int) -> list[int]:
    row: list[int] = [0] * (n + 1)
    row[n] = 2**n
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (2 * (n - k))
    return row


@set_attributes(hermiteH, "HermiteH", ["A060821"], False)
def HermiteH(n: int, k: int) -> int:
    return hermiteH(n)[k]


@cache
def laguerre(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + laguerre(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row


@set_attributes(laguerre, "Laguerre", ["A021009", "A021010", "A144084"], True)
def Laguerre(n: int, k: int) -> int:
    return laguerre(n)[k]


@cache
def lah(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = lah(n - 1) + [1]
    row[0] = 0
    for k in range(n - 1, 0, -1):
        row[k] = row[k] * (n + k - 1) + row[k - 1]
    return row


@set_attributes(
    lah, "Lah", ["A008297", "A066667", "A089231", "A105278", "A111596", "A271703"], True
)
def Lah(n: int, k: int) -> int:
    return lah(n)[k]


@cache
def t(n: int, k: int, m: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return n**k
    return m * t(n, k - 1, m) + t(n - 1, k, m + 1)


@cache
def lehmer(n: int) -> list[int]:
    return [t(k - 1, n - k, n - k) if n != k else 1 for k in range(n + 1)]


@set_attributes(lehmer, "Lehmer", ["A039621", "A354794"], True)
def Lehmer(n: int, k: int) -> int:
    return lehmer(n)[k]


@cache
def leibniz(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = leibniz(n - 1) + [n + 1]
    row[0] = row[n] = n + 1
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@set_attributes(leibniz, "Leibniz", ["A003506"], False)
def Leibniz(n: int, k: int) -> int:
    return leibniz(n)[k]


@cache
def levin(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = levin(n - 1) + [1]
    row[0] = row[n] = (row[n - 1] * (4 * n - 2)) // n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@set_attributes(levin, "Levin", ["A356546"], False)
def Levin(n: int, k: int) -> int:
    return levin(n)[k]


@cache
def lozanic(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [1] + lozanic(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    if n % 2 != 0:
        return row
    b = binomial(n // 2 - 1)
    for k in range(1, n, 2):
        row[k] -= b[(k - 1) // 2]
    return row


@set_attributes(lozanic, "Lozanic", ["A034851"], True)
def Lozanic(n: int, k: int) -> int:
    return lozanic(n)[k]


@cache
def motzkin(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]
    l = 0 if n % 2 else (motzkin(n - 2)[n - 2] * 2 * (n - 1)) // (n // 2 + 1)
    row = motzkin(n - 1) + [l]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row


@set_attributes(motzkin, "Motzkin", ["A359364"], False)
def Motzkin(n: int, k: int) -> int:
    return motzkin(n)[k]


@cache
def motzkin_gf(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return motzkin_gf(n - 1)[k] if k >= 0 and k < n else 0

    row: list[int] = motzkin_gf(n - 1) + [1]
    for k in range(0, n):
        row[k] += r(k - 1) + r(k + 1)
    return row


@set_attributes(motzkin_gf, "MotzkinGF", ["A026300", "A064189", "A009766"], True)
def MotzkinGF(n: int, k: int) -> int:
    return motzkin_gf(n)[k]


@cache
def narayana(n: int) -> list[int]:
    if n < 3:
        return [[1], [0, 1], [0, 1, 1]][n]
    a: list[int] = narayana(n - 2) + [0, 0]
    row: list[int] = narayana(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = (
            (row[k] + row[k - 1]) * (2 * n - 1)
            - (a[k] - 2 * a[k - 1] + a[k - 2]) * (n - 2)
        ) // (n + 1)
    return row


@set_attributes(narayana, "Narayana", ["A001263", "A090181", "A131198"], True)
def Narayana(n: int, k: int) -> int:
    return narayana(n)[k]


@cache
def nicomachus(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = nicomachus(n - 1) + [3 * nicomachus(n - 1)[n - 1]]
    for k in range(0, n):
        row[k] *= 2
    return row


@set_attributes(nicomachus, "Nicomachus", ["A036561", "A081954", "A175840"], False)
def Nicomachus(n: int, k: int) -> int:
    return nicomachus(n)[k]


@cache
def one(n: int) -> list[int]:
    if n == 0:
        return [1]
    return one(n - 1) + [1]


@set_attributes(one, "One", ["A000012", "A008836", "A014077"], True)
def One(n: int, k: int) -> int:
    return one(n)[k]


@cache
def ordinals(n: int) -> list[int]:
    if n == 0:
        return [0]
    return ordinals(n - 1) + [n]


@set_attributes(
    ordinals, "Ordinals", ["A002260", "A002262", "A004736", "A025581"], False
)
def Ordinals(n: int, k: int) -> int:
    return ordinals(n)[k]


@cache
def ordered_cycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = ordered_cycle(n - 1) + [0]
    row[n] = row[n] * n
    for k in range(n, 0, -1):
        row[k] = (n - 1) * row[k] + k * row[k - 1]
    return row


@set_attributes(ordered_cycle, "OrderedCycle", ["A048594", "A075181", "A225479"], False)
def OrderedCycle(n: int, k: int) -> int:
    return ordered_cycle(n)[k]


@cache
def part(n: int, k: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return 1 if n == 0 else 0
    return part(n - 1, k - 1) + part(n - k, k)


@cache
def partnum_exact(n: int) -> list[int]:
    return [part(n, k) for k in range(n + 1)]


@set_attributes(partnum_exact, "Partition", ["A008284", "A058398", "A072233"], True)
def PartnumExact(n: int, k: int) -> int:
    return partnum_exact(n)[k]


@cache
def partnum_max(n: int) -> list[int]:
    return list(accumulate(partnum_exact(n)))


@set_attributes(partnum_max, "PartitionMax", ["A008284", "A058398", "A072233"], False)
def PartnumMax(n: int, k: int) -> int:
    return partnum_max(n)[k]


@cache
def polygonal(n: int) -> list[int]:
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    rov: list[int] = polygonal(n - 2)
    row: list[int] = polygonal(n - 1) + [n]
    row[n - 1] += row[n - 2]
    for k in range(2, n - 1):
        row[k] += row[k] - rov[k]
    return row


@set_attributes(
    polygonal, "Polygonal", ["A057145", "A134394", "A139600", "A139601"], False
)
def Polygonal(n: int, k: int) -> int:
    return polygonal(n)[k]


@cache
def powlag(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = powlag(n - 1) + [1]
    row[0] = row[n] = row[0] * n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@set_attributes(powlag, "PowLaguerre", ["A021012", "A196347"], False)
def PowLaguerre(n: int, k: int) -> int:
    return powlag(n)[k]


@cache
def rencontres(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = [
        (n - 1) * (rencontres(n - 1)[0] + rencontres(n - 2)[0])
    ] + rencontres(n - 1)
    for k in range(1, n - 1):
        row[k] = (n * row[k]) // k
    return row


@set_attributes(rencontres, "Rencontres", ["A008290", "A098825"], True)
def Rencontres(n: int, k: int) -> int:
    return rencontres(n)[k]


@cache
def rising_factorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + rising_factorial(n - 1)
    for k in range(0, n):
        row[k] += (n - k) * row[k + 1]
    return row


@set_attributes(
    rising_factorial,
    "RisingFact",
    ["A008279", "A068424", "A094587", "A173333", "A181511"],
    True,
)
def RisingFactorial(n: int, k: int) -> int:
    return rising_factorial(n)[k]


@cache
def schroeder(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = schroeder(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + row[k + 1]
    return row


@set_attributes(
    schroeder,
    "Schroeder",
    ["A033877", "A080245", "A080247", "A122538", "A106579"],
    True,
)
def Schroeder(n: int, k: int) -> int:
    return schroeder(n)[k]


@cache
def schroeder_paths(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = schroeder_paths(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * (2 * n - k)) // k
    row[0] = (row[0] * (4 * n - 2)) // n
    return row


@set_attributes(schroeder_paths, "SchroederP", ["A063007", "A104684"], True)
def SchroederPaths(n: int, k: int) -> int:
    return schroeder_paths(n)[k]


@cache
def seidel(n: int) -> list[int]:
    if n == 0:
        return [1]
    rowA: list[int] = seidel(n - 1)
    row: list[int] = [0] + seidel(n - 1)
    row[1] = row[n]
    for k in range(2, n + 1):
        row[k] = row[k - 1] + rowA[n - k]
    return row


@set_attributes(seidel, "Seidel", ["A008281", "A008282", "A010094"], False)
def Seidel(n: int, k: int) -> int:
    return seidel(n)[k]


def seidel_boust(n: int) -> list[int]:
    return seidel(n) if n % 2 else seidel(n)[::-1]


@set_attributes(
    seidel_boust, "SeidelBoust", ["A008280", "A108040", "A236935", "A239005"], False
)
def SeidelBoust(n: int, k: int) -> int:
    return seidel_boust(n)[k]


@cache
def sierpinski(n: int) -> list[int]:
    b = binomial(n)
    return [b[k] % 2 for k in range(n + 1)]


@set_attributes(
    sierpinski,
    "Sierpinski",
    ["A047999", "A090971", "A114700", "A143200", "A166282"],
    True,
)
def Sierpinski(n: int, k: int) -> int:
    return sierpinski(n)[k]


@cache
def stirling_cycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + stirling_cycle(n - 1)
    for k in range(1, n):
        row[k] = row[k] + (n - 1) * row[k + 1]
    return row


@set_attributes(
    stirling_cycle,
    "StirlingCyc",
    ["A008275", "A008276", "A048994", "A054654", "A094638", "A130534", "A132393"],
    True,
)
def StirlingCycle(n: int, k: int) -> int:
    return stirling_cycle(n)[k]


@cache
def stirling_cycle2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]
    rov: list[int] = stirling_cycle2(n - 2)
    row: list[int] = stirling_cycle2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * (rov[k - 1] + row[k])
    return row


@set_attributes(
    stirling_cycle2, "StirlingCyc2", ["A358622", "A008306", "A106828"], False
)
def StirlingCycle2(n: int, k: int) -> int:
    return stirling_cycle2(n)[k]


@cache
def stirling_cycleB(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = stirling_cycleB(n - 1) + [1]
    m = 2 * n - 1
    for k in range(n - 1, 0, -1):
        row[k] = m * row[k] + row[k - 1]
    row[0] *= m
    return row


@set_attributes(
    stirling_cycleB, "StirlingCycB", ["A028338", "A039757", "A039758", "A109692"], True
)
def StirlingCycleB(n: int, k: int) -> int:
    return stirling_cycleB(n)[k]


@cache
def stirling_set(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + stirling_set(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row


@set_attributes(
    stirling_set,
    "StirlingSet",
    [
        "A008277",
        "A008278",
        "A048993",
        "A080417",
        "A106800",
        "A151511",
        "A151512",
        "A154959",
        "A213735",
    ],
    True,
)
def StirlingSet(n: int, k: int) -> int:
    return stirling_set(n)[k]


@cache
def stirling_set2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]
    rov: list[int] = stirling_set2(n - 2)
    row: list[int] = stirling_set2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * rov[k - 1] + k * row[k]
    return row


@set_attributes(stirling_set2, "StirlingSet2", ["A358623", "A008299", "A137375"], False)
def StirlingSet2(n: int, k: int) -> int:
    return stirling_set2(n)[k]


@cache
def stirling_setB(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    pow: list[int] = stirling_setB(n - 1)
    row: list[int] = stirling_setB(n - 1) + [1]
    row[0] += 2 * row[1]
    for k in range(1, n - 1):
        row[k] = 2 * (k + 1) * pow[k + 1] + (2 * k + 1) * pow[k] + pow[k - 1]
    row[n - 1] = (2 * n - 1) * pow[n - 1] + pow[n - 2]
    return row


@set_attributes(stirling_setB, "StirlingSetB", ["A154602"], True)
def StirlingSetB(n: int, k: int) -> int:
    return stirling_setB(n)[k]


@cache
def sylvester(n: int) -> list[int]:
    def s(n: int, k: int) -> int:
        return sum(
            Binomial(n, k - j) * StirlingCycle(n - k + j, j) for j in range(k + 1)
        )

    return [s(n, k) for k in range(n + 1)]


@set_attributes(sylvester, "Sylvester", ["A341101"], False)
def Sylvester(n: int, k: int) -> int:
    return sylvester(n)[k]


@cache
def sympoly(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = sympoly(n - 1) + [1]
    for m in range(n - 1, 0, -1):
        row[m] = (n - m + 1) * row[m] + row[m - 1]
    row[0] *= n
    return row


@set_attributes(sympoly, "SymPoly", ["A093905", "A105954", "A165674", "A165675"], True)
def Sympoly(n: int, k: int) -> int:
    return sympoly(n)[k]


@cache
def ternary_tree(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = ternary_tree(n - 1) + [ternary_tree(n - 1)[n - 1]]
    return list(accumulate(accumulate(row)))


@set_attributes(ternary_tree, "TernaryTrees", ["A355172"], False)
def TernaryTree(n: int, k: int) -> int:
    return ternary_tree(n)[k]


@cache
def ward_set(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = ward_set(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k] + (n + k - 1) * row[k - 1]
    return row


@set_attributes(ward_set, "WardSet", ["A134991", "A269939"], False)
def WardSet(n: int, k: int) -> int:
    return ward_set(n)[k]


@cache
def worpitzky(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = worpitzky(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k - 1] + (k + 1) * row[k]
    return row


@set_attributes(
    worpitzky,
    "Worpitzky",
    ["A028246", "A053440", "A075263", "A130850", "A163626"],
    False,
)
def Worpitzky(n: int, k: int) -> int:
    return worpitzky(n)[k]


tabl_fun: list[tgen] = [
    Abel,
    Baxter,
    Bell,
    Bessel,
    Bessel2,
    Binomial,
    Catalan,
    CatalanAer,
    CatalanSqr,
    CentralCycle,
    CentralSet,
    ChebyshevS,
    ChebyshevT,
    ChebyshevU,
    Composition,
    CompoMax,
    Ctree,
    Delannoy,
    Euler,
    Eulerian,
    Eulerian2,
    EulerianB,
    EulerSec,
    EulerTan,
    FallingFactorial,
    Fibonacci,
    Fubini,
    FussCatalan,
    Gaussq2,
    Genocchi,
    Harmonic,
    HermiteE,
    HermiteH,
    Laguerre,
    Lah,
    Lehmer,
    Leibniz,
    Levin,
    Lozanic,
    Motzkin,
    MotzkinGF,
    Narayana,
    Nicomachus,
    One,
    Ordinals,
    OrderedCycle,
    PartnumExact,
    PartnumMax,
    Polygonal,
    PowLaguerre,
    Rencontres,
    RisingFactorial,
    Schroeder,
    SchroederPaths,
    Seidel,
    SeidelBoust,
    Sierpinski,
    StirlingCycle,
    StirlingCycle2,
    StirlingCycleB,
    StirlingSet,
    StirlingSet2,
    StirlingSetB,
    Sylvester,
    Sympoly,
    TernaryTree,
    WardSet,
    Worpitzky,
]


def CrossReferences(path: str = "crossrefs.md") -> None:
    """Writes a table in markdown style.
    Uses stored data from fun.sim (no searching)
    """
    with open(path, "w+") as xrefs:
        xrefs.write("| Table |  Source | Traits   |  OEIS similars |\n")
        xrefs.write("| :---  | :---    | :---     |  :---          |\n")
        for fun in tabl_fun:
            id = fun.id
            similars = fun.sim
            anum = ""
            s = str(similars).replace("[", "").replace("]", "").replace("'", "")
            for sim in similars:
                anum += "%7Cid%3A" + sim
            xrefs.write(
                f"| [{id}](https://github.com/PeterLuschny/tabl/blob/main/data/md/{id}.md) | [source](https://github.com/PeterLuschny/tabl/blob/main/src/{id}.py) | [traits](https://luschny.de/math/oeis/{id}.html) | [{s}](https://oeis.org/search?q={anum}) |\n"
            )


def SaveExtendedTables(dim: int = 9) -> None:
    tim: int = dim + dim
    path = GetMdPath()
    for fun in tabl_fun:
        tblfile = fun.id + ".md"
        tablpath = (path / tblfile).resolve()
        with open(tablpath, "w+") as dest:
            with contextlib.redirect_stdout(dest):
                PrintViews(fun, dim)
                I = inversion_wrapper(fun, tim)
                if I != None:
                    PrintViews(I, dim)
                r = reversion_wrapper(fun, tim)
                PrintViews(r, dim)
                r = revinv_wrapper(fun, tim)
                if r != None:
                    PrintViews(r, dim)
                r = invrev_wrapper(fun, tim)
                if r != None:
                    PrintViews(r, dim)


def GetFormulas() -> dict[str, str]:
    FORMULA: dict[str, str] = {}
    FORMULA["Tabl"] = "T(n, k), 0 &le; k &le; n"
    FORMULA["RevTabl"] = "T(n, n - k), 0 &le; k &le; n"
    FORMULA["InvTabl"] = "T<sup>-1</sup>(n, k), 0 &le; k &le; n"
    FORMULA["RevInvTabl"] = "T<sup>-1</sup>(n, n - k), 0 &le; k &le; n"
    FORMULA["InvRevTabl"] = "(T(n, n - k))<sup>-1</sup>, 0 &le; k &le; n"
    FORMULA["AccTabl"] = "see docs"
    FORMULA["RevAccTabl"] = "see docs"
    FORMULA["AccRevTabl"] = "see docs"
    FORMULA["AntiDiagTabl"] = "see docs"
    FORMULA["BinTabl"] = "see docs"
    FORMULA["InvBinTabl"] = "see docs"
    FORMULA["DiffxTabl"] = "T(n, k) (k+1)"
    FORMULA["RowSum"] = "&sum;<sub> k=0..n </sub> T(n, k)"
    FORMULA["EvenSum"] = "&sum;<sub> k=0..n </sub> T(n, k) even(k)"
    FORMULA["OddSum"] = "&sum;<sub> k=0..n </sub> T(n, k) odd(k)"
    FORMULA["AltSum"] = "&sum;<sub> k=0..n </sub> T(n, k) (-1)^k"
    FORMULA["AntiDiagSum"] = "&sum;<sub> k=0..n // 2 </sub> T(n - k, k)"
    FORMULA["AccSum"] = "&sum;<sub> k=0..n </sub>&sum;<sub> j=0..k </sub> T(n, j)"
    FORMULA[
        "AccRevSum"
    ] = "&sum;<sub> k=0..n </sub>&sum;<sub> j=0..k </sub> T(n, n - j)"
    FORMULA["RowLcm"] = "Lcm<sub> k=0..n </sub> | T(n, k) | &gt; 1"
    FORMULA["RowGcd"] = "Gcd<sub> k=0..n </sub> | T(n, k) | &gt; 1"
    FORMULA["RowMax"] = "Max<sub> k=0..n </sub> | T(n, k) |"
    FORMULA["ColMiddle"] = "T(n, n // 2)"
    FORMULA["ColECentral"] = "T(2 n, n)"
    FORMULA["ColOCentral"] = "T(2 n + 1, n)"
    FORMULA["ColLeft"] = "T(n, 0)"
    FORMULA["ColRight"] = "T(n, n)"
    FORMULA["BinConv"] = "&sum;<sub> k=0..n </sub> C(n, k) T(n, k)"
    FORMULA["InvBinConv"] = "&sum;<sub> k=0..n </sub> C(n, k) T(n, n - k) (-1)^k"
    FORMULA["TransSqrs"] = "&sum;<sub> k=0..n </sub> T(n, k) k^2"
    FORMULA["TransNat0"] = "&sum;<sub> k=0..n </sub> T(n, k) k"
    FORMULA["TransNat1"] = "&sum;<sub> k=0..n </sub> T(n, k) (k + 1)^k"
    FORMULA["DiagRow1"] = "T(n + 1, n)"
    FORMULA["DiagRow2"] = "T(n + 2, n)"
    FORMULA["DiagRow3"] = "T(n + 3, n)"
    FORMULA["DiagCol1"] = "T(n + 1, 1)"
    FORMULA["DiagCol2"] = "T(n + 2, 2)"
    FORMULA["DiagCol3"] = "T(n + 3, 3)"
    FORMULA["PolyTabl"] = "see docs"
    FORMULA["PolyRow1"] = "&sum;<sub> k=0..1 </sub>T(1, k) n^k"
    FORMULA["PolyRow2"] = "&sum;<sub> k=0..2 </sub>T(2, k) n^k"
    FORMULA["PolyRow3"] = "&sum;<sub> k=0..3 </sub>T(3, k) n^k"
    FORMULA["PolyCol2"] = "&sum;<sub> k=0..n </sub>T(n, k) 2^k"
    FORMULA["PolyCol3"] = "&sum;<sub> k=0..n </sub>T(n, k) 3^k"
    FORMULA["PolyDiag"] = "&sum;<sub> k=0..n </sub>T(n, k) n^k"
    FORMULA["PosHalf"] = "&sum;<sub> k=0..n </sub>2^n T(n, k) (1/2)^k"
    FORMULA["NegHalf"] = "&sum;<sub> k=0..n </sub>(-2)^n T(n, k) (-1/2)^k"
    return FORMULA


Header = [
    "<!DOCTYPE html>",
    "<html lang='en'><head><meta charset='UTF-8'/>",
    "<meta name='viewport' content='width=device-width, initial-scale=1.0'/>",
]
CSS = [
    "<style> body {font-family: 'Segoe UI', sans-serif;} ",
    "table, td, th, p { border-collapse: collapse; color: blue;} ",
    "td, th { border-bottom: 0; padding: 4px} ",
    "td { text-align: left} ",
    "tr:nth-child(odd) { background: #eee;} ",
    "tr:nth-child(even) { background: #fff;} ",
    "tr.header { background: orange !important; color: white; font-weight: 700;} ",
    "tr.subheader { background: lightgray !important; color: black;} ",
    "tr.headerLastRow { border-bottom: 2px solid black;} ",
    "th.rowNumber, td.rowNumber { text-align: right;} ",
    "a {text-decoration: none; color:brown;} ",
    "a:hover {background-color: #AFE1AF;} ",
    "#rcor1 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 40px; height: 0px;} ",
    "#rcor2 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 550px; height: 0px;} ",
    "#rcor3 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 88px; height: 20px; font-weight: 700; text-align: center;} ",
    ".center {margin-top: 1em;} ",
    ".tooltip { position: relative; display: inline-block; font-weight: 600;} ",
    ".tooltip .formula { visibility: hidden; width: 200px; background-color: lightgray; text-align: center; border-radius: 6px; padding: 5px 0; position: absolute; z-index: 1; top: +2px; left: 105%;} ",
    ".tooltip:hover .formula { visibility: visible; } ",
    "</style></head><body>",
]

Table = [
    "<table class='sortable'><thead><tr>",
    "<th id='rcor1'>&#8597; Trait</th>",
    "<th id='rcor1'>&#8597; A</th>",
    "<th id='rcor2'>Sequence</th>",
    "</tr></thead><tbody>",
]
SCRIPT = [
    "\n<script>",
    "var table = document.querySelector('.massive')\n",
    "var tbody = table.tBodies[0]\n",
    "var rows = [].slice.call(tbody.rows, 0)\n",
    "var fragment = document.createDocumentFragment()\n",
    "for (var k = 0; k < 50; k++) {\n",
    "for (var i = 0; i < rows.length; i++) {\n",
    "fragment.appendChild(rows[i].cloneNode(true)) } }\n",
    "tbody.innerHTML = '' \n",
    "tbody.appendChild(fragment)\n",
    "</script> <script src='sortable.js'></script> <script>\n",
    "function prepareAdvancedTable() { \n",
    "var size_table = document.querySelector('.advanced-table')\n",
    "var rows = size_table.tBodies[0].rows\n",
    "for (let i = 0; i < rows.length; i++) { \n",
    "const date_element = rows[i].cells[2]\n",
    "const size_element = rows[i].cells[1]\n",
    "date_element.setAttribute('data-sort', date_element.innerText.replace",
    r"(/(\d+)\/(\d+)\/(\d+)/, '$3$1$2'))",
    "\nsize_element.setAttribute('data-sort', toBytes(size_element.innerText)) } }\n",
    "function toBytes(size) {",
    "const units = [, 'k', 'm', 'g', 't']\n",
    "const match = size.match" r"(/(\d+\.\d+|\d+)\s*([kmgt])b?/i)",
    "\nif (!match) return parseFloat(size)\n",
    "const [value, unit] = match.slice(1)\n",
    "const index = units.indexOf(unit.toLowerCase())\n",
    "return Math.round(parseFloat(value) * Math.pow(1024, index)) }\n",
    "prepareAdvancedTable()\n",
    "</script>\n" "<p>&nbsp;</p></body></html>",
]
Footer = [
    "<p style='margin-left:8px'>Note: The A-numbers are based on a finite number of numerical comparisons.<br>",
    "They ignore the sign and the OEIS-offset, and might differ in the first few values.<br>"
    "Here the offset of all triangles is 0 and consequently also the offset of all sequences.</p>",
]


def HtmlTriangle(fun: tgen) -> str:
    s = ""
    for n in range(6):
        s += "[{n}] " + str(fun.gen(n)).replace("[", "").replace("]", "") + "<br>"
    return s


funnames = [fun.id for fun in tabl_fun]


def getprevnext(funname: list[str]) -> tuple[str, str]:
    idx = funnames.index(funname)
    prev = idx - 1
    succ = idx + 1
    if idx == 0:
        prev = len(tabl_fun) - 1
    if idx == len(tabl_fun) - 1:
        succ = 0
    return (funnames[prev], funnames[succ])


def navbar(fun: tgen) -> list[str]:
    anums = ""
    for s in fun.sim:
        anums += "%7Cid%3A" + s
    prevnext = getprevnext(fun.id)
    rc = "style='border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 108px; height: 20px; font-weight: 700; text-align: center; margin-left: 8px; margin-right: 8px;'"
    NAVBAR = ["<table class='center'><tr>"]
    NAVBAR.append(
        f"<td {rc};><a style='color:white' href='https://luschny.de/math/oeis/{prevnext[0]}.html'>&nbsp;&lt;&lt;&nbsp;</a></td>"
    )
    NAVBAR.append(
        f"<td {rc};><a style='color:white' href='https://github.com/PeterLuschny/tabl/blob/main/data/md/{fun.id}.md'>Table</a></td>"
    )
    NAVBAR.append(
        f"<td {rc};><a style='color:white' href='https://github.com/PeterLuschny/tabl/blob/main/src/{fun.id}.py'>Source</a></td>"
    )
    NAVBAR.append(
        f"<td {rc};><a style='color:white' href='https://oeis.org/search?q={anums}'>Similars</a></td>"
    )
    NAVBAR.append(
        f"<td {rc};><a style='color:white' href='https://luschny.de/math/oeis/index.html'>Index</a></td>"
    )
    NAVBAR.append(
        f"<td {rc};><a style='color:white' href='https://luschny.de/math/oeis/{prevnext[1]}.html'>&nbsp;&gt;&gt;&nbsp;</a></td>"
    )
    NAVBAR.append("</tr></table>")
    return NAVBAR


def CsvToHtml(fun: tgen, csvpath: Path, outpath: Path) -> None:
    name = fun.id
    # csvfile = (csvpath / (name + "X.csv")).resolve()
    csvfile = (csvpath / (name + ".csv")).resolve()
    outfile = (outpath / (name + ".html")).resolve()
    FORMULA = GetFormulas()
    with open(csvfile, "r") as csvfile:
        reader = csv.reader(csvfile)
        with open(outfile, "w") as outfile:
            for l in Header:
                outfile.write(l)
            outfile.write(f"<title>{name} : IntegerTriangles.py</title>")
            for l in CSS:
                outfile.write(l)
            l = next(reader)  # column names
            sim = str(fun.sim).replace("'", "").replace("[", "").replace("]", "")
            outfile.write(
                f"<div class='tooltip' style='border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 160px; height: 20px; font-weight: 700; text-align: center;'>{name.upper()}<span class='formula' style=' background: #73AD21; font-weight:600; width: 220px;'>{HtmlTriangle(fun)}</span></div>"
            )
            outfile.write(
                f"<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OEIS Similars: {sim}\n</p>"
            )
            for l in Table:
                outfile.write(l)
            for line in reader:
                if line[0][0] == "#":
                    continue
                if line[3] == "[]":
                    continue
                # trait
                l2 = line[2]
                tip = FORMULA[l2]
                if "Tabl" in l2:
                    l2 = "&#916;" + l2.replace("Tabl", "")
                outfile.write(
                    f"<tr><td class='tooltip'>{l2}<span class='formula'>{tip}</span></td>"
                )
                seq = line[3].replace("[", "").replace(" ]", "")
                # Anum
                if line[1] == "":
                    sep = seq.replace(" ", "+")
                    # outfile.write(f"<td><a href='https://oeis.org/?q={seq}&sort=&#language=&go=search' target='_blank'>search</a></td>")
                    outfile.write(
                        f"<td style='text-align:center;'><a href='http://sequencedb.net/index.html?s={sep}' target='_blank'>search</a></td>"
                    )
                else:
                    outfile.write(
                        f"<td><a href='https://oeis.org/{line[1]}'>{line[1]}</a></td>"
                    )
                # seq
                outfile.write(f"<td>{seq}</td></tr>")
            outfile.write("</tbody></table>")
            for l in navbar(fun):
                outfile.write(l)
            for l in Footer:
                outfile.write(l)
            for l in SCRIPT:
                outfile.write(l)


def AllCsvToHtml(csvpath: Path = GetCsvPath(), outpath: Path = GetHtmlPath()) -> None:
    for fun in tabl_fun:
        CsvToHtml(fun, csvpath, outpath)


def get_compressed() -> None:
    oeisstripped = "https://oeis.org/stripped.gz"
    r = requests.get(oeisstripped, stream=True)
    with open(strippedpath, "wb") as local:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                local.write(chunk)
    with gzip.open(strippedpath, "rb") as gz:
        with open(oeispath, "wb") as da:
            da.write(gz.read())


def oeisabsdata() -> None:
    """Make all terms absolute."""
    with open(oeispath, "r") as oeisdata:
        with open(datapath, "w") as absdata:
            for seq in oeisdata:
                if not "#" in seq:
                    absdata.write(seq.replace("-", ""))


def GetOEISdata() -> None:
    get_compressed()
    oeisabsdata()


def SeqToFixlenString(seq: list[int], maxlen: int = 90, separator: str = ",") -> str:
    stri = "["
    maxl = 3
    for trm in seq:
        s = str(trm) + separator
        maxl += len(s)
        if maxl > maxlen:
            break
        stri += s
    return stri + "]"


def FindSequence(seq: str) -> str:
    """Search for a match in the database.
    Nota bene: The database is assumed to have abs terms!
    Args:
        seq (str): The stringified sequence
    Returns:
        str: The oeis A-number if found, "" otherwise.
    """
    datapath = GetDataPath()
    with open(datapath, "r") as database:
        for data in database:
            if seq in data:
                return data[:7]
    return ""


def GetAnumber(seq: list[int]) -> str:
    """Search for a match in the database.
    Increase the 'offset' twice if not found.
    Args:
        seq (list[int]): The sequence as a list of integers
    Returns:
        str: The oeis A-number if found, "" otherwise
    """
    for n in range(3):
        seqstr = SeqToFixlenString(seq[n:], 100, ",")
        abstr = seqstr.replace("-", "").replace(" ", "")[1:-1]
        anum = FindSequence(abstr)
        if anum != "":
            return anum
    zerofree = [t for t in seq[1:] if t != 0]
    if zerofree != seq:
        seqstr = SeqToFixlenString(zerofree, 100, ",")
        abstr = seqstr.replace("-", "").replace(" ", "")[1:-1]
        anum = FindSequence(abstr)
        if anum != "":
            return anum
    return ""


def flat(t: tabl) -> list[int]:
    """Flatten table to sequence
    Args:
        t (tabl): table
    Returns:
        list[int]: sequence
    """
    if t == []:
        return []
    return [i for row in t for i in row]


TRAIT: dict[str, Callable[[tabl], trow]] = {}


def RegisterTrait(f: Callable[[tabl], trow]) -> None:
    TRAIT[f.__name__] = f


TRAIT2: dict[str, Callable[[rgen, int], trow]] = {}


def RegisterTrait2(f: Callable[[rgen, int], trow]) -> None:
    TRAIT2[f.__name__] = f


def register() -> None:
    RegisterTrait(FlatTabl)
    RegisterTrait(FlatRevTabl)
    RegisterTrait(FlatInvTabl)
    RegisterTrait(FlatRevInvTabl)
    RegisterTrait(FlatInvRevTabl)
    RegisterTrait(FlatAccTabl)
    RegisterTrait(FlatRevAccTabl)  # rarely found
    RegisterTrait(FlatAccRevTabl)
    RegisterTrait(FlatAntiDiagTabl)
    RegisterTrait(FlatBinTabl)  # rarely found
    RegisterTrait(FlatInvBinTabl)  # rarely found
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


def PrintTraits(
    g: tgen,
    size: int,
    withanum: bool = False,
    markdown: bool = True,
    onlythefound: bool = True,
) -> None:
    trianglename = g.id
    T = g.tab(size)
    gen = g.gen
    if markdown:
        if withanum:
            print("| Triangle    | Anum    | Trait    |  Sequence   |")
            print("| :---        | :---    |  :---    |  :---  |")
        else:
            print("| Triangle    | Trait   |  Sequence  |")
            print("| :---        | :---    |  :---      |")
        for traitname, trait in TRAIT.items():
            name = traitname[4:] if traitname.startswith("Flat") else traitname
            tt = trait(T)
            if withanum:
                anum = "" if tt == [] else GetAnumber(tt)
                if anum != "":
                    print(traitname)
                    if onlythefound:
                        continue
                seqstr = SeqToFixlenString(tt, 70, " ")
                print(f"| {trianglename} | {anum:7} | {name:<12} | {seqstr} |")
            else:
                seqstr = SeqToFixlenString(tt, 70, " ")
                print(f"| {trianglename} | {name:<12} | {seqstr} |")
    else:  # TXT simple dictionary, no options, no anums
        for traitname, trait in TRAIT.items():
            name = traitname[4:] if traitname.startswith("Flat") else traitname
            seqstr = SeqToFixlenString(trait(T), 70, " ")
            print(f"{trianglename}:{name:<14} {seqstr}")
    if markdown:
        for traitname, trait in TRAIT2.items():
            tt = trait(gen, size)
            if withanum:
                anum = "" if tt == [] else GetAnumber(tt)
                if anum != "":
                    print(traitname)
                    if onlythefound:
                        continue
                seqstr = SeqToFixlenString(tt, 70, " ")
                print(f"| {trianglename} | {anum:7} | {traitname:<12} | {seqstr} |")
            else:
                seqstr = SeqToFixlenString(tt, 70, " ")
                print(f"| {trianglename} | {traitname:<12} | {seqstr} |")
    else:  # TXT simple dictionary, no options, no anums
        for traitname, trait in TRAIT2.items():
            seqstr = SeqToFixlenString(trait(gen, size), 70, " ")
            print(f"{trianglename}:{traitname:<14} {seqstr}")


def SaveTraitsToFile(
    g: tgen,
    size: int,
    withanum: bool = False,
    markdown: bool = True,
    onlythefound: bool = True,
) -> None:
    trianglename = g.id
    T = g.tab(size)
    gen = g.gen
    if markdown:
        filepath = (GetMdPath() / f"{trianglename}.md").resolve()
    else:
        filepath = (GetCsvPath() / f"{trianglename}.csv").resolve()
    with open(filepath, "w") as target:
        if markdown:
            if withanum:
                target.write("| Triangle    | Anum    | Trait    |  Seq   |\n")
                target.write("| :---        | :---    |  :---    |  :---  |\n")
            else:
                target.write("| Triangle    | Trait   |  Seq       |\n")
                target.write("| :---        | :---    |  :---      |\n")
        else:  # CSV
            if withanum:
                target.write("Triangle,Anum,Trait,Sequence\n")
            else:
                target.write("Triangle,Trait,Sequence\n")
        if markdown:
            for traitname, trait in TRAIT.items():
                name = traitname[4:] if traitname.startswith("Flat") else traitname
                tt = trait(T)
                if withanum:
                    anum = "" if tt == [] else GetAnumber(tt)
                    if anum != "":
                        print(traitname)
                        if onlythefound:
                            continue
                    seqstr = SeqToFixlenString(tt, 70, " ")
                    target.write(
                        f"| {trianglename} | {anum:7} | {name:<12} | {seqstr} |\n"
                    )
                else:
                    seqstr = SeqToFixlenString(tt, 70, " ")
                    target.write(f"| {trianglename} | {name:<12} | {seqstr} |\n")
        else:  # CSV
            for traitname, trait in TRAIT.items():
                name = traitname[4:] if traitname.startswith("Flat") else traitname

                tt = trait(T)
                if withanum:
                    anum = "" if tt == [] else GetAnumber(tt)
                    if anum == "":
                        print(traitname)
                        if onlythefound:
                            continue
                    seqstr = SeqToFixlenString(tt, 70, " ")
                    target.write(f"{trianglename},{anum},{name},{seqstr}\n")
                else:
                    seqstr = SeqToFixlenString(tt, 70, " ")
                    target.write(f"{trianglename},{name},{seqstr}\n")
        if markdown:
            for traitname, trait in TRAIT2.items():
                tt = trait(gen, size)
                if withanum:
                    anum = "" if tt == [] else GetAnumber(tt)
                    if anum != "":
                        print(traitname)
                        if onlythefound:
                            continue
                    seqstr = SeqToFixlenString(tt, 70, " ")
                    target.write(
                        f"| {trianglename} | {anum:7} | {traitname:<12} | {seqstr} |\n"
                    )
                else:
                    seqstr = SeqToFixlenString(tt, 70, " ")
                    target.write(f"| {trianglename} | {traitname:<12} | {seqstr} |\n")
        else:  # CSV
            for traitname, trait in TRAIT2.items():
                tt = trait(gen, size)
                if withanum:
                    anum = "" if tt == [] else GetAnumber(tt)
                    if anum == "":
                        print(traitname)
                        if onlythefound:
                            continue
                    seqstr = SeqToFixlenString(tt, 70, " ")
                    target.write(f"{trianglename},{anum},{traitname},{seqstr}\n")
                else:
                    seqstr = SeqToFixlenString(tt, 70, " ")
                    target.write(f"{trianglename},{traitname},{seqstr}\n")


def PrintExtendedTraits(
    T: tgen, size: int, withanum: bool = False, markdown: bool = True
) -> None:
    tim: int = size + size // 2
    print("\n# Normal.")
    Tid = T.id
    T.id = T.id + ":Std"
    PrintTraits(T, size, withanum, markdown)
    T.id = Tid
    print("\n# Reverse.")
    r = reversion_wrapper(T, tim)
    PrintTraits(r, size, withanum, markdown)
    I = inversion_wrapper(T, tim)
    if I != None:
        print("\n# Inverse.")
        PrintTraits(I, size, withanum, markdown)
    r = revinv_wrapper(T, tim)
    if r != None:
        print("\n# Reverse of inverse.")
        PrintTraits(r, size, withanum, markdown)
    r = invrev_wrapper(T, tim)
    if r != None:
        print("\n# Inverse of reverse.")
        PrintTraits(r, size, withanum, markdown)


def SaveExtendedTraitsToCSV(G: tgen, size: int) -> None:
    # register()
    tim: int = size + size // 2
    R = reversion_wrapper(G, tim)
    I = inversion_wrapper(G, tim)
    cases = [G, R]

    if I != None:
        cases.append(I)
    filepath = (GetCsvPath() / f"{G.id}X.csv").resolve()
    savedid = G.id
    G.id = G.id + ":Std"

    with open(filepath, "w") as target:
        target.write("Triangle,Anum,Trait,Sequence\n")
        for g in cases:
            trianglename = g.id
            T = g.tab(size)
            gen = g.gen
            print("#", trianglename)
            for traitname, trait in TRAIT.items():
                name = traitname[4:] if traitname.startswith("Flat") else traitname
                tt = trait(T)
                anum = "" if tt == [] else GetAnumber(tt)
                if anum == "":
                    print(traitname)
                    continue
                seqstr = SeqToFixlenString(tt, 70, " ")
                target.write(f"{trianglename},{anum},{name},{seqstr}\n")
            for traitname, trait in TRAIT2.items():
                tt = trait(gen, size)
                anum = "" if tt == [] else GetAnumber(tt)
                if anum == "":
                    print(traitname)
                    continue
                seqstr = SeqToFixlenString(tt, 70, " ")
                target.write(f"{trianglename},{anum},{traitname},{seqstr}\n")
    G.id = savedid


def PrintAllTraitsWithAnumber(size: int) -> None:
    for fun in tabl_fun:
        PrintTraits(fun, size, withanum=True)


def PrintAllTraits(size: int) -> None:
    for fun in tabl_fun:
        PrintTraits(fun, size, withanum=False)


def SaveAllFoundTraitsToCSV() -> None:
    register()
    for fun in tabl_fun:
        print("#", fun.id)
        SaveTraitsToFile(fun, 20, withanum=True, markdown=False, onlythefound=True)


def SaveAllTraitsToCSV() -> None:
    register()
    for fun in tabl_fun:
        print("#", fun.id)
        SaveTraitsToFile(fun, 20, withanum=True, markdown=False, onlythefound=False)


def SaveAllExtendedTraitsToCSV() -> None:
    register()
    for fun in tabl_fun:
        print("##", fun.id)
        SaveExtendedTraitsToCSV(fun, 20)
