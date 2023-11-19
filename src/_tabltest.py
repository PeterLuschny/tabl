import sys
from _tablviews import PrintViews
from _tablinverse import InvertTabl
from _tabltypes import tgen, rgen


def TablTest(T: tgen, dim: int = 8, short: bool = False) -> None:

    # Increase the default recursion limit
    sys.setrecursionlimit(3000)
    sys.set_int_max_str_digits(5000)

    PrintViews(T, dim, verbose=True)

    arg: int = 500 if short else 1000
    gen: rgen = T.gen

    eq: bool = T(arg, arg) == gen(arg)[-1]

    a1: str = str(arg)
    a2: str = str(arg // 2)

    if eq:
        print(f"py> T({a1}, {a1}) == row({a1})[-1] = {eq}")
    else:
        print(f"Error! \n {T(arg, arg)} \n {gen(arg)[-1]}")

    try:
        print(f"py> tabl[{arg}][{a2}] =")
        print(gen(arg)[arg // 2])
    except ValueError:
        print("Exceeds the limit for integer string conversion.")

    V = InvertTabl(T.tab(8))
    if V == []:
        print("\nTriangle is not invertibel.")
    else:
        print("\nInverse triangle:")
        for row in V:
            print(row)

    print("\n--- TablTest done!\n")


if __name__ == "__main__":

    print(sys.getrecursionlimit())
    sys.setrecursionlimit(3000)
    print(sys.getrecursionlimit())

    sys.set_int_max_str_digits(5000)
