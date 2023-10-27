from pathlib import Path

# #@

path = Path(__file__).parent.parent

strippedpath = (path / "data/stripped").resolve()


def GetPath(name: str) -> Path:
    return (path / name).resolve()
  

def GetData(name: str) -> Path:
    relpath = f"data/{name}"
    return (path / relpath).resolve()


def GetDataPath(name: str, fix: str)  -> Path:
    relpath = f"data/{fix}/{name}.{fix}"
    return (path / relpath).resolve()


# githubtab = "https://github.com/PeterLuschny/tabl/blob/main/tables.md"
# githubsrc = "https://github.com/PeterLuschny/tabl/blob/main/src/"
# htmltraits = "https://luschny.de/math/oeis/" 
# oeisstripped = "https://oeis.org/stripped.gz"
# oeissearch = "https://oeis.org/search?q="
