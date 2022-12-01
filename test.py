from io import TextIOWrapper
import contextlib
from tabl import PrintViews, PrintExtendedProfile, PrintProfile, Profile, tabl_fun


def SaveTables() -> None:
    path = "tables.md"
    with open(path, "w+") as dest:
        with contextlib.redirect_stdout(dest):
            for fun in tabl_fun:
                PrintViews(fun)


def SaveProfiles(seqonly: bool) -> None:
    dest: TextIOWrapper = open("profiles.csv", "w+")

    for fun in tabl_fun:
        p: dict[str, list[int]] = Profile(fun)
        id: str = fun.id
        for seq in p.items():
            if seqonly:
                dest.write(f"{seq[1]}\n")
            else:
                dest.write(f"{seq[1]},{seq[0]},{id}\n")
    dest.close()


for fun in tabl_fun:
    dim = 20
    format = 'twolines' # 'nonames'

    #PrintViews(fun)
    #PrintProfile(fun, dim, 'oneline')
    PrintExtendedProfile(fun, dim, format)
#   SaveTables()
#   SaveProfiles(True)

