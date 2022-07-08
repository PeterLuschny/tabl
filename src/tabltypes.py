from typing import Callable, TypeAlias

#@

'''table row'''
trow: TypeAlias = list[int]
'''table'''
tabl: TypeAlias = list[list[int]]
'''row generator'''
rgen: TypeAlias = Callable[[int], trow]
'''table generator'''
tgen: TypeAlias = Callable[[int, int | None], int | trow | tabl]

def TablGenerator(g: rgen, name: str, id: str) -> tgen:

    def T(n: int, k: int | None=None) -> int | trow | tabl:
        if n < 0:
            return [g(k) for k in range(-n)]
        if k == None:
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
