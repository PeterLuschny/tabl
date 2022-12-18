from _tabltypes import tri, tabl, trow
from _tablsums import tabl_accsum, tabl_altsum, tabl_diagsum, tabl_evensum, tabl_oddsum, tabl_revaccsum, tabl_sum, diag_tabl, tabl_accrevsum
from _tabltransforms import rev_tabl, row_diag, revacc_tabl, row_poly, col_diag, col_poly, inv_tabl, acc_tabl, accrev_tabl, middle, central, left_side, right_side, pos_half, neg_half, trans_seq, invtrans_seq, trans_self, invtrans_self, diag_tabl, poly_tabl, flat_acc, flat_revacc, flat_accrev, trans, poly_diag, transbin_tabl, invtransbin_tabl, transbin_val, invtransbin_val

# #@


def GetSeqnum(S: list[int]) -> str:
    return "--" # "A123456"


def SeqToFixlenString(seq: list[int], maxlen:int=90) -> str:
    separator = " "
    stri = "[ "
    maxl = 3
    for trm in seq:
        s = str(trm) + separator
        maxl += len(s)
        if maxl > maxlen: break
        stri += s
    return stri + "]"

def Flat(t: tabl) -> list[int]: 
    return [i for row in t for i in row] 

def FlatAcc   (T:tabl)->list[int]: return flat_acc(T)
def FlatRevAcc(T:tabl)->list[int]: return flat_revacc(T)
def FlatAccRev(T:tabl)->list[int]: return flat_accrev(T)

def DiagTri  (T:tabl)->list[int]: return diag_tabl(T)
def PolyTri  (f:tri, n:int)->list[int]: return poly_tabl(f, n)
def ConvTri  (f:tri, n:int)->list[int]: return trans_self(f, n)
def BinConT  (f:tri, n:int)->list[int]: return transbin_tabl(f, n)
def IBinConT (f:tri, n:int)->list[int]: return invtransbin_tabl(f, n)

def Sum      (T:tabl)->list[int]: return tabl_sum(T)
def EvenSum  (T:tabl)->list[int]: return tabl_evensum(T)
def OddSum   (T:tabl)->list[int]: return tabl_oddsum(T)
def AltSum   (T:tabl)->list[int]: return tabl_altsum(T)
def AccSum   (T:tabl)->list[int]: return tabl_accsum(T)
def AccRevSum(T:tabl)->list[int]: return tabl_accrevsum(T)
def RevAccSum(T:tabl)->list[int]: return tabl_revaccsum(T)
def DiagSum  (T:tabl)->list[int]: return tabl_diagsum(T)
def Middle   (T:tabl)->list[int]: return middle(T)
def Central  (T:tabl)->list[int]: return central(T)
def LeftSide (T:tabl)->list[int]: return left_side(T)
def RightSide(T:tabl)->list[int]: return right_side(T)
def PosHalf  (T:tabl)->list[int]: return pos_half(T)
def NegHalf  (T:tabl)->list[int]: return neg_half(T)
def BinConV  (f:tri, n:int)->list[int]: return transbin_val(f, n)
def IBinConV (f:tri, n:int)->list[int]: return invtransbin_val(f, n)
def TransSqrs(f,n:int)->list[int]: return trans(f,lambda k: k * k, n)
def TransNat0(f,n:int)->list[int]: return trans(f,lambda k: k, n)
def TransNat1(f,n:int)->list[int]: return trans(f,lambda k: k + 1, n)
def DiagRow0 (f:tri,n:int)->list[int]: return row_diag(f,0,n)
def DiagRow1 (f:tri,n:int)->list[int]: return row_diag(f,1,n)
def DiagRow2 (f:tri,n:int)->list[int]: return row_diag(f,2,n)
def DiagRow3 (f:tri,n:int)->list[int]: return row_diag(f,3,n)
def DiagCol0 (f:tri,n:int)->list[int]: return col_diag(f,0,n)
def DiagCol1 (f:tri,n:int)->list[int]: return col_diag(f,1,n)
def DiagCol2 (f:tri,n:int)->list[int]: return col_diag(f,2,n)
def DiagCol3 (f:tri,n:int)->list[int]: return col_diag(f,3,n)
def PolyRow0 (f:tri,n:int)->list[int]: return row_poly(f,0,n)
def PolyRow1 (f:tri,n:int)->list[int]: return row_poly(f,1,n)
def PolyRow2 (f:tri,n:int)->list[int]: return row_poly(f,2,n)
def PolyRow3 (f:tri,n:int)->list[int]: return row_poly(f,3,n)
def PolyCol0 (f:tri,n:int)->list[int]: return col_poly(f,0,n)
def PolyCol1 (f:tri,n:int)->list[int]: return col_poly(f,1,n)
def PolyCol2 (f:tri,n:int)->list[int]: return col_poly(f,2,n)
def PolyCol3 (f:tri,n:int)->list[int]: return col_poly(f,3,n)
def PolyDiag (f:tri,n:int)->list[int]: return poly_diag(f, n)


