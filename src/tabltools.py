# #@

from tabltypes import rgen, tgen, trow


def poly(R: rgen, n: int, x: int) -> int:
    row: trow = R(n)
    return sum(c * x ** k for (k, c) in enumerate(row))


def row_poly(T: tgen, n: int, leng: int) -> trow:
    return [poly(T.row, n, k) for k in range(leng)]


def col_poly(T: tgen, n: int, leng: int) -> trow:
    return [poly(T.row, k, n) for k in range(leng)]


def trans_poly(t: rgen, s: rgen, n: int) -> trow:
    rowt: trow = t(n)
    rows: trow = s(n)
    return [sum(rowt[k] * x ** k for k in range(n) for x in rows)]


####################################################################

if __name__ == "__main__":
    from tabltypes import tabl
    from tabltrans import rev_tabl
    from Abel import abel

    t: tabl = [
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

    print(trans_poly(lambda n: t[n], abel.row, 6))
    print(trans_poly(abel.row, lambda n: t[n], 6))
    revabel: tabl = rev_tabl(abel(9))
    print(trans_poly(lambda n: revabel[n], lambda n: t[n], 8))
    print(trans_poly(abel.row, abel.row, 6))
