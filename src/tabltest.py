from tablprint import PrintViews
from sys import setrecursionlimit
from tabltypes import tgen


def TablTest(T:tgen, dim: int = 8, short: bool = False) -> None:

    PrintViews(T, dim, verbose=True)

    # Increase the default recursion limit
    setrecursionlimit(2100)

    arg: int = 500 if short else 1000
    eq: bool = T.row(arg - 1) is T(arg)[-1]

    a1: str = str(arg - 1)
    a2: str = str(arg // 2)
    print(f"py> row({a1}) == tabl[{arg}][-1] = {eq}") 

    print(f"py> tabl[{arg}][{a2}] =")
    print(T.val(arg, arg // 2))

    print("\n--- TablTest done!\n")
