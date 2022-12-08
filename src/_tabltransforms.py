from itertools import accumulate
from _tabltypes import seq, tri, tabl, trow


# #@


def poly(R: tri, n: int, x: int) -> int:
    row: trow = R(n)
    return sum(c * x ** k for (k, c) in enumerate(row))


def row_poly(T: tri, n: int, leng: int) -> trow:
    return [poly(T, n, k) for k in range(leng)]


def col_poly(T: tri, n: int, leng: int) -> trow:
    return [poly(T, k, n) for k in range(leng)]


def trans_seq(T: tri, a: seq, lg: int) -> trow:
    return [sum(T(n, k) * a(k) for k in range(n + 1)) for n in range(lg)]


def invtrans_seq(T: tri, a: seq, lg: int) -> trow:
    return [
        sum((-1) ** (n - k) * T(n, k) * a(k) for k in range(n + 1))
        for n in range(lg)
    ]


def diag_tabl(t: tabl) -> tabl:
    U: tabl = []
    for n in range(1, len(t)):
        R: trow = []
        for k in range((n + 1) // 2):
            R.append(t[n - k - 1][k])
        U.append(R)
    return U


def accu_tabl(t: tabl) -> tabl:
    U: tabl = []
    for row in t:
        U.append(list(accumulate(row)))
    return U


def rev_tabl(t: tabl) -> tabl:
    U: tabl = []
    for row in t:
        U.append(list(reversed(row)))
    return U


def revaccu_tabl(t: tabl) -> tabl:
    return rev_tabl(accu_tabl(t))


def accurev_tabl(t: tabl) -> tabl:
    return accu_tabl(rev_tabl(t))


def flat_tabl(t: tabl) -> trow:
    return [i for row in t for i in row]


def flat_rev(t: tabl) -> trow:
    return [i for row in rev_tabl(t) for i in row]


def flat_diag(t: tabl) -> trow:
    return [i for row in diag_tabl(t) for i in row]


def flat_accu(t: tabl) -> trow:
    return [i for row in accu_tabl(t) for i in row]


def flat_revaccu(t: tabl) -> trow:
    return [i for row in revaccu_tabl(t) for i in row]


def flat_accurev(t: tabl) -> trow:
    return [i for row in accurev_tabl(t) for i in row]


if __name__ == "__main__":

    from Binomial import binomial
    from StirlingSet import stirling_set
    from StirlingCycle import stirling_cycle
    from Motzkin import motzkin

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

    print(trans_seq(binomial, catalan_number, 11))
    print(invtrans_seq(binomial, catalan_number, 11))

    print(trans_seq(stirling_cycle, catalan_number, 11))
    print(invtrans_seq(stirling_cycle, catalan_number, 11))

    print(trans_seq(stirling_set, catalan_number, 11))
    print(invtrans_seq(stirling_set, catalan_number, 11))

    S: tabl = motzkin.tab(7)
    
    print(diag_tabl(T))
    print("---")
    print(diag_tabl(S))
    print("---")
    print(accu_tabl(T))
    print("---")
    print(accu_tabl(S))
    print("---")
    print(rev_tabl(T))
    print("---")
    print(rev_tabl(S))
    print("---")

    print(flat_tabl(T))
    print(flat_rev(T))
    print(flat_diag(T))
    print(flat_accu(T))
    print(flat_revaccu(T))
    print(flat_accurev(T))
