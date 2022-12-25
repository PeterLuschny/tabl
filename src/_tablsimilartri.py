import csv
from _tabltypes import tri, tabl
from tabl import tabl_fun

# #@

# T ENUMERATED AS A TRIANGLE
#
# T(0,0)
# T(1,0)  T(1,1)
# T(2,0)  T(2,1)  T(2,2)
# T(3,0)  T(3,1)  T(3,2)  T(3,3)
# T(4,0)  T(4,1)  T(4,2)  T(4,3)  T(4,4)
# T(5,0)  T(5,1)  T(5,2)  T(5,3)  T(5,4)  T(5,5)
#
# A subtriangle of the standard triangle T as indexed above
# is given by a new root node [N, K].
# For some dimension dim > 0 it is defined as
# T[N, K, dim] = [[T(n, k) for k in range(K, K - N + n + 1)] for n in range(N, N + dim)]
#
# Let AT = abs(T) and AS = abs(S).
# We say a triangle S is 'similar' to the triangle T iff
# AS = AT                         or AS = reversed(AT)
# or AS = AT.AbsSubTriangle(1, 0) or AS = reversed(AT.AbsSubTriangle(1,0))
# or AS = AT.AbsSubTriangle(1, 1) or AS = reversed(AT.AbsSubTriangle(1, 1))

def SubTriangle(T: tri, N: int, K: int, dim: int) -> tabl:
    return [[T(n, k) for k in range(K, K - N + n + 1)] for n in range(N, N + dim)]


def AbsSubTriangle(T: tri, N: int, K: int, dim: int) -> tabl:
    return [[abs(T(n, k)) for k in range(K, K - N + n + 1)] for n in range(N, N + dim)]


def search_db(Seqs, wanted: list[int]) -> list | None:
    similars = []
    for seq in Seqs:
        if seq[1] == wanted:
            similars.append(seq[0][:-1])
    return similars


# Assumes database Seqs with abs-items!
def lookup_similar_triangles(Seqs, T: tri) -> None:

    dim = 7 # do not change! It corresponds to the short data file.
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
        R = search_db(Seqs, var)
        similars.extend(R)

    return sorted(set(similars))


def SingleSimilarTriangles(datapath, fun) -> None:

        seq_list = []
        with open(datapath, "r") as oeisdata:
            reader = csv.reader(oeisdata)
            seq_list = [[seq[0], [int(t) for t in seq[1:-1]]] for seq in reader]

        similars = lookup_similar_triangles(seq_list, fun)
        print(fun.id, "Similars:", similars)
        return

def Readme() -> None:

    print("Tables |  Src   | Traits   |  OEIS  SIMILARS |")
    print("| :--- | :---   | :---     |    :---         |")

    for fun in tabl_fun:
        id = fun.id
        similars = fun.sim
        anum = ""
        s = ( str(similars)
                .replace("[", "")
                .replace("]", "")
                .replace("'", "")
            )
        for sim in similars: anum += "%7Cid%3A" + sim
        print(f"| [{id}](https://github.com/PeterLuschny/tabl/blob/main/tables.md#{id}) | [src](https://github.com/PeterLuschny/tabl/blob/main/src/{id}.py) | [traits](https://luschny.de/math/oeis/{id}.html) | [{s}](https://oeis.org/search?q={anum}) |\n")


def SimilarTriangles(datapath: str, md: bool = True) -> None:

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
            s = (   str(similars)
                    .replace("[", "")
                    .replace("]", "")
                    .replace("'", "")
                )
            id = fun.id
            print(f"| [{id}](https://github.com/PeterLuschny/tabl/blob/main/tables.md#{id}) | [{s}](https://oeis.org/search?q={anum}) |")
        else:
            print(fun.id, "Similars:", similars)
    return


if __name__ == "__main__":

    # Alternative:
    # seqdata = read_seqdata(GetDataPath()) if seqnum else []
    # if seqnum: print(SimilarSequences(seqdata, seq))


    '''
    from pathlib import Path
    from Lah import lah

    path = Path(__file__).parent.parent
    reldatapath = "data/oeis_data.csv"
    datapath = (path / reldatapath).resolve()

    relshortdatapath = "data/short_data.csv"
    shortdatapath = (path / relshortdatapath).resolve()

    #print(lah.tab(7))
    #print(SubTriangle(lah, 3, 3, 4))

    #SimilarTriangles(shortdatapath)
    SingleSimilarTriangles(shortdatapath, lah)
    print("Done")

    # Essentially equal triangles are:
    # LAHTRIANGLES Similars: ['A008297', 'A066667', 'A089231', 
    #'A105278', 'A111596', 'A271703']
    '''

    Readme()
