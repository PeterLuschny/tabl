from _tabltypes import tgen, tabl
from _tabltypes import inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper
from _tabltraits import RegisterTraits, RegisterGenericTables
from _tablpaths import GetDataPath, GetCsvPath, GetMdPath
from _tabldata import fnv_hash, querydbhash, querydbseq 


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

STRINGLEN = 60

def SeqToFixlenString(seq:list[int], maxlen:int=STRINGLEN, separator:str=',') -> str:
    # fnv = fnv_hash(seq, True)
    # isin = queryoeis(fnv, seq, oeis_cur)
    stri = " | "
    maxl = 3
    for trm in seq:
        s = str(trm) + separator
        maxl += len(s)
        if maxl > maxlen: break
        stri += s
    return stri 

def PrintTraits(g: tgen, size: int, 
                withanum: bool = False, 
                markdown: bool = True,
                onlythefound: bool = True) -> None:
    print("Sorry!")


def PrintExtendedTraits(T: tgen, size: int, withanum: bool = False, markdown: bool = True) -> None:

    tim: int = size + size // 2

    print("\n# Normal.")
    Tid = T.id; T.id = T.id + ":Std"
    PrintTraits(T, size, withanum, markdown)
    T.id = Tid 

    print("\n# Reverse.", '*-*' * 20)
    r = reversion_wrapper(T, tim)
    PrintTraits(r, size, withanum, markdown)

    I = inversion_wrapper(T, tim)
    if I != None:
        print("\n# Inverse.", '*-*' * 20)
        PrintTraits(I, size, withanum, markdown)
    else:
        print("\nInfo: Inverse does not exists!\n")
    
    r = revinv_wrapper(T, tim)
    if r != None:
        print("\n# Reverse of inverse.", '*-*' * 20)
        PrintTraits(r, size, withanum, markdown)
    else:
        print("\nInfo: Reverse of inverse does not exists!\n")  

    r = invrev_wrapper(T, tim)
    if r != None:
        print("\n# Inverse of reverse.", '*-*' * 20)
        PrintTraits(r, size, withanum, markdown)
    else:
        print("\nInfo: Inverse of reverse does not exists!\n")    

if __name__ == "__main__":

    from tabl import tabl_fun
    from Abel import Abel
    from Bell import Bell
    from Lah import Lah
    from StirlingSet import StirlingSet
    from StirlingCyc import StirlingCycle
    from Fubini import Fubini
    from Motzkin import Motzkin
    from MotzkinGF import MotzkinGF
    from Delannoy import Delannoy
    from SchroederL import SchroederL
    from SchroederP import SchroederPaths
    from Binomial import Binomial
    from CatalanSqr import CatalanSqr
    from Catalan import Catalan
    from PowLaguerre import PowLaguerre
    from LabeledGraphs import LabeledGraphs
    from BinomialCatalan import BinomialCatalan
    from BinomialBell import BinomialBell
    from MoebiusMat import MoebiusMat
    from Euclid import Euclid
    from PartitionDist import PartnumDist
    from EulerianB import EulerianB
    
    RegisterTraits()

    # Minimum: 32 = 2 * 15 for hash + 2 for shift

    # SaveAllTraitsToCSV()

    # SaveExtendedTraitsToCSV(StirlingSet, 32) 
    # SaveAllExtendedTraitsToCSV()
    # SaveAllFoundTraitsToCSV()

    #SaveTraitsToFile(LabGraphs, 32, withanum = True, markdown = False, onlythefound = False)
    # PrintTraits(BinomialCatalan, 32, withanum = True, markdown = True, onlythefound = False)
    # PrintTraits(PartnumDist, 32, withanum = False, markdown = False, onlythefound = False)
    # PrintTraits(Lah, 32, withanum = False, markdown = True, onlythefound = False)
    # PrintTraits(StirlingCycle, 32, withanum = False, markdown = False, onlythefound = False)

    SEQ = StirlingSet

    #PrintExtendedTraits(SEQ, 32, False, True)
    #PrintExtendedTraits(Lah, 32, False, True)
    #PrintExtendedTraits(Delannoy, 32, False, True)
    #PrintExtendedTraits(SchroederPaths, 32, False, True)
    #PrintExtendedTraits(SchroederL, 32, False, True)
    #PrintExtendedTraits(Abel, 32, False, True)
    #PrintExtendedTraits(Fubini, 32, False, True)
    #PrintExtendedTraits(Catalan, 32, False, True)
    #PrintExtendedTraits(MotzkinGF, 32, False, True)
    #PrintExtendedTraits(EulerianB, 32, False, True)

    # With A-numbers, but slower:
    #PrintTraits(SEQ, 32, withanum = False, markdown = True)

    # Greater size increases the precision of the anumber.
    # Creates a md file which saves all sequences.
    # SaveTraitsToFile(SEQ, 32, withanum = True, markdown = True)

    # Creates a csv file which saves only the sequences found.
    # SaveTraitsToFile(SEQ, 32, withanum = True, markdown = False)

    # PrintExtendedTraits(SEQ, 32, withanum = False, markdown = True)

    for fun in tabl_fun:
        PrintExtendedTraits(fun, 32, False, True)
   
    print("Done")
