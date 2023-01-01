from _tabltypes import tri, tabl, trow
from _tablsums import tabl_accsum, tabl_altsum, tabl_diagsum, tabl_evensum, tabl_oddsum, tabl_revaccsum, tabl_sum, diag_tabl, tabl_accrevsum
from _tabltransforms import rev_tabl, row_diag, revacc_tabl, row_poly, col_diag, col_poly, inv_tabl, acc_tabl, accrev_tabl, middle, central, left_side, right_side, pos_half, neg_half, trans_seq, invtrans_seq, trans_self, invtrans_self, diag_tabl, poly_tabl, flat_acc, flat_revacc, flat_accrev, trans, poly_diag, transbin_tabl, tabl_lcm, tabl_gcd, tabl_max, invtransbin_tabl, transbin_val, invtransbin_val, trans_sqrs, trans_nat0, trans_nat1, SeqToFixlenString


from math import floor
from itertools import count
from pathlib import Path

path = Path(__file__).parent.parent
relprofpath = 'data/profiles.csv'
relsortpath = 'data/sortedprofiles.csv'

relshortdatapath = 'data/short_data.csv'
shortdatapath = (path / relshortdatapath).resolve()

reldatapath = 'data/oeis_data.csv'
longdatapath = (path / reldatapath).resolve()

propath = (path / relprofpath).resolve()
sorpath = (path / relsortpath).resolve()

relcsvpath = 'data/TraitCards'
allcsvfile = 'data/allcsv.csv'
csvpath = (path / relcsvpath).resolve()
allcsvpath = (path / allcsvfile).resolve()

def GetLongDataPath() -> Path: return longdatapath
def GetShortDataPath() -> Path: return shortdatapath


# #@


# Nota bene: OEIS data with abs terms!
def FindAnumber(seq: str) -> str:
    datapath = GetLongDataPath()
    with open(datapath, "r") as oeisdata:
        for data in oeisdata:
            if seq in data:
                return data[:6]
    return ""


def GetAnumber(seq: list[int]) -> str:
    for n in range(3):
        seqstr = SeqToFixlenString(seq[n:], 100, ',')
        abstr = seqstr.replace("-", "").replace(" ", "")[1:-1]
        anum = FindAnumber(abstr)
        if anum != "": 
            return anum
    return ""


def flat(t: tabl) -> list[int]: 
    if t == [] or t == None: return []
    return [i for row in t for i in row] 



