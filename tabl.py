from functools import cache
from itertools import accumulate
from sys import setrecursionlimit
from typing import Callable, TypeAlias
from io import TextIOWrapper
from difflib import SequenceMatcher
import contextlib
import csv
from fractions import Fraction as frac
from sympy import Matrix, Rational
from pathlib import Path

path = Path(__file__).parent
reldatapath = "data/oeis_data.csv"
datapath = (path / reldatapath).resolve()


def GetDataPath() -> Path:
    return datapath


setrecursionlimit(2100)


def isintegerinv(T: list[list[int]]) -> bool:
    for row in T:
        for k in row:
            if type(k) == Rational:
                return False
    return True


def InverseTriangle(r, dim: int) -> list[list[int]]:
    M = [[r(n)[k] if k <= n else 0 for k in range(dim)] for n in range(dim)]
    try:
        I = Matrix(M) ** -1
    except:  # NonInvertibleMatrixError
        return []
    T = [[I[n, k] for k in range(n + 1)] for n in range(dim)]
    if not isintegerinv(T):
        return []
    return T


def InverseTabl(M: list[list[int]]) -> list[list[int]]:
    try:
        I = Matrix(M) ** -1
    except:  # NonInvertibleMatrixError
        return []
    T = [[I[n, k] for k in range(n + 1)] for n in range(len(M))]
    if not isintegerinv(T):
        return []
    return T


"""Type: table row"""
trow: TypeAlias = list[int]
"""Type: table"""
tabl: TypeAlias = list[list[int]]
"""Type: sequence generator"""
seq: TypeAlias = Callable[[int], int]
"""Type: row generator"""
rgen: TypeAlias = Callable[[int], trow]
"""Type: table generator"""
tgen: TypeAlias = Callable[[int], tabl]
"""Type: triangle"""
tri: TypeAlias = Callable[[int, int], trow | int]


def inversion_wrapper(T: tri, dim: int) -> tri | None:
    t = T.inv(dim)
    if t == []:
        return None

    def _psgen(n: int) -> trow:
        return list(t[n])

    @set_attributes(_psgen, T.id + "|INV", True)
    def psgen(n: int, k: int = -1) -> list[int] | int:
        if k == -1:
            return _psgen(n)
        return _psgen(n)[k]

    return psgen


def reversion_wrapper(T: tri, dim: int) -> tri:
    t = T.rev(dim)

    def _rsgen(n: int) -> trow:
        return list(t[n])

    @set_attributes(_rsgen, T.id + "|REV", True)
    def rsgen(n: int, k: int = -1) -> list[int] | int:
        if k == -1:
            return _rsgen(n)
        return _rsgen(n)[k]

    return rsgen


def revinv_wrapper(T: tri, dim: int) -> tri | None:
    I = inversion_wrapper(T, dim)
    if I == None:
        return None
    T = reversion_wrapper(I, dim)

    def _rigen(n: int) -> trow:
        return list(T(n))

    @set_attributes(_rigen, T.id, True)
    def rigen(n: int, k: int = -1) -> list[int] | int:
        if k == -1:
            return _rigen(n)
        return _rigen(n)[k]

    return rigen


def invrev_wrapper(T: tri, dim: int) -> tri | None:
    R = reversion_wrapper(T, dim)
    T = inversion_wrapper(R, dim)
    if T == None:
        return None

    def _tigen(n: int) -> trow:
        return list(T(n))

    @set_attributes(_tigen, T.id, True)
    def tigen(n: int, k: int = -1) -> list[int] | int:
        if k == -1:
            return _tigen(n)
        return _tigen(n)[k]

    return tigen


def set_attributes(r: rgen, id: str, vert: bool = False) -> Callable[[tri], tri]:
    def maketab(dim: int) -> tabl:
        return [list(r(n)) for n in range(dim)]

    def makerev(dim: int) -> tabl:
        return [list(reversed(r(n))) for n in range(dim)]

    def makemat(dim: int) -> tabl:
        return [[r(n)[k] if k <= n else 0 for k in range(dim)] for n in range(dim)]

    def makeflat(dim: int) -> tabl:
        return [r(n)[k] for n in range(dim) for k in range(n + 1)]

    def makeinv(dim: int) -> tabl:
        if not vert:
            return []
        return InverseTriangle(r, dim)

    def makerevinv(dim: int) -> tabl:
        if not vert:
            return []
        I = InverseTriangle(r, dim)
        return [[I[n][n - k] for k in range(n + 1)] for n in range(dim)]

    def makeinvrev(dim: int) -> tabl:
        R = [list(reversed(r(n))) for n in range(dim)]
        M = [[R[n][k] if k <= n else 0 for k in range(dim)] for n in range(dim)]
        return InverseTabl(M)

    def wrapper(f: tri) -> tri:
        f.tab = maketab
        f.rev = makerev
        f.mat = makemat
        f.inv = makeinv
        f.flat = makeflat
        f.revinv = makerevinv
        f.invrev = makeinvrev
        f.id = id
        return f

    return wrapper


def poly(T: tri, n: int, x: int) -> int:
    row: trow = T(n)
    return sum(c * (x**j) for (j, c) in enumerate(row))


def poly_frac(T: tabl, x: frac) -> list[frac]:
    return [sum(c * (x**k) for (k, c) in enumerate(row)) for row in T]


def row_poly(T: tri, n: int, leng: int) -> trow:
    return [poly(T, n, k) for k in range(leng)]


def col_poly(T: tri, n: int, leng: int) -> trow:
    return [poly(T, k, n) for k in range(leng)]


def diag_poly(T: tri, n: int) -> trow:
    return [poly(T, n - k, k) for k in range(n + 1)]


def poly_diag(T: tri, leng: int) -> trow:
    return [poly(T, n, n) for n in range(leng)]


def poly_tabl(T: tri, leng: int) -> tabl:
    return [diag_poly(T, n) for n in range(leng)]


def pos_half(T: tabl) -> list[int]:
    R = poly_frac(T, frac(1, 2))
    return [((2**n) * r).numerator for n, r in enumerate(R)]


