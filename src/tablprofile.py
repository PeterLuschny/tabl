from tabltransform import row_poly, col_poly, flat_tabl
from tablsums import tabl_sum, tabl_evensum, tabl_oddsum, tabl_altsum, tabl_cumsum, tabl_revcumsum, tabl_diagsum
from tabltypes import tri, tabl, inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper


# #@


def Profile(T: tri, hor: int, ver: int) -> dict[str, list[int]]:

    d: dict[str, list[int]] = {}
    t: tabl = T.tab(hor)

    # Triangle flattened
    d["tabflt"] = flat_tabl(T.tab(6))

    # Row sums
    d["rowsum"] = tabl_sum(t)
    d["evesum"] = tabl_evensum(t)
    d["oddsum"] = tabl_oddsum(t)
    d["altsum"] = tabl_altsum(t)
    d["cumsum"] = tabl_cumsum(t)
    d["revcum"] = tabl_revcumsum(t)
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
    d: dict[str, list[int]] = Profile(T, dim // 2, dim // 4)

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
    PrintProfile(T, dim, format)
    I = inversion_wrapper(T, dim)
    if I != None:
        PrintProfile(I, dim, format)

    R = reversion_wrapper(T, dim)
    PrintProfile(R, dim, format)

    R = revinv_wrapper(T, dim)
    if R != None:
        PrintProfile(R, dim, format)

    R = invrev_wrapper(T, dim)
    if R != None:
        PrintProfile(R, dim, format)
    
    if format == 'nonames':
        global counter
        print(counter, "sequences generated.")



if __name__ == "__main__":

    from Rencontres import rencontres
    from Motzkin import motzkin
    from Leibniz import leibniz

    dim = 20
    format = 'twolines' # 'nonames'
    PrintExtendedProfile(motzkin, dim, format)
    PrintExtendedProfile(leibniz, dim, format)
