from _tabldata import GetCompressed, OeisToSql, SaveAllTraitsToDB,SaveTraitsToDB, SaveDB_CSV_MD
from _tablexport import SaveExtendedTables, CrossReferences
from _tablhtml import AllCsvToHtml
from _tablpaths import GetRoot, GetDataPath
from tabl import tabl_fun

# #@

''' This function updates all data related to the defined integer 
    triangles (including downloading the latest compressed database 
    from the OEIS), updates the corresponding csv files and the 
    corresponding html files as well as the crossreferences. 
    This will take a considerably amount of time. Normally this is 
    done only by the administrator when preparing a new release.
'''
def setup() -> None:
    print("Info: Building database. This takes some time! (~2 hour)")
    
    print("Info: Updating OEIS data ...")
    GetCompressed()
    OeisToSql()
    print("Info: OEIS data updated!")
   
    SaveAllTraitsToDB(tabl_fun)

    for fun in tabl_fun:
        SaveTraitsToDB(fun)
        SaveDB_CSV_MD(GetDataPath(fun.id, 'db') )

    print("Info: All traits saved to data/db.")

    print("Warning: You have to be online now!") 
    print("Info: Building html pages; this will take long since we are querying OEIS.")

    AllCsvToHtml()
    print("Warning: You must put the files 'sortable.js' and 'style.css' into the html directory!")
    print("Info: Building extended tables.")

    SaveExtendedTables()
    CrossReferences()

    print("Done ...")


if __name__ == "__main__":

    '''Make sure to reference tabl.py in its current state.'''
    exec(open(GetRoot("src/_tablmake.py")).read())

    '''
    DO NOT USE 'setup' if you only want to update tabl.py.
    If you want to update 'tabl.py' after you have added a new
    triangle implementation just run "src/_tablmake.py".
    '''
    # setup()