def neg_half(T: tabl) -> list[int]:
    R = poly_frac(T, frac(-1, 2))
    return [(((-2) ** n) * r).numerator for n, r in enumerate(R)]


def trans_seq(T: tri, a: seq, lg: int) -> trow:
    return [sum(T(n, k) * a(k) for k in range(n + 1)) for n in range(lg)]


def trans_self(T: tri, lg: int) -> tabl:
    return [trans_seq(T, lambda k: T(n, k), n + 1) for n in range(lg)]


def transbin_tabl(T: tri, lg: int) -> tabl:
    return [trans_seq(binomial, lambda k: T(n, k), n + 1) for n in range(lg)]


def transbin_val(f: tri, lg: int) -> trow:
    T = transbin_tabl(f, lg)
    return [row[-1] for row in T]


def invtrans_seq(T: tri, a: seq, lg: int) -> trow:
    return [
        sum((-1) ** (n - k) * T(n, k) * a(k) for k in range(n + 1)) for n in range(lg)
    ]


def invtrans_self(T: tri, lg: int) -> tabl:
    return [invtrans_seq(T, lambda k: T(n, k), n + 1) for n in range(lg)]


def invtransbin_tabl(T: tri, lg: int) -> tabl:
    return [invtrans_seq(binomial, lambda k: T(n, k), n + 1) for n in range(lg)]


def invtransbin_val(f: tri, lg: int) -> trow:
    T = invtransbin_tabl(f, lg)
    return [row[-1] for row in T]


def row_diag(T: tri, j: int, leng: int) -> trow:
    return [T(j + k, k) for k in range(leng)]


def col_diag(T: tri, j: int, leng: int) -> trow:
    return [T(j + k, j) for k in range(leng)]


def trans(M: tri, V: Callable, leng: int) -> list[int]:
    return [sum(M(n, k) * V(k) for k in range(n + 1)) for n in range(leng)]


