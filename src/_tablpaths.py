from pathlib import Path


# root
#    |
#    data
#       | -> csv
#           | -> oeis.csv
#           | -> Abel.csv
#           | -> *.csv
#       | -> db
#           | -> oeismini.db
#           | -> traits.db
#           | -> Abel.db
#           | -> *.db
#       | -> md
#           | -> Abel.md
#           | -> Abel.tbl.md
#           | -> *.md
#           | -> *.tbl.md
#    |
#    docs
#       | -> sortable.js
#       | -> Abel.html
#       | -> *.html


# #@

path = Path(__file__).parent.parent

strippedpath = (path / "data/stripped").resolve()
oeisnamespath = (path / "data/names").resolve()


def GetRoot(name: str = '') -> Path:
    return (path / name).resolve()


def GetData(name: str) -> Path:
    relpath = f"data/{name}"
    return (path / relpath).resolve()


def GetDataPath(name: str, fix: str) -> Path:
    relpath = f"data/{fix}/{name}.{fix}"
    return (path / relpath).resolve()


def MakeDirectory(dir: Path) -> None:
    """Checks if a path exists, and if not,
    creates the new path."""
    Path(dir).mkdir(parents=True, exist_ok=True)


def EnsureDataDirectories() -> None:
    MakeDirectory(GetRoot("data/csv"))
    MakeDirectory(GetRoot("data/db"))
    MakeDirectory(GetRoot("data/md"))
    MakeDirectory(GetRoot("docs"))  # for *.html files


# githubtab    = "https://github.com/PeterLuschny/tabl/blob/main/tables.md"
# githubsrc    = "https://github.com/PeterLuschny/tabl/blob/main/src/"
# htmltraits   = "https://peterluschny.github.io/tabl/"
# oeisstripped = "https://oeis.org/stripped.gz"
# oeissearch   = "https://oeis.org/search?q="
# sortable     = "https://github.com/tofsjonas/sortable"


if __name__ == "__main__":
    print(GetRoot())
    print(GetRoot("README.md"))
    print(GetRoot("src/_tablmake.py"))

    # Make sure to reference tabl.py in its current state.
    # exec(open(mkpath).read())

    EnsureDataDirectories()
