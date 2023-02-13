from typing import Callable
from itertools import accumulate
from _tabltypes import tabl, trow, tgen, rgen

'''Naming convention for 'g composed with f': (g o f)(x):= g(f(x))

    The function 
    reversed(accumulate(R)) will be named 'RevAcc';
    accumulate(reversed(R)) will be named 'AccRev';
'''

# #@

def even_sum(r: trow) -> int:
    return sum(r[::2])

def even_sum_(g: rgen, index: int) -> int:
    return even_sum(g(index))

def odd_sum(r: trow) -> int:
    return sum(r[1::2])

def odd_sum_(g: rgen, index: int) -> int:
    return odd_sum(g(index))

def antidiag_sum(r: trow) -> int:
    return sum(r)

def antidiag_sum_(g: rgen, n: int) -> int:
    return sum([g(n - k)[k] for k in range((n + 2) // 2)]) 

def acc_sum(r: trow) -> int:
    return sum(accumulate(r))

def acc_sum_(g: rgen, index: int) -> int:
    return acc_sum(g(index))

def accrev_sum(r: trow) -> int:
    return sum(accumulate(reversed(r)))

def accrev_sum_(g: rgen, index: int) -> int:
    return acc_sum(g(index))

def alt_sum(r: trow) -> int:
    return even_sum(r) - odd_sum(r)

def alt_sum_(g: rgen, index: int) -> int:
    return alt_sum(g(index))


def RowSum(t: tabl) -> trow:
    return [sum(row) for row in t]

def RowSum_(g: rgen, size: int) -> trow:
    return [sum(g(n)) for n in range(size)]

def EvenSum(t: tabl) -> trow:
    return [even_sum(row) for row in t]

def EvenSum_(g: rgen, size: int) -> trow:
    return [even_sum(g(n)) for n in range(size)]

def OddSum(t: tabl) -> trow:
    return [odd_sum(row) for row in t]

def OddSum_(g: rgen, size: int) -> trow:
    return [odd_sum(g(n)) for n in range(size)]

def AltSum(t: tabl) -> trow:
    return [alt_sum(row) for row in t]

def AltSum_(g: rgen, size: int) -> trow:
    return [alt_sum(g(n)) for n in range(size)]

def AccSum(t: tabl) -> trow:
    return [acc_sum(row) for row in t]

def AccSum_(g: rgen, size: int) -> trow:
    return [acc_sum(g(n)) for n in range(size)]

def AccRevSum(t: tabl) -> trow:
    return [accrev_sum(row) for row in t]

def AccRevSum_(g: rgen, size: int) -> trow:
    return [accrev_sum(g(n)) for n in range(size)]

def AntiDiagSum(t: tabl) -> trow:
    row = lambda n: [t[n - k - 1][k] for k in range((n + 1) // 2)]
    return [sum(row(n)) for n in range(1, len(t) + 1)]

def AntiDiagSum_(g: rgen, size: int) -> trow:
    return [antidiag_sum_(g, n) for n in range(size)]


def PrintSums(T: tabl, trianglename: str, mdformat: bool = True) -> None:

    SUMTRAIT: dict[str, Callable] = {}
    def RegisterSumTrait(f: Callable[[tabl], trow]) -> None: 
        SUMTRAIT[f.__name__] = f

    RegisterSumTrait(RowSum)
    RegisterSumTrait(EvenSum)
    RegisterSumTrait(OddSum)
    RegisterSumTrait(AltSum)
    RegisterSumTrait(AccSum)
    RegisterSumTrait(AccRevSum)
    RegisterSumTrait(AntiDiagSum)

    if mdformat:
        print("#", trianglename, ": Sums")
        print( "| Trait        |   Seq  |")
        print( "| :---         |  :---  |")
        for traitname, trait in SUMTRAIT.items():
            print(f'| {traitname:<12} | {trait(T)} |')
        print()
    else:
        for traitname, trait in SUMTRAIT.items():
            print(f'{trianglename + ":" + traitname:<18} {trait(T)}')


if __name__ == "__main__":

    from Abel import Abel
    from Bell import Bell

    PrintSums(Abel.tab(8), Abel.id)
    PrintSums(Bell.tab(6), Bell.id, False)
