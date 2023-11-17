from os import remove
from functools import cache, reduce
from itertools import accumulate
from math import lcm, gcd, factorial
from sys import setrecursionlimit, set_int_max_str_digits
from typing import Callable, TypeAlias
from inspect import signature
from tabulate import tabulate
import contextlib
import csv
import urllib.request
import urllib.error
import requests
import time
import gzip
import sqlite3
import pandas as pd
from fractions import Fraction as frac
from pathlib import Path

setrecursionlimit(3000)
set_int_max_str_digits(5000)
path = Path(__file__).parent.parent
strippedpath = (path / "data/stripped").resolve()


def GetRoot(name: str = "") -> Path:
    return (path / name).resolve()


def GetData(name: str) -> Path:
    relpath = f"data/{name}"
    return (path / relpath).resolve()


def GetDataPath(name: str, fix: str) -> Path:
    relpath = f"data/{fix}/{name}.{fix}"
    return (path / relpath).resolve()


def MakeDirectory(dir: Path) -> None:
    """Checks if a path exists, and if not,
    creates the new path."""
    Path(dir).mkdir(parents=True, exist_ok=True)


def EnsureDataDirectories() -> None:
    MakeDirectory(GetRoot("data/csv"))
    MakeDirectory(GetRoot("data/db"))
    MakeDirectory(GetRoot("data/html"))
    MakeDirectory(GetRoot("data/md"))


def InvertTabl(L: list[list[int]]) -> list[list[int]]:
    # Inverse of a lower triangular matrix
    n = len(L)
    inv = [[0 for i in range(n)] for _ in range(n)]  # Identity matrix
    for i in range(n):
        inv[i][i] = 1
    for k in range(n):
        for j in range(n):
            for i in range(k):
                inv[k][j] -= inv[i][j] * L[k][i]
            a = inv[k][j]
            b = L[k][k]
            if b == 0:
                # print("Warning: Inverse does not exist!")
                return []
            a, r = divmod(a, b)  # make sure that a is integer
            if r != 0:
                # print("Warning: Integer terms do not exist!")
                return []
    return [row[0 : n + 1] for n, row in enumerate(inv)]


def InvertTriangle(r, dim: int) -> list[list[int]]:
    M = [[r(n)[k] if k <= n else 0 for k in range(dim)] for n in range(dim)]
    return InvertTabl(M)


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


def Flat(T: tabl) -> list[int]:
    """Flatten table to sequence
    Args:
        T (tabl): table
    Returns:
        list[int]: sequence
    """
    if T == []:
        return []
    return [i for row in T for i in row]


def SeqString(seq: list[int], maxlen: int) -> str:
    seqstr = ""
    maxl = 0
    for trm in seq:
        s = str(trm) + ","
        maxl += len(s)
        if maxl > maxlen:
            break
        seqstr += s
    return seqstr


def InvTable(T: tgen, size: int) -> tgen | None:
    """_summary_
    Args:
        T (tgen): _description_
        size (int): _description_
    Returns:
        tgen | None: _description_
    """
    t = T.inv(size)
    if t == []:
        return None

    @cache
    def psgen(n: int) -> trow:
        return list(t[n])

    @MakeTriangle(psgen, T.id + ":Inv", [], True)
    def Psgen(n: int, k: int) -> int:
        return psgen(n)[k]

    return Psgen


def RevTable(T: tgen, size: int) -> tgen:
    """_summary_
    Args:
        T (tgen): _description_
        size (int): _description_
    Returns:
        tgen: _description_
    """
    t = T.tab(size)

    @cache
    def rsgen(n: int) -> trow:
        row = t[n]
        return [row[n - i] for i in range(n + 1)]

    @MakeTriangle(rsgen, T.id + ":Rev", [], True)
    def Rsgen(n: int, k: int) -> int:
        return rsgen(n)[k]

    return Rsgen


def RevInvTable(T: tgen, size: int) -> tgen | None:
    """First inverse, then reverse.
       read: Rev(Inv(T))
    Args:
        T (tgen): _description_
        size (int): _description_
    Returns:
        tgen | None: _description_
    """
    V = InvTable(T, size)
    if V is None:
        return None
    J = RevTable(V, size)

    @cache
    def rigen(n: int) -> trow:
        return list(J.gen(n))

    @MakeTriangle(rigen, J.id, [], True)
    def Rigen(n: int, k: int) -> int:
        return rigen(n)[k]

    return Rigen


def InvRevTable(T: tgen, size: int) -> tgen | None:
    """First reverse, then inverse.
       read: Inv(Rev(T))
    Args:
        T (tgen): _description_
        size (int): _description_
    Returns:
        tgen | None: _description_
    """
    R = RevTable(T, size)
    S = InvTable(R, size)
    if S is None:
        return None

    @cache
    def tigen(n: int) -> trow:
        return list(S.gen(n))

    @MakeTriangle(tigen, S.id, [], True)
    def Tigen(n: int, k: int) -> int:
        return tigen(n)[k]

    return Tigen


def SubTriangle(g: rgen, N: int, K: int, size: int) -> tabl:
    return [[g(n)[k] for k in range(K, K - N + n + 1)] for n in range(N, N + size)]


def AbsSubTriangle(g: rgen, N: int, K: int, size: int) -> tabl:
    return [[abs(g(n)[k]) for k in range(K, K - N + n + 1)] for n in range(N, N + size)]


def MakeTriangle(
    gen: rgen, id: str, sim: list[str], vert: bool = False
) -> Callable[..., Callable[[int, int], int]]:
    def makerow(n: int) -> trow:
        return list(gen(n))

    def maketab(size: int) -> tabl:
        return [list(gen(n)) for n in range(size)]

    def makerev(size: int) -> tabl:
        return [list(reversed(gen(n))) for n in range(size)]

    def makemat(size: int) -> tabl:
        return [[gen(n)[k] if k <= n else 0 for k in range(size)] for n in range(size)]

    def makeflat(size: int) -> trow:
        return [gen(n)[k] for n in range(size) for k in range(n + 1)]

    def makeinv(size: int) -> tabl:
        if not vert:
            return []
        return InvertTriangle(gen, size)

    def makerevinv(size: int) -> tabl:
        if not vert:
            return []
        V = InvertTriangle(gen, size)
        if V == []:
            return []
        return [[V[n][n - k] for k in range(n + 1)] for n in range(size)]

    def makeinvrev(size: int) -> tabl:
        R = [list(reversed(gen(n))) for n in range(size)]
        M = [[R[n][k] if k <= n else 0 for k in range(size)] for n in range(size)]
        return InvertTabl(M)

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

    def Triangle(f: Callable[[int, int], int]) -> Callable[[int, int], int]:
        f.tab = maketab
        f.rev = makerev
        f.mat = makemat
        f.inv = makeinv
        f.flat = makeflat
        f.row = makerow
        f.revinv = makerevinv
        f.invrev = makeinvrev
        f.sub = sub
        f.abssub = abssub
        f.sim = sim
        f.id = id
        f.gen = gen
        return f

    return Triangle


