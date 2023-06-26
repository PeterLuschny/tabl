from typing import Callable
from _tablpaths import GetDataPath, GetCsvPath, GetMdPath
from _tabltypes import rgen, tgen, tabl, trow
from _tabltypes import inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper
from _tablpoly import PolyRow0, PolyRow1, PolyRow2, PolyRow3, PolyCol0, PolyCol1, PolyCol2, PolyCol3, PolyDiag, PosHalf, NegHalf, PolyTabl
from _tablsums import RowSum, EvenSum, OddSum, AltSum, AccSum, AccRevSum, AntiDiagSum
from _tabltabls import FlatTabl, FlatAccTabl, FlatRevAccTabl, FlatAccRevTabl, FlatAntiDiagTabl, FlatRevTabl, FlatInvTabl, FlatInvRevTabl, FlatRevInvTabl, FlatDiffxTabl 
from _tabltransforms import FlatBinTabl, FlatInvBinTabl, BinConv, InvBinConv,  RowLcm, RowGcd, RowMax, DiagRow0, DiagRow1, DiagRow2, DiagRow3, DiagCol0, DiagCol1, DiagCol2, DiagCol3, TransSqrs, TransNat0, TransNat1, ColMiddle, ColECentral, ColOCentral, ColLeft, ColRight 


"""
Pretty printing of triangles trait cards.

| A-number | Triangle   | Form | Function  | Sequence                                    |
|----------|------------|------|-----------|---------------------------------------------|
| A000302  | Binomial   | Std  | PolyVal3  | 1, 4, 16, 64, 256, 1024, 4096, 16384        |
| A001333  | SchroederB | Inv  | AltSum    | 1, -1, 3, -7, 17, -41, 99, -239             |
| A006012  | SchroederL | Inv  | AltSum    | 1, -2, 6, -20, 68, -232, 792, -2704         |
| A026302  | Motzkin    | Rev  | Central   | 1, 2, 9, 44, 230, 1242, 6853, 38376         |
| A103194  | Laguerre   | Std  | TransNat0 | 0, 1, 6, 39, 292, 2505, 24306, 263431       |
| A111884  | Lah        | Std  | TransAlts | 1, -1, -1, -1, 1, 19, 151, 1091             |
| A000000  | Laguerre   | Rev  | TransNat1 | 1, 3, 15, 97, 753, 6771, 68983, 783945      |
"""

# #@


def SeqToFixlenString(seq:list[int], maxlen:int=90, separator:str=',') -> str:
    stri = "["
    maxl = 3
    for trm in seq:
        s = str(trm) + separator
        maxl += len(s)
        if maxl > maxlen: break
        stri += s
    return stri + "]"


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
                return data[:7]
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

    zerofree = [t for t in seq[1:] if t != 0]
    if zerofree != seq:
        seqstr = SeqToFixlenString(zerofree, 100, ',')
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
    if t == []: return []
    return [i for row in t for i in row] 



#########################################################

TRAIT: dict[str, Callable[[tabl], trow]] = {}
def RegisterTrait(f: Callable[[tabl], trow]) -> None: 
    TRAIT[f.__name__] = f

TRAIT2: dict[str, Callable[[rgen, int], trow]] = {}
def RegisterTrait2(f: Callable[[rgen, int], trow]) -> None:
    TRAIT2[f.__name__] = f

