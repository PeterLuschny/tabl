
#@


def even_sum(L: list[int]) -> int:
    return sum(L[::2])


def odd_sum(L: list[int]) -> int:
    return sum(L[1::2])


def alt_sum(L: list[int]) -> int:
    return even_sum(L) - odd_sum(L)


def tabl_sum(T: list[list[int]]) -> list[int]:
    return [sum(row) for row in T]


def tabl_evensum(T: list[list[int]]) -> list[int]:
    return [even_sum(row) for row in T]


def tabl_oddsum(T: list[list[int]]) -> list[int]:
    return [odd_sum(row) for row in T]


def tabl_altsum(T: list[list[int]]) -> list[int]:
    return [alt_sum(row) for row in T]


def PrintSums(T: list[list[int]]) -> None:
    print(tabl_sum(T))
    print(tabl_evensum(T))
    print(tabl_oddsum(T))
    print(tabl_altsum(T))


####################################################################

if __name__ == "__main__":

    T = [ [1],
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
        [0, 1, 21, 228, 1700, 9750, 45630, 180180, 610740, 1781325, 4382625, 
    8414640] ]

    PrintSums(T)
