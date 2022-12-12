from _tabltransforms import row_poly, col_poly, flat_tabl
from _tablsums import tabl_sum, tabl_evensum, tabl_oddsum, tabl_altsum, tabl_accusum, tabl_revaccusum, tabl_diagsum
from _tabltypes import tri, tabl, inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper


# #@


def Profile(T: tri, hor: int = 10) -> dict[str, list[int]]:

    d: dict[str, list[int]] = {}
    t: tabl = T.tab(hor)
    ver: int = hor // 2

    # Triangle flattened
    d["tabflt"] = flat_tabl(T.tab(6))

    # Row sums
    d["rowsum"] = tabl_sum(t)
    d["evesum"] = tabl_evensum(t)
    d["oddsum"] = tabl_oddsum(t)
    d["altsum"] = tabl_altsum(t)
    d["accusum"] = tabl_accusum(t)
    d["revaccu"] = tabl_revaccusum(t)
    d["diasum"] = tabl_diagsum(t)

    # DiagsAsRowArray
    rows: int = ver
    cols: int = hor
    for j in range(rows):
        d["dirow" + str(j)] = [T(j + k, k) for k in range(cols)]

    # DiagsAsColArray
    rows: int = hor
    cols: int = ver
    for j in range(cols):
        d["dicol" + str(j)] = [T(j + k, j) for k in range(rows)]

    # RowPolyArray
    rows: int = ver
    cols: int = hor
    for j in range(rows):
        d["porow" + str(j)] = row_poly(T, j, cols)

    # ColPolyArray
    rows: int = ver
    cols: int = hor
    for j in range(rows):
        if j == 1:
            continue
        d["pocol" + str(j)] = col_poly(T, j, cols)

    return d


counter: int = 0

def PrintProfile(T: tri, dim: int, format: str) -> None:

    d: dict[str, list[int]] = Profile(T, dim)

    if format == 'twolines':
        for seq in d.items():
            print(f"{T.id}|{seq[0]}\n{seq[1]}")

    if format == 'oneline':
        print(T.id)
        for seq in d.items():
            print(f"|{seq[0]}, {seq[1]}")
        print()

    if format == 'nonames':
        global counter
        for seq in d.items():
            counter += 1
            print(seq[1])


def PrintExtendedProfile(T: tri, dim: int, format: str) -> None:
    
    tim: int = dim + dim // 2

    PrintProfile(T, dim, format)

    I = inversion_wrapper(T, tim)
    if I != None:
        PrintProfile(I, dim, format)

    R = reversion_wrapper(T, tim)
    PrintProfile(R, dim, format)

    R = revinv_wrapper(T, tim)
    if R != None:
        PrintProfile(R, dim, format)

    R = invrev_wrapper(T, tim)
    if R != None:
        PrintProfile(R, dim, format)
    
    if format == 'nonames':
        global counter
        print(counter, "sequences generated.")



if __name__ == "__main__":

    from Rencontres import rencontres
    from Motzkin import motzkin
    from Leibniz import leibniz
    from ChebyshevS import chebyshevS

    dim = 14
    format = 'nonames' # 'twolines' #

    #PrintProfile(leibniz, dim, 'twolines')
    #PrintProfile(motzkin, dim, format)
    PrintExtendedProfile(chebyshevS, dim, 'twolines')
    #PrintExtendedProfile(motzkin, dim, format)