def diag_tabl(t: tabl) -> tabl:
    U: tabl = []
    for n in range(1, len(t)):
        R: trow = []
        for k in range((n + 1) // 2):
            R.append(t[n - k - 1][k])
        U.append(R)
    return U


def acc_tabl(t: tabl) -> tabl:
    return [list(accumulate(row)) for row in t]


def rev_tabl(t: tabl) -> tabl:
    return [list(reversed(row)) for row in t]


def inv_tabl(t: tabl) -> tabl:
    return InverseTabl(t)


def revacc_tabl(t: tabl) -> tabl:
    return rev_tabl(acc_tabl(t))


def accrev_tabl(t: tabl) -> tabl:
    return acc_tabl(rev_tabl(t))


def flat_tabl(t: tabl) -> trow:
    return [i for row in t for i in row]


def flat_rev(t: tabl) -> trow:
    return [i for row in rev_tabl(t) for i in row]


def flat_diag(t: tabl) -> trow:
    return [i for row in diag_tabl(t) for i in row]


def flat_acc(t: tabl) -> trow:
    return [i for row in acc_tabl(t) for i in row]


def flat_revacc(t: tabl) -> trow:
    return [i for row in revacc_tabl(t) for i in row]


def flat_accrev(t: tabl) -> trow:
    return [i for row in accrev_tabl(t) for i in row]


def middle(t: tabl) -> list[int]:
    return [row[n // 2] for n, row in enumerate(t)]


def central(t: tabl) -> list[int]:
    return [row[n // 2] for n, row in enumerate(t) if n % 2 == 0]


def left_side(t: tabl) -> list[int]:
    return [row[0] for row in t]


def right_side(t: tabl) -> list[int]:
    return [row[-1] for row in t]


def even_sum(r: trow) -> int:
    return sum(r[::2])


def odd_sum(r: trow) -> int:
    return sum(r[1::2])


def alt_sum(r: trow) -> int:
    return even_sum(r) - odd_sum(r)


def tabl_sum(t: tabl) -> trow:
    return [sum(row) for row in t]


def tabl_evensum(t: tabl) -> trow:
    return [even_sum(row) for row in t]


def tabl_oddsum(t: tabl) -> trow:
    return [odd_sum(row) for row in t]


def tabl_altsum(t: tabl) -> trow:
    return [alt_sum(row) for row in t]


def tabl_diagsum(t: tabl) -> trow:
    diagt: tabl = diag_tabl(t)
    return [sum(row) for row in diagt]


def tabl_accsum(t: tabl) -> trow:
    acc: tabl = acc_tabl(t)
    return [sum(row) for row in acc]


def tabl_revaccsum(t: tabl) -> trow:
    revacc: tabl = acc_tabl(rev_tabl(t))
    return [sum(row) for row in revacc]


def tabl_accrevsum(t: tabl) -> trow:
    accurev: tabl = rev_tabl(acc_tabl(t))
    return [sum(row) for row in accurev]


def PrintTabl(t: tabl) -> None:
    print(t)


def PrintFlat(t: tabl) -> None:
    print(flat_tabl(t))


def PrintRows(t: tabl) -> None:
    print("| trow  |  list  |")
    print("| :---  |  :---  |")
    for n, row in enumerate(t):
        print(f"| trow{n} | {row} |")


def PrintTerms(t: tabl) -> None:
    count = 0
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print(count, [n, k], term)
            count += 1


def PrintRowArray(T: tri, rows: int, cols: int) -> None:
    print("| rdiag  |   seq  |")
    print("| :---   |  :---  |")
    for j in range(rows):
        print(f"| rdiag{j} | {[T(j + k, k) for k in range(cols)]}|")


def PrintColArray(T: tri, rows: int, cols: int) -> None:
    print("| cdiag  |   seq  |")
    print("| :---   |  :---  |")
    for j in range(cols):
        print(f"| cdiag{j} | {[T(j + k, j) for k in range(rows)]} |")


def PrintRowPolyArray(T: tri, rows: int, cols: int) -> None:
    print("| rpdiag  |   seq  |")
    print("| :---    |  :---  |")
    for n in range(rows):
        print(f"| rpdiag{n} | {row_poly(T, n, cols)} |")


def PrintColPolyArray(T: tri, rows: int, cols: int) -> None:
    print("| cpdiag  |   seq  |")
    print("| :---    |  :---  |")
    for n in range(rows):
        print(f"| cpdiag{n} | {col_poly(T, n, cols)} |")


def PrintSums(t: tabl) -> None:
    print("| sum        |   seq  |")
    print("| :---       |  :---  |")
    print(f"| sum       | {tabl_sum(t)} |")
    print(f"| evensum   | {tabl_evensum(t)} |")
    print(f"| oddsum    | {tabl_oddsum(t)} |")
    print(f"| altsum    | {tabl_altsum(t)} |")
    print(f"| diagsum   | {tabl_diagsum(t)} |")
    print(f"| accusum   | {tabl_accsum(t)} |")
    print(f"| revaccusum | {tabl_revaccsum(t)} |")


def PrintFlats(t: tabl) -> None:
    print("| flat      |   seq  |")
    print("| :---      |  :---  |")
    print(f"| tabl     | {flat_tabl(t)} |")
    print(f"| rev      | {flat_rev(t)} |")
    print(f"| accu     | {flat_acc(t)} |")
    print(f"| revaccu  | {flat_revacc(t)} |")
    print(f"| accurev  | {flat_accrev(t)} |")
    print(f"| diag     | {flat_diag(t)} |")


def PrintViews(T: tri, rows: int = 7, verbose: bool = True) -> None:
    print("# " + T.id)
    cols: int = rows
    print()
    t: tabl = T.tab(rows)
    if verbose:
        print(T.id, "Triangle view")
    PrintRows(t)
    print()
    if verbose:
        print(T.id, "Flattened seqs")
    PrintFlats(t)
    print()
    if verbose:
        print(T.id, "Row sums")
    PrintSums(t)
    print()
    if verbose:
        print(T.id, "Diagonals as rows")
    PrintRowArray(T, rows, cols)
    print()
    if verbose:
        print(T.id, "Diagonals as columns")
    PrintColArray(T, rows, cols)
    print()
    if verbose:
        print(T.id, "Polynomial values as rows")
    PrintRowPolyArray(T, rows, cols)
    print()
    if verbose:
        print(T.id, "Polynomial values as columns")
    PrintColPolyArray(T, rows, cols)
    print()


def Profile(T: tri, hor: int = 10) -> dict[str, list[int]]:
    d: dict[str, list[int]] = {}
    t: tabl = T.tab(hor)
    ver: int = hor // 2
    # Triangle flattened
    d["tabflt"] = flat_tabl(T.tab(6))
    # Row sums
    d["rowsum"] = tabl_sum(t)
    d["evesum"] = tabl_evensum(t)
    d["oddsum"] = tabl_oddsum(t)
    d["altsum"] = tabl_altsum(t)
    d["accusum"] = tabl_accsum(t)
    d["revaccu"] = tabl_revaccsum(t)
    d["diasum"] = tabl_diagsum(t)
    # DiagsAsRowArray
    rows: int = ver
    cols: int = hor
    for j in range(rows):
        d["dirow" + str(j)] = [T(j + k, k) for k in range(cols)]
    # DiagsAsColArray
    rows: int = hor
    cols: int = ver
    for j in range(cols):
        d["dicol" + str(j)] = [T(j + k, j) for k in range(rows)]
    # RowPolyArray
    rows: int = ver
    cols: int = hor
    for j in range(rows):
        d["porow" + str(j)] = row_poly(T, j, cols)
    # ColPolyArray
    rows: int = ver
    cols: int = hor
    for j in range(rows):
        if j == 1:
            continue
        d["pocol" + str(j)] = col_poly(T, j, cols)
    return d


counter: int = 0


def PrintProfile(T: tri, dim: int, format: str) -> None:
    d: dict[str, list[int]] = Profile(T, dim)
    if format == "twolines":
        for seq in d.items():
            print(f"{T.id}|{seq[0]}\n{seq[1]}")
    if format == "oneline":
        print(T.id)
        for seq in d.items():
            print(f"|{seq[0]}, {seq[1]}")
        print()
    if format == "nonames":
        global counter
        for seq in d.items():
            counter += 1
            print(seq[1])


def PrintExtendedProfile(T: tri, dim: int, format: str) -> None:

    tim: int = dim + dim // 2
    PrintProfile(T, dim, format)
    I = inversion_wrapper(T, tim)
    if I != None:
        PrintProfile(I, dim, format)
    R = reversion_wrapper(T, tim)
    PrintProfile(R, dim, format)
    R = revinv_wrapper(T, tim)
    if R != None:
        PrintProfile(R, dim, format)
    R = invrev_wrapper(T, tim)
    if R != None:
        PrintProfile(R, dim, format)

    if format == "nonames":
        global counter
        print(counter, "sequences generated.")


@cache
def _abel(n: int) -> list[int]:
    if n == 0:
        return [1]
    return [binomial(n - 1, k - 1) * n ** (n - k) if k > 0 else 0 for k in range(n + 1)]


@set_attributes(_abel, "ABELPOLYNOMS", True)
def abel(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _abel(n).copy()
    return _abel(n)[k]


@cache
def _bell(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [_bell(n - 1)[n - 1]] + _bell(n - 1)
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row


@set_attributes(_bell, "BELLTRIANGLE", False)
def bell(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _bell(n).copy()
    return _bell(n)[k]


@cache
def _bessel(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _bessel(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = row[k - 1] + (2 * (n - 1) - k) * row[k]
    return row


@set_attributes(_bessel, "BESSELPOLYNO", True)
def bessel(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _bessel(n).copy()
    return _bessel(n)[k]


@cache
def _binomial(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [1] + _binomial(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    return row


@set_attributes(_binomial, "BINOMIALCOEF", True)
def binomial(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _binomial(n).copy()
    return _binomial(n)[k]


@cache
def _catalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _catalan(n - 1) + [_catalan(n - 1)[n - 1]]
    return list(accumulate(row))


@set_attributes(_catalan, "FUSSCATALAN1", False)
def catalan(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _catalan(n).copy()
    return _catalan(n)[k]


@cache
def _catalan_aerated(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return _catalan_aerated(n - 1)[k] if k >= 0 and k < n else 0

    row: list[int] = _catalan_aerated(n - 1) + [1]
    for k in range(0, n):
        row[k] = r(k - 1) + r(k + 1)
    return row


@set_attributes(_catalan_aerated, "CATALANAERAT", True)
def catalan_aerated(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _catalan_aerated(n).copy()
    return _catalan_aerated(n)[k]


@cache
def _central_cycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _central_cycle(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n + k - 1) * (row[k] + row[k - 1])
    return row


@set_attributes(_central_cycle, "CENTRCYCFACT", False)
def central_cycle(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _central_cycle(n).copy()
    return _central_cycle(n)[k]


@cache
def _central_set(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _central_set(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = k**2 * row[k] + row[k - 1]
    return row


@set_attributes(_central_set, "CENTRSETFACT", True)
def central_set(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _central_set(n).copy()
    return _central_set(n)[k]


@cache
def _chebyshevS(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    rov: list[int] = _chebyshevS(n - 2)
    row: list[int] = [0] + _chebyshevS(n - 1)
    for k in range(0, n - 1):
        row[k] -= rov[k]
    return row


@set_attributes(_chebyshevS, "CHEBYSHEVSPO", True)
def chebyshevS(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _chebyshevS(n).copy()
    return _chebyshevS(n)[k]


@cache
def _chebyshevT(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    rov: list[int] = _chebyshevT(n - 2)
    row: list[int] = [0] + _chebyshevT(n - 1)
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] = 2 * row[k] - rov[k]
    return row


@set_attributes(_chebyshevT, "CHEBYSHEVTPO", True)
def chebyshevT(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _chebyshevT(n).copy()
    return _chebyshevT(n)[k]


@cache
def _chebyshevU(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 2]
    rov: list[int] = _chebyshevU(n - 2)
    row: list[int] = [0] + _chebyshevU(n - 1)
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] = 2 * row[k] - rov[k]
    return row


@set_attributes(_chebyshevU, "CHEBYSHEVUPO", True)
def chebyshevU(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _chebyshevU(n).copy()
    return _chebyshevU(n)[k]


@cache
def _ctree(n: int) -> list[int]:
    if n % 2 == 1:
        return [1] * (n + 1)
    return [1, 0] * (n // 2) + [1]


@set_attributes(_ctree, "CHRISMASTREE", True)
def ctree(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _ctree(n).copy()
    return _ctree(n)[k]


@cache
def _delannoy(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    rov: list[int] = _delannoy(n - 2)
    row: list[int] = _delannoy(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + rov[k - 1]
    return row


@set_attributes(_delannoy, "DELANNOYTRIA", False)
def delannoy(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _delannoy(n).copy()
    return _delannoy(n)[k]


@cache
def _euler(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _euler(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * n) // (k)
    row[0] = -sum((-1) ** (j // 2) * row[j] for j in range(n, 0, -2))
    return row


@set_attributes(_euler, "EULERTRIANGL", True)
def euler(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _euler(n).copy()
    return _euler(n)[k]


def euler_num(n: int) -> int:
    return _euler(n)[0]


@cache
def _eulerian(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _eulerian(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n - k) * row[k - 1] + (k + 1) * row[k]
    return row


@set_attributes(_eulerian, "EULERIANTRIA", False)
def eulerian(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _eulerian(n).copy()
    return _eulerian(n)[k]


@cache
def _eulerian2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _eulerian2(n - 1) + [0]
    for k in range(n, 1, -1):
        row[k] = (2 * n - k) * row[k - 1] + k * row[k]
    return row


@set_attributes(_eulerian2, "EULERIANORD2", False)
def eulerian2(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _eulerian2(n).copy()
    return _eulerian2(n)[k]


@cache
def _eulerianB(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _eulerianB(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = (2 * (n - k) + 1) * row[k - 1] + (2 * k + 1) * row[k]
    return row


@set_attributes(_eulerianB, "EULERIANTYPB", True)
def eulerianB(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _eulerianB(n).copy()
    return _eulerianB(n)[k]


@cache
def _euler_sec(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [
        binomial(n, k) * _euler_sec(n - k)[0] if k > 0 else 0 for k in range(n + 1)
    ]
    if n % 2 == 0:
        row[0] = -sum(row[2::2])
    return row


@set_attributes(_euler_sec, "EULERSECANTO", True)
def euler_sec(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _euler_sec(n).copy()
    return _euler_sec(n)[k]


def eulerS(n: int) -> int:
    return 0 if n % 2 == 1 else _euler_sec(n)[0]


@cache
def _euler_tan(n: int) -> list[int]:
    row: list[int] = [
        binomial(n, k) * _euler_tan(n - k)[0] if k > 0 else 0 for k in range(n + 1)
    ]
    if n % 2 == 1:
        row[0] = -sum(row[2::2]) + 1
    return row


@set_attributes(_euler_tan, "EULERTANGENT", False)
def euler_tan(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _euler_tan(n).copy()
    return _euler_tan(n)[k]


def eulerT(n: int) -> int:
    return 0 if n % 2 == 0 else _euler_tan(n)[0]


@cache
def _falling_factorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    r: list[int] = _falling_factorial(n - 1)
    row: list[int] = [n * r[k] for k in range(-1, n)]
    row[0] = 1
    return row


@set_attributes(_falling_factorial, "FALFACTORIAL", False)
def falling_factorial(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _falling_factorial(n).copy()
    return _falling_factorial(n)[k]


@cache
def _fibonacci(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _fibonacci(n - 1) + [1]
    s: int = row[1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1]
    row[0] = s
    return row


@set_attributes(_fibonacci, "FIBONACPASCA")
def fibonacci(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _fibonacci(n).copy()
    return _fibonacci(n)[k]


@cache
def _fubini(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return _fubini(n - 1)[k] if k <= n - 1 else 0

    row: list[int] = [0] + _fubini(n - 1)
    for k in range(1, n + 1):
        row[k] = k * (r(k - 1) + r(k))
    return row


@set_attributes(_fubini, "FUBINITRIANG", False)
def fubini(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _fubini(n).copy()
    return _fubini(n)[k]


@cache
def _gaussq2(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = _gaussq2(n - 1)
    pow: list[int] = [1] + _gaussq2(n - 1)
    p = 2
    for k in range(1, n):
        pow[k] = row[k - 1] + p * row[k]
        p *= 2
    return pow


@set_attributes(_gaussq2, "GAUSSQ2COEFF", True)
def gaussq2(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _gaussq2(n).copy()
    return _gaussq2(n)[k]


@cache
def _genocchi(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _genocchi(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] += row[k + 1]
    for k in range(2, n + 2):
        row[k] += row[k - 1]
    return row[1:]


@set_attributes(_genocchi, "GENOCCHITRIA", False)
def genocchi(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _genocchi(n).copy()
    return _genocchi(n)[k]


@cache
def _harmonic(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _harmonic(n - 1) + [1]
    sav: int = row[1]
    for k in range(n - 1, 0, -1):
        row[k] = (n - 1) * row[k] + row[k - 1]
    row[1] += sav
    return row


@set_attributes(_harmonic, "HARMONICPOLY", True)
def harmonic(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _harmonic(n).copy()
    return _harmonic(n)[k]


@cache
def _hermite(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    rowA: list[int] = _hermite(n - 1)
    row: list[int] = _hermite(n - 1) + [0]
    for k in range(1, n):
        row[k] = rowA[k - 1] + (k + 1) * row[k + 1]
    row[0] = rowA[1]
    row[n] = 1
    return row


@set_attributes(_hermite, "HERMITEPOLYC", True)
def hermite(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _hermite(n).copy()
    return _hermite(n)[k]


@cache
def _laguerre(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _laguerre(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row


@set_attributes(_laguerre, "LAGUERREPOLY", True)
def laguerre(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _laguerre(n).copy()
    return _laguerre(n)[k]


@cache
def _lah(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _lah(n - 1) + [1]
    row[0] = 0
    for k in range(n - 1, 0, -1):
        row[k] = row[k] * (n + k - 1) + row[k - 1]
    return row


@set_attributes(_lah, "LAHTRIANGLES", True)
def lah(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _lah(n).copy()
    return _lah(n)[k]


@cache
def t(n: int, k: int, m: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return n**k
    return m * t(n, k - 1, m) + t(n - 1, k, m + 1)


@cache
def _lehmer(n: int) -> list[int]:
    return [t(k - 1, n - k, n - k) if n != k else 1 for k in range(n + 1)]


@set_attributes(_lehmer, "LEHMERCOMTET", True)
def lehmer(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _lehmer(n).copy()
    return _lehmer(n)[k]


@cache
def _leibniz(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _leibniz(n - 1) + [n + 1]
    row[0] = row[n] = n + 1
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@set_attributes(_leibniz, "LEIBNIZTRIAN", False)
def leibniz(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _leibniz(n).copy()
    return _leibniz(n)[k]


@cache
def _levin(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _levin(n - 1) + [1]
    row[0] = row[n] = (row[n - 1] * (4 * n - 2)) // n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@set_attributes(_levin, "LEVINSTRIANG", False)
def levin(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _levin(n).copy()
    return _levin(n)[k]


@cache
def _lozanic(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [1] + _lozanic(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    if n % 2 != 0:
        return row
    for k in range(1, n, 2):
        row[k] -= binomial(n // 2 - 1, (k - 1) // 2)
    return row


@set_attributes(_lozanic, "LOZANICTRIAN", True)
def lozanic(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _lozanic(n).copy()
    return _lozanic(n)[k]


@cache
def _motzkin(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return _motzkin(n - 1)[k] if k >= 0 and k < n else 0

    row: list[int] = _motzkin(n - 1) + [1]
    for k in range(0, n):
        row[k] += r(k - 1) + r(k + 1)
    return row


@set_attributes(_motzkin, "MOTZKINTRIAN", True)
def motzkin(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _motzkin(n).copy()
    return _motzkin(n)[k]


@cache
def _narayana(n: int) -> list[int]:
    if n < 3:
        return ([1], [0, 1], [0, 1, 1])[n]
    a: list[int] = _narayana(n - 2) + [0, 0]
    row: list[int] = _narayana(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = (
            (row[k] + row[k - 1]) * (2 * n - 1)
            - (a[k] - 2 * a[k - 1] + a[k - 2]) * (n - 2)
        ) // (n + 1)
    return row


@set_attributes(_narayana, "NARAYANATRIA", True)
def narayana(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _narayana(n).copy()
    return _narayana(n)[k]


@cache
def _nicomachus(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _nicomachus(n - 1) + [3 * _nicomachus(n - 1)[n - 1]]
    for k in range(0, n):
        row[k] *= 2
    return row


@set_attributes(_nicomachus, "NICOMACHUSTR", False)
def nicomachus(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _nicomachus(n).copy()
    return _nicomachus(n)[k]


@cache
def _one(n: int) -> list[int]:
    if n == 0:
        return [1]
    return _one(n - 1) + [1]


@set_attributes(_one, "ONEPERTUTTIS", True)
def one(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _one(n).copy()
    return _one(n)[k]


@cache
def _ordinals(n: int) -> list[int]:
    if n == 0:
        return [0]
    return _ordinals(n - 1) + [n]


@set_attributes(_ordinals, "ORDINALNUMBR", False)
def ordinals(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _ordinals(n).copy()
    return _ordinals(n)[k]


@cache
def _ordered_cycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _ordered_cycle(n - 1) + [0]
    row[n] = row[n] * n
    for k in range(n, 0, -1):
        row[k] = (n - 1) * row[k] + k * row[k - 1]
    return row


@set_attributes(_ordered_cycle, "ORDEREDCYCLE", False)
def ordered_cycle(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _ordered_cycle(n).copy()
    return _ordered_cycle(n)[k]


@cache
def _p(n: int, k: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return 1 if n == 0 else 0
    return _p(n - 1, k - 1) + _p(n - k, k)


@cache
def _partnum_exact(n: int) -> list[int]:
    return [_p(n, k) for k in range(n + 1)]


@cache
def _partnum_atmost(n: int) -> list[int]:
    return list(accumulate(_partnum_exact(n)))


@set_attributes(_partnum_exact, "PARTITIONNUM", True)
def partnum_exact(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _partnum_exact(n).copy()
    return _partnum_exact(n)[k]


@set_attributes(_partnum_atmost, "PARTITIONMAX", False)
def partnum_atmost(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _partnum_atmost(n).copy()
    return _partnum_atmost(n)[k]


@cache
def _polygonal(n: int) -> list[int]:
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    rov: list[int] = _polygonal(n - 2)
    row: list[int] = _polygonal(n - 1) + [n]
    row[n - 1] += row[n - 2]
    for k in range(2, n - 1):
        row[k] += row[k] - rov[k]
    return row


@set_attributes(_polygonal, "POLYGONALNUM", False)
def polygonal(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _polygonal(n).copy()
    return _polygonal(n)[k]


@cache
def _powlag(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _powlag(n - 1) + [1]
    row[0] = row[n] = row[0] * n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@set_attributes(_powlag, "POWERSLAGUER", False)
def powlag(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _powlag(n).copy()
    return _powlag(n)[k]


@cache
def _rencontres(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = [
        (n - 1) * (_rencontres(n - 1)[0] + _rencontres(n - 2)[0])
    ] + _rencontres(n - 1)
    for k in range(1, n - 1):
        row[k] = (n * row[k]) // k
    return row


@set_attributes(_rencontres, "RENCONTRESTR", True)
def rencontres(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _rencontres(n).copy()
    return _rencontres(n)[k]


@cache
def _rising_factorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _rising_factorial(n - 1)
    for k in range(0, n):
        row[k] += (n - k) * row[k + 1]
    return row


@set_attributes(_rising_factorial, "RISFACTORIAL", True)
def rising_factorial(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _rising_factorial(n).copy()
    return _rising_factorial(n)[k]


@cache
def _schroeder(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _schroeder(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + row[k + 1]
    return row


@set_attributes(_schroeder, "SCHROEDERTRI", True)
def schroeder(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _schroeder(n).copy()
    return _schroeder(n)[k]


@cache
def _bilatpath(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _bilatpath(n - 1) + [1]

    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * (2 * n - k)) // k
    row[0] = (row[0] * (4 * n - 2)) // n
    return row


@set_attributes(_bilatpath, "BILATERALSCH", True)
def bilatpath(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _bilatpath(n).copy()
    return _bilatpath(n)[k]


@cache
def _seidel(n: int) -> list[int]:
    if n == 0:
        return [1]
    rowA: list[int] = _seidel(n - 1)
    row: list[int] = [0] + _seidel(n - 1)
    row[1] = row[n]
    for k in range(2, n + 1):
        row[k] = row[k - 1] + rowA[n - k]
    return row


def _seidel_boust(n: int) -> list[int]:
    return _seidel(n) if n % 2 else _seidel(n)[::-1]


@set_attributes(_seidel, "SEIDELTRIANG", False)
def seidel(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _seidel(n).copy()
    return _seidel(n)[k]


@set_attributes(_seidel_boust, "SEIDELBOUSTO", False)
def seidel_boust(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _seidel_boust(n).copy()
    return _seidel_boust(n)[k]


@cache
def _sierpinski(n: int) -> list[int]:
    return [binomial(n, k) % 2 for k in range(n + 1)]


@set_attributes(_sierpinski, "SIERPINSKITR", True)
def sierpinski(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _sierpinski(n).copy()
    return _sierpinski(n)[k]


@cache
def _stirling_cycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _stirling_cycle(n - 1)
    for k in range(1, n):
        row[k] = row[k] + (n - 1) * row[k + 1]
    return row


@set_attributes(_stirling_cycle, "STIRLING1CYC", True)
def stirling_cycle(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _stirling_cycle(n).copy()
    return _stirling_cycle(n)[k]


@cache
def _stirling_cycle2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]
    rov: list[int] = _stirling_cycle2(n - 2)
    row: list[int] = _stirling_cycle2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * (rov[k - 1] + row[k])
    return row


@set_attributes(_stirling_cycle2, "STIRLCYCORD2", False)
def stirling_cycle2(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _stirling_cycle2(n).copy()
    return _stirling_cycle2(n)[k]


@cache
def _stirling_cycleB(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _stirling_cycleB(n - 1) + [1]
    m = 2 * n - 1
    for k in range(n - 1, 0, -1):
        row[k] = m * row[k] + row[k - 1]
    row[0] *= m
    return row


@set_attributes(_stirling_cycleB, "STIRLCYCANAB", True)
def stirling_cycleB(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _stirling_cycleB(n).copy()
    return _stirling_cycleB(n)[k]


@cache
def _stirling_set(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _stirling_set(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row


@set_attributes(_stirling_set, "STIRLING2SET", True)
def stirling_set(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _stirling_set(n).copy()
    return _stirling_set(n)[k]


@cache
def _stirling_set2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]
    rov: list[int] = _stirling_set2(n - 2)
    row: list[int] = _stirling_set2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * rov[k - 1] + k * row[k]
    return row


@set_attributes(_stirling_set2, "STIRLSETORD2", False)
def stirling_set2(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _stirling_set2(n).copy()
    return _stirling_set2(n)[k]


@cache
def _stirling_setB(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    pow: list[int] = _stirling_setB(n - 1)
    row: list[int] = _stirling_setB(n - 1) + [1]
    row[0] += 2 * row[1]

    for k in range(1, n - 1):
        row[k] = 2 * (k + 1) * pow[k + 1] + (2 * k + 1) * pow[k] + pow[k - 1]
    row[n - 1] = (2 * n - 1) * pow[n - 1] + pow[n - 2]
    return row


@set_attributes(_stirling_setB, "STIRLSETANAB", True)
def stirling_setB(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _stirling_setB(n).copy()
    return _stirling_setB(n)[k]


@cache
def _sylvester(n: int) -> list[int]:
    return [
        sum(binomial(n, k - j) * stirling_cycle(n - k + j, j) for j in range(k + 1))
        for k in range(n + 1)
    ]


@set_attributes(_sylvester, "SYLVESTERPOL", False)
def sylvester(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _sylvester(n).copy()
    return _sylvester(n)[k]


@cache
def _sympoly(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _sympoly(n - 1) + [1]
    for m in range(n - 1, 0, -1):
        row[m] = (n - m + 1) * row[m] + row[m - 1]
    row[0] *= n
    return row


@set_attributes(_sympoly, "SYMPOLYNOMIA", True)
def sympoly(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _sympoly(n).copy()
    return _sympoly(n)[k]


@cache
def _ternary_tree(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _ternary_tree(n - 1) + [_ternary_tree(n - 1)[n - 1]]
    return list(accumulate(accumulate(row)))


@set_attributes(_ternary_tree, "TERNARYTREES", False)
def ternary_tree(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _ternary_tree(n).copy()
    return _ternary_tree(n)[k]


@cache
def _ward_set(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _ward_set(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k] + (n + k - 1) * row[k - 1]
    return row


@set_attributes(_ward_set, "WARDSETNUMBR", False)
def ward_set(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _ward_set(n).copy()
    return _ward_set(n)[k]


@cache
def _worpitzky(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _worpitzky(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k - 1] + (k + 1) * row[k]
    return row


@set_attributes(_worpitzky, "WORPITZKYNUM", False)
def worpitzky(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _worpitzky(n).copy()
    return _worpitzky(n)[k]


tabl_fun: list[tri] = [
    abel,
    bell,
    bessel,
    bilatpath,
    binomial,
    catalan,
    catalan_aerated,
    central_cycle,
    central_set,
    chebyshevS,
    chebyshevT,
    chebyshevU,
    ctree,
    delannoy,
    euler,
    eulerian,
    eulerian2,
    eulerianB,
    euler_sec,
    euler_tan,
    falling_factorial,
    fibonacci,
    fubini,
    gaussq2,
    genocchi,
    harmonic,
    hermite,
    laguerre,
    lah,
    lehmer,
    leibniz,
    levin,
    lozanic,
    motzkin,
    narayana,
    nicomachus,
    one,
    ordinals,
    ordered_cycle,
    partnum_exact,
    partnum_atmost,
    polygonal,
    powlag,
    rencontres,
    rising_factorial,
    schroeder,
    seidel,
    seidel_boust,
    sierpinski,
    stirling_cycle,
    stirling_cycle2,
    stirling_cycleB,
    stirling_set,
    stirling_set2,
    stirling_setB,
    sylvester,
    sympoly,
    ternary_tree,
    ward_set,
    worpitzky,
]


def sortfile(inpath, outpath) -> None:
    with open(inpath, "r") as infile:
        with open(outpath, "w") as outfile:
            inlines = infile.readlines()
            outlines = sorted(set(inlines))
            for line in outlines:
                outfile.write(line)


def SaveTables(dim: int = 7) -> None:
    path = "tables.md"
    with open(path, "w+") as dest:
        with contextlib.redirect_stdout(dest):
            for fun in tabl_fun:
                PrintViews(fun, dim)


def SaveExtendedTables(dim: int = 7) -> None:
    tim: int = dim + dim
    path = "tables.md"
    with open(path, "w+") as dest:
        with contextlib.redirect_stdout(dest):
            for fun in tabl_fun:
                PrintViews(fun, dim)
                I = inversion_wrapper(fun, tim)
                if I != None:
                    PrintViews(I, dim)
                R = reversion_wrapper(fun, tim)
                PrintViews(R, dim)
                R = revinv_wrapper(fun, tim)
                if R != None:
                    PrintViews(R, dim)
                R = invrev_wrapper(fun, tim)
                if R != None:
                    PrintViews(R, dim)


def WriteProfile(
    dest: TextIOWrapper, fun: tri, dim: int = 10, seqonly: bool = True
) -> None:
    p: dict[str, list[int]] = Profile(fun, dim)
    id: str = fun.id
    for seq in p.items():
        if seqonly:
            dest.write(f"{seq[1]}\n")
        else:
            dest.write(f"{seq[1]},{seq[0]},{id}\n")


def SaveProfiles(path: str, dim: int = 10, seqonly: bool = True) -> None:
    dest: TextIOWrapper = open(path, "w+")
    for fun in tabl_fun:
        WriteProfile(dest, fun, dim, seqonly)
    dest.close()


def SaveExtendedProfiles(path: str, dim: int = 10, seqonly: bool = True) -> None:
    dest: TextIOWrapper = open(path, "w+")
    tim: int = dim + dim // 2
    for fun in tabl_fun:
        WriteProfile(dest, fun, dim, seqonly)
        I = inversion_wrapper(fun, tim)
        if I != None:
            WriteProfile(dest, I, dim, seqonly)
        R = reversion_wrapper(fun, tim)
        WriteProfile(dest, R, dim, seqonly)
        R = revinv_wrapper(fun, tim)
        if R != None:
            WriteProfile(dest, R, dim, seqonly)
        R = invrev_wrapper(fun, tim)
        if R != None:
            WriteProfile(dest, R, dim, seqonly)
    dest.close()


def shortabsdata(inpath: str, outpath: str) -> None:
    with open(inpath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        seq_list = [[seq[0], [abs(int(t)) for t in seq[1:-1]]] for seq in reader]
        with open(outpath, "w") as outfile:
            for seq in seq_list:
                if len(seq[1]) < 29:
                    continue
                s = (
                    str(seq[1][0:28])
                    .replace("[", ",")
                    .replace("]", ",")
                    .replace(" ", "")
                )
                outfile.write(str(seq[0]) + s + "\n")


def ess_equal(s: list[int], tt: list[int]) -> tuple[int, int, int]:
    t = [abs(x) for x in tt]
    K = min(len(t), len(s)) // 2
    for i in range(K):
        for k in range(K):
            L = len(s[i : i + K])
            if s[i : i + K] == t[k : k + L]:
                j = 0
                while i + j < len(s) and k + j < len(t) and s[i + j] == t[k + j]:
                    j += 1
                return (i, k, j)
    return (-1, -1, 0)


def read_seqdata(datapath: str) -> list[list]:
    seq_list = []
    with open(datapath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        seq_list = [[seq[0], [int(t) for t in seq[1:-1]]] for seq in reader]
    return seq_list


def SimilarSequences(Seqs: list[list], A: list[int]) -> list:
    candidates = []
    count = 0
    Abs = [abs(x) for x in A]
    for seq in Seqs:
        a, b, size = ess_equal(Abs, seq[1])
        if size > min(16, len(A) // 2):
            candidates.append([seq[0], (a, b, size)])
            count += 1
        if count > 9:
            break
    return candidates


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


def lookup_similar_triangles(Seqs, T: tri) -> None:
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


def SimilarTriangles(datapath: str, md: bool = True) -> None:
    seq_list = []
    with open(datapath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        seq_list = [[seq[0], [int(t) for t in seq[1:-1]]] for seq in reader]
    if md:
        print("|  ID    |  OEIS  SIMILARS |")
        print("| :---:  |  :---  |")
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


def flat(t: tabl) -> list[int]:
    return [i for row in t for i in row]


def SeqToFixlenString(seq: list[int], maxlen: int = 90) -> str:
    separator = ","
    stri = "[ "
    maxl = 3
    for trm in seq:
        s = str(trm) + separator
        maxl += len(s)
        if maxl > maxlen:
            break
        stri += s
    return stri + "]"


def Traits(f: tri, dim: int, seqnum: bool = False) -> None:
    T = f.tab(dim)
    R = f.rev(dim)
    I = f.inv(dim)
    RI = f.revinv(dim)
    IR = f.invrev(dim)
    funname = f.id
    maxlen = (dim * (dim + 1)) // 2
    seqdata = []
    if seqnum:
        datapath = GetDataPath()
        seqdata = read_seqdata(datapath)

    def printer(seq, traitname) -> None:
        print(funname, traitname)
        if seqnum:
            print(SimilarSequences(seqdata, seq))
        print(SeqToFixlenString(seq, 80))
        # sep = ","
        # write(f"{candidates}{sep}{funname}{sep}{traitname}{sep}{seqstr}")

    print(f"\n=================\n{funname}\n")
    print("ANumber,Triangle,Trait,Sequence")
    printer(flat(T), "Triangle ")
    printer(flat(R), "Reverse  ")
    if I != []:
        printer(flat(I), "Inverse  ")
        printer(flat(RI), "RevInv   ")
    if IR != []:
        printer(flat(IR), "InvRev   ")
    printer(flat_acc(T), "AccTri   ")
    printer(flat_revacc(T), "RevAccTri")
    printer(flat_accrev(T), "AccRevTri")
    printer(flat(diag_tabl(T)), "DiagTri  ")
    printer(flat(poly_tabl(f, dim)), "PolyTri  ")
    printer(flat(trans_self(f, dim)), "ConvTri  ")
    printer(flat(transbin_tabl(f, dim)), "BinConT  ")
    printer(flat(invtransbin_tabl(f, dim)), "IBinConT ")
    printer(tabl_sum(T), "Sum      ")
    printer(tabl_evensum(T), "EvenSum  ")
    printer(tabl_oddsum(T), "OddSum   ")
    printer(tabl_altsum(T), "AltSum   ")
    printer(tabl_accsum(T), "AccSum   ")
    printer(tabl_accrevsum(T), "AccRevSum")
    printer(tabl_revaccsum(T), "RevAccSum")
    printer(tabl_diagsum(T), "DiagSum  ")
    printer(middle(T), "Middle   ")
    printer(central(T), "Central  ")
    printer(left_side(T), "LeftSide ")
    printer(right_side(T), "RightSide")
    printer(pos_half(T), "PosHalf  ")
    printer(neg_half(T), "NegHalf  ")
    printer(transbin_val(f, maxlen), "BinConV  ")
    printer(invtransbin_val(f, maxlen), "IBinConV ")

    def TransSqrs(f, n: int) -> list[int]:
        return trans(f, lambda k: k * k, n)

    def TransNat0(f, n: int) -> list[int]:
        return trans(f, lambda k: k, n)

    def TransNat1(f, n: int) -> list[int]:
        return trans(f, lambda k: k + 1, n)

    printer(TransSqrs(f, maxlen), "TransSqrs")
    printer(TransNat0(f, maxlen), "TransNat0")
    printer(TransNat1(f, maxlen), "TransNat1")
    printer(row_diag(f, 0, maxlen), "DiagRow0 ")
    printer(row_diag(f, 1, maxlen), "DiagRow1 ")
    printer(row_diag(f, 2, maxlen), "DiagRow2 ")
    printer(row_diag(f, 3, maxlen), "DiagRow3 ")
    printer(col_diag(f, 0, maxlen), "DiagCol0 ")
    printer(col_diag(f, 1, maxlen), "DiagCol1 ")
    printer(col_diag(f, 2, maxlen), "DiagCol2 ")
    printer(col_diag(f, 3, maxlen), "DiagCol3 ")
    printer(row_poly(f, 0, maxlen), "PolyRow0 ")
    printer(row_poly(f, 1, maxlen), "PolyRow1 ")
    printer(row_poly(f, 2, maxlen), "PolyRow2 ")
    printer(row_poly(f, 3, maxlen), "PolyRow3 ")
    printer(col_poly(f, 0, maxlen), "PolyCol0 ")
    printer(col_poly(f, 1, maxlen), "PolyCol1 ")
    printer(col_poly(f, 2, maxlen), "PolyCol2 ")
    printer(col_poly(f, 3, maxlen), "PolyCol3 ")
    printer(poly_diag(f, maxlen), "PolyDiag ")
