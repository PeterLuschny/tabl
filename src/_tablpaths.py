from pathlib import Path

path = Path(__file__).parent.parent

relprofpath = "data/profiles.csv"
relsortpath = "data/sortedprofiles.csv"

relstrippedpath = "data/stripped"
strippedpath = (path / relstrippedpath).resolve()

reloeispath = "data/oeis.csv"
oeispath = (path / reloeispath).resolve()

reldatapath = "data/abs_data.csv"
datapath = (path / reldatapath).resolve()

propath = (path / relprofpath).resolve()
sorpath = (path / relsortpath).resolve()

relcsvpath = "data/TraitCards"
allcsvfile = "data/allcsv.csv"

csvpath = (path / relcsvpath).resolve()
allcsvpath = (path / allcsvfile).resolve()

propath = (path / relprofpath).resolve()
sorpath = (path / relsortpath).resolve()

relcsvpath = 'data/csv'
csvpath = (path / relcsvpath).resolve()

relhtmlpath = 'data/html'
htmlpath = (path / relhtmlpath).resolve()


def GetDataPath() -> Path:
    return datapath

def GetCsvPath() -> Path:
    return csvpath


def GetAllCsvPath() -> Path:
    return allcsvpath


def GetHtmlPath() -> Path:
    return htmlpath


githubtab = "https://github.com/PeterLuschny/tabl/blob/main/tables.md"
githubsrc = "https://github.com/PeterLuschny/tabl/blob/main/src/"
htmltraits = "https://luschny.de/math/oeis/" 
oeisstripped = "https://oeis.org/stripped.gz"
oeissearch = "https://oeis.org/search?q="
