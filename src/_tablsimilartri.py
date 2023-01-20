import csv
from _tabltypes import tri, tabl, SubTriangle, AbsSubTriangle
# from tabl import tabl_fun

# #@

def search_db(database: list[list[int]], wanted: list[int]) -> list:
    """Runs through the database looking for the given triangle.
    Uses only the first 28 terms of the sequences.

    Args:
        database (list[list[int]]): oeis_data
        wanted (list[int]): sequence looked for

    Returns:
        list: oeis A-numbers of similar triangles
    """
    similars = []
    count = 0
    for seq in database:
        if wanted == seq[1][:28]:
            similars.append(seq[0])
            count += 1
            if count > 6: break
    return similars


def lookup_similar_triangles(database: list[list[int]], T: tri) -> list:
    """Tries to identify triangles similar to the given one.
    Assumes database is given with absulute terms!
    Let AT = abs(T) and AS = abs(S).  We say a triangle S is 'similar' 
    to the triangle T iff
    * AS = AT                        or AS = reversed(AT)
    * or AS = AT.AbsSubTriangle(1,0) or AS = reversed(AT.AbsSubTriangle(1,0))
    * or AS = AT.AbsSubTriangle(1,1) or AS = reversed(AT.AbsSubTriangle(1,1))

    Args:
        database (list[list[int]]): oeis_data
        T (tri): generator of the triangle

    Returns:
        list: oeis A-numbers of similar triangles
    """
    dim = 7  # do not change! It corresponds to the short data file.
    similars = []

    T00 = AbsSubTriangle(T, 0, 0, dim)
    T10 = AbsSubTriangle(T, 1, 0, dim)
    T11 = AbsSubTriangle(T, 1, 1, dim)

    variants = [
        [k for row in T00 for k in row],
        [k for row in T00 for k in list(reversed(row))],
        [k for row in T10 for k in row],
        [k for row in T10 for k in list(reversed(row))],
        [k for row in T11 for k in row],
        [k for row in T11 for k in list(reversed(row))],
    ]

    for var in variants:
        R = search_db(database, var)
        similars.extend(R)

    return sorted(set(similars))


def GetSimilarTriangles(datapath: str, fun: tri) -> list:
    """Assumes the database in csv-format.

    Args:
        datapath (str): location of the database
        fun (tri): generator of the reference triangle

    Returns:
        list: oeis A-numbers of similar triangles

    Examples:
        in>  GetSimilarTriangles(GetShortDataPath(), lah)
        out> lah similars: ['A008297', 'A066667', 'A089231',
            'A105278', 'A111596', 'A271703']
    """
    seq_list = []
    with open(datapath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        seq_list = [[seq[0], [int(t) for t in seq[1:-1]]] for seq in reader]

        similars = lookup_similar_triangles(seq_list, fun)
        print(fun.id, "similars:", similars)
        return similars


def SimilarTriangles(datapath: str, md: bool = True) -> None:
    """Searches the database for all similar triangles for all
    triangles defined in this package (listed in tabl_fun).

    Args:
        datapath (str): location of the database
        md (bool, optional): format option markdown. Defaults to True.
    """
    seq_list = []
    with open(datapath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        seq_list = [[seq[0], [int(t) for t in seq[1:-1]]] for seq in reader]

    if md:
        print("|  ID    |  OEIS  SIMILARS |")
        print("| :---:  |  :---:          |")

    for fun in tabl_fun:
        similars = lookup_similar_triangles(seq_list, fun)[:10]
        if md:
            anum = ""
            for sim in similars:
                anum += "%7Cid%3A" + sim
            s = str(similars).replace("[", "").replace("]", "").replace("'", "")
            id = fun.id
            print(
                f"| [{id}](https://github.com/PeterLuschny/tabl/blob/main/tables.md#{id}) | [{s}](https://oeis.org/search?q={anum}) |"
            )
        else:
            print(fun.id, "Similars:", similars)
    return


if __name__ == "__main__":

    from _tablpaths import GetDataPath
    from Lah import lah

    # Essentially equal triangles are:
    # Lah similars: ['A008297', 'A066667', 'A089231',
    #                'A105278', 'A111596', 'A271703']
    GetSimilarTriangles(GetDataPath(), lah)