def Traits(f: tri, dim: int, seqnum: bool = False, csvfile = None) -> None: 

    T  = f.tab(dim) 
    R  = f.rev(dim) 
    I  = f.inv(dim) 
    RI = f.revinv(dim) 
    IR = f.invrev(dim) 
    # funname = f.id
    funname = f.__name__

    maxlen = (dim * (dim + 1)) // 2

    count_all_traits = count()
    count_traits_with_anum = count()
    no_oeis = []

    def printer(seq: list[int], traitname: str) -> None:
        next(count_all_traits)

        seqstr = SeqToFixlenString(seq, 70, ' ')
        line = ""

        if seqnum:
            anum = GetAnumber(seq)
            if anum == "": 
                anum = "nothing"
                no_oeis.append(traitname) 
            else:
                next(count_traits_with_anum)

            line = f"{funname},{traitname},{anum},{seqstr}"
            if csvfile != None:
                csvfile.write(line + '\n')
        else:
            line = f"{funname},{traitname},{seqstr}"
            if csvfile != None:
                csvfile.write(line + '\n')
        print(line)


    printer(flat(T), "Triangle ")
    printer(flat(R), "TriRev   ")

    if I != []:
        printer(flat(I),  "TriInv   ")
        printer(flat(RI), "TriRevInv")

    if IR != []:
        printer(flat(IR), "TriInvRev")

    printer(flat_acc(T),                    "TriAcc   ")
    printer(flat_revacc(T),                 "TriRevAcc")
    printer(flat_accrev(T),                 "TriAccRev")
    printer(flat(diag_tabl(T)),             "TriDiag  ")
    printer(flat(poly_tabl(f, dim)),        "TriPoly  ")
    printer(flat(trans_self(f, dim)),       "TriConv  ")
    printer(flat(transbin_tabl(f, dim)),    "TriBin   ")
    printer(flat(invtransbin_tabl(f, dim)), "TriInvBin")

    printer(tabl_sum(T),       "Sum      ")
    printer(tabl_evensum(T),   "EvenSum  ")
    printer(tabl_oddsum(T),    "OddSum   ")
    printer(tabl_altsum(T),    "AltSum   ")
    printer(tabl_accsum(T),    "AccSum   ")
    printer(tabl_accrevsum(T), "AccRevSum")
    printer(tabl_revaccsum(T), "RevAccSum")
    printer(tabl_diagsum(T),   "DiagSum  ")
    printer(tabl_lcm(f, dim),  "RowLcm   ")
    printer(tabl_gcd(f, dim),  "RowGcd   ")
    printer(tabl_max(f, dim),  "RowMax   ")
    printer(middle(T),         "Middle   ")
    printer(central(T),        "Central  ")
    printer(left_side(T),      "LeftSide ")
    printer(right_side(T),     "RightSide")
    printer(pos_half(T),       "PosHalf  ")
    printer(neg_half(T),       "NegHalf  ")
    printer(transbin_val(f, maxlen),    "Bin      ")
    printer(invtransbin_val(f, maxlen), "InvBin   ")

    printer(trans_sqrs(f, maxlen),  "TransSqrs")
    printer(trans_nat0(f, maxlen),  "TransNat0")
    printer(trans_nat1(f, maxlen),  "TransNat1")
    printer(row_diag(f, 0, maxlen), "DiagRow0 ")
    printer(row_diag(f, 1, maxlen), "DiagRow1 ")
    printer(row_diag(f, 2, maxlen), "DiagRow2 ")
    printer(row_diag(f, 3, maxlen), "DiagRow3 ")
    printer(col_diag(f, 0, maxlen), "DiagCol0 ")
    printer(col_diag(f, 1, maxlen), "DiagCol1 ")
    printer(col_diag(f, 2, maxlen), "DiagCol2 ")
    printer(col_diag(f, 3, maxlen), "DiagCol3 ")
    printer(row_poly(f, 0, maxlen), "PolyRow0 ")
    printer(row_poly(f, 1, maxlen), "PolyRow1 ")
    printer(row_poly(f, 2, maxlen), "PolyRow2 ")
    printer(row_poly(f, 3, maxlen), "PolyRow3 ")
    printer(col_poly(f, 0, maxlen), "PolyCol0 ")
    printer(col_poly(f, 1, maxlen), "PolyCol1 ")
    printer(col_poly(f, 2, maxlen), "PolyCol2 ")
    printer(col_poly(f, 3, maxlen), "PolyCol3 ")
    printer(poly_diag(f, maxlen),   "PolyDiag ")

    if seqnum:
        atraits = next(count_all_traits)
        ntraits = next(count_traits_with_anum)
        perc = floor(100 * ntraits / atraits)
        w = f"# {f.__name__}, {atraits} traits, {ntraits} A-numbers,{perc}%"
        if csvfile != None: csvfile.write(w)
        print(w)
        print(f"Not found in the OEIS: {no_oeis}\n")


if __name__ == "__main__":

    from Abel import abel
    from Bell import bell
    from Lah import lah
    from Binomial import binomial
    from StirlingSet import stirling_set
    from StirlingCyc import stirling_cycle
    from ChebyshevT import chebyshevT
    from Laguerre import laguerre
    from Fubini import fubini
    from Eulerian import eulerian
    from Catalan import catalan
    from Motzkin import motzkin
    from Narayana import narayana
    from Baxter import baxter
    from ChristTree import ctree
    from SchroederL import schroederL

    # Quick ckeck without A-numbers, recommended.
    # Traits(catalan, 12, True)

    # With A-numbers, much slower:
    Traits(schroederL, 20, True)
