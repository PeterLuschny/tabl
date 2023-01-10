from typing import Callable
from itertools import accumulate
from fractions import Fraction as frac
from Binomial import binomial
from math import lcm, gcd
from functools import reduce
from _tablinverse import InverseTabl
from _tabltypes import seq, tri, tabl, trow


# #@

def SeqToFixlenString(seq: list[int], maxlen:int=90, separator=',') -> str:
    stri = "["
    maxl = 3
    for trm in seq:
        s = str(trm) + separator
        maxl += len(s)
        if maxl > maxlen: break
        stri += s
    return stri + "]"


def poly(T: tri, n: int, x: int) -> int:
    row: trow = T(n)
    return sum(c * (x ** j) for (j, c) in enumerate(row))


def poly_frac(T: tabl, x: frac) -> list[frac]:
    return [sum(c * (x ** k) for (k, c) in enumerate(row)) for row in T]


def row_poly(T: tri, n: int, leng: int) -> trow:
    return [poly(T, n, k) for k in range(leng)]


def col_poly(T: tri, n: int, leng: int) -> trow:
    return [poly(T, k, n) for k in range(leng)]


def diag_poly(T: tri, n: int) -> trow:
    return [poly(T, n - k, k) for k in range(n + 1)]


def poly_diag(T: tri, leng: int) -> trow:
    return [poly(T, n, n) for n in range(leng)]


def poly_tabl(T: tri, leng: int) -> tabl:
    return [diag_poly(T, n) for n in range(leng)]


def pos_half(T: tabl) -> list[int]:
    R = poly_frac(T, frac(1, 2))
    return [((2 ** n) * r).numerator for n, r in enumerate(R)]


def neg_half(T: tabl) -> list[int]:
    R = poly_frac(T, frac(-1, 2))
    return [(((-2) ** n) * r).numerator for n, r in enumerate(R)]


def trans_seq(T: tri, a: seq, lg: int) -> trow:
    return [sum(T(n, k) * a(k) for k in range(n + 1)) for n in range(lg)]


def trans_self(T: tri, lg: int) -> tabl:
    return [trans_seq(T, lambda k: T(n, k), n + 1) for n in range(lg)]


def transbin_tabl(T: tri, lg: int) -> tabl:
    return [trans_seq(binomial, lambda k: T(n, k), n + 1) for n in range(lg)]


def transbin_val(f: tri, lg: int) -> trow:
    T = transbin_tabl(f, lg)
    return [row[-1] for row in T]


def invtrans_seq(T: tri, a: seq, lg: int) -> trow:
    return [ sum((-1) ** (n - k) * T(n, k) * a(k) for k in range(n + 1))
        for n in range(lg) ]


def invtrans_self(T: tri, lg: int) -> tabl:
    return [invtrans_seq(T, lambda k: T(n, k), n + 1) for n in range(lg)]


def invtransbin_tabl(T: tri, lg: int) -> tabl:
    return [invtrans_seq(binomial, lambda k: T(n, k), n + 1) for n in range(lg)]


def invtransbin_val(f: tri, lg: int) -> trow:
    T = invtransbin_tabl(f, lg)
    return [row[-1] for row in T]


def row_diag(T: tri, j: int, leng: int) -> trow:
    return [T(j + k, k) for k in range(leng)]


def col_diag(T: tri, j: int, leng: int) -> trow:
    return [T(j + k, j) for k in range(leng)]


# Note our convention to exclude 0 and 1.
def row_lcm(f: tri, n: int) -> int:
    Z = [v for v in f(n) if not v in [-1, 0, 1]]
    return reduce(lcm, Z) if Z != [] else 1


# Note our convention to exclude 0 and 1.
def row_gcd(f: tri, n: int) -> int:
    Z = [v for v in f(n) if not v in [-1, 0, 1]]
    return reduce(gcd, Z) if Z != [] else 1


def tabl_lcm(f: tri, leng: int) -> list[int]:
    return [row_lcm(f, n) for n in range(leng)]


def tabl_gcd(f: tri, leng: int) -> list[int]:
    return [row_gcd(f, n) for n in range(leng)]


def row_max(f: tri, n: int) -> int:
    absf =[abs(t) for t in f(n)]
    return reduce(max, absf) 


