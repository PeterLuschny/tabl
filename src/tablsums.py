
# #@

from tabltypes import tabl, trow


def even_sum(r: trow) -> int:
    return sum(r[::2])


def odd_sum(r: trow) -> int:
    return sum(r[1::2])


def alt_sum(r: trow) -> int:
    return even_sum(r) - odd_sum(r)


def tabl_sum(t: tabl) -> trow:
    return [sum(row) for row in t]


def tabl_evensum(t: tabl) -> trow:
    return [even_sum(row) for row in t]


def tabl_oddsum(t: tabl) -> trow:
    return [odd_sum(row) for row in t]


def tabl_altsum(t: tabl) -> trow:
    return [alt_sum(row) for row in t]


def PrintSums(t: tabl) -> None:
    print(tabl_sum(t))
    print(tabl_evensum(t))
    print(tabl_oddsum(t))
    print(tabl_altsum(t))


####################################################################

if __name__ == "__main__":

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

    PrintSums(T)