def Traits(f: tri, dim: int, seqnum: bool = False) -> None: 

    T  = f.tab(dim)
    R  = f.rev(dim)
    I  = f.inv(dim)
    RI = f.revinv(dim) 
    IR = f.invrev(dim)
    funname = f.id

    maxlen = (dim * (dim + 1)) // 2

    def printer(S, traitname) -> None:
        sep = ","
        anum = GetSeqnum(S) if seqnum else ""
        print(f"{anum}{sep}{funname}{sep}{traitname}{sep}{SeqToFixlenString(S, 80)}")

    print("\n=================")
    print(funname)
    print()
    print("ANumber,Triangle,Trait,Sequence")

    printer(Flat(T), "Triangle ")
    printer(Flat(R), "Reverse  ")

    if I != []:
        printer(Flat(I),  "Inverse  ")
        printer(Flat(RI), "RevInv   ")

    if IR != []:
        printer(Flat(IR), "InvRev   ")

    printer(FlatAcc(T),             "AccTri   ")
    printer(FlatRevAcc(T),          "RevAccTri")
    printer(FlatAccRev(T),          "AccRevTri")
    printer(Flat(DiagTri(T)),       "DiagTri  ")
    printer(Flat(PolyTri(f, dim)),  "PolyTri  ")
    printer(Flat(ConvTri(f, dim)),  "ConvTri  ")
    printer(Flat(BinConT(f, dim)),  "BinConT  ")
    printer(Flat(IBinConT(f, dim)), "IBinConT ")

    printer(Sum(T),       "Sum      ")
    printer(EvenSum(T),   "EvenSum  ")
    printer(OddSum(T),    "OddSum   ")
    printer(AltSum(T),    "AltSum   ")
    printer(AccSum(T),    "AccSum   ")
    printer(RevAccSum(T), "RevAccSum")
    printer(DiagSum(T),   "DiagSum  ")
    printer(Middle(T),    "Middle   ")
    printer(Central(T),   "Central  ")
    printer(LeftSide(T),  "LeftSide ")
    printer(RightSide(T), "RightSide")
    printer(PosHalf(T),   "PosHalf  ")
    printer(NegHalf(T),   "NegHalf  ")

    printer(BinConV(f, maxlen),  "BinConV  ")
    printer(IBinConV(f, maxlen), "IBinConV ")

    printer(TransSqrs(f, maxlen), "TransSqrs")
    printer(TransNat0(f, maxlen), "TransNat0")
    printer(TransNat1(f, maxlen), "TransNat1")

    printer(DiagRow0(f, maxlen), "DiagRow0 ")
    printer(DiagRow1(f, maxlen), "DiagRow1 ")
    printer(DiagRow2(f, maxlen), "DiagRow2 ")
    printer(DiagRow3(f, maxlen), "DiagRow3 ")
    printer(DiagCol0(f, maxlen), "DiagCol0 ")
    printer(DiagCol1(f, maxlen), "DiagCol1 ")
    printer(DiagCol2(f, maxlen), "DiagCol2 ")
    printer(DiagCol3(f, maxlen), "DiagCol3 ")
    printer(PolyRow0(f, maxlen), "PolyRow0 ")
    printer(PolyRow1(f, maxlen), "PolyRow1 ")
    printer(PolyRow2(f, maxlen), "PolyRow2 ")
    printer(PolyRow3(f, maxlen), "PolyRow3 ")
    printer(PolyCol0(f, maxlen), "PolyCol0 ")
    printer(PolyCol1(f, maxlen), "PolyCol1 ")
    printer(PolyCol2(f, maxlen), "PolyCol2 ")
    printer(PolyCol3(f, maxlen), "PolyCol3 ")
    printer(PolyDiag(f, maxlen), "PolyDiag ")


if __name__ == "__main__":

    from Binomial import binomial
    from Abel import abel
    from Bell import bell
    from StirlingSet import stirling_set
    from StirlingCycle import stirling_cycle
    from Laguerre import laguerre

    Traits(stirling_set, 20, True)
