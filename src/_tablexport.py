import contextlib
from io import TextIOWrapper
from _tablprofile import Profile
from _tablviews import PrintViews
from _tabltypes import tri, inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper
from _tabltraitcard import Traits
# from tabl import tabl_fun

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
relcsvpath = 'data/csv'
csvpath = (path / relcsvpath).resolve()
allcsvfile = 'data/allcsv.csv'
csvpath = (path / relcsvpath).resolve()
allcsvpath = (path / allcsvfile).resolve()

# #@

def sortfile(inpath, outpath) -> None:

    with open(inpath, 'r') as infile:
        with open(outpath, 'w') as outfile:
            inlines = infile.readlines()
            outlines = sorted(set(inlines))
            for line in outlines:
                outfile.write(line)

def SaveToCsv(fun: tri, dim: int = 24) -> None:
    csvfile = fun.id + ".csv"
    path = (csvpath / csvfile).resolve()
    with open(path, 'w+') as dest:
        dest.write("Triangle,Trait,ANumber,Sequence\n")
        s = str(fun.sim).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        dest.write(f"OEIS Similars: {s},,,\n")
        Traits(fun, dim, True, dest)


def SaveAllToCsv(dim: int = 24) -> None:
    for fun in tabl_fun:
        SaveToCsv(fun, dim)


def AllTraits(seqnum: bool = False) -> None:
    dim = 28
    csvfile = open(allcsvpath, 'w')
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


if __name__ == "__main__":

    from Abel import abel
    SaveToCsv(abel, 10)