def AntiDiagTabl(T: tabl) -> tabl:
    """Return the table of (upward) anti-diagonals."""
    return [
        [T[n - k - 1][k] for k in range((n + 1) // 2)] for n in range(1, len(T) + 1)
    ]


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


def Diffx1(T: tabl) -> trow:  # flat tabl
    return [(k + 1) * c for row in T for k, c in enumerate(row)]


def Diffx1Tabl(T: tabl) -> tabl:
    return [[(k + 1) * c for k, c in enumerate(row)] for row in T]


def Diffx0(T: tabl) -> trow:  # flat tabl
    return [k * c for row in T for k, c in enumerate(row)]


def Diffx0Tabl(T: tabl) -> tabl:
    return [[k * c for k, c in enumerate(row)] for row in T]


def Triangle(T: tabl) -> trow:
    return [i for row in T for i in row]


def Triangle_(g: rgen, row: int) -> trow:
    return g(row)


def Inv(T: tabl) -> trow:
    IT = InvTabl(T)
    if InvTabl(T) == []:
        return []
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


def PrintTabls(g: tgen, size: int = 8, mdformat: bool = True) -> None:
    TABLSTRAIT: dict[str, Callable[[tabl], trow]] = {}

    def RegisterTablsTrait(f: Callable[[tabl], trow]) -> None:
        TABLSTRAIT[f.__name__] = f

    T = g.tab(size)
    RegisterTablsTrait(Triangle)
    RegisterTablsTrait(Rev)
    RegisterTablsTrait(Inv)
    RegisterTablsTrait(InvRev)
    RegisterTablsTrait(RevInv)
    RegisterTablsTrait(Acc)
    RegisterTablsTrait(RevAcc)
    RegisterTablsTrait(AccRev)
    RegisterTablsTrait(AntiDiag)
    RegisterTablsTrait(Diffx0)
    trianglename = g.id
    if mdformat:
        print("#", trianglename, ": Tables")
        print()  # reqiured!
        print("| Trait    |   Seq  |")
        print("| :---     |  :---  |")
        for traitname, trait in TABLSTRAIT.items():
            print(f"| {traitname:<15} | {trait(T)} |")
    else:
        for traitname, trait in TABLSTRAIT.items():
            print(f'{trianglename+":"+traitname:<21} {trait(T)}')


def PolyEval_(g: rgen, n: int, x: int) -> int:
    row = g(n)
    return sum(c * (x**j) for (j, c) in enumerate(row))


def PolyEval(T: tabl, n: int, x: int) -> int:
    return sum(T[n][k] * (x**k) for k in range(n + 1))


def PolyRow(g: rgen, size: int, row: int) -> trow:
    return [PolyEval_(g, row, x) for x in range(size)]


def PolyRow0(g: rgen, size: int) -> trow:
    return PolyRow(g, size, 0)


def PolyRow1(g: rgen, size: int) -> trow:
    return PolyRow(g, size, 1)


def PolyRow2(g: rgen, size: int) -> trow:
    return PolyRow(g, size, 2)


def PolyRow3(g: rgen, size: int) -> trow:
    return PolyRow(g, size, 3)


def PolyCol(g: rgen, size: int, col: int) -> trow:
    return [PolyEval_(g, k, col) for k in range(size)]


def PolyCol0(g: rgen, size: int) -> trow:
    return PolyCol(g, size, 0)


def PolyCol1(g: rgen, size: int) -> trow:
    return PolyCol(g, size, 1)


def PolyCol2(g: rgen, size: int) -> trow:
    return PolyCol(g, size, 2)


def PolyCol3(g: rgen, size: int) -> trow:
    return PolyCol(g, size, 3)


def PolyDiag(g: rgen, size: int) -> trow:
    return [PolyEval_(g, n, n) for n in range(size)]


def AntiDiagPoly(g: rgen, n: int) -> trow:
    return [PolyEval_(g, n - k, k) for k in range(n + 1)]


def PolyDiagTabl(g: rgen, size: int) -> tabl:
    return [AntiDiagPoly(g, n) for n in range(size)]


def Poly(g: rgen, size: int) -> trow:
    return [i for row in PolyDiagTabl(g, size) for i in row]


def PolyFrac(T: tabl, x: frac) -> list[frac | int]:
    return [sum(c * (x**k) for (k, c) in enumerate(row)) for row in T]


def PosHalf_(g: rgen, size: int) -> trow:
    T = [g(n) for n in range(size)]
    R = PolyFrac(T, frac(1, 2))
    return [((2**n) * r).numerator for n, r in enumerate(R)]


def PosHalf(T: tabl) -> trow:
    R = PolyFrac(T, frac(1, 2))
    return [((2**n) * r).numerator for n, r in enumerate(R)]


def NegHalf_(g: rgen, size: int) -> trow:
    T = [g(n) for n in range(size)]
    R = PolyFrac(T, frac(-1, 2))
    return [(((-2) ** n) * r).numerator for n, r in enumerate(R)]


def NegHalf(T: tabl) -> trow:
    R = PolyFrac(T, frac(-1, 2))
    return [(((-2) ** n) * r).numerator for n, r in enumerate(R)]


def PrintPolys(t: tgen, size: int = 8, mdformat: bool = True) -> None:
    POLYTRAIT: dict[str, Callable[[t.gen, int], trow]] = {}

    def RegisterPolyTrait(f: Callable[[t.gen, int], trow]) -> None:
        POLYTRAIT[f.__name__] = f

    RegisterPolyTrait(Poly)
    RegisterPolyTrait(PolyRow0)
    RegisterPolyTrait(PolyRow1)
    RegisterPolyTrait(PolyRow2)
    RegisterPolyTrait(PolyRow3)
    RegisterPolyTrait(PolyCol0)
    RegisterPolyTrait(PolyCol1)
    RegisterPolyTrait(PolyCol2)
    RegisterPolyTrait(PolyCol3)
    RegisterPolyTrait(PolyDiag)
    RegisterPolyTrait(PosHalf_)
    RegisterPolyTrait(NegHalf_)
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


def RowSum(T: tabl) -> trow:
    return [sum(row) for row in T]


def RowSum_(g: rgen, size: int) -> trow:
    return [sum(g(n)) for n in range(size)]


def EvenSum(T: tabl) -> trow:
    return [even_sum(row) for row in T]


def EvenSum_(g: rgen, size: int) -> trow:
    return [even_sum(g(n)) for n in range(size)]


def OddSum(T: tabl) -> trow:
    return [odd_sum(row) for row in T]


def OddSum_(g: rgen, size: int) -> trow:
    return [odd_sum(g(n)) for n in range(size)]


def AltSum(T: tabl) -> trow:
    return [alt_sum(row) for row in T]


def AltSum_(g: rgen, size: int) -> trow:
    return [alt_sum(g(n)) for n in range(size)]


def AccSum(T: tabl) -> trow:
    return [acc_sum(row) for row in T]


def AccSum_(g: rgen, size: int) -> trow:
    return [acc_sum(g(n)) for n in range(size)]


def AccRevSum(T: tabl) -> trow:
    return [accrev_sum(row) for row in T]


def AccRevSum_(g: rgen, size: int) -> trow:
    return [accrev_sum(g(n)) for n in range(size)]


def DiagSum(T: tabl) -> trow:
    def row(n: int) -> list[int]:
        return [T[n - k - 1][k] for k in range((n + 1) // 2)]

    return [sum(row(n)) for n in range(1, len(T) + 1)]


def DiagSum_(g: rgen, size: int) -> trow:
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
    RegisterSumTrait(DiagSum)
    if mdformat:
        # print("#", trianglename, ": Sums")
        print("| Trait        |   Seq  |")
        print("| :---         |  :---  |")
        for traitname, trait in SUMTRAIT.items():
            print(f"| {traitname:<12} | {trait(T)} |")
    else:
        for traitname, trait in SUMTRAIT.items():
            print(f'{trianglename + ":" + traitname:<18} {trait(T)}')


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


def PrintTabl(t: tabl) -> None:
    for row in t:
        print(row)


def PrintFlat(t: tabl) -> None:
    print([i for r in t for i in r])


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
    print(f"| Triangle   | {t} |")
    print(f"| RevTabl    | {RevTabl(t)} |")
    print(f"| AntiDiag   | {AntiDiagTabl(t)} |")
    print(f"| AccTabl    | {AccTabl(t)} |")
    print(f"| RevAccTabl | {RevAccTabl(t)} |")
    print(f"| AccRevTabl | {AccRevTabl(t)} |")
    print(f"| DiffxTabl  | {Diffx1Tabl(t)} |")


def PrintTrans(t: tabl) -> None:
    print("| Trans      |   Seq  |")
    print("| :---       |  :---  |")
    print(f"| RowLcm     | {RowLcm(t)} |")
    print(f"| RowGcd     | {RowGcd(t)} |")
    print(f"| RowMax     | {RowMax(t)} |")
    print(f"| CentralE   | {CentralE(t)} |")
    print(f"| CentralO   | {CentralO(t)} |")
    print(f"| ColMiddle  | {ColMiddle(t)} |")
    print(f"| ColLeft    | {ColLeft(t)} |")
    print(f"| ColRight   | {ColRight(t)} |")
    print(f"| BinConv    | {BinConv(t)} |")
    print(f"| InvBinConv | {InvBinConv(t)} |")
    print(f"| TransSqrs  | {TransSqrs(t)} |")
    print(f"| TransNat0  | {TransNat0(t)} |")
    print(f"| TransNat1  | {TransNat1(t)} |")
    print(f"| PosHalf    | {PosHalf(t)} |")
    print(f"| NegHalf    | {NegHalf(t)} |")


def PrintViews(g: tgen, rows: int = 7, verbose: bool = True) -> None:
    print("# " + g.id)
    print(g.sim)
    cols: int = rows
    print()
    T: tabl = g.tab(rows)
    if verbose:
        print(g.id, "Triangle view")
        print()
    PrintRows(T)
    print()
    if verbose:
        print(g.id, "Triangles\n")
    PrintFlats(T)
    print()
    if verbose:
        print(g.id, "Row sums\n")
    PrintSums(T, g.id)
    print()
    if verbose:
        print(g.id, "Transforms\n")
    PrintTrans(T)
    print()
    if verbose:
        print(g.id, "Diagonals as rows\n")
    PrintRowArray(g.gen, rows, cols)
    print()
    if verbose:
        print(g.id, "Diagonals as columns\n")
    PrintColArray(g.gen, rows, cols)
    print()
    if verbose:
        print(g.id, "Polynomial values as rows\n")
    PrintPolyRowArray(g.gen, rows, cols)
    print()
    if verbose:
        print(g.id, "Polynomial values as columns\n")
    PrintPolyColArray(g.gen, rows, cols)
    print()


def PrintProfile(fun: tgen, dim: int = 10) -> None:
    tim: int = dim + dim
    PrintViews(fun, dim)
    V = InvTable(fun, tim)
    if V is not None:
        PrintViews(V, dim)
    r = RevTable(fun, tim)
    PrintViews(r, dim)
    r = RevInvTable(fun, tim)
    if r is not None:
        PrintViews(r, dim)
    r = InvRevTable(fun, tim)
    if r is not None:
        PrintViews(r, dim)


@cache
def abel(n: int) -> list[int]:
    if n == 0:
        return [1]
    b = binomial(n - 1)
    return [b[k - 1] * n ** (n - k) if k > 0 else 0 for k in range(n + 1)]


@MakeTriangle(abel, "Abel", ["A137452", "A061356", "A139526"], True)
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


@MakeTriangle(baxter, "Baxter", ["A359363", "A056939"], False)
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


@MakeTriangle(bell, "Bell", ["A011971", "A011972", "A123346"], False)
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


@MakeTriangle(bessel, "Bessel", ["A132062", "A001497", "A001498", "A122850"], True)
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


@MakeTriangle(
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


@MakeTriangle(
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
def binomialbell(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    a = binomialbell(n - 1) + [1]
    s = sum(a) - 1
    for j in range(n - 2, 0, -1):
        a[j + 1] = (a[j] * (n - 1)) // j
    a[1] = s
    return a


@MakeTriangle(binomialbell, "BinomialBell", ["A056857", "A056860"], True)
def BinomialBell(n: int, k: int) -> int:
    return binomialbell(n)[k]


@cache
def binomialcatalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    a = binomialcatalan(n - 1) + [0]
    row = [0] * (n + 1)
    row[0] = 1
    row[1] = n
    for k in range(2, n + 1):
        row[k] = (a[k] * (n + k + 1) + a[k - 1] * (4 * k - 2)) // (n + 1)
    return row


@MakeTriangle(binomialcatalan, "BinomialCatalan", ["A124644", "A098474"], True)
def BinomialCatalan(n: int, k: int) -> int:
    return binomialcatalan(n)[k]


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


@MakeTriangle(catalan, "Catalan", ["A128899", "A039598"], True)
def Catalan(n: int, k: int) -> int:
    return catalan(n)[k]


@cache
def catalanaer(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return catalanaer(n - 1)[k] if k >= 0 and k < n else 0

    row: list[int] = catalanaer(n - 1) + [1]
    for k in range(0, n):
        row[k] = r(k - 1) + r(k + 1)
    return row


@MakeTriangle(
    catalanaer, "CatalanAer", ["A053121", "A052173", "A112554", "A322378"], True
)
def CatalanAer(n: int, k: int) -> int:
    return catalanaer(n)[k]


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


@MakeTriangle(catalansqr, "CatalanSqr", ["A039599", "A050155"], True)
def CatalanSqr(n: int, k: int) -> int:
    return catalansqr(n)[k]


@cache
def centralcycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = centralcycle(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n + k - 1) * (row[k] + row[k - 1])
    return row


@MakeTriangle(centralcycle, "CentralCycle", ["A269940", "A111999", "A259456"], False)
def CentralCycle(n: int, k: int) -> int:
    return centralcycle(n)[k]


@cache
def centralset(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = centralset(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = k**2 * row[k] + row[k - 1]
    return row


@MakeTriangle(centralset, "CentralSet", ["A269945", "A008957", "A036969"], True)
def CentralSet(n: int, k: int) -> int:
    return centralset(n)[k]


@cache
def chebyshevs(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    rov: list[int] = chebyshevs(n - 2)
    row: list[int] = [0] + chebyshevs(n - 1)
    for k in range(0, n - 1):
        row[k] -= rov[k]
    return row


@MakeTriangle(
    chebyshevs, "ChebyshevS", ["A049310", "A053119", "A112552", "A168561"], True
)
def ChebyshevS(n: int, k: int) -> int:
    return chebyshevs(n)[k]


@cache
def chebyshevt(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    rov: list[int] = chebyshevt(n - 2)
    row: list[int] = [0] + chebyshevt(n - 1)
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] = 2 * row[k] - rov[k]
    return row


@MakeTriangle(chebyshevt, "ChebyshevT", ["A053120", "A039991", "A081265"], True)
def ChebyshevT(n: int, k: int) -> int:
    return chebyshevt(n)[k]


@cache
def chebyshevu(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 2]
    rov: list[int] = chebyshevu(n - 2)
    row: list[int] = [0] + chebyshevu(n - 1)
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] = 2 * row[k] - rov[k]
    return row


@MakeTriangle(chebyshevu, "ChebyshevU", ["A053117", "A053118", "A115322"], True)
def ChebyshevU(n: int, k: int) -> int:
    return chebyshevu(n)[k]


@cache
def ctree(n: int) -> list[int]:
    if n % 2 == 1:
        return [1] * (n + 1)
    return [1, 0] * (n // 2) + [1]


@MakeTriangle(ctree, "ChristTree", ["A106465", "A106470"], True)
def Ctree(n: int, k: int) -> int:
    return ctree(n)[k]


@cache
def composition(n: int) -> list[int]:
    if n == 0:
        return [1]
    cm = compomax(n)
    return [cm[k] - cm[k - 1] if k > 0 else 0 for k in range(n + 1)]


@MakeTriangle(composition, "Composition", ["A048004"], True)
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


@MakeTriangle(compomax, "CompositionMax", ["A126198"], False)
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


@MakeTriangle(delannoy, "Delannoy", ["A008288"], True)
def Delannoy(n: int, k: int) -> int:
    return delannoy(n)[k]


@cache
def divisibility(n: int) -> list[int]:
    if n == 0:
        return [1]
    L = [0 for _ in range(n + 1)]
    L[1] = L[n] = 1
    i = 1
    div = n
    while i < div:
        div, mod = divmod(n, i)
        if mod == 0:
            L[i] = L[div] = 1
        i += 1
    return L


@MakeTriangle(divisibility, "Divisibility", ["A113704", "A051731"], True)
def Divisibility(n: int, k: int) -> int:
    return divisibility(n)[k]


@cache
def _euclid(n: int, k: int) -> int:
    while k != 0:
        t = k
        k = n % k
        n = t
    return 1 if n == 1 else 0


@cache
def euclid(n: int) -> list[int]:
    return [_euclid(i, n) for i in range(n + 1)]


@MakeTriangle(euclid, "Euclid", ["A217831"], False)
def Euclid(n: int, k: int) -> int:
    return euclid(n)[k]


@cache
def euler(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = euler(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * n) // (k)
    row[0] = -sum((-1) ** (j // 2) * row[j] for j in range(n, 0, -2))
    return row


@MakeTriangle(euler, "Euler", ["A247453", "A109449"], True)
def Euler(n: int, k: int) -> int:
    return euler(n)[k]


@cache
def eulerian(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = eulerian(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n - k) * row[k - 1] + (k + 1) * row[k]
    return row


@MakeTriangle(eulerian, "Eulerian", ["A173018", "A008292", "A123125"], False)
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


@MakeTriangle(
    eulerian2, "Eulerian2", ["A340556", "A008517", "A112007", "A163936"], False
)
def Eulerian2(n: int, k: int) -> int:
    return eulerian2(n)[k]


@cache
def eulerianb(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = eulerianb(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = (2 * (n - k) + 1) * row[k - 1] + (2 * k + 1) * row[k]
    return row


@MakeTriangle(eulerianb, "EulerianB", ["A060187", "A138076"], True)
def EulerianB(n: int, k: int) -> int:
    return eulerianb(n)[k]


@cache
def eulersec(n: int) -> list[int]:
    if n == 0:
        return [1]
    b = binomial(n)
    row = [b[k] * eulersec(n - k)[0] if k > 0 else 0 for k in range(n + 1)]
    if n % 2 == 0:
        row[0] = -sum(row[2::2])
    return row


@MakeTriangle(eulersec, "EulerSec", ["A119879", "A081658", "A153641"], True)
def EulerSec(n: int, k: int) -> int:
    return eulersec(n)[k]


def eulerS(n: int) -> int:
    return 0 if n % 2 == 1 else eulersec(n)[0]


@cache
def eulertan(n: int) -> list[int]:
    b = binomial(n)
    row = [b[k] * eulertan(n - k)[0] if k > 0 else 0 for k in range(n + 1)]
    if n % 2 == 1:
        row[0] = -sum(row[2::2]) + 1
    return row


@MakeTriangle(
    eulertan, "EulerTan", ["A162660", "A350972", "A155585", "A009006", "A000182"], False
)
def EulerTan(n: int, k: int) -> int:
    return eulertan(n)[k]


def eulerT(n: int) -> int:
    return 0 if n % 2 == 0 else eulertan(n)[0]


@cache
def fallingfactorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    r: list[int] = fallingfactorial(n - 1)
    row: list[int] = [n * r[k] for k in range(-1, n)]
    row[0] = 1
    return row


@MakeTriangle(
    fallingfactorial,
    "FallingFact",
    ["A008279", "A068424", "A094587", "A173333", "A181511"],
    False,
)
def FallingFactorial(n: int, k: int) -> int:
    return fallingfactorial(n)[k]


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


@MakeTriangle(fibonacci, "Fibonacci", ["A354267", "A105809", "A228074"], False)
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


@MakeTriangle(fubini, "Fubini", ["A131689", "A019538", "A090582", "A278075"], False)
def Fubini(n: int, k: int) -> int:
    return fubini(n)[k]


@cache
def fusscatalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = fusscatalan(n - 1) + [fusscatalan(n - 1)[n - 1]]
    return list(accumulate(row))


@MakeTriangle(fusscatalan, "FussCatalan", ["A355173", "A030237", "A054445"], False)
def FussCatalan(n: int, k: int) -> int:
    return fusscatalan(n)[k]


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


@MakeTriangle(gaussq2, "Gaussq2", ["A022166"], True)
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


@MakeTriangle(genocchi, "Genocchi", ["A297703"], False)
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


@MakeTriangle(harmonic, "Harmonic", ["A358694", "A109822"], True)
def Harmonic(n: int, k: int) -> int:
    return harmonic(n)[k]


@cache
def hermitee(n: int) -> list[int]:
    row: list[int] = [0] * (n + 1)
    row[n] = 1
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (n - k)
    return row


@MakeTriangle(hermitee, "HermiteE", ["A099174", "A066325", "A073278"], True)
def HermiteE(n: int, k: int) -> int:
    return hermitee(n)[k]


@cache
def hermiteh(n: int) -> list[int]:
    row: list[int] = [0] * (n + 1)
    row[n] = 2**n
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (2 * (n - k))
    return row


@MakeTriangle(hermiteh, "HermiteH", ["A060821"], False)
def HermiteH(n: int, k: int) -> int:
    return hermiteh(n)[k]


@cache
def labeledgraphs(n: int) -> list[int]:
    if n == 0:
        return [1]
    s = [
        2 ** (((k - n + 1) * (k - n)) // 2)
        * Binomial(n - 1, k - 1)
        * labeledgraphs(k)[k]
        for k in range(1, n)
    ]
    b = 2 ** (((n - 1) * n) // 2) - sum(s)
    return [0] + s + [b]


@MakeTriangle(labeledgraphs, "LabeledGraphs", ["A360603"], True)
def LabeledGraphs(n: int, k: int) -> int:
    return labeledgraphs(n)[k]


@cache
def laguerre(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + laguerre(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row


@MakeTriangle(laguerre, "Laguerre", ["A021009", "A021010", "A144084"], True)
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


@MakeTriangle(
    lah, "Lah", ["A271703", "A008297", "A066667", "A089231", "A105278", "A111596"], True
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


@MakeTriangle(lehmer, "Lehmer", ["A354794", "A039621"], True)
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


@MakeTriangle(leibniz, "Leibniz", ["A003506"], False)
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


@MakeTriangle(levin, "Levin", ["A356546"], False)
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


@MakeTriangle(lozanic, "Lozanic", ["A034851"], True)
def Lozanic(n: int, k: int) -> int:
    return lozanic(n)[k]


@cache
def moebius(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return -1
    return -sum(moebius(k) for k, i in enumerate(divisibility(n)[: n - 1]) if i != 0)


@cache
def moebiusmat(n: int) -> list[int]:
    if n == 0:
        return [1]
    r = [0 for _ in range(n + 1)]
    r[n] = 1
    for k in range(1, n):
        if n % k == 0:
            r[k] = moebius(n // k)
    return r


@MakeTriangle(moebiusmat, "MoebiusMat", ["A363914", "A054525"], True)
def MoebiusMat(n: int, k: int) -> int:
    return moebiusmat(n)[k]


@cache
def motzkin(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]
    h = 0 if n % 2 else (motzkin(n - 2)[n - 2] * 2 * (n - 1)) // (n // 2 + 1)
    row = motzkin(n - 1) + [h]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row


@MakeTriangle(motzkin, "Motzkin", ["A359364"], False)
def Motzkin(n: int, k: int) -> int:
    return motzkin(n)[k]


@cache
def motzkingf(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return motzkingf(n - 1)[k] if k >= 0 and k < n else 0

    row: list[int] = motzkingf(n - 1) + [1]
    for k in range(0, n):
        row[k] += r(k - 1) + r(k + 1)
    return row


@MakeTriangle(motzkingf, "MotzkinGF", ["A064189", "A026300", "A009766"], True)
def MotzkinGF(n: int, k: int) -> int:
    return motzkingf(n)[k]


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


@MakeTriangle(narayana, "Narayana", ["A090181", "A001263", "A131198"], True)
def Narayana(n: int, k: int) -> int:
    return narayana(n)[k]


@cache
def naturals(n: int) -> list[int]:
    R = range((n * (n + 1)) // 2, ((n + 1) * (n + 2)) // 2)
    return [i + 1 for i in R]


@MakeTriangle(naturals, "Naturals", ["A000027", "A001477"], True)
def Naturals(n: int, k: int) -> int:
    return naturals(n)[k]


@cache
def nicomachus(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = nicomachus(n - 1) + [3 * nicomachus(n - 1)[n - 1]]
    for k in range(0, n):
        row[k] *= 2
    return row


@MakeTriangle(nicomachus, "Nicomachus", ["A036561", "A081954", "A175840"], False)
def Nicomachus(n: int, k: int) -> int:
    return nicomachus(n)[k]


@cache
def one(n: int) -> list[int]:
    if n == 0:
        return [1]
    return one(n - 1) + [1]


@MakeTriangle(one, "One", ["A000012", "A008836", "A014077"], True)
def One(n: int, k: int) -> int:
    return one(n)[k]


@cache
def ordinals(n: int) -> list[int]:
    if n == 0:
        return [0]
    return ordinals(n - 1) + [n]


@MakeTriangle(ordinals, "Ordinals", ["A002262", "A002260", "A004736", "A025581"], False)
def Ordinals(n: int, k: int) -> int:
    return ordinals(n)[k]


@cache
def orderedcycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = orderedcycle(n - 1) + [0]
    row[n] = row[n] * n
    for k in range(n, 0, -1):
        row[k] = (n - 1) * row[k] + k * row[k - 1]
    return row


@MakeTriangle(orderedcycle, "OrderedCycle", ["A225479", "A048594", "A075181"], False)
def OrderedCycle(n: int, k: int) -> int:
    return orderedcycle(n)[k]


@cache
def part(n: int, k: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return 1 if n == 0 else 0
    return part(n - 1, k - 1) + part(n - k, k)


@cache
def partnumexact(n: int) -> list[int]:
    return [part(n, k) for k in range(n + 1)]


@MakeTriangle(partnumexact, "Partition", ["A072233", "A008284", "A058398"], True)
def PartnumExact(n: int, k: int) -> int:
    return partnumexact(n)[k]


@cache
def _pdist(n: int, k: int, r: int) -> int:
    if n == 0:
        return 1 if k == 0 else 0
    if k == 0 or r == 0:
        return 0
    return sum(_pdist(n - r * j, k - 1, r - 1) for j in range(1, n // r + 1)) + _pdist(
        n, k, r - 1
    )


@cache
def partnumdist(n) -> list[int]:
    return [_pdist(n, k, n) for k in range(n + 1)]


@MakeTriangle(partnumdist, "PartitionDist", ["A365676", "A116608", "A060177"], False)
def PartnumDist(n: int, k: int) -> int:
    return partnumdist(n)[k]


@cache
def partnummax(n: int) -> list[int]:
    return list(accumulate(partnumexact(n)))


@MakeTriangle(partnummax, "PartitionMax", ["A026820"], False)
def PartnumMax(n: int, k: int) -> int:
    return partnummax(n)[k]


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


@MakeTriangle(
    polygonal, "Polygonal", ["A139600", "A057145", "A134394", "A139601"], False
)
def Polygonal(n: int, k: int) -> int:
    return polygonal(n)[k]


@cache
def powlaguerre(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = powlaguerre(n - 1) + [1]
    row[0] = row[n] = row[0] * n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@MakeTriangle(powlaguerre, "PowLaguerre", ["A196347", "A021012"], False)
def PowLaguerre(n: int, k: int) -> int:
    return powlaguerre(n)[k]


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


@MakeTriangle(rencontres, "Rencontres", ["A008290", "A098825"], True)
def Rencontres(n: int, k: int) -> int:
    return rencontres(n)[k]


@cache
def risingfactorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + risingfactorial(n - 1)
    for k in range(0, n):
        row[k] += (n - k) * row[k + 1]
    return row


@MakeTriangle(
    risingfactorial,
    "RisingFact",
    ["A008279", "A068424", "A094587", "A173333", "A181511"],
    True,
)
def RisingFactorial(n: int, k: int) -> int:
    return risingfactorial(n)[k]


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


@MakeTriangle(
    schroeder,
    "Schroeder",
    ["A122538", "A033877", "A080245", "A080247", "A106579"],
    True,
)
def Schroeder(n: int, k: int) -> int:
    return schroeder(n)[k]


@cache
def schroederpaths(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = schroederpaths(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * (2 * n - k)) // k
    row[0] = (row[0] * (4 * n - 2)) // n
    return row


@MakeTriangle(schroederpaths, "SchroederP", ["A104684", "A063007"], True)
def SchroederPaths(n: int, k: int) -> int:
    return schroederpaths(n)[k]


@cache
def schroederl(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    arow: list[int] = schroederl(n - 1) + [0]
    row: list[int] = schroederl(n - 1) + [1]
    row[0] = row[0] + 2 * row[1]
    for k in range(1, n):
        row[k] = arow[k - 1] + 3 * arow[k] + 2 * arow[k + 1]
    return row


@MakeTriangle(schroederl, "SchroederL", ["A172094"], True)
def SchroederL(n: int, k: int) -> int:
    return schroederl(n)[k]


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


@MakeTriangle(seidel, "Seidel", ["A008281", "A008282", "A010094"], False)
def Seidel(n: int, k: int) -> int:
    return seidel(n)[k]


def seidelboust(n: int) -> list[int]:
    return seidel(n) if n % 2 else seidel(n)[::-1]


@MakeTriangle(
    seidelboust, "SeidelBoust", ["A008280", "A108040", "A236935", "A239005"], False
)
def SeidelBoust(n: int, k: int) -> int:
    return seidelboust(n)[k]


@cache
def sierpinski(n: int) -> list[int]:
    return [int(not ~n & k) for k in range(n + 1)]


@MakeTriangle(
    sierpinski,
    "Sierpinski",
    ["A047999", "A090971", "A114700", "A143200", "A166282"],
    True,
)
def Sierpinski(n: int, k: int) -> int:
    return sierpinski(n)[k]


@cache
def stirlingcycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + stirlingcycle(n - 1)
    for k in range(1, n):
        row[k] = row[k] + (n - 1) * row[k + 1]
    return row


@MakeTriangle(
    stirlingcycle,
    "StirlingCyc",
    ["A132393", "A008275", "A008276", "A048994", "A054654", "A094638", "A130534"],
    True,
)
def StirlingCycle(n: int, k: int) -> int:
    return stirlingcycle(n)[k]


@cache
def stirlingcycle2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]
    rov: list[int] = stirlingcycle2(n - 2)
    row: list[int] = stirlingcycle2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * (rov[k - 1] + row[k])
    return row


@MakeTriangle(stirlingcycle2, "StirlingCyc2", ["A358622", "A008306", "A106828"], False)
def StirlingCycle2(n: int, k: int) -> int:
    return stirlingcycle2(n)[k]


@cache
def stirlingcycleb(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = stirlingcycleb(n - 1) + [1]
    m = 2 * n - 1
    for k in range(n - 1, 0, -1):
        row[k] = m * row[k] + row[k - 1]
    row[0] *= m
    return row


@MakeTriangle(
    stirlingcycleb, "StirlingCycB", ["A028338", "A039757", "A039758", "A109692"], True
)
def StirlingCycleB(n: int, k: int) -> int:
    return stirlingcycleb(n)[k]


@cache
def stirlingset(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + stirlingset(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row


@MakeTriangle(
    stirlingset,
    "StirlingSet",
    [
        "A048993",
        "A008277",
        "A008278",
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
    return stirlingset(n)[k]


@cache
def stirlingset2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]
    rov: list[int] = stirlingset2(n - 2)
    row: list[int] = stirlingset2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * rov[k - 1] + k * row[k]
    return row


@MakeTriangle(stirlingset2, "StirlingSet2", ["A358623", "A008299", "A137375"], False)
def StirlingSet2(n: int, k: int) -> int:
    return stirlingset2(n)[k]


@cache
def stirlingsetb(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    pow: list[int] = stirlingsetb(n - 1)
    row: list[int] = stirlingsetb(n - 1) + [1]
    row[0] += 2 * row[1]
    for k in range(1, n - 1):
        row[k] = 2 * (k + 1) * pow[k + 1] + (2 * k + 1) * pow[k] + pow[k - 1]
    row[n - 1] = (2 * n - 1) * pow[n - 1] + pow[n - 2]
    return row


@MakeTriangle(stirlingsetb, "StirlingSetB", ["A154602"], True)
def StirlingSetB(n: int, k: int) -> int:
    return stirlingsetb(n)[k]


@cache
def sylvester(n: int) -> list[int]:
    def s(n: int, k: int) -> int:
        return sum(
            Binomial(n, k - j) * StirlingCycle(n - k + j, j) for j in range(k + 1)
        )

    return [s(n, k) for k in range(n + 1)]


@MakeTriangle(sylvester, "Sylvester", ["A341101"], False)
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


@MakeTriangle(sympoly, "SymPoly", ["A165675", "A093905", "A105954", "A165674"], True)
def SymPoly(n: int, k: int) -> int:
    return sympoly(n)[k]


@cache
def ternarytree(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = ternarytree(n - 1) + [ternarytree(n - 1)[n - 1]]
    return list(accumulate(accumulate(row)))


@MakeTriangle(ternarytree, "TernaryTrees", ["A355172"], False)
def TernaryTree(n: int, k: int) -> int:
    return ternarytree(n)[k]


@cache
def wardset(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = wardset(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k] + (n + k - 1) * row[k - 1]
    return row


@MakeTriangle(wardset, "WardSet", ["A269939", "A134991"], False)
def WardSet(n: int, k: int) -> int:
    return wardset(n)[k]


@cache
def worpitzky(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = worpitzky(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k - 1] + (k + 1) * row[k]
    return row


@MakeTriangle(
    worpitzky,
    "Worpitzky",
    ["A028246", "A053440", "A075263", "A130850", "A163626"],
    False,
)
def Worpitzky(n: int, k: int) -> int:
    return worpitzky(n)[k]


@cache
def zarankiewicz(n: int) -> list[int]:
    def s(n: int):
        return (1 + n // 2) * (1 + (n + 1) // 2)

    sn = s(n)
    return [sn * s(k) for k in range(n + 1)]


@MakeTriangle(
    zarankiewicz,
    "Zarankiewicz",
    ["A298368"],
    False,
)
def Zarankiewicz(n: int, k: int) -> int:
    return zarankiewicz(n)[k]


def bell_num(n: int) -> int:
    if n == 0:
        return 1
    return bell(n - 1)[-1]


def Bernoulli(n: int) -> frac:
    if n < 2:
        return frac(1, n + 1)
    if n % 2 == 1:
        return frac(0, 1)
    g = genocchi(n // 2 - 1)[-1]
    f = frac(g, 2 ** (n + 1) - 2)
    return -f if n % 4 == 0 else f


def euler_num(n: int) -> int:
    return euler(n)[0]


@cache
def eulerphi(n: int) -> int:
    return sum(k * moebiusmat(n)[k] for k in range(n + 1))


def motzkin_num(n: int) -> int:
    return sum(motzkin(n))


def partlist_num(n: int) -> int:
    return sum(lah(n))


def part_num(n: int) -> int:
    return sum(partnumexact(n))


def riordan_num(n: int) -> int:
    return sum((-1) ** (n - k) * BinomialCatalan(n, k) for k in range(n + 1))


tabl_fun: list[tgen] = [
    Abel,
    Baxter,
    Bell,
    Bessel,
    Bessel2,
    Binomial,
    BinomialBell,
    BinomialCatalan,
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
    Divisibility,
    Euclid,
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
    LabeledGraphs,
    Laguerre,
    Lah,
    Lehmer,
    Leibniz,
    Levin,
    Lozanic,
    MoebiusMat,
    Motzkin,
    MotzkinGF,
    Narayana,
    Naturals,
    Nicomachus,
    One,
    Ordinals,
    OrderedCycle,
    PartnumExact,
    PartnumDist,
    PartnumMax,
    Polygonal,
    PowLaguerre,
    Rencontres,
    RisingFactorial,
    Schroeder,
    SchroederL,
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
    SymPoly,
    TernaryTree,
    WardSet,
    Worpitzky,
    Zarankiewicz,
]
readme_header = """
*** La sélection du Chef ***
INTEGER SEQUENCES ARE ONLY THE SHADOWS OF INTEGER TRIANGLES
Python implementations of integer sequences dubbed tabl in the OEIS.
The notebook gives a first introduction for the user.
"""


def CrossReferences(name: str = "README.md") -> None:
    """Writes the crossreferences as a md-table to the root."""
    path = GetRoot(name)
    with open(path, "w+", encoding="utf-8") as xrefs:
        xrefs.write(readme_header)
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
                f"| [{id}](https://github.com/PeterLuschny/tabl/blob/main/data/md/{id}.tbl.md) | [source](https://github.com/PeterLuschny/tabl/blob/main/src/{id}.py) | [traits](https://luschny.de/math/oeis/{id}.html) | [{s}](https://oeis.org/search?q={anum}) |\n"
            )
    print("Info: 'README.md' written to the root folder.")


def SaveExtendedTables(dim: int = 10) -> None:
    tim: int = dim + dim
    for fun in tabl_fun:
        tablpath = GetDataPath(fun.id + ".tbl", "md")
        with open(tablpath, "w+") as dest:
            with contextlib.redirect_stdout(dest):
                PrintViews(fun, dim)
                V = InvTable(fun, tim)
                if V is not None:
                    PrintViews(V, dim)
                r = RevTable(fun, tim)
                PrintViews(r, dim)
                r = RevInvTable(fun, tim)
                if r is not None:
                    PrintViews(r, dim)
                r = InvRevTable(fun, tim)
                if r is not None:
                    PrintViews(r, dim)
    print("Info: Extended tables written to the data/md folder as 'name.tbl.md'.")


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
    "#rcor1 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 60px; height: 0px;} ",
    "#rcor2 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 60px; height: 0px;} ",
    "#rcor3 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 66px; height: 0px;} ",
    "#rcor4 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 880px; height: 20px; font-weight: 700; text-align: center;} ",
    ".center {margin-top: 1em;} ",
    ".type { font-weight: 600; text-align: center;} ",
    ".tooltip { position: relative; font-weight: 600; text-align: center;} ",
    ".tooltip .formula { visibility: hidden; width: 200px; background-color: lightgray; text-align: center; border-radius: 6px; padding: 5px 0; position: absolute; z-index: 1; top: +2px; left: 95%;} ",
    ".tooltip:hover .formula { visibility: visible; } ",
    "</style></head><body>",
]
Table = [
    "<table class='sortable'><thead><tr>",
    "<th id='rcor1'>&#8597; Type</th>",
    "<th id='rcor2'>&#8597; Trait</th>",
    "<th id='rcor3'>&#8597; Anum</th>",
    "<th id='rcor4'>&#8597; Sequence</th>",
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
        s += f"[{n}] " + str(fun.gen(n)).replace("[", "").replace("]", "") + "<br>"
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
        f"<td {rc};><a style='color:white' href='https://github.com/PeterLuschny/tabl/blob/main/data/md/{fun.id}.tbl.md'>Table</a></td>"
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


def CsvToHtml(fun: tgen) -> None:
    name = fun.id
    csvfile = GetDataPath(name, "csv")
    outfile = GetDataPath(name, "html")
    FORMULA = Formulas()
    with open(csvfile, "r") as csvfile:
        reader = csv.reader(csvfile)
        with open(outfile, "w+") as outfile:
            for h in Header:
                outfile.write(h)
            outfile.write(f"<title>{name} : IntegerTriangles.py</title>")
            for h in CSS:
                outfile.write(h)
            h = next(reader)  # column names
            sim = str(fun.sim).replace("'", "").replace("[", "").replace("]", "")
            outfile.write(
                "<div class='tooltip' style='border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 160px; height: 20px; font-weight: 700; text-align: center;'>"
            )
            outfile.write(
                f"{name.upper()}<span class='formula' style=' background: #73AD21; font-weight:600; width: 220px;'>{HtmlTriangle(fun)}</span></div>"
            )
            outfile.write(
                f"<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OEIS Similars: {sim}\n</p>"
            )
            for h in Table:
                outfile.write(h)
            for line in reader:
                # Layout: index,triangle,trait,anum,seq
                # 0,Abel:Std,Triangle,A137452,1 0 1 0 ...
                # index = line[0]
                h = line[1]
                type = h[h.index(":") + 1 :]
                trait = line[2]
                anum = line[3]
                seq = line[4]
                outfile.write(f"<tr><td class='type'>{type}</td>")
                tip = FORMULA[trait]
                outfile.write(
                    f"<td class='tooltip'>{trait}<span class='formula'>{tip}</span></td>"
                )
                sseq = (seq.split(" ", 3)[3]).replace(" ", ",")
                if anum == "missing":
                    color = "rgb(127, 0, 255)"
                    url = f"https://oeis.org/search?q={sseq}"
                    outfile.write(
                        f"<td><a href='{url}' target='_blank'>missing</a></td>"
                    )
                elif anum == "variant":
                    color = "rgb(167, 199, 231)"
                    url = f"https://oeis.org/search?q={sseq}"
                    outfile.write(
                        f"<td><a href='{url}' target='_blank'>variant</a></td>"
                    )
                else:
                    color = "rgb(0, 0, 255)"
                    outfile.write(
                        f"<td><a href='https://oeis.org/{anum}' target='_blank'>{anum}</a></td>"
                    )
                # seq
                outfile.write(
                    f"<td style='font-family:Consolas;color:{color}'>{seq}</td></tr>"
                )
            outfile.write("</tbody></table>")
            for h in navbar(fun):
                outfile.write(h)
            for h in Footer:
                outfile.write(h)
            for h in SCRIPT:
                outfile.write(h)


def AllCsvToHtml() -> None:
    for fun in tabl_fun:
        print(f"Info: Generating data/html/{fun.id}.html.")
        CsvToHtml(fun)


def is_tabletrait(f: Callable):
    sig = signature(f)
    ann = list(sig.parameters.values())[0].annotation
    return ann == list[list[int]]


def RegisterTraits() -> dict[str, Callable]:
    TRAITS: dict[str, Callable] = {}

    def RegisterTrait(f: Callable):
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
    FORMULA["DiagSum"] = "&sum;<sub> k=0..n // 2 </sub> T(n - k, k)"
    FORMULA["AccSum"] = "&sum;<sub> k=0..n </sub>&sum;<sub> j=0..k </sub> T(n, j)"
    FORMULA[
        "AccRevSum"
    ] = "&sum;<sub> k=0..n </sub>&sum;<sub> j=0..k </sub> T(n, n - j)"
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


def IsInOEIS(seq: list[int]) -> bool:
    """
    Args:
        seq (list[int]): sequence
    Returns:
        bool: found?
    """
    strseq = SeqString(seq, 160)
    url = f"https://oeis.org/search?q={strseq}&fmt=json"
    for _ in range(1, 4):
        time.sleep(4)  # give the OEIS server some time to relax
        try:
            with urllib.request.urlopen(url) as response:
                page = response.read()
                # If "count": 0 exists then 'find' returns a value >= 0,
                # that means that no sequence was found.
                # Otherwise 'find' returns -1, that means that
                # a substring similar to the sequence was found.
                return -1 == page.find(b'"count": 0')
        except urllib.error.HTTPError as he:
            print(he.__dict__)
        except urllib.error.URLError as ue:
            print(ue.__dict__)

    raise Exception(f"Could not open {url}.")


def fnv(data: bytes) -> int:
    """
    FNV-1a hash algorithm.
    """
    # assert isinstance(data, bytes)
    hval = 0xCBF29CE484222325
    for byte in data:
        hval = hval ^ byte
        hval = (hval * 0x100000001B3) % 0x10000000000000000
    return hval


MINTERMS = 15


def fnv_hash(seq: list[int], absolut: bool = False) -> str:
    """Returns the fnv-hash of an integer sequence based on the first MINTERMS terms.
    Args:
        seq (list[int]):
        absolut (bool, optional): Take the absolute value of the terms? Defaults to False.
    Returns:
        str: The hex value of the hash without the '0x'-head.
    """
    if len(seq) < MINTERMS:
        print(f"*** Warning *** Hash based only on {len(seq)} terms.")
        if seq == []:
            return "0"
    if absolut:
        s = str([abs(i) for i in seq[0:MINTERMS]])
    else:
        s = str(seq[0:MINTERMS])
    x = s.translate(str.maketrans("", "", "[],"))
    return hex(fnv(bytes(x, encoding="ascii")))[2:]


def GetCompressed() -> None:
    oeisstripped = "https://oeis.org/stripped.gz"
    r = requests.get(oeisstripped, stream=True)
    with open(strippedpath, "wb") as local:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                local.write(chunk)
    with gzip.open(strippedpath, "rb") as gz:
        with open(GetDataPath("oeis", "csv"), "wb") as da:
            da.write(gz.read())
    print("Info: OEIS-data saved as oeis.csv in data/csv.")


def MakeOeisminiWithFnv() -> None:
    """Make all terms absolute, take MINTERMS terms, add fnv."""
    with open(GetDataPath("oeis", "csv"), "r") as oeisdata:
        reader = csv.reader(oeisdata)
        with open(GetDataPath("oeismini", "csv"), "w") as minidata:
            #    A000003 ,1
            seq_list = [
                [txt[0][0:7], [abs(int(s)) for s in txt[1:-1]]] for txt in reader
            ]
            for s in seq_list:
                if len(s[1]) < MINTERMS:
                    continue
                x = str(s[1][0:MINTERMS]).translate(str.maketrans("", "", "[],"))
                f = hex(fnv(bytes(x, encoding="ascii")))[2:]
                minidata.write(f + "," + s[0] + "," + x + ",\n")
    print("Info: Hashed OEIS-data saved as oeismini.csv in data/csv.")


def OeisToSql() -> None:
    """Make all terms absolute, take MINTERMS terms, add fnv.
    Write (fnv, anum, seq) to oeis.db.
    """
    tabl = sqlite3.connect(GetDataPath("oeismini", "db"))
    cur = tabl.cursor()
    sql = "CREATE TABLE sequences(hash, anum, seq)"
    cur.execute(sql)
    with open(GetDataPath("oeis", "csv"), "r") as oeisdata:
        reader = csv.reader(oeisdata)
        seq_list = [[txt[0][0:7], [abs(int(s)) for s in txt[1:-1]]] for txt in reader]
        for s in seq_list:
            if len(s[1]) < MINTERMS:
                continue
            x = str(s[1][0:MINTERMS]).translate(str.maketrans("", "", "[],"))
            f = hex(fnv(bytes(x, encoding="ascii")))[2:]
            tup = (f, s[0], x)
            sql = "INSERT INTO sequences VALUES(?, ?, ?)"
            cur.execute(sql, tup)
    tabl.commit()
    tabl.close()
    print("Info: Database oeismini.db saved in data/db.")


def QueryDBhash(H: str, oeis_cur: sqlite3.Cursor) -> str:
    """_summary_
    Args:
        H (str): hash
        oeis_cur (OEISCursor): _description_
    Returns:
        str: _description_
    """
    sql = "SELECT anum FROM sequences WHERE hash=? LIMIT 1"
    res = oeis_cur.execute(sql, (H,))
    record = res.fetchone()
    return "missing" if record is None else record[0]


def QueryDBstr(seq: list[int], oeis_cur: sqlite3.Cursor) -> str:
    """_summary_
    Args:
        seq (list[int]): _description_
        oeis_cur (_type_): _description_
    Returns:
        str: _description_
    """
    x = str([abs(int(s)) for s in seq[0:MINTERMS]]).translate(
        str.maketrans("", "", "[],")
    )
    sql = "SELECT anum FROM sequences WHERE seq=? LIMIT 1"
    res = oeis_cur.execute(sql, (x,))
    record = res.fetchone()
    return "missing" if record is None else record[0]


def QueryMiniOeis(H: str, seq: list[int], oeis_cur: sqlite3.Cursor) -> str:
    """Query oeis_mini db only.
    Args:
        H (str): _description_
        seq (list[int]): _description_
        oeis_cur (SQLCursor): _description_
    Returns:
        str: _description_
    """
    sql = "SELECT anum FROM sequences WHERE hash=? LIMIT 1"
    res = oeis_cur.execute(sql, (H,))
    record = res.fetchone()
    if record is not None:
        return record[0]
    # not found by hash, perhaps shifted by one?
    H = fnv_hash(seq[1 : MINTERMS + 1], True)
    res = oeis_cur.execute(sql, (H,))
    record = res.fetchone()
    return "missing" if record is None else record[0]


def QueryOeis(H: str, seq: list[int], oeis_cur: sqlite3.Cursor) -> str:
    """First query oeis_mini (local),
       if nothing found query OEIS (internet).
    Args:
        H (str): _description_
        seq (list[int]): _description_
        oeis_cur (SQLCursor): _description_
    Returns:
        str: _description_
    """
    rec = QueryMiniOeis(H, seq, oeis_cur)
    if rec != "missing":
        return rec
    if IsInOEIS(seq):
        return "variant"
    else:
        return "missing"


def GetType(name: str) -> str:
    # There are 6 types:
    # ["", "Std", "Rev", "Inv", "Rev:Inv", "Inv:Rev"]
    sp = name.split(":", 1)
    if len(sp) == 1:
        return ""
    return name.split(":", 1)[1]


def CreateTable(name: str) -> str:
    return f"CREATE TABLE {name}(triangle, type, trait, anum, hash, seq)"


def InsertTable(name: str) -> str:
    return f"INSERT INTO {name} VALUES(?, ?, ?, ?, ?, ?)"


def GetMaxStrLen() -> int:
    return 100


def SaveTraits(
    g: tgen,
    size: int,
    traits_cur: sqlite3.Cursor,
    oeis_cur: sqlite3.Cursor,
    table: str,
    TRAITS: dict,
) -> None:
    """Warning: uses internet!
    Args:
        g : _description_
        size : _description_
        traits_cur : _description_
        oeis_cur : _description_
        table : _description_
        TRAITS : _description_
    """
    T = g.tab(size)
    r = g.gen
    triname = g.id
    trityp = GetType(triname)
    for traitname, trait in TRAITS.items():
        if trityp == traitname:
            # print("Skiped:", triname, trityp, traitname)
            continue
        seq = trait(T) if is_tabletrait(trait) else trait(r, size)
        if seq == []:
            print(f"Info: {triname} -> {traitname} does not exist.")
            continue
        hash = fnv_hash(seq, True)
        ###################### The undocumented switch.
        # Much faster in the local version, but no OEIS check.
        # anum = queryminioeis(hash, seq, oeis_cur)  # local
        anum = QueryOeis(hash, seq, oeis_cur)  # with internet
        seqstr = ""
        maxl = 0
        for trm in seq:
            s = str(trm) + " "
            maxl += len(s)
            if maxl > GetMaxStrLen():
                break
            seqstr += s
        tup = (triname, trityp, traitname, anum, hash, seqstr)
        # print(tup)
        sql = InsertTable(table)
        traits_cur.execute(sql, tup)


def SaveExtendedTraitsToDB(
    t: tgen, size: int, traits_cur: sqlite3.Cursor, oeis_cur: sqlite3.Cursor, table: str
) -> None:
    """Warning: uses internet!
    Args:
        t (tgen): _description_
        size (int): _description_
        traits_cur (_type_): _description_
        oeis_cur (_type_): _description_
        table (_type_): _description_
    """
    tim: int = size + size // 2
    Tid = t.id
    t.id = t.id + ":Std"
    TRAITS = RegisterTraits()
    thash = fnv_hash(t.tab(MINTERMS))
    SaveTraits(t, size, traits_cur, oeis_cur, table, TRAITS)
    t.id = Tid
    r = RevTable(t, tim)
    rhash = fnv_hash(r.tab(MINTERMS))
    if thash != rhash:
        SaveTraits(r, size, traits_cur, oeis_cur, table, TRAITS)
        # ir = InvRevTable(t, tim)
        ir = InvTable(r, tim)
        if ir is not None:
            SaveTraits(ir, size, traits_cur, oeis_cur, table, TRAITS)
    i = InvTable(t, tim)
    ihash = "0"
    if i is not None:
        ihash = fnv_hash(i.tab(MINTERMS))
        SaveTraits(i, size, traits_cur, oeis_cur, table, TRAITS)
        # ri = RevInvTable(t, tim)
        ri = RevTable(i, tim)
        if ri is not None:
            rihash = fnv_hash(ri.tab(MINTERMS))
            if ihash != rihash:
                SaveTraits(ri, size, traits_cur, oeis_cur, table, TRAITS)


def SaveTraitsToDB(fun: tgen) -> None:
    """Warning: uses internet!"""
    name = fun.id
    with sqlite3.connect(GetDataPath(name, "db")) as db:
        traits_cur = db.cursor()
        traits_cur.execute(CreateTable(name))
        with sqlite3.connect(GetDataPath("oeismini", "db")) as oeis:
            oeis_cur = oeis.cursor()
            SaveExtendedTraitsToDB(fun, 32, traits_cur, oeis_cur, name)
        db.commit()
    print(f"Info: Created database {name}.db in data/db.")


def ConvertDBtoCSVandMD(dbpath: Path, funname: str) -> int:
    size = 0
    with sqlite3.connect(dbpath) as db:
        cursor = db.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor.execute(sql)
        tables = cursor.fetchall()
        for table_name in tables:
            table_name = table_name[0]
            sql = f"""SELECT triangle, trait, anum, seq
                      FROM {table_name}
                      WHERE anum != 'A000012'
                      AND anum != 'A000007'
                      AND anum != 'A000004' """
            table = pd.read_sql_query(sql, db)
            table.to_csv(GetDataPath(table_name, "csv"), index_label="index")
            table.to_markdown(GetDataPath(table_name, "md"))
            size = table.size // 4
        cursor.close()
    print(f"Info: Created data/csv/{funname}.csv and data/md/{funname}.md.")
    return size


def SaveAllTraitsToDBandCSVandMD(tabl_fun: list[tgen]) -> None:
    """Warning: uses internet!"""
    for fun in tabl_fun:
        SaveTraitsToDB(fun)
        ConvertDBtoCSVandMD(GetDataPath(fun.id, "db"), fun.id)
    return


def MergeDBs(tablfun: list[tgen]):
    destname = "traits"
    destpath = GetDataPath(destname, "db")
    with sqlite3.connect(destpath) as dest:
        dest_cursor = dest.cursor()
        dest_cursor.execute(CreateTable(destname))
        for src in tablfun:
            srcpath = GetDataPath(src.id, "db")
            with sqlite3.connect(srcpath) as src:
                src_cursor = src.cursor()
                sql = "SELECT name FROM sqlite_master WHERE type='table';"
                src_cursor.execute(sql)
                tables = src_cursor.fetchall()
                for table_name in tables:
                    table_name = table_name[0]
                    print(table_name)
                    sql = f"SELECT * FROM {table_name}"
                    res = src_cursor.execute(sql)
                    trs = res.fetchall()
                    sql = InsertTable(destname)
                    dest_cursor.executemany(sql, trs)
                src_cursor.close()
        dest.commit()
        dest_cursor.close()
    print("Info: Created database traits.db in data/db.")