def register() -> None:

    RegisterTrait(FlatTabl)   # must always come first!
    RegisterTrait(FlatRevTabl)
    RegisterTrait(FlatInvTabl)
    RegisterTrait(FlatRevInvTabl)
    RegisterTrait(FlatInvRevTabl)

    RegisterTrait(FlatAccTabl)
    RegisterTrait(FlatRevAccTabl) # rarely found
    RegisterTrait(FlatAccRevTabl)
    RegisterTrait(FlatAntiDiagTabl)
    RegisterTrait(FlatBinTabl)    # rarely found
    RegisterTrait(FlatInvBinTabl) # rarely found
    RegisterTrait(FlatDiffxTabl)

    RegisterTrait(RowSum)
    RegisterTrait(EvenSum)
    RegisterTrait(OddSum)
    RegisterTrait(AltSum)
    RegisterTrait(AntiDiagSum)
    RegisterTrait(AccSum)
    RegisterTrait(AccRevSum)

    RegisterTrait(RowLcm)
    RegisterTrait(RowGcd)
    RegisterTrait(RowMax)
    RegisterTrait(ColMiddle)
    RegisterTrait(ColECentral)
    RegisterTrait(ColOCentral)
    RegisterTrait(ColLeft)
    RegisterTrait(ColRight)
    
    RegisterTrait(BinConv)
    RegisterTrait(InvBinConv)

# -------------------------------------------

    RegisterTrait2(TransNat0)
    RegisterTrait2(TransNat1)
    RegisterTrait2(TransSqrs)
    # RegisterTrait2(DiagRow0) same as ColRight
    RegisterTrait2(DiagRow1)
    RegisterTrait2(DiagRow2)
    RegisterTrait2(DiagRow3)
    # RegisterTrait2(DiagCol0) same as ColLeft
    RegisterTrait2(DiagCol1)
    RegisterTrait2(DiagCol2)
    RegisterTrait2(DiagCol3)

    RegisterTrait2(PolyTabl)
    # RegisterTrait2(PolyRow0)
    RegisterTrait2(PolyRow1)
    RegisterTrait2(PolyRow2)
    RegisterTrait2(PolyRow3)
    # RegisterTrait2(PolyCol0) same as ColLeft
    # RegisterTrait2(PolyCol1) same as RowSum
    RegisterTrait2(PolyCol2) 
    RegisterTrait2(PolyCol3)
    RegisterTrait2(PolyDiag)
    RegisterTrait2(PosHalf)
    RegisterTrait2(NegHalf)


def PrintTraits(g: tgen, size: int, 
                withanum: bool = False, 
                markdown: bool = True,
                onlythefound: bool = True) -> None:

    trianglename = g.id
    T = g.tab(size)
    gen = g.gen
    anum = g.sim[0]  # Note that the similars are ordered!

    if markdown:

        if withanum:
            print( "| Triangle    | Anum    | Trait    |  Sequence   |")
            print( "| :---        | :---    |  :---    |  :---  |")
        else:
            print( "| Triangle    | Trait   |  Sequence  |")
            print( "| :---        | :---    |  :---      |")

        for traitname, trait in TRAIT.items():
            name = traitname[4:] if traitname.startswith("Flat") else traitname
            tt = trait(T)
            if withanum:
                if anum == '': # which is always the case exept in the first loop
                    if tt != []:
                        anum = GetAnumber(tt)
                        if anum == "": 
                            # print(traitname)
                            if onlythefound: continue
                seqstr = SeqToFixlenString(tt, 70, ' ')    
                print(f'| {trianglename} | {anum:7} | {name:<12} | {seqstr} |')
                anum = '' 
            else:
                seqstr = SeqToFixlenString(tt, 70, ' ')
                print(f'| {trianglename} | {name:<12} | {seqstr} |')

    else: # TXT simple dictionary, no options, no anums 

        for traitname, trait in TRAIT.items():
            name = traitname[4:] if traitname.startswith("Flat") else traitname
            seqstr = SeqToFixlenString(trait(T), 70, ' ')
            print(f'{trianglename}:{name:<14} {seqstr}')

    if markdown:

        for traitname, trait in TRAIT2.items():
            tt = trait(gen, size)
            if withanum:
                if anum == '': # which is always the case exept in the first loop
                    if tt != []:
                        anum = GetAnumber(tt)
                        if anum == "": 
                            # print(traitname)
                            if onlythefound: continue
                seqstr = SeqToFixlenString(tt, 70, ' ')    
                print(f'| {trianglename} | {anum:7} | {traitname:<12} | {seqstr} |')
                anum = '' 
            else:
                seqstr = SeqToFixlenString(tt, 70, ' ')
                print(f'| {trianglename} | {traitname:<12} | {seqstr} |')

    else:  # TXT simple dictionary, no options, no anums 

        for traitname, trait in TRAIT2.items():
            seqstr = SeqToFixlenString(trait(gen, size), 70, ' ')
            print(f'{trianglename}:{traitname:<14} {seqstr}')


