from _tabltypes import tgen, tabl
from _tabltypes import inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper
from _tabltraits import TRAIT, TRAIT2, RegisterTraits
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


STRINGLEN = 100

def PrintTraits(g: tgen, size: int, 
                withanum: bool = False, 
                markdown: bool = True,
                onlythefound: bool = True) -> None:

    trianglename = g.id
    T = g.tab(size)
    gen = g.gen
    anum = "" # ???? (g.sim)[0]  # Note that the similars are ordered!

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
                seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')    
                print(f'| {trianglename} | {anum:7} | {name:<12} | {seqstr} |')
                anum = '' 
            else:
                seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')
                print(f'| {trianglename} | {name:<12} | {seqstr} |')

    else: # TXT simple dictionary, no options, no anums 

        for traitname, trait in TRAIT.items():
            name = traitname[4:] if traitname.startswith("Flat") else traitname
            seqstr = SeqToFixlenString(trait(T), STRINGLEN, ' ')
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
                seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')    
                print(f'| {trianglename} | {anum:7} | {traitname:<12} | {seqstr} |')
                anum = '' 
            else:
                seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')
                print(f'| {trianglename} | {traitname:<12} | {seqstr}|')

    else:  # TXT simple dictionary, no options, no anums 

        for traitname, trait in TRAIT2.items():
            seqstr = SeqToFixlenString(trait(gen, size), STRINGLEN, ' ')
            print(f'{trianglename}:{traitname:<14} {seqstr}')


def SaveTraitsToFile(g: tgen, size: int, 
                     withanum: bool = False, 
                     markdown: bool = True,
                     onlythefound: bool = True) -> None:

    trianglename = g.id
    T = g.tab(size)
    gen = g.gen
    anum = "" # BUG (g.sim)[0]  # Note that the similars are ordered!
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
                    seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')    
                    target.write(f'| {trianglename} | {anum:7} | {name:<12} | {seqstr} |\n')
                    anum = '' 
                else:
                    seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')
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
                    seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')    
                    target.write(f'{trianglename},{anum},{name},{seqstr}\n')
                    anum = '' 
                else:
                    seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')
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
                    seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')    
                    target.write(f'| {trianglename} | {anum:7} | {traitname:<12} | {seqstr} |\n')
                    anum = '' 
                else:
                    seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')
                    target.write(f'| {trianglename} | {traitname:<12} | {seqstr} |\n')

        else: # CSV

            for traitname, trait in TRAIT2.items():
                tt = trait(gen, size)
                if withanum:
                    anum = '' if tt == [] else GetAnumber(tt)
                    if anum == "": 
                        print(traitname) 
                        if onlythefound: continue
                    seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')
                    target.write(f'{trianglename},{anum},{traitname},{seqstr}\n')
                else:
                    seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')
                    target.write(f'{trianglename},{traitname},{seqstr}\n')


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
                seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')
                target.write(f'{trianglename},{anum},{name},{seqstr}\n')

            for traitname, trait in TRAIT2.items():
                tt = trait(gen, size)
                anum = '' if tt == [] else GetAnumber(tt)
                if anum == "": 
                    print(traitname) 
                    continue
                seqstr = SeqToFixlenString(tt, STRINGLEN, ' ')
                target.write(f'{trianglename},{anum},{traitname},{seqstr}\n')

    G.id = savedid


def PrintAllTraitsWithAnumber(size: int) -> None:
    for fun in tabl_fun:
        PrintTraits(fun, size, withanum = True)


def PrintAllTraits(size: int) -> None:
    for fun in tabl_fun:
        PrintTraits(fun, size, withanum = False)


def SaveAllFoundTraitsToCSV() -> None:
    RegisterTraits()
    for fun in tabl_fun:
        print("#", fun.id)
        SaveTraitsToFile(fun, 20, 
                         withanum = True,
                         markdown = False,
                         onlythefound = True)


def SaveAllTraitsToCSV() -> None:
    RegisterTraits()
    for fun in tabl_fun:
        print("#", fun.id)
        SaveTraitsToFile(fun, 20,
                         withanum = True,
                         markdown = False,
                         onlythefound = False)


def SaveAllExtendedTraitsToCSV() -> None:
    RegisterTraits()
    for fun in tabl_fun:
        print("##", fun.id)
        SaveExtendedTraitsToCSV(fun, 20)


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
