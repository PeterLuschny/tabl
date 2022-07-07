from tabltools import row_poly, col_poly
from tablsums import tabl_sum, tabl_evensum, tabl_oddsum, tabl_altsum

#@

def Profile(T, hor=10, ver=5):

    d = {}
    tabl = T(-hor)

    # Triangle flattened
    d["tabflt"] = tabl[0] + tabl[1] + tabl[2] + tabl[3]

    # Row sums
    d["rowsum"] = tabl_sum(tabl)
    d["evesum"] = tabl_evensum(tabl)
    d["oddsum"] = tabl_oddsum(tabl)
    d["altsum"] = tabl_altsum(tabl)

    # DiagsAsRowArray
    rows = ver
    cols = hor
    for j in range(rows):
        d["dirow" + str(j)] = [T(j + k, k) for k in range(cols)]

    # DiagsAsColArray
    rows = hor
    cols = ver
    for j in range(cols):
        d["dicol" + str(j)] = [T(j + k, j) for k in range(rows)]

    # RowPolyArray
    rows = ver
    cols = hor
    for j in range(rows):
        d["porow" + str(j)] = row_poly(T, j, cols)

    # ColPolyArray
    rows = ver
    cols = hor
    for j in range(rows):
        d["pocol" + str(j)] = col_poly(T, j, cols)

    return d


def PrintProfile(T):
    d = Profile(T)

    print()
    print(T.id)
    for seq in d.items():
        print(f"{seq[0]}, {seq[1]}")
    print()


####################################################################

if __name__ == "__main__":

    from SymmetricPolynomial import sympoly
    from Rencontres import rencontres

    PrintProfile(sympoly)
    PrintProfile(rencontres)
