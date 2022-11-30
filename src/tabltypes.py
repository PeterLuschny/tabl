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


def set_attributes(r: rgen, id: str, inv: bool=False) -> Callable[[tri], tri]:

    def maketab(dim: int) -> tabl:
        return [r(n).copy() for n in range(dim)]

    def makerev(dim: int) -> tabl:
        return [[r(n)[n - k] for k in range(n + 1)] for n in range(dim)]

    def makemat(dim: int) -> tabl:
        return [[r(n)[k] if k <= n else 0 for k in range(dim)] for n in range(dim)]

    def makeinv(dim: int) -> tabl:
        if not inv: return []
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

# https://stackoverflow.com/questions/47056059/best-way-to-add-attributes-to-a-python-function
