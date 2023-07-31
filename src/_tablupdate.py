###############################################
# * First copy this file to the project folder.

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
Normally this is done only by the administrator when preparing
a new release.
'''
def update() -> None:
    print("Updating OEIS data ...")
    GetOEISdata()
    SaveAllTraitsToCSV()
    AllCsvToHtml()
    SaveExtendedTables()
    CrossReferences()


if __name__ == "__main__":

    '''Update project.'''
    update()

'''
Clean up by hand: 
* Delete the copy of _tablupdate from the project folder.
* Move tabl.py from the project folder to the src folder.
* Format tabl.py.
* Copy the header of README.md to crossrefs. md.
* Delete README.md
* Rename crossrefs.md to README.md.
* Convert README.md to html using the VS plugin
* 'Markdown All in One'.
'''