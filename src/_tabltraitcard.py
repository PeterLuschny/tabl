from _tabltypes import tri, tabl, trow
from _tablsimilarseq import read_seqdata, SimilarSequences 
from _tablsums import tabl_accsum, tabl_altsum, tabl_diagsum, tabl_evensum, tabl_oddsum, tabl_revaccsum, tabl_sum, diag_tabl, tabl_accrevsum
from _tabltransforms import rev_tabl, row_diag, revacc_tabl, row_poly, col_diag, col_poly, inv_tabl, acc_tabl, accrev_tabl, middle, central, left_side, right_side, pos_half, neg_half, trans_seq, invtrans_seq, trans_self, invtrans_self, diag_tabl, poly_tabl, flat_acc, flat_revacc, flat_accrev, trans, poly_diag, transbin_tabl, invtransbin_tabl, transbin_val, invtransbin_val

from pathlib import Path

path = Path(__file__).parent.parent
relprofpath = 'data/profiles.csv'
relsortpath = 'data/sortedprofiles.csv'
relshortdatapath = 'data/short_data.csv'
reldatapath = 'data/oeis_data.csv'
propath = (path / relprofpath).resolve()
sorpath = (path / relsortpath).resolve()
shortdatapath = (path / relshortdatapath).resolve()
datapath = (path / reldatapath).resolve()

def GetDataPath() -> Path: return datapath

# #@

def flat(t: tabl) -> list[int]: 
    return [i for row in t for i in row] 


def SeqToFixlenString(seq: list[int], maxlen:int=90) -> str:
    separator = ","
    stri = "[ "
    maxl = 3
    for trm in seq:
        s = str(trm) + separator
        maxl += len(s)
        if maxl > maxlen: break
        stri += s
    return stri + "]"


def Traits(f: tri, dim: int, seqnum: bool = False) -> None: 

    T  = f.tab(dim)
    R  = f.rev(dim)
    I  = f.inv(dim)
    RI = f.revinv(dim) 
    IR = f.invrev(dim)
    funname = f.id

    maxlen = (dim * (dim + 1)) // 2

    seqdata = []
    if seqnum:
        datapath = GetDataPath()
        seqdata = read_seqdata(datapath)


    def printer(seq, traitname) -> None:
        print(funname, traitname)
        if seqnum: print(SimilarSequences(seqdata, seq))
        print(SeqToFixlenString(seq, 80))
        # sep = ","
        # write(f"{candidates}{sep}{funname}{sep}{traitname}{sep}{seqstr}")


    print(f"\n=================\n{funname}\n")
    print("ANumber,Triangle,Trait,Sequence")

    printer(flat(T), "Triangle ")
    printer(flat(R), "Reverse  ")

    if I != []:
        printer(flat(I),  "Inverse  ")
        printer(flat(RI), "RevInv   ")

    if IR != []:
        printer(flat(IR), "InvRev   ")

    printer(flat_acc(T),                    "AccTri   ")
    printer(flat_revacc(T),                 "RevAccTri")
    printer(flat_accrev(T),                 "AccRevTri")
    printer(flat(diag_tabl(T)),             "DiagTri  ")
    printer(flat(poly_tabl(f, dim)),        "PolyTri  ")
    printer(flat(trans_self(f, dim)),       "ConvTri  ")
    printer(flat(transbin_tabl(f, dim)),    "BinConT  ")
    printer(flat(invtransbin_tabl(f, dim)), "IBinConT ")

    printer(tabl_sum(T),       "Sum      ")
    printer(tabl_evensum(T),   "EvenSum  ")
    printer(tabl_oddsum(T),    "OddSum   ")
    printer(tabl_altsum(T),    "AltSum   ")
    printer(tabl_accsum(T),    "AccSum   ")
    printer(tabl_accrevsum(T), "AccRevSum")
    printer(tabl_revaccsum(T), "RevAccSum")
    printer(tabl_diagsum(T),   "DiagSum  ")
    printer(middle(T),         "Middle   ")
    printer(central(T),        "Central  ")
    printer(left_side(T),      "LeftSide ")
    printer(right_side(T),     "RightSide")
    printer(pos_half(T),       "PosHalf  ")
    printer(neg_half(T),       "NegHalf  ")

    printer(transbin_val(f, maxlen),    "BinConV  ")
    printer(invtransbin_val(f, maxlen), "IBinConV ")

    def TransSqrs(f,n:int)->list[int]: return trans(f,lambda k: k * k, n)
    def TransNat0(f,n:int)->list[int]: return trans(f,lambda k: k, n)
    def TransNat1(f,n:int)->list[int]: return trans(f,lambda k: k + 1, n)

    printer(TransSqrs(f, maxlen),   "TransSqrs")
    printer(TransNat0(f, maxlen),   "TransNat0")
    printer(TransNat1(f, maxlen),   "TransNat1")

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


if __name__ == "__main__":

    from Binomial import binomial
    from Abel import abel
    from Bell import bell
    from StirlingSet import stirling_set
    from StirlingCycle import stirling_cycle
    from Laguerre import laguerre

    # Quick ckeck:
    Traits(stirling_set, 12)

    # very SLOW, but with A-numbers:
    #Traits(stirling_set, 20, True)
