from tabltransform import row_poly, col_poly, flat_tabl
from tablsums import tabl_sum, tabl_evensum, tabl_oddsum, tabl_altsum, tabl_cumsum, tabl_revcumsum, tabl_diagsum
from tabltypes import tgen, tabl


# #@

def Profile(T: tgen, hor: int = 10, ver: int = 5) -> dict[str, list[int]]:

    d: dict[str, list[int]] = {}
    t: tabl = T(hor)  

    # Triangle flattened
    d["tabflt"] = flat_tabl(T(6))

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
        d["dirow" + str(j)] = [T.val(j + k, k) for k in range(cols)]  

    # DiagsAsColArray
    rows: int = hor
    cols: int = ver
    for j in range(cols):
        d["dicol" + str(j)] = [T.val(j + k, j) for k in range(rows)]  

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


def PrintProfile(T: tgen) -> None:
    d: dict[str, list[int]] = Profile(T)

    print()
    print(T.id)
    for seq in d.items():
        print(f"{seq[0]}, {seq[1]}")
    print()


"""
from io import TextIOWrapper
from tabl import tabl_fun
def SaveProfiles() -> None:
    dest: TextIOWrapper = open("profiles.csv", "w+")

    for fun in tabl_fun:
        p: dict[str, list[int]] = Profile(fun)
        id: str = fun.id
        for seq in p.items():
            dest.write(f"{seq[1]},{seq[0]},{id}\n")
    dest.close()
"""

####################################################################

if __name__ == "__main__":

    from SymmetricPolynomial import sympoly
    from Rencontres import rencontres

    PrintProfile(sympoly)
    PrintProfile(rencontres)
    #SaveProfiles()
