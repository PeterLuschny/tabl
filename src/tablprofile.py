from io import TextIOWrapper
from tabltools import row_poly, col_poly
from tablsums import tabl_sum, tabl_evensum, tabl_oddsum, tabl_altsum

#@

def Profile(T, hor=10, ver=5) -> dict[str, list[int]]:

    d: dict[str, list[int]] = {}
    tabl: list[list[int]] = T(-hor)

    # Triangle flattened
    d["tabflt"] = tabl[0] + tabl[1] + tabl[2] + tabl[3]

    # Row sums
    d["rowsum"] = tabl_sum(tabl)
    d["evesum"] = tabl_evensum(tabl)
    d["oddsum"] = tabl_oddsum(tabl)
    d["altsum"] = tabl_altsum(tabl)

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
        if j == 1: continue
        d["pocol" + str(j)] = col_poly(T, j, cols)

    return d


def PrintProfile(T) -> None:
    d: dict[str, list[int]] = Profile(T)

    print()
    print(T.id)
    for seq in d.items():
        print(f"{seq[0]}, {seq[1]}")
    print()


#from tabl import tabl_fun
def SaveProfiles() -> None:
    dest: TextIOWrapper = open("profiles.csv", "w+") 

    #for fun in tabl_fun:
    for fun in []:
        p: dict[str, list[int]] = Profile(fun)
        id: str = fun.id
        for seq in p.items():
            dest.write(f"{seq[1]},{seq[0]},{id}\n")
    dest.close()


####################################################################

if __name__ == "__main__":

    from SymmetricPolynomial import sympoly
    from Rencontres import rencontres

    PrintProfile(sympoly)
    PrintProfile(rencontres)
    SaveProfiles()
