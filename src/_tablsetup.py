from _tabldata import GetCompressed, OeisToSql, SaveAllTraitsToDBandCSVandMD, MergeDBs
from _tablexport import SaveExtendedTables, CrossReferences
from _tablpaths import GetRoot, EnsureDataDirectories
from _tablhtml import AllCsvToHtml
from tabl import tabl_fun


# #@

""" This function updates all data related to the defined integer
    triangles (including downloading the latest compressed database
    from the OEIS), updates the corresponding csv files and the
    corresponding html files as well as the crossreferences.
    This will take a considerably amount of time. Normally this is
    done only by the administrator when preparing a new release.
"""


def setup() -> None:
    EnsureDataDirectories()

    print("Info: Building database. This takes some time! (~2 hour)")
    print("Warning: You have to be online now, since we are querying OEIS!")
    print("Info: Updating OEIS data ...")

    GetCompressed()
    OeisToSql()
    print("Info: OEIS data updated!")

    SaveAllTraitsToDBandCSVandMD(tabl_fun)
    MergeDBs(tabl_fun)
    print("Info: All traits of all sequences saved to db, csv, and md!")

    AllCsvToHtml()
    print("Warning: You must put also the file 'sortable.js' into the html directory!")
    print("Info: Building extended tables.")

    SaveExtendedTables()
    CrossReferences()

    print("Done ...")


if __name__ == "__main__":
    """Make sure to reference tabl.py in its current state."""
    exec(open(GetRoot("src/_tablmake.py")).read())

    """
    DO NOT USE 'setup' if you only want to update tabl.py.
    If you want to update 'tabl.py' after you have added a new
    triangle implementation just run "src/_tablmake.py".
    """
    # setup()
