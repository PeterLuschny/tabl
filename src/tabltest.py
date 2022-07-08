from tablprint import PrintViews
from sys import setrecursionlimit
from typing import Callable


def TablTest(seq: Callable, dim=8, short=False) -> None:

    PrintViews(seq, dim, verbose=True)

    # Increase the default recursion limit
    setrecursionlimit(2000)

    big: int = 100 if short else 1000
    Trow: list[int] = seq(big)
    b: str = str(big); b2: str = str(big // 2)

    print("py> Trow[", b2, "] ==", seq.name, "(", b, ",", b2, ") =", 
           Trow[big // 2] == seq(big, big // 2))
    print("py>", seq.name, "(", b, ",", b2, ") =") 
    print(Trow[big // 2])
    
    print("--- TablTest done!\n")
