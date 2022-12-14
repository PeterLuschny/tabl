from _tablviews import PrintViews
from sys import setrecursionlimit, set_int_max_str_digits
from _tabltypes import tri


def TablTest(T:tri, dim: int = 8, short: bool = False) -> None:

    PrintViews(T, dim, verbose=True)

    # Increase the default recursion limit
    setrecursionlimit(3000)
    set_int_max_str_digits(5000)

    arg: int = 500 if short else 1000
    eq: bool = T(arg, arg) == T(arg)[-1]

    a1: str = str(arg)
    a2: str = str(arg // 2)

    if eq:
        print(f"py> T({a1}, {a1}) == row({a1})[-1] = {eq}") 
    else:
        print(f"Error! \n {T(arg, arg)} \n {T(arg)[-1]}") 

    try:
        print(f"py> tabl[{arg}][{a2}] =")
        print(T(arg, arg // 2))
    except: 
        print("Exceeds the limit for integer string conversion.")

    print("\n--- TablTest done!\n")