def SaveTraitsToFile(g: tgen, size: int, 
                     withanum: bool = False, 
                     markdown: bool = True,
                     onlythefound: bool = True) -> None:

    trianglename = g.id
    T = g.tab(size)
    gen = g.gen
    anum = g.sim[0]  # Note that the similars are ordered!
    print(anum)

    if markdown:
        filepath = (GetMdPath() / f"{trianglename}.md").resolve()    
    else:
        filepath = (GetCsvPath() / f"{trianglename}.csv").resolve()

    with open(filepath, "w") as target:

        if markdown:

            if withanum:
                target.write( "| Triangle    | Anum    | Trait    |  Seq   |\n")
                target.write( "| :---        | :---    |  :---    |  :---  |\n")
            else:
                target.write( "| Triangle    | Trait   |  Seq       |\n")
                target.write( "| :---        | :---    |  :---      |\n")

        else: # CSV
            
            if withanum:
                target.write( "Triangle,Anum,Trait,Sequence\n")
            else:
                target.write( "Triangle,Trait,Sequence\n")

        if markdown:

            for traitname, trait in TRAIT.items():
                name = traitname[4:] if traitname.startswith("Flat") else traitname
                tt = trait(T)
                if withanum:
                    if anum == '': # which is always the case exept in the first loop
                        if tt != []:
                            anum = GetAnumber(tt)
                            if anum == "": 
                                print(traitname)
                                if onlythefound: continue
                    print(anum)
                    seqstr = SeqToFixlenString(tt, 70, ' ')    
                    target.write(f'| {trianglename} | {anum:7} | {name:<12} | {seqstr} |\n')
                    anum = '' 
                else:
                    seqstr = SeqToFixlenString(tt, 70, ' ')
                    target.write(f'| {trianglename} | {name:<12} | {seqstr} |\n')

        else: # CSV

            for traitname, trait in TRAIT.items():
                name = traitname[4:] if traitname.startswith("Flat") else traitname
                
                tt = trait(T)
                if withanum:
                    if anum == '': # which is always the case exept in the first loop
                        if tt != []:
                            anum = GetAnumber(tt)
                            if anum == "": 
                                print(traitname)
                                if onlythefound: continue
                    seqstr = SeqToFixlenString(tt, 70, ' ')    
                    target.write(f'{trianglename},{anum},{name},{seqstr}\n')
                    anum = '' 
                else:
                    seqstr = SeqToFixlenString(tt, 70, ' ')
                    target.write(f'{trianglename},{name},{seqstr}\n')

        if markdown:

            for traitname, trait in TRAIT2.items():
                tt = trait(gen, size)
                if withanum:
                    if anum == '': # which is always the case exept in the first loop
                        if tt != []:
                            anum = GetAnumber(tt)
                            if anum == "": 
                                print(traitname)
                                if onlythefound: continue
                    seqstr = SeqToFixlenString(tt, 70, ' ')    
                    target.write(f'| {trianglename} | {anum:7} | {traitname:<12} | {seqstr} |\n')
                    anum = '' 
                else:
                    seqstr = SeqToFixlenString(tt, 70, ' ')
                    target.write(f'| {trianglename} | {traitname:<12} | {seqstr} |\n')

        else: # CSV

            for traitname, trait in TRAIT2.items():
                tt = trait(gen, size)
                if withanum:
                    anum = '' if tt == [] else GetAnumber(tt)
                    if anum == "": 
                        print(traitname) 
                        if onlythefound: continue
                    seqstr = SeqToFixlenString(tt, 70, ' ')
                    target.write(f'{trianglename},{anum},{traitname},{seqstr}\n')
                else:
                    seqstr = SeqToFixlenString(tt, 70, ' ')
                    target.write(f'{trianglename},{traitname},{seqstr}\n')


