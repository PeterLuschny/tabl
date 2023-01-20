import contextlib
from io import TextIOWrapper
from _tablprofile import Profile
from _tablviews import PrintViews
from _tabltypes import tri, inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper
from _tabltraitcard import Traits
from _tablpaths import GetCsvPath, GetAllCsvPath
# from tabl import tabl_fun


# #@


def sortfile(inpath, outpath) -> None:

    with open(inpath, 'r') as infile:
        with open(outpath, 'w') as outfile:
            inlines = infile.readlines()
            outlines = sorted(set(inlines))
            for line in outlines:
                outfile.write(line)


def GenerateCsvFile(fun: tri, dim: int = 24) -> None:
    csvfile = fun.id + ".csv"
    path = (GetCsvPath() / csvfile).resolve()
    with open(path, 'w+') as dest:
        dest.write("Triangle,Trait,ANumber,Sequence\n")
        s = str(fun.sim).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        dest.write(f"OEIS Similars: {s},,,\n")
        Traits(fun, dim, True, dest)


def GenerateAllCsvFiles(dim: int = 24) -> None:
    for fun in tabl_fun:
        print(fun.id)
        GenerateCsvFile(fun, dim)


def AllTraits(seqnum: bool = False) -> None:
    dim = 28
    csvfile = open(GetAllCsvPath(), 'w')
    if seqnum:
        csvfile.write("Triangle,Trait,ANumber,Sequence\n")
    else:
        csvfile.write("Triangle,Trait,Sequence\n")

    for fun in tabl_fun:  # is in tabl.py
        Traits(fun, dim, False, csvfile)
    csvfile.close()


def SaveTables(dim: int = 7) -> None:
    path = 'tables.md'
    with open(path, 'w+') as dest:
        with contextlib.redirect_stdout(dest):
            for fun in tabl_fun:
                PrintViews(fun, dim)


def SaveExtendedTables(dim: int = 7) -> None:

    tim: int = dim + dim 
    path = 'tables.md'

    with open(path, 'w+') as dest:
        with contextlib.redirect_stdout(dest):
            for fun in tabl_fun:
                PrintViews(fun, dim)

                I = inversion_wrapper(fun, tim)
                if I != None:
                    PrintViews(I, dim)

                R = reversion_wrapper(fun, tim)
                PrintViews(R, dim)

                R = revinv_wrapper(fun, tim)
                if R != None:
                    PrintViews(R, dim)

                R = invrev_wrapper(fun, tim)
                if R != None:
                    PrintViews(R, dim)


def WriteProfile(dest: TextIOWrapper, fun: tri, dim: int = 10, seqonly: bool = True) -> None:

    p: dict[str, list[int]] = Profile(fun, dim)
    id: str = fun.id
    for seq in p.items():
        if seqonly:
            dest.write(f"{seq[1]}\n")
        else:
            dest.write(f"{seq[1]},{seq[0]},{id}\n")


def SaveProfiles(path: str, dim: int = 10, seqonly: bool = True) -> None:
    dest: TextIOWrapper = open(path, 'w+')

    for fun in tabl_fun:
        WriteProfile(dest, fun, dim, seqonly)

    dest.close()


def SaveExtendedProfiles(path: str, dim: int = 10, seqonly: bool = True) -> None:

    dest: TextIOWrapper = open(path, 'w+')
    tim: int = dim + dim // 2

    for fun in tabl_fun:
        WriteProfile(dest, fun, dim, seqonly)

        I = inversion_wrapper(fun, tim)
        if I != None:
            WriteProfile(dest, I, dim, seqonly)

        R = reversion_wrapper(fun, tim)
        WriteProfile(dest, R, dim, seqonly)

        R = revinv_wrapper(fun, tim)
        if R != None:
            WriteProfile(dest, R, dim, seqonly)

        R = invrev_wrapper(fun, tim)
        if R != None:
            WriteProfile(dest, R, dim, seqonly)

    dest.close()


def CrossReferences(path = 'xrefs.md') -> None:
    """Writes a table in markdown style (for readme.md)
    Uses stored data from fun.sim (no searching) 
    
    """

    with open(path, 'w+') as xrefs:
        
        xrefs.write("Tables |  Src   | Traits   |  OEIS  SIMILARS |\n")
        xrefs.write("| :--- | :---   | :---     |    :---         |\n")

        for fun in tabl_fun:
            id = fun.id
            similars = fun.sim
            anum = ""
            s = str(similars).replace("[", "").replace("]", "").replace("'", "")
            for sim in similars:
                anum += "%7Cid%3A" + sim
            xrefs.write(
                f"| [{id}](https://github.com/PeterLuschny/tabl/blob/main/tables.md#{id}) | [src](https://github.com/PeterLuschny/tabl/blob/main/src/{id}.py) | [traits](https://luschny.de/math/oeis/{id}.html) | [{s}](https://oeis.org/search?q={anum}) |\n"
            )


if __name__ == "__main__":

    #from Abel import abel
    #GenerateCsvFile(abel, 12)

    GenerateAllCsvFiles()
    #SaveExtendedTables()
    #CrossReferences()
    print("Done")