def tabl_max(f: tri, leng: int) -> list[int]:
    return [row_max(f, n) for n in range(leng)]


################################################

def trans(M: tri, V: Callable, leng: int) -> list[int]:
    return [sum(M(n, k) * V(k) for k in range(n + 1)) for n in range(leng)]


def trans_sqrs(f: tri, n:int) -> list[int]: 
    return trans(f, lambda k: k * k, n)


def trans_nat0(f: tri, n:int) -> list[int]: 
    return trans(f, lambda k: k, n)


def trans_nat1(f: tri, n:int) -> list[int]: 
    return trans(f, lambda k: k + 1, n)


def diag_tabl(t: tabl) -> tabl:
    U: tabl = []
    for n in range(1, len(t)):
        R: trow = []
        for k in range((n + 1) // 2):
            R.append(t[n - k - 1][k])
        U.append(R)
    return U


def acc_tabl(t: tabl) -> tabl:
    return [list(accumulate(row)) for row in t]


def rev_tabl(t: tabl) -> tabl:
    return [list(reversed(row)) for row in t]


def inv_tabl(t: tabl) -> tabl:
    return InverseTabl(t)


def revacc_tabl(t: tabl) -> tabl:
    return rev_tabl(acc_tabl(t))


def accrev_tabl(t: tabl) -> tabl:
    return acc_tabl(rev_tabl(t))


def flat_tabl(t: tabl) -> trow:
    return [i for row in t for i in row]


def flat_rev(t: tabl) -> trow:
    return [i for row in rev_tabl(t) for i in row]


def flat_diag(t: tabl) -> trow:
    return [i for row in diag_tabl(t) for i in row]


def flat_acc(t: tabl) -> trow:
    return [i for row in acc_tabl(t) for i in row]


def flat_revacc(t: tabl) -> trow:
    return [i for row in revacc_tabl(t) for i in row]


def flat_accrev(t: tabl) -> trow:
    return [i for row in accrev_tabl(t) for i in row]


def middle(t: tabl) -> list[int]:
    return [row[n // 2] for n, row in enumerate(t)]


def central(t: tabl) -> list[int]:
    return [row[n // 2] for n, row in enumerate(t) if n % 2 == 0]


def left_side(t: tabl) -> list[int]:
    return [row[0] for row in t]


def right_side(t: tabl)  -> list[int]:
    return [row[-1] for row in t]



if __name__ == "__main__":

    from Binomial import binomial
    from StirlingSet import stirling_set
    from StirlingCyc import stirling_cycle
    from MotzkinGF import motzkin

    #col_poly
    #print(col_poly(stirling_set, 0, 12))

    T = invtransbin_tabl(binomial, 16)
    print([sum((v) for v in t) for t in T])
    for t in T: print(t)

'''

    nums = [0, 1, 15, 117, 627, 2565, 8379, 21945, 43263]
    print([c*k for c,k in enumerate(nums)])


    T: tabl = [
        [1],
        [0, 1],
        [0, 1, 3],
        [0, 1, 5, 12],
        [0, 1, 7, 25, 55],
        [0, 1, 9, 42, 130, 273],
        [0, 1, 11, 63, 245, 700, 1428],
        [0, 1, 13, 88, 408, 1428, 3876, 7752],
        [0, 1, 15, 117, 627, 2565, 8379, 21945, 43263],
        [0, 1, 17, 150, 910, 4235, 15939, 49588, 126500, 246675],
        [0, 1, 19, 187, 1265, 6578, 27830, 98670, 296010, 740025, 1430715],
        [0, 1, 21, 228, 1700, 9750, 45630, 180180, 610740, 1781325, 4382625, 8414640],
    ]

    def catalan_number(n: int) -> int:
        return binomial(2 * n, n) // (n + 1)

    S: tabl = motzkin.tab(7)

    print(diag_tabl(T))
    print("---")
    print(diag_tabl(S))
    print("--- acctabl")
    print(acc_tabl(T))
    print("--- acctabl")
    print(acc_tabl(S))
    print("---")
    print(rev_tabl(T))
    print("---")
    print(rev_tabl(S))
    print("---")

    print(flat_tabl(T))
    print(flat_rev(T))
    print(flat_diag(T))
    print(flat_acc(T))
    print(flat_revacc(T))
    print(flat_accrev(T))
'''
