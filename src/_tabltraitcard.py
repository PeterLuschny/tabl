from itertools import count
from math import floor
from pathlib import Path
from _tablpaths import GetDataPath
from _tabltypes import tri, tabl
from _tablsimilartri import GetSimilarTriangles
from _tablsums import tabl_accsum, tabl_altsum, tabl_diagsum, tabl_evensum, tabl_oddsum, tabl_revaccsum, tabl_sum, diag_tabl, tabl_accrevsum
from _tabltransforms import row_diag, row_poly, col_diag, col_poly, middle, central, left_side, right_side, pos_half, neg_half, trans_self, diag_tabl, poly_tabl, flat_acc, flat_revacc, flat_accrev, poly_diag, transbin_tabl, tabl_lcm, tabl_gcd, tabl_max, invtransbin_tabl, transbin_val, invtransbin_val, trans_sqrs, trans_nat0, trans_nat1, SeqToFixlenString

# #@


def FindSequence(seq: str) -> str:
    """Search for a match in the database.
    Nota bene: The database is assumed to have abs terms!

    Args:
        seq (str): The stringified sequence

    Returns:
        str: The oeis A-number if found, "" otherwise.
    """
    datapath = GetDataPath()
    with open(datapath, "r") as database:
        for data in database:
            if seq in data:
                return data[:6]
    return ""


def GetAnumber(seq: list[int]) -> str:
    """Search for a match in the database.
    Increase the 'offset' twice if not found.

    Args:
        seq (list[int]): The sequence as a list of integers

    Returns:
        str: The oeis A-number if found, "" otherwise
    """
    for n in range(3):
        seqstr = SeqToFixlenString(seq[n:], 100, ',')
        abstr = seqstr.replace("-", "").replace(" ", "")[1:-1]
        anum = FindSequence(abstr)
        if anum != "": 
            return anum
    return ""


def flat(t: tabl) -> list[int]: 
    """Flatten table to sequence

    Args:
        t (tabl): table

    Returns:
        list[int]: sequence
    """
    if t == [] or t == None: return []
    return [i for row in t for i in row] 


def Traits(f: tri, dim: int, seqnum: bool = False, csvfile = None) -> None: 
    """Generate the traits of a triangle and look them up
    in the database, then write the result in a csv file.

    Args:
        f (tri): Triangle (function)
        dim (int): Length of triangle table to generate
        seqnum (bool, optional): Look up the oeis A-number. Defaults to False.
        csvfile (TextIOWrapper, optional): Open csv file. Defaults to None.
    """
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

    def printer(seq: list[int], traitname: str, tria: bool=False) -> None:
        """Writes to the csv file if given or prints otherwise.

        Args:
            seq (list[int]): sequence
            traitname (str): trait
            tria (bool, optional): Is seq a triangle?. Defaults to False.
        """    
        next(count_all_traits)

        seqstr = SeqToFixlenString(seq, 70, ' ')
        line = ""

        if seqnum:
            #if tria:  # needs function, not tabl
            #    anum = GetSimilarTriangles()
            #else:
            anum = GetAnumber(seq)
            if anum == "": 
                sanum = "nothing"
                no_oeis.append(traitname) 
            else:
                next(count_traits_with_anum)
                sanum = 'A' + str(anum)

            line = f"{funname},{traitname},{sanum},{seqstr}"
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

    printer(flat_acc(T),                    "TriAcc   ", True)
    printer(flat_revacc(T),                 "TriRevAcc", True)
    printer(flat_accrev(T),                 "TriAccRev", True)
    printer(flat(diag_tabl(T)),             "TriDiag  ", True)
    printer(flat(poly_tabl(f, dim)),        "TriPoly  ", True)
    printer(flat(trans_self(f, dim)),       "TriConv  ", True)
    printer(flat(transbin_tabl(f, dim)),    "TriBin   ", True)
    printer(flat(invtransbin_tabl(f, dim)), "TriInvBin", True)

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
    
    # Quick ckeck without A-numbers, recommended.
    # Traits(lah, 12)

    # With A-numbers, much slower:
    Traits(lah, 20, True)