def PrintExtendedTraits(T: tgen, size: int, withanum: bool = False, markdown: bool = True) -> None:

    tim: int = size + size // 2

    print("\n# Normal.")
    Tid = T.id; T.id = T.id + ":Std"
    PrintTraits(T, size, withanum, markdown)
    T.id = Tid 

    print("\n# Reverse.")
    r = reversion_wrapper(T, tim)
    PrintTraits(r, size, withanum, markdown)

    I = inversion_wrapper(T, tim)
    if I != None:
        print("\n# Inverse.")
        PrintTraits(I, size, withanum, markdown)

    r = revinv_wrapper(T, tim)
    if r != None:
        print("\n# Reverse of inverse.")
        PrintTraits(r, size, withanum, markdown)

    r = invrev_wrapper(T, tim)
    if r != None:
        print("\n# Inverse of reverse.")
        PrintTraits(r, size, withanum, markdown)


def SaveExtendedTraitsToCSV(G: tgen, size: int) -> None:

    # register()

    tim: int = size + size // 2
    R = reversion_wrapper(G, tim)
    I = inversion_wrapper(G, tim)
    cases = [G, R]
    
    if I != None:
        cases.append(I)

    filepath = (GetCsvPath() / f"{G.id}X.csv").resolve()
    savedid = G.id
    G.id = G.id + ":Std"
    

    with open(filepath, "w") as target:

        target.write( "Triangle,Anum,Trait,Sequence\n")

        for g in cases: 
            
            trianglename = g.id
            T = g.tab(size)
            gen = g.gen
            print('#', trianglename)

            for traitname, trait in TRAIT.items():
                name = traitname[4:] if traitname.startswith("Flat") else traitname
                tt = trait(T)
                anum = '' if tt == [] else GetAnumber(tt)
                if anum == "": 
                    print(traitname) 
                    continue
                seqstr = SeqToFixlenString(tt, 70, ' ')
                target.write(f'{trianglename},{anum},{name},{seqstr}\n')

            for traitname, trait in TRAIT2.items():
                tt = trait(gen, size)
                anum = '' if tt == [] else GetAnumber(tt)
                if anum == "": 
                    print(traitname) 
                    continue
                seqstr = SeqToFixlenString(tt, 70, ' ')
                target.write(f'{trianglename},{anum},{traitname},{seqstr}\n')

    G.id = savedid


def PrintAllTraitsWithAnumber(size: int) -> None:
    for fun in tabl_fun:
        PrintTraits(fun, size, withanum = True)


def PrintAllTraits(size: int) -> None:
    for fun in tabl_fun:
        PrintTraits(fun, size, withanum = False)


def SaveAllFoundTraitsToCSV() -> None:
    register()
    for fun in tabl_fun:
        print("#", fun.id)
        SaveTraitsToFile(fun, 20, 
                         withanum = True,
                         markdown = False,
                         onlythefound = True)


def SaveAllTraitsToCSV() -> None:
    register()
    for fun in tabl_fun:
        print("#", fun.id)
        SaveTraitsToFile(fun, 20,
                         withanum = True,
                         markdown = False,
                         onlythefound = False)


def SaveAllExtendedTraitsToCSV() -> None:
    register()
    for fun in tabl_fun:
        print("##", fun.id)
        SaveExtendedTraitsToCSV(fun, 20)



