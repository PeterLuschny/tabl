from typing import Callable, TypeAlias  # , Optional

# #@

"""table row"""
trow: TypeAlias = list[int]
"""table"""
tabl: TypeAlias = list[list[int]]
"""row generator"""
rgen: TypeAlias = Callable[[int], list[int]]
"""table generator"""
tgen: TypeAlias = Callable[[int, int | None], int | trow | tabl]


def TablGenerator(g: rgen, name: str, id: str) -> tgen:
    def T(n: int, k: int | None = None) -> int | trow | tabl:
        if k is None:
            if n < 0:
                return [g(j) for j in range(-n)]
            return g(n)
        return g(n)[k]

    T.name = name
    T.id = id
    return T


def isTablGenerator(T) -> bool:
    return (
        isinstance(T, tgen)
        and isinstance(T(0, 0), int)
        and isinstance(T(0, None), list)
    )


####################################################################

# def T(n: int, k: Optional[int]=None) -> int | trow | tabl:

# https://stackoverflow.com/questions/62732402/can-i-omit-optional-if-i-set-default-to-none

# https://stackoverflow.com/questions/14749328/
