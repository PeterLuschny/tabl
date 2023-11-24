from functools import cache
from typing import Callable, TypeAlias
from _tablinverse import InvertTriangle, InvertTabl

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

"""Type: triangle (resp. table)"""
tabl: TypeAlias = list[list[int]]

"""Type: sequence generator"""
seq: TypeAlias = Callable[[int], int]

"""Type: row generator"""
rgen: TypeAlias = Callable[[int], trow]

"""Type: triangle (resp. table) generator"""
# tgen: TypeAlias = Callable[[int, int], list[int] | int]  | Callable[[int], list[int] | int]
tgen: TypeAlias = Callable[[int, int], int]


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


def SeqString(seq: list[int], maxlen: int, offset: int = 0) -> str:
    """
    Converts a sequence of integers into a string representation.

    Args:
        seq (list[int]): The sequence of integers to be converted.
        maxlen (int): The maximum length of the resulting string.
        offset (int, optional): The starting index of the sequence. Defaults to 0.

    Returns:
        str: The string representation of the sequence.

    """
    seqstr = ""
    maxl = 0
    for trm in seq[offset:]:
        s = str(trm) + ","
        maxl += len(s)
        if maxl > maxlen:
            break
        seqstr += s
    return seqstr


def InvTable(T: tgen, size: int) -> tgen | None:
    """
    Returns a generator for the inverse triangle if the triangle is ivertible.

    Args:
        T (tgen): The generator of the triangle.
        size (int): Size of the inverse triangle to be generated.

    Returns:
        tgen : The generator of the inverse triangle.
        None : If the inverse triangle does not exist.
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
    """
    Returns a generator for the reversed triangle.

    Args:
        T (tgen): The generator of the triangle.
        size (int): Size of the reversed triangle to be generated.

    Returns:
        tgen: The generator of the reversed triangle.
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


def AltTable(T: tgen, size: int = 0) -> tgen:
    """
    Returns a generator for the triangle with alternating signs.

    Args:
        T (tgen): The generator of the triangle.
        size (int): Size of the sign-changed triangle to be generated.

    Returns:
        tgen: The generator of the sign-changed triangle.
    """

    #t = T.tab(size)
    r = T.gen

    @cache
    def asgen(n: int) -> trow:
        #row = t[n]
        return [(-1) ** k * term for k, term in enumerate(r(n))]

    @MakeTriangle(asgen, T.id + ":Alt", [], True)
    def Asgen(n: int, k: int) -> int:
        return asgen(n)[k]

    return Asgen



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
    """
    Generates a sub-triangle of a given size from a given row generator function.

    Args:
        g (rgen): The row generator function used to generate the elements of the triangle.
        N (int): The starting row index of the sub-triangle.
        K (int): The starting column index of the sub-triangle.
        size (int): The size of the sub-triangle.

    Returns:
        tabl: The generated sub-triangle.

    """
    return [[g(n)[k] for k in range(K, K - N + n + 1)] for n in range(N, N + size)]


def AbsSubTriangle(g: rgen, N: int, K: int, size: int) -> tabl:
    """
    Generates a sub-triangle with absolute values of a given size from a given row generator function.

    Args:
        g (rgen): The row generator function used to generate the elements of the triangle.
        N (int): The starting row index of the sub-triangle.
        K (int): The starting column index of the sub-triangle.
        size (int): The size of the sub-triangle.

    Returns:
        tabl: The generated sub-triangle with absolute values.
    """
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


if __name__ == "__main__":
    from Abel import Abel

    print(Abel.id)
    print(Abel.tab(7))
    print()

    def abel11(n):
        return Abel.sub(1, 1)(n)

    @MakeTriangle(abel11, "Abel11", ["A359", "A05"], False)
    def Abel11(n: int, k: int) -> int:
        return abel11(n)[k]

    print(Abel11(3, 2))
