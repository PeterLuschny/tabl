
from _tablpoly import PolyRow0,PolyRow1,PolyRow2,PolyRow3,PolyCol0,PolyCol1,PolyCol2,PolyCol3, PolyDiag,PosHalf,NegHalf,PolyRow,PolyCol
from _tablsums import RowSum,EvenSum, OddSum,AltSum,AccSum,AccRevSum,AntiDiagSum
from _tabltypes import tgen, tabl, inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper

def flat(t: tabl) -> list[int]: 
    """Flatten table to sequence

    Args:
        t (tabl): table

    Returns:
        list[int]: sequence
    """
    if t == []: return []
    return [i for row in t for i in row] 


# #@

def Profile(T: tgen, hor: int = 10) -> dict[str, list[int]]:

    d: dict[str, list[int]] = {}
    t: tabl = T.tab(hor)
    ver: int = hor // 2

    # Triangle flattened
    d["Triangle"] = flat(T.tab(6))

    # Row sums
    d["RowSum"] = RowSum(t)
    d["EvenSum"] = EvenSum(t)
    d["OddSum"] = OddSum(t)
    d["AltSum"] = AltSum(t)
    d["AccSum"] = AccSum(t)
    d["AccRevSum"] = AccRevSum(t)
    d["AntiDiagSum"] = AntiDiagSum(t)

    # DiagsAsRowArray
    rows: int = ver
    cols: int = hor
    for j in range(rows):
        d["DiagRow" + str(j)] = [T.gen(j + k)[k] for k in range(cols)]

    # DiagsAsColArray
    rows = hor
    cols = ver
    for j in range(cols):
        d["DiagCol" + str(j)] = [T.gen(j + k)[j] for k in range(rows)]

    # RowPolyArray
    rows = ver
    cols = hor
    for j in range(rows):
        d["PolyRow" + str(j)] = PolyRow(T.gen, j, cols)

    # ColPolyArray
    rows = ver
    cols = hor
    for j in range(rows):
        if j == 1:
            continue
        d["PolyCol" + str(j)] = PolyCol(T.gen, j, cols)

    return d


counter: int = 0

def PrintProfile(T: tgen, dim: int, format: str) -> None:

    d: dict[str, list[int]] = Profile(T, dim)

    if format == 'twolines':
        for seq in d.items():
            print(f"{T.id}:{seq[0]}\n{seq[1]}")

    if format == 'oneline':
        print(T.id)
        for seq in d.items():
            print(f"{seq[0]}, {seq[1]}")
        print()

    if format == 'nonames':
        global counter
        for seq in d.items():
            counter += 1
            print(seq[1])


def PrintExtendedProfile(T: tgen, dim: int, format: str) -> None:

    tim: int = dim + dim // 2

    PrintProfile(T, dim, format)

    I = inversion_wrapper(T, tim)
    if I != None:
        PrintProfile(I, dim, format)

    R = reversion_wrapper(T, tim)
    PrintProfile(R, dim, format)

    r = revinv_wrapper(T, tim)
    if r != None:
        PrintProfile(r, dim, format)

    r = invrev_wrapper(T, tim)
    if r != None:
        PrintProfile(r, dim, format)

    if format == 'nonames':
        global counter
        print(counter, "sequences generated.")


if __name__ == "__main__":

    from Rencontres import Rencontres
    from Motzkin import Motzkin
    from Leibniz import Leibniz
    from ChebyshevS import ChebyshevS

    dim = 14
    format = 'nonames' # 'twolines' #

    F = Motzkin
    #PrintProfile(Leibniz, dim, 'twolines')
    #PrintProfile(Motzkin, dim, format)
    PrintProfile(F, dim, 'twolines')
    PrintExtendedProfile(F, dim, 'oneline')
    #PrintExtendedProfile(Motzkin, dim, format)
