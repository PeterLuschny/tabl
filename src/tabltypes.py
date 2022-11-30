from typing import Callable, TypeAlias
from sympy import Matrix

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
        I = Matrix(makemat(dim)) ** -1
        return [[I[n, k] for k in range(n + 1)] for n in range(dim)]

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

    @set_attributes(_psgen, "INV" + T.id, True)
    def psgen(n: int, k: int = -1) -> list[int] | int: 
        if k == -1: return list(t[n])
        return t[n][k]

    return psgen


def reversion_wrapper(T: tri, dim: int) -> tri:

    t = T.rev(dim)
    def _rsgen(n: int) -> trow: return list(t[n]) 

    @set_attributes(_rsgen, "REV" + T.id)
    def rsgen(n: int, k: int = -1) -> list[int] | int: 
        if k == -1: return list(t[n])
        return t[n][k]

    return rsgen



if __name__ == "__main__":
    from Abel import abel

    dim = 6
    print(abel.tab(dim))
    print(abel.inv(dim))
    i = inversion_wrapper(abel, dim)
    print(i.tab(dim))
    print(i.inv(dim))
    print()
    print(abel.tab(dim))
    print(abel.rev(dim))
    i = reversion_wrapper(abel, dim)
    print(i.tab(dim))
    print(i.rev(dim))


# https://stackoverflow.com/questions/47056059/best-way-to-add-attributes-to-a-python-function
