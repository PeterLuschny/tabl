from typing import Callable, TypeAlias

# #@

"""table row"""
trow: TypeAlias = list[int]

"""table"""
tabl: TypeAlias = list[list[int]]

"""row generator"""
rgen: TypeAlias = Callable[[int], trow]

"""table generator"""
tgen: TypeAlias = Callable[[int], tabl]


def tvals(r: rgen, id: str) -> Callable[[tgen], tgen]:
    def v(n: int, k: int) -> int: 
        return r(n)[k]

    def wrapper(f: tgen) -> tgen:
        f.row = r
        f.val = v
        f.id = id
        return f

    return wrapper

# https://stackoverflow.com/questions/47056059/best-way-to-add-attributes-to-a-python-function
