import contextlib
from io import TextIOWrapper
from _tablprofile import PrintExtendedProfile, PrintProfile, Profile
from _tablviews import PrintViews
from _tabltypes import tri, inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper
from tabl import tabl_fun # <- this is tricky


# #@

def sortfile() -> None:
    inpath = 'profiles.csv'
    outpath = 'sortedprofiles.csv'

    with open(inpath, 'r') as infile:
        with open(outpath, 'w') as outfile:
            inlines = infile.readlines()
            outlines = sorted(set(inlines))
            for line in outlines:
                outfile.write(line)


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


def WriteProfile(dest: TextIOWrapper, fun: tri, dim: int, seqonly: bool) -> None:

    p: dict[str, list[int]] = Profile(fun, dim)
    id: str = fun.id
    for seq in p.items():
        if seqonly:
            dest.write(f"{seq[1]}\n")
        else:
            dest.write(f"{seq[1]},{seq[0]},{id}\n")


def SaveProfiles(seqonly: bool = True) -> None:
    dest: TextIOWrapper = open('profiles.csv', 'w+')

    for fun in tabl_fun:
        WriteProfile(dest, fun, seqonly)

    dest.close()


def SaveExtendedProfiles(dim: int = 10, seqonly: bool = True) -> None:

    dest: TextIOWrapper = open('profiles.csv', 'w+')
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

# 4239 1960

    def test1() -> None:
        dim = 10
        format = 'twolines'

        for fun in tabl_fun:
           PrintViews(fun)
           PrintProfile(fun, dim, 'oneline')
           PrintExtendedProfile(fun, dim, 'nonames')


    def test2() -> None:
        #SaveTables()
        SaveExtendedTables()


    def test3() -> None:

        #SaveProfiles(True)
        #sortfile()

        SaveExtendedProfiles()
        sortfile()

    print("... bussy")
    test2()
    print("Done!")
