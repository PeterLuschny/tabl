from tablprint import PrintViews
from sys import setrecursionlimit
from tabltypes import tgen, trow


def TablTest(T: tgen, dim: int = 8, short: bool = False) -> None:

    PrintViews(T, dim, verbose=True)

    # Increase the default recursion limit
    setrecursionlimit(2000)

    big: int = 100 if short else 1000
    r: trow = T(big)
    b: str = str(big)
    b2: str = str(big // 2)

    print("py> row[", b2, "] ==", T.name, "(", b, ",", b2, ") =", 
           r[big // 2] == T(big, big // 2))
    print("py>", T.name, "(", b, ",", b2, ") =")
    print(r[big // 2])

    print("\n--- TablTest done!\n")
