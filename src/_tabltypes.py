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
# For some dimension size > 0 it is defined as
# T[N, K, size] = [[T(n, k) for k in range(K, K - N + n + 1)] for n in range(N, N + size)]


"""Type: table row"""
trow: TypeAlias = list[int]

"""Type: table"""
tabl: TypeAlias = list[list[int]]

"""Type: sequence generator"""
seq: TypeAlias = Callable[[int], int]

"""Type: row generator"""
rgen: TypeAlias = Callable[[int], trow]

"""Type: table generator"""
#tgen: TypeAlias = Callable[[int, int], list[int] | int]  | Callable[[int], list[int] | int] 
tgen: TypeAlias = Callable[[int, int], int]

"""Type: triangle"""
tri: TypeAlias = Callable[[int, int], int]

#   Two types of traits:
#   print(signature(EvenSum))
#   (t: list[list[int]]) -> list[int]
#   print(signature(DiagRow0))
#   (g: Callable[[int], list[int]], size: int) -> list[int]


def inversion_wrapper(T: tgen, size: int) -> tgen | None:

    t = T.inv(size)
    if t == []: return None
    def psgen(n: int) -> trow: return list(t[n])

    @set_attributes(psgen, T.id + ":Inv", [], True)
    def Psgen(n: int, k: int) ->  int:
        return psgen(n)[k]

    return Psgen


def reversion_wrapper(T: tgen, size: int) -> tgen:

    t = T.rev(size)
    def rsgen(n: int) -> trow: return list(t[n]) 

    @set_attributes(rsgen, T.id + ":Rev", [], True)
    def Rsgen(n: int, k: int) -> int:
        return rsgen(n)[k]

    return Rsgen


def revinv_wrapper(T: tgen, size: int) -> tgen | None:

    I = inversion_wrapper(T, size)
    if I == None: return None
    J = reversion_wrapper(I, size)

    def rigen(n: int) -> trow: return list(J.gen(n))

    @set_attributes(rigen, J.id, [], True)
    def Rigen(n: int, k: int) -> int:
        return rigen(n)[k]

    return Rigen


def invrev_wrapper(T: tgen, size: int) -> tgen | None:

    R = reversion_wrapper(T, size)
    S = inversion_wrapper(R, size)
    if S == None: return None

    def tigen(n: int) -> trow: return list(S.gen(n))

    @set_attributes(tigen, S.id, [], True)
    def Tigen(n: int, k: int) -> int:
        return tigen(n)[k]

    return Tigen


def SubTriangle(g: rgen, N: int, K: int, size: int) -> tabl:
    return [[g(n)[k] for k in range(K, K - N + n + 1)] for n in range(N, N + size)]


def AbsSubTriangle(g: rgen, N: int, K: int, size: int) -> tabl:
    return [[abs(g(n)[k]) for k in range(K, K - N + n + 1)] for n in range(N, N + size)]


def set_attributes(gen: rgen, id: str, sim: list[str], vert: bool=False) -> Callable[..., Callable[[int,int], int]]:

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
        if not vert: return []
        return InverseTriangle(gen, size)

    def makerevinv(size: int) -> tabl:
        if not vert: return []
        I = InverseTriangle(gen, size)
        if I == []: return []
        return [[I[n][n - k] for k in range(n + 1)] for n in range(size)]

    def makeinvrev(size: int) -> tabl:
        R = [list(reversed(gen(n))) for n in range(size)]
        M = [[R[n][k] if k <= n else 0 for k in range(size)] for n in range(size)]
        return InverseTabl(M)

    def sub(N: int, K: int) -> Callable[[int], tabl]:
        def gsub(size: int) -> tabl:
            return [[gen(n)[k] for k in range(K, K - N + n + 1)] for n in range(N, N + size)]
        return gsub

    def abssub(N: int, K: int) -> Callable[[int], tabl]:
        def gabssub(size: int) -> tabl:
            return [[abs(gen(n)[k]) for k in range(K, K - N + n + 1)] for n in range(N, N + size)]
        return gabssub

    def wrapper(f: Callable[[int, int], int]) -> Callable[[int, int], int]:
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

    return wrapper


if __name__ == "__main__":

    from Abel import Abel
    from Bell import Bell
    from StirlingSet import StirlingSet
    from Delannoy import Delannoy
    from ChebyshevT import ChebyshevT

    F = StirlingSet 
    G = Delannoy
    size = 7

    T = F.tab(size)
    print("tgen   ", T)

    T = F.flat(size)
    print("FLAT   ", T)

    i = reversion_wrapper(F, size)
    T = i.tab(size)
    print("REV    ", T)

    i = inversion_wrapper(F, size)
    if i != None:
        T = i.tab(size)
        print("INV    ", T)


    print("Stirling +++++++++++++++++")

    i = revinv_wrapper(F, size)
    if i != None:
        T = i.tab(size)
        print("INV|REV", T)
    else:
        print("None")

    print("#", F.revinv(size))

    print("---")

    i = invrev_wrapper(F, size)
    if i != None:
        T = i.tab(size)
        print("REV|INV", T)
    else:
        print("None")

    print("#", F.invrev(size))

    print("Delannoy +++++++++++++++++")

    i = revinv_wrapper(G, size)
    if i != None:
        T = i.tab(size)
        print("INV|REV", T)
    else:
        print("None")

    print("#", G.revinv(size))

    print("---")

    i = invrev_wrapper(G, size)
    if i != None:
        T = i.tab(size)
        print("REV|INV", T)
    else:
        print("None")

    print("#", G.invrev(size))

    print("xxxxx")
    print(Abel.sim)
    print("===")
    print(Abel.tab(6))
    print(Abel.sub(0,0)(6))
    print(Abel.sub(1,0)(6))
    print(Abel.sub(1,1)(6))
    print("===")
    print(Bell.tab(6))
    print(Bell.sub(0,0)(6))
    print(Bell.sub(1,0)(6))
    print(Bell.sub(1,1)(6))

    print(Abel.tab(7))
    print()

    abel11 = lambda n: Abel.sub(1,1)(n)

    @set_attributes(
    abel11, "Abel11", ['A359', 'A05'], False)
    def Abel11(n: int, k: int) -> int: 
        return abel11(n)[k]
    print(Abel11(3,2))

  