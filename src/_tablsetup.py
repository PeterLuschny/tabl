"""
    This module sets up and updates all data related to defined integer triangles.
    Functions:
    setup: Updates all data related to the defined integer triangles, including
           downloading the latest compressed database from the OEIS, updating
           the corresponding CSV and HTML files, and managing cross-references.
           This process is typically only performed by the administrator when 
           preparing a new release.
    Usage:
        Run this module directly to execute the setup function. Ensure you are
        online as it queries the OEIS database. The process will take
        approximately 4 hours to complete.
"""

from _tabldata import (
    GetCompressed,
    GetNames,
    OeisToSql,
    ConvertLocalDBtoCSVandMD,
    SaveAllTraitsToDBandCSVandMD,
    MergeAllDBs,
)
from _tablexport import SaveExtendedTables, CrossReferences
from _tablpaths import GetRoot, EnsureDataDirectories
from _tablhtml import AllCsvToHtml
from _tablstatistic import TuttiStats
from tabl import tabl_fun


# #@


def setup() -> None:
    """
    This function updates all data related to the defined integer
    triangles (including downloading the latest compressed database
    from the OEIS), updates the corresponding csv files and the
    corresponding html files as well as the crossreferences.
    This will take a considerably amount of time. Normally this is
    done only by the administrator when preparing a new release.
    """

    EnsureDataDirectories()

    print("Warning: You have to be online now, since we are querying OEIS!")
    print("Info: Building database. This takes some time! (~4 hour)")
    print("Info: Updating OEIS data ...")

    GetCompressed()
    GetNames()
    OeisToSql()
    ConvertLocalDBtoCSVandMD()
    print("Info: OEIS data updated!")

    SaveAllTraitsToDBandCSVandMD(tabl_fun)
    MergeAllDBs(tabl_fun)
    print("Info: All traits of all sequences saved to db, csv, and md!")

    AllCsvToHtml()
    print("Info: Building extended tables.")

    SaveExtendedTables()
    CrossReferences()

    print("Done ...")
    print("... but you must still put the file 'sortable.js' into the html directory!")

    print("\nAnd here are the new statistics with the current ranking:\n")
    TuttiStats()


if __name__ == "__main__":
    # Make sure to reference tabl.py in its current state.
    exec(open(GetRoot("src/_tablmake.py")).read())

    # DO NOT USE 'setup' if you only want to update tabl.py.
    # If you want to update 'tabl.py' after you have added a new
    # triangle implementation just run "src/_tablmake.py".
    # Or use the function 'SingleMake(triangle)' from _tablsinglemake
    # where 'triangle' is the generator of the triangle.
    setup()
