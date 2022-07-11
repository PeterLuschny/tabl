from itertools import accumulate
from tabltypes import tabl, trow

# #@


def diag_tabl(t: tabl) -> tabl:
    U: tabl = []
    for n in range(1, len(t)):
        R: trow = []
        for k in range((n + 1) // 2):
            R.append(t[n - k - 1][k])
        U.append(R)
    return U


def cum_tabl(t: tabl) -> tabl:
    U: tabl = []
    for row in t:
        U.append(list(accumulate(row)))
    return U


def rev_tabl(t: tabl) -> tabl:
    U: tabl = []
    for row in t:
        U.append(list(reversed(row)))
    return U


def revcum_tabl(t: tabl) -> tabl:
    return rev_tabl(cum_tabl(t))


def cumrev_tabl(t: tabl) -> tabl:
    return cum_tabl(rev_tabl(t))


def flat_tabl(t: tabl) -> trow:
    return [i for row in t for i in row ]


def flat_rev(t: tabl) -> trow:
    return [i for row in rev_tabl(t) for i in row ]


def flat_diag(t: tabl) -> trow:
    return [i for row in diag_tabl(t) for i in row ]


def flat_cum(t: tabl) -> trow:
    return [i for row in cum_tabl(t) for i in row ]


def flat_revcum(t: tabl) -> trow:
    return [i for row in revcum_tabl(t) for i in row ]


def flat_cumrev(t: tabl) -> trow:
    return [i for row in cumrev_tabl(t) for i in row ]


####################################################################

if __name__ == "__main__":
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
    ]

    S: tabl = motzkin(7)

    print(diag_tabl(T))
    print("---")
    print(diag_tabl(S))
    print("---")
    print(cum_tabl(T))
    print("---")
    print(cum_tabl(S))
    print("---")
    print(rev_tabl(T))
    print("---")
    print(rev_tabl(S))  
    print("---")

    print(flat_tabl(T))
    print(flat_rev(T))
    print(flat_diag(T))
    print(flat_cum(T))
    print(flat_revcum(T))
    print(flat_cumrev(T))


"""
Return the diagonal triangle T(n - k - 1, k) where k is in range((n + 1) // 2).

python> print(diagonal_tabl(Motzkin(9)))   # A106489

[1]
[1]
[2, 1]
[4, 2]
[9, 5, 1]
[21, 12, 3]
[51, 30, 9, 1]
[127, 76, 25, 4]
"""