if __name__ == "__main__":

    from tabl import tabl_fun
    from Abel import Abel
    from Bell import Bell
    from Lah import Lah
    from StirlingSet import StirlingSet
    from Motzkin import Motzkin
    from Binomial import Binomial
    from CatalanSqr import CatalanSqr
    from PowLaguerre import PowLaguerre
    from LabeledGraphs import LabeledGraphs
    from BinomialCatalan import BinomialCatalan
    from BinomialBell import BinomialBell

    register()

    # SaveAllTraitsToCSV()

    # SaveExtendedTraitsToCSV(StirlingSet, 20) 
    # SaveAllExtendedTraitsToCSV()
    # SaveAllFoundTraitsToCSV()

    
    #SaveTraitsToFile(LabGraphs, 20,
    #                    withanum = True,
    #                    markdown = False,
    #                    onlythefound = False)
    
    #PrintTraits(BinomialCatalan, 20,
    #            withanum = True,
    #            markdown = True,
    #            onlythefound = False)
    
    PrintTraits(BinomialBell, 20,
                withanum = True,
                markdown = True,
                onlythefound = False)
    
    #SaveTraitsToFile(Lah, 20, 
    #                withanum = True, 
    #                markdown = False,
    #                onlythefound = False)

    # SEQ = StirlingSet
    #PrintTraits(SEQ, 12, withanum = False, markdown = False)
    # With A-numbers, but slower:
    #PrintTraits(SEQ, 12, withanum = False, markdown = True)

    # Greater size increases the precision of the anumber.
    # Creates a md file which saves all sequences.
    # SaveTraitsToFile(SEQ, 20, withanum = True, markdown = True)

    # Creates a csv file which saves only the sequences found.
    # SaveTraitsToFile(SEQ, 20, withanum = True, markdown = False)

    # PrintExtendedTraits(SEQ, 12, withanum = False, markdown = True)

    #for fun in tabl_fun:
    #    PrintExtendedTraits(fun, 12, False)
   
    print("Done")

'''
for fun in tabl_fun:
        PrintTraits(fun, 20, True)

for traitname, hits in HITS.items():
    print(f'| {hits} | {traitname:<16} |')


[ 0]  6  FlatDiffx
[ 1]  7  RevAccTabl
[ 2] 11  AccRevTabl
[ 3] 12  InvRevTabl
[ 4] 13  AccTabl
[ 5] 14  RowLcm
[ 6] 15  Poly
#------------------- 
[ 7] 19  TransSqrs
[ 8] 22  RevInvTabl
[ 9] 28  AntiDiagTabl
[10] 28  PolyDiag
[11] 29  ColMiddle
[12] 29  InvTabl
[13] 32  AccSum
[14] 32  BinConv
[15] 32  InvBinConv
[16] 34  AccRevSum
[17] 34  TransNat1
[18] 35  PolyRow3
[19] 36  PolyCol3
[20] 40  AntiDiagSum
[21] 40  TransNat0
[22] 42  OddSum
[23] 45  EvenSum
[24] 45  RowMax
[25] 46  NegHalf
[26] 47  PosHalf
[27] 48  PolyCol2
[28] 51  ColCentral
[29] 53  RowGcd
[30] 54  RevTabl
[31] 55  DiagRow3
[32] 57  AltSum
[33] 58  DiagCol3
[34] 60  DiagCol2
[35] 61  DiagRow2
[36] 65  DiagCol1
[37] 65  PolyRow2
[38] 66  DiagRow1
--
[39] 67  ColLeft
[40] 67  ColRight
[41] 67  * DiagCol0
[42] 67  * DiagRow0
[43] 67  Tabl
[44] 67  * PolyCol0
[45] 67  * PolyCol1
[46] 67  * PolyRow0
[47] 67  PolyRow1
[48] 67  RowSum

DiagCol0 = PolyCol0 = ColLeft
DiagRow0 = PolyRow0 = ColRight
RowSum   = PolyCol1

'''


