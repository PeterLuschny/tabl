'''
This module provides functions to save extended tables and generate cross-references for integer triangles.
Functions:
    CrossReferences(name: str = "README.md") -> None:
        Writes the cross-references as a markdown table to the root directory.
    SaveExtendedTables(dim: int = 10) -> None:
        Saves the extended tables to the data/md folder with the specified dimension.
'''

import contextlib
from tabl import tabl_fun
from _tablpaths import GetRoot, GetDataPath
from _tablviews import PrintViews
from _tabltypes import (InvTable, RevTable, RevInvTable, InvRevTable)

'''
Memo for the developer:
The html version of the 'readme' (crossreference table) needs (and only needs):
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/4.0.0/github-markdown.min.css">
'''

# #@

readme_header = """

# Tables à la carte

  INTEGER SEQUENCES ARE ONLY THE SHADOWS OF INTEGER TRIANGLES

Python implementations of integer sequences dubbed tabl in the OEIS.
The notebook gives a first introduction for the user.


"""


def CrossReferences(name: str = "README.md") -> None:
    """
    Writes the crossreferences as a md-table to the root.

    Args:
        name (str, optional): The name of the file to write the crossreferences to. Defaults to "README.md".
    """
    path = GetRoot(name)

    with open(path, "w+", encoding='utf-8') as xrefs:

        xrefs.write(readme_header)
        xrefs.write("| Table |  Source | Traits   |  OEIS similars |\n")
        xrefs.write("| :---  | :---    | :---     |  :---          |\n")

        for fun in tabl_fun:
            id = fun.id
            similars = fun.sim
            anum = ""
            s = str(similars).replace("[", "").replace("]", "").replace("'", "")
            for sim in similars:
                anum += "%7Cid%3A" + sim
            xrefs.write(f"| [{id}](https://github.com/PeterLuschny/tabl/blob/main/data/md/{id}.tbl.md) | [source](https://github.com/PeterLuschny/tabl/blob/main/src/{id}.py) | [traits](https://peterluschny.github.io/tabl/{id}.html) | [{s}](https://oeis.org/search?q={anum}) |\n")

    print("Info: 'README.md' written to the root folder.")


def SaveExtendedTables(dim: int = 10) -> None:
    """
    Saves the extended tables to the data/md folder.

    Args:
        dim (int, optional): The dimension of the tables. Defaults to 10.
    """
    tim: int = dim + dim

    for fun in tabl_fun:
        tablpath = GetDataPath(fun.id + '.tbl', 'md')
        with open(tablpath, "w+", encoding="utf-8") as dest:
            with contextlib.redirect_stdout(dest):
                PrintViews(fun, dim)

                V = InvTable(fun, tim)
                if V is not None:
                    PrintViews(V, dim)

                r = RevTable(fun, tim)
                PrintViews(r, dim)

                r = RevInvTable(fun, tim)
                if r is not None:
                    PrintViews(r, dim)

                r = InvRevTable(fun, tim)
                if r is not None:
                    PrintViews(r, dim)

    print("Info: Extended tables written to the data/md folder as 'name.tbl.md'.")


if __name__ == "__main__":
    # SaveExtendedTables()
    CrossReferences()
