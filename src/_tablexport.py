import contextlib
from io import TextIOWrapper
from _tablprofile import Profile
from _tablviews import PrintViews
from _tabltypes import tri, inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper


# #@

def sortfile(inpath, outpath) -> None:

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

    # Please test in tabltest.py
    def nothinghere() -> None: return None
