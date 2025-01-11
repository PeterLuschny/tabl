"""
This module provides utility functions for managing file paths and directories
within a project structure. It includes functions to get paths for various
directories and files, create directories if they do not exist, and ensure
that specific data directories are present.
Functions:
- GetRoot(name: str = '') -> Path: Returns the root path of the project or a
    specified subpath.
- GetData(name: str) -> Path: Returns the path to a specified data subdirectory.
- GetDataPath(name: str, fix: str) -> Path: Returns the path to a specific data
    file with a given extension.
- GetDocsPath(name: str, fix: str) -> Path: Returns the path to a specific
    documentation file with a given extension.
- MakeDirectory(dir: Path) -> None: Creates a directory if it does not exist.
- EnsureDataDirectories() -> None: Ensures that the required data directories
    (csv, db, md) exist.
Constants:
- path: The root path of the project.
- strippedpath: The path to the stripped data directory.
- oeisnamespath: The path to the names data directory.
Usage:
- This module can be run as a script to print the root path and ensure that
    the required data directories are created.
"""

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


def GetDocsPath(name: str, fix: str) -> Path:
    relpath = f"docs/{name}.{fix}"
    return (path / relpath).resolve()


def MakeDirectory(dir: Path) -> None:
    """Checks if a path exists, and if not,
    creates the new path."""
    Path(dir).mkdir(parents=True, exist_ok=True)


def EnsureDataDirectories() -> None:
    MakeDirectory(GetRoot("data/csv"))
    MakeDirectory(GetRoot("data/db"))
    MakeDirectory(GetRoot("data/md"))



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
