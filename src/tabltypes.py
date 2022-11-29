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

"""Type: triangle"""
tri: TypeAlias = Callable[[int, int], trow | int]


def set_name(r: rgen, id: str):
    def tabmaker(n: int, k: int = -1) -> list[int] | int:
        return [r(j).copy() for j in range(n)]

    def wrapper(f: tri) -> tri:
        f.tab = tabmaker
        f.id = id
        return f
    return wrapper


# https://stackoverflow.com/questions/47056059/best-way-to-add-attributes-to-a-python-function
