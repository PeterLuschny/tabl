from _tabltypes import tri, tabl, trow
from _tablsimilarseq import read_seqdata, OEISANumber, SimilarSequences
from _tablsums import tabl_accsum, tabl_altsum, tabl_diagsum, tabl_evensum, tabl_oddsum, tabl_revaccsum, tabl_sum, diag_tabl, tabl_accrevsum
from _tabltransforms import rev_tabl, row_diag, revacc_tabl, row_poly, col_diag, col_poly, inv_tabl, acc_tabl, accrev_tabl, middle, central, left_side, right_side, pos_half, neg_half, trans_seq, invtrans_seq, trans_self, invtrans_self, diag_tabl, poly_tabl, flat_acc, flat_revacc, flat_accrev, trans, poly_diag, transbin_tabl, tabl_lcm, tabl_gcd, tabl_max, invtransbin_tabl, transbin_val, invtransbin_val, trans_sqrs, trans_nat0, trans_nat1


from math import floor
from itertools import count
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
relcsvpath = 'data/TraitCards'
allcsvfile = 'data/allcsv.csv'
csvpath = (path / relcsvpath).resolve()
allcsvpath = (path / allcsvfile).resolve()

def GetDataPath() -> Path: return datapath


# #@


def flat(t: tabl) -> list[int]: 
    if t == [] or t == None: return []
    return [i for row in t for i in row] 


def trim(s: str, lg: int) -> str:
    r = s[:lg]
    p = r.rfind(',')
    return r[:p]


def SeqToFixlenString(seq: list[int], maxlen:int=90, separator=',') -> str:
    stri = "["
    maxl = 3
    for trm in seq:
        s = str(trm) + separator
        maxl += len(s)
        if maxl > maxlen: break
        stri += s
    return stri + "]"


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

    def printer(seq, traitname) -> None:
        next(count_all_traits)
        anum = ""
        if seqnum:
            # TODO optimize this! Push this to OEISANumber.
            # Note: we start at different positions!
            seqstr = SeqToFixlenString(seq, 100, ',')
            anum = OEISANumber(seqstr)
            if anum == "": 
                seqstr = SeqToFixlenString(seq[1:], 100, ',')
                anum = OEISANumber(seqstr)
                if anum == "": 
                    seqstr = SeqToFixlenString(seq[2:], 100, ',')
                    anum = OEISANumber(seqstr)
                    if anum == "": 
                        no_oeis.append(traitname) 
                        return
            next(count_traits_with_anum)

        tstr = SeqToFixlenString(seq, 70, ' ')

        if seqnum:
            print(f"{funname},{traitname},{anum},{tstr}")
            if csvfile != None:
                csvfile.write(f"{funname},{traitname},{anum},{tstr}\n")
        else:
            print(f"{funname},{traitname},{tstr}")
            if csvfile != None:
                csvfile.write(f"{funname},{traitname},{tstr}\n")


    if seqnum:
        print("Triangle,Trait,ANumber,Sequence")
    else:
        print("Triangle,Trait,Sequence")


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
    printer(tabl_lcm(f, dim),  "RowLcm   ")
    printer(tabl_gcd(f, dim),  "RowGcd   ")
    printer(tabl_max(f, dim),  "RowMax   ")
    printer(middle(T),         "Middle   ")
    printer(central(T),        "Central  ")
    printer(left_side(T),      "LeftSide ")
    printer(right_side(T),     "RightSide")
    printer(pos_half(T),       "PosHalf  ")
    printer(neg_half(T),       "NegHalf  ")
    printer(transbin_val(f, maxlen), "BinConV  ")
    printer(invtransbin_val(f, maxlen), "IBinConV ")

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

    # Quick ckeck without A-numbers, recommended.
    Traits(stirling_set, 12)

    # With A-numbers, much slower:
    # Traits(stirling_set, 20, True)

    # very SLOW, but also with similar A-numbers:
    # use SimilarSequences (see the two outcommented lines)
    #Traits(stirling_set, 20, True)

