from tabltools import row_poly, col_poly
from tablsums import tabl_sum, tabl_evensum, tabl_oddsum, tabl_altsum


def Profile(T, hor=8, ver=5):

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


"""
Trait,ANumber,Sequence
Triangle,A053121,[1 0 1 1 0 1 0 2 0 1 ]
Reverse,A052173,[1 1 0 1 0 1 1 0 2 0 ]
Inverse,A049310,[1 0 1 -1 0 1 0 -2 0 1 ]
RevInv,A053119,[1 1 0 1 0 -1 1 0 -2 0 ]
DiagTri,nothing,[1 0 1 1 0 0 2 2 1 0 ]
PolyTri,nothing,[1 0 1 1 1 1 0 2 2 1 ]
Sum,A001405,[1 1 2 3 6 10 20 35 70 126 ]
EvenSum,A126869,[1 0 2 0 6 0 20 0 70 0 ]
OddSum,A138364,[0 1 0 3 0 10 0 35 0 126 ]
AltSum,A001405,[1 -1 2 -3 6 -10 20 -35 70 -126 ]
DiagSum,nothing,[1 0 2 0 5 0 14 0 42 0 ]
Middle,nothing,[1 0 0 2 3 0 0 14 20 0 ]
Central,nothing,[1 0 3 0 20 0 154 0 1260 0 ]
LeftSide,A126120,[1 0 1 0 2 0 5 0 14 0 ]
RightSide,A000012,[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 ]
PosHalf,A121724,[1 1 5 9 45 97 485 1145 5725 14289 ]
NegHalf,A121724,[1 1 5 9 45 97 485 1145 5725 14289 ]
PolyVal2,A054341,[1 2 5 12 30 74 185 460 1150 2868 ]
PolyVal3,A126931,[1 3 10 33 110 366 1220 4065 13550 45162 ]
BinConv,A344500,[1 1 2 7 21 66 216 715 2395 8101 ]
IBinConv,A344500,[1 1 2 7 21 66 216 715 2395 8101 ]
TransSqrs,nothing,[0 1 4 11 28 66 152 339 748 1622 ]
TransNat0,A045621,[0 1 2 5 10 22 44 93 186 386 ]
TransNat1,A000079,[1 2 4 8 16 32 64 128 256 512 ]
"""
