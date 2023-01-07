from typing import Callable, TypeAlias
from _tablinverse import InverseTriangle, InverseTabl

# #@

# T ENUMERATED AS A TRIANGLE
#
# T(0,0)
# T(1,0)  T(1,1)
# T(2,0)  T(2,1)  T(2,2)
# T(3,0)  T(3,1)  T(3,2)  T(3,3)
# T(4,0)  T(4,1)  T(4,2)  T(4,3)  T(4,4)
# T(5,0)  T(5,1)  T(5,2)  T(5,3)  T(5,4)  T(5,5)
#
# A subtriangle of the standard triangle T as indexed above
# is given by a new root node [N, K].
# For some dimension dim > 0 it is defined as
# T[N, K, dim] = [[T(n, k) for k in range(K, K - N + n + 1)] for n in range(N, N + dim)]


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


def inversion_wrapper(T: tri, dim: int) -> tri | None:

    t = T.inv(dim)
    if t == []: return None
    def _psgen(n: int) -> trow: return list(t[n])

    @set_attributes(_psgen, T.id + "Inv", True)
    def psgen(n: int, k: int = -1) -> list[int] | int:
        if k == -1: return _psgen(n)
        return _psgen(n)[k]

    return psgen


def reversion_wrapper(T: tri, dim: int) -> tri:

    t = T.rev(dim)
    def _rsgen(n: int) -> trow: return list(t[n]) 

    @set_attributes(_rsgen, T.id + "Rev", True)
    def rsgen(n: int, k: int = -1) -> list[int] | int:
        if k == -1: return _rsgen(n)
        return _rsgen(n)[k]

    return rsgen


def revinv_wrapper(T: tri, dim: int) -> tri | None:

    I = inversion_wrapper(T, dim)
    if I == None: return None
    T = reversion_wrapper(I, dim)

    def _rigen(n: int) -> trow: return list(T(n))

    @set_attributes(_rigen, T.id, True)
    def rigen(n: int, k: int = -1) -> list[int] | int:
        if k == -1: return _rigen(n)
        return _rigen(n)[k]

    return rigen


def invrev_wrapper(T: tri, dim: int) -> tri | None:

    R = reversion_wrapper(T, dim)
    T = inversion_wrapper(R, dim)
    if T == None: return None

    def _tigen(n: int) -> trow: return list(T(n))

    @set_attributes(_tigen, T.id, True)
    def tigen(n: int, k: int = -1) -> list[int] | int:
        if k == -1: return _tigen(n)
        return _tigen(n)[k]

    return tigen


def SubTriangle(T: tri, N: int, K: int, dim: int) -> tabl:
    return [[T(n, k) for k in range(K, K - N + n + 1)] for n in range(N, N + dim)]


def AbsSubTriangle(T: tri, N: int, K: int, dim: int) -> tabl:
    return [[abs(T(n, k)) for k in range(K, K - N + n + 1)] for n in range(N, N + dim)]



def set_attributes(r: rgen, id: str, sim: list, vert: bool=False) -> Callable[[tri], tri]:

    def maketab(dim: int) -> tabl:
        return [list(r(n)) for n in range(dim)]

    def makerev(dim: int) -> tabl:
        return [list(reversed(r(n))) for n in range(dim)]

    def makemat(dim: int) -> tabl:
        return [[r(n)[k] if k <= n else 0 for k in range(dim)] for n in range(dim)]

    def makeflat(dim: int) -> tabl:
        return [r(n)[k] for n in range(dim) for k in range(n + 1)]

    def makeinv(dim: int) -> tabl:
        if not vert: return []
        return InverseTriangle(r, dim)

    def makerevinv(dim: int) -> tabl:
        if not vert: return []
        I = InverseTriangle(r, dim)
        if I == []: return []
        return [[I[n][n - k] for k in range(n + 1)] for n in range(dim)]

    def makeinvrev(dim: int) -> tabl:
        R = [list(reversed(r(n))) for n in range(dim)]
        M = [[R[n][k] if k <= n else 0 for k in range(dim)] for n in range(dim)]
        return InverseTabl(M)

    def sub(N: int, K: int) -> Callable[[int], tabl]:
        def gsub(dim: int) -> tabl:
            return [[r(n)[k] for k in range(K, K - N + n + 1)] for n in range(N, N + dim)]
        return gsub

    def abssub(N: int, K: int) -> Callable[[int], tabl]:
        def gabssub(dim: int) -> tabl:
            return [[abs(r(n)[k]) for k in range(K, K - N + n + 1)] for n in range(N, N + dim)]
        return gabssub


    def wrapper(f: tri) -> tri:
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
        return f
    return wrapper


if __name__ == "__main__":

    from Abel import abel
    from Bell import bell
    from StirlingSet import stirling_set
    from Delannoy import delannoy
    from ChebyshevT import chebyshevT

    f = chebyshevT # stirling_set
    g = delannoy
    dim = 6


    T = f.tab(dim)
    print("TRI    ", T)

    T = f.flat(dim)
    print("FLAT   ", T)

    i = reversion_wrapper(f, dim)
    T = i.tab(dim)
    print("REV    ", T)

    i = inversion_wrapper(f, dim)
    if i != None:
        T = i.tab(dim)
        print("INV    ", T)


    print("Stirling +++++++++++++++++")

    i = revinv_wrapper(f, dim)
    if i != None:
        T = i.tab(dim)
        print("INV|REV", T)
    else:
        print("None")

    print("#", f.revinv(dim))

    print("---")

    i = invrev_wrapper(f, dim)
    if i != None:
        T = i.tab(dim)
        print("REV|INV", T)
    else:
        print("None")

    print("#", f.invrev(dim))

    print("Delannoy +++++++++++++++++")

    i = revinv_wrapper(g, dim)
    if i != None:
        T = i.tab(dim)
        print("INV|REV", T)
    else:
        print("None")

    print("#", g.revinv(dim))

    print("---")

    i = invrev_wrapper(g, dim)
    if i != None:
        T = i.tab(dim)
        print("REV|INV", T)
    else:
        print("None")

    print("#", g.invrev(dim))

    print("xxxxx")
    print(abel.sim)
    print("===")
    print(abel.tab(6))
    print(abel.sub(0,0)(6))
    print(abel.sub(1,0)(6))
    print(abel.sub(1,1)(6))
    print("===")
    print(bell.tab(6))
    print(bell.sub(0,0)(6))
    print(bell.sub(1,0)(6))
    print(bell.sub(1,1)(6))
