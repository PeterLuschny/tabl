from typing import Callable, TypeAlias
from tablinverse import InverseTriangle

# #@

"""Type: table row"""
trow: TypeAlias = list[int]

"""Type: table"""
tabl: TypeAlias = list[list[int]]

"""Type: sequence generator"""
seq: TypeAlias = Callable[[int], int]

"""Type: row generator"""
rgen: TypeAlias = Callable[[int], trow]

"""Type: table generator"""
tgen: TypeAlias = Callable[[int], tabl]

"""Type: triangle"""
tri: TypeAlias = Callable[[int, int], trow | int]


def set_attributes(r: rgen, id: str, vert: bool=False) -> Callable[[tri], tri]:

    def maketab(dim: int) -> tabl:
        return [list(r(n)) for n in range(dim)]

    def makerev(dim: int) -> tabl:
        return [list(reversed(r(n))) for n in range(dim)]

    def makemat(dim: int) -> tabl:
        return [[r(n)[k] if k <= n else 0 for k in range(dim)] for n in range(dim)]

    def makeinv(dim: int) -> tabl:
        if not vert: return []
        return InverseTriangle(r, dim)

    def wrapper(f: tri) -> tri:
        f.tab = maketab
        f.rev = makerev
        f.mat = makemat
        f.inv = makeinv
        f.id = id
        return f
    return wrapper


def inversion_wrapper(T: tri, dim: int) -> tri | None:

    t = T.inv(dim)
    if t == []: return None
    def _psgen(n: int) -> trow: return list(t[n])

    @set_attributes(_psgen, T.id + "|INV", True)
    def psgen(n: int, k: int = -1) -> list[int] | int:
        if k == -1: return _psgen(n)
        return _psgen(n)[k]

    return psgen


def reversion_wrapper(T: tri, dim: int) -> tri:

    t = T.rev(dim)
    def _rsgen(n: int) -> trow: return list(t[n]) 

    @set_attributes(_rsgen, T.id + "|REV", True)
    def rsgen(n: int, k: int = -1) -> list[int] | int:
        if k == -1: return _rsgen(n)
        return _rsgen(n)[k]

    return rsgen

def revinv_wrapper(T: tri, dim: int) -> tri | None:

    I = inversion_wrapper(T, dim)
    if I == None: return None
    T = reversion_wrapper(I, dim)

    def _rigen(n: int) -> trow: return list(T(n))

    @set_attributes(_rigen, T.id + "|INV|REV", True)
    def rigen(n: int, k: int = -1) -> list[int] | int:
        if k == -1: return _rigen(n)
        return _rigen(n)[k]

    return rigen

def invrev_wrapper(T: tri, dim: int) -> tri | None:

    R = reversion_wrapper(T, dim)
    T = inversion_wrapper(R, dim)
    if T == None: return None

    def _tigen(n: int) -> trow: return list(T(n))

    @set_attributes(_tigen, T.id + "|REV|INV", True)
    def tigen(n: int, k: int = -1) -> list[int] | int:
        if k == -1: return _tigen(n)
        return _tigen(n)[k]

    return tigen


if __name__ == "__main__":
    from Abel import abel
    from Laguerre import laguerre

    f = laguerre
    dim = 6

    T = f.tab(dim)
    print("TRI    ", T)

    i = reversion_wrapper(f, dim)
    T = i.tab(dim)
    print("REV    ", T)

    i = inversion_wrapper(f, dim)
    if i != None:
        T = i.tab(dim)
        print("INV    ", T)

    i = revinv_wrapper(f, dim)
    if i != None:
        T = i.tab(dim)
        print("INV|REV", T)

    i = invrev_wrapper(f, dim)
    if i != None:
        T = i.tab(dim)
        print("REV|INV", T)
