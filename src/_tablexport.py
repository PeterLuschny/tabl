from tabl import tabl_fun

import contextlib
from _tablviews import PrintViews
from _tablpaths import GetMdPath
from _tabltypes import (
    inversion_wrapper,
    reversion_wrapper,
    revinv_wrapper,
    invrev_wrapper,
)


# #@


def CrossReferences(path: str="crossrefs.md") -> None:
    """Writes a table in markdown style.
    Uses stored data from fun.sim (no searching)
    """

    with open(path, "w+") as xrefs:

        xrefs.write("| Table |  Source | Traits   |  OEIS similars |\n")
        xrefs.write("| :---  | :---    | :---     |  :---          |\n")

        for fun in tabl_fun:
            id = fun.id
            similars = fun.sim
            anum = ""
            s = str(similars).replace("[", "").replace("]", "").replace("'", "")
            for sim in similars:
                anum += "%7Cid%3A" + sim
            xrefs.write(
                f"| [{id}](https://github.com/PeterLuschny/tabl/blob/main/data/md/{id}.md) | [source](https://github.com/PeterLuschny/tabl/blob/main/src/{id}.py) | [traits](https://luschny.de/math/oeis/{id}.html) | [{s}](https://oeis.org/search?q={anum}) |\n"
            )



def SaveExtendedTables(dim: int = 9) -> None:

    tim: int = dim + dim
    path = GetMdPath()

    for fun in tabl_fun:
        tblfile = fun.id + ".md"
        tablpath = (path / tblfile).resolve()

        with open(tablpath, "w+") as dest:
            with contextlib.redirect_stdout(dest):
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

if __name__ == "__main__":

    CrossReferences()
