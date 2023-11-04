from typing import Callable
from fractions import Fraction as frac
from _tabltypes import rgen, tgen, tabl, trow

# #@


def PolyEval_(g: rgen, n: int, x: int) -> int:
    row = g(n)
    return sum(c * (x ** j) for (j, c) in enumerate(row))


def PolyEval(T: tabl, n: int, x: int) -> int:
    return sum(T[n][k] * (x ** k) for k in range(n + 1))


def PolyRow(g: rgen, size: int, row: int) -> trow:
    return [PolyEval_(g, row, x) for x in range(size)]


def PolyRow0(g: rgen, size: int) -> trow: return PolyRow(g, size, 0)
def PolyRow1(g: rgen, size: int) -> trow: return PolyRow(g, size, 1)
def PolyRow2(g: rgen, size: int) -> trow: return PolyRow(g, size, 2)
def PolyRow3(g: rgen, size: int) -> trow: return PolyRow(g, size, 3)


def PolyCol(g: rgen, size: int, col: int) -> trow:
    return [PolyEval_(g, k, col) for k in range(size)]


def PolyCol0(g: rgen, size: int) -> trow: return PolyCol(g, size, 0)
def PolyCol1(g: rgen, size: int) -> trow: return PolyCol(g, size, 1)
def PolyCol2(g: rgen, size: int) -> trow: return PolyCol(g, size, 2)
def PolyCol3(g: rgen, size: int) -> trow: return PolyCol(g, size, 3)


def PolyDiag(g: rgen, size: int) -> trow:
    return [PolyEval_(g, n, n) for n in range(size)]


def AntiDiagPoly(g: rgen, n: int) -> trow:
    return [PolyEval_(g, n - k, k) for k in range(n + 1)]


def PolyDiagTabl(g: rgen, size: int) -> tabl:
    return [AntiDiagPoly(g, n) for n in range(size)]


def Poly(g: rgen, size: int) -> trow:
    return [i for row in PolyDiagTabl(g, size) for i in row]


def PolyFrac(T: tabl, x: frac) -> list[frac | int]:
    return [sum(c * (x ** k) for (k, c) in enumerate(row)) for row in T]


def PosHalf_(g: rgen, size: int) -> trow:
    T = [g(n) for n in range(size)]
    R = PolyFrac(T, frac(1, 2))
    return [((2 ** n) * r).numerator for n, r in enumerate(R)]


def PosHalf(T: tabl) -> trow:
    R = PolyFrac(T, frac(1, 2))
    return [((2 ** n) * r).numerator for n, r in enumerate(R)]


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
            print(f'| {traitname:<8} | {trait(gen, size)} |')
        print()
    else:
        for traitname, trait in POLYTRAIT.items():
            print(f'{trianglename+":"+traitname:<14} {trait(gen, size)}')


if __name__ == "__main__":

    from Abel import Abel
    from Bell import Bell

    PrintPolys(Abel)
    # PrintPolys(Bell, 6, False)

    print(PolyDiag(Abel.gen, 8))
    print(PolyDiagTabl(Abel.gen, 8))
    print(Poly(Abel.gen, 8))
