from pathlib import Path
path = Path(__file__).parent
mkpath = (path / "src/_tablmake.py").resolve()

'''Make sure to reference tabl.py in its current state.'''
exec(open(mkpath).read())

from tabl import GetOEISdata, SaveAllTraitsToCSV, AllCsvToHtml, SaveExtendedTables, CrossReferences 

'''
DO NOT USE this function if you only want to update tabl.py.
If you want to update table.py after you have added a new
triangle implementation just run "src/_tablmake.py".
As a normal user this is all you want and it is quick.

On the other hand this function updates all data related to the 
defined integer triangles (including downloading the latest 
compressed database from the OEIS), updates the corresponding 
csv files and the corresponding html files as well as the 
crossreferences. This will take a considerably amount of time.
Normally this is done only when preparing a new release.
'''
def update() -> None:
    GetOEISdata()
    SaveAllTraitsToCSV()
    AllCsvToHtml()
    SaveExtendedTables()
    CrossReferences()


if __name__ == "__main__":

    '''Update project.'''
    update()
