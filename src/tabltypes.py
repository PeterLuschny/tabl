from typing import Callable, TypeAlias

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


def tstruct(r: rgen, id: str) -> Callable[[tgen], tgen]:
    def v(n: int, k: int) -> int: 
        return r(n)[k]

    def wrapper(f: tgen) -> tgen:
        f.row = r
        f.val = v
        f.id = id
        return f

    return wrapper

# https://stackoverflow.com/questions/47056059/best-way-to-add-attributes-to-a-python-function
