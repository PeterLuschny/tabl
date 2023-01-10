from functools import cache, reduce
from itertools import accumulate, count
from math import lcm, gcd, floor, factorial
from sys import setrecursionlimit
from typing import Callable, TypeAlias
from io import TextIOWrapper
import contextlib
import csv
from fractions import Fraction as frac
from sympy import Matrix, Rational
from pathlib import Path

path = Path(__file__).parent
reldatapath = "data/oeis_data.csv"
datapath = (path / reldatapath).resolve()
relcsvpath = "data/csv"
csvpath = (path / relcsvpath).resolve()
allcsvfile = "data/allcsv.csv"
allcsvpath = (path / allcsvfile).resolve()


def GetDataPath() -> Path:
    return datapath


def GetCsvPath() -> Path:
    return csvpath


def GetAllCsvPath() -> Path:
    return allcsvpath


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

    @set_attributes(_psgen, T.id + "Inv", True)
    def psgen(n: int, k: int = -1) -> list[int] | int:
        if k == -1:
            return _psgen(n)
        return _psgen(n)[k]

    return psgen


def reversion_wrapper(T: tri, dim: int) -> tri:
    t = T.rev(dim)

    def _rsgen(n: int) -> trow:
        return list(t[n])

    @set_attributes(_rsgen, T.id + "Rev", True)
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


def SubTriangle(T: tri, N: int, K: int, dim: int) -> tabl:
    return [[T(n, k) for k in range(K, K - N + n + 1)] for n in range(N, N + dim)]


def AbsSubTriangle(T: tri, N: int, K: int, dim: int) -> tabl:
    return [[abs(T(n, k)) for k in range(K, K - N + n + 1)] for n in range(N, N + dim)]


def set_attributes(
    r: rgen, id: str, sim: list, vert: bool = False
) -> Callable[[tri], tri]:
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
        if I == []:
            return []
        return [[I[n][n - k] for k in range(n + 1)] for n in range(dim)]

    def makeinvrev(dim: int) -> tabl:
        R = [list(reversed(r(n))) for n in range(dim)]
        M = [[R[n][k] if k <= n else 0 for k in range(dim)] for n in range(dim)]
        return InverseTabl(M)

    def sub(N: int, K: int) -> Callable[[int], tabl]:
        def gsub(dim: int) -> tabl:
            return [
                [r(n)[k] for k in range(K, K - N + n + 1)] for n in range(N, N + dim)
            ]

        return gsub

    def abssub(N: int, K: int) -> Callable[[int], tabl]:
        def gabssub(dim: int) -> tabl:
            return [
                [abs(r(n)[k]) for k in range(K, K - N + n + 1)]
                for n in range(N, N + dim)
            ]

        return gabssub

    def wrapper(f: tri) -> tri:
        f.tab = maketab
        f.rev = makerev
        f.mat = makemat
        f.inv = makeinv
        f.flat = makeflat
        f.revinv = makerevinv
        f.invrev = makeinvrev
        f.sub = sub
        f.abssub = abssub
        f.sim = sim
        f.id = id
        return f

    return wrapper


def SeqToFixlenString(seq: list[int], maxlen: int = 90, separator=",") -> str:
    stri = "["
    maxl = 3
    for trm in seq:
        s = str(trm) + separator
        maxl += len(s)
        if maxl > maxlen:
            break
        stri += s
    return stri + "]"


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


def row_lcm(f: tri, n: int) -> int:
    Z = [v for v in f(n) if not v in [-1, 0, 1]]
    return reduce(lcm, Z) if Z != [] else 1


def row_gcd(f: tri, n: int) -> int:
    Z = [v for v in f(n) if not v in [-1, 0, 1]]
    return reduce(gcd, Z) if Z != [] else 1


def tabl_lcm(f: tri, leng: int) -> list[int]:
    return [row_lcm(f, n) for n in range(leng)]


def tabl_gcd(f: tri, leng: int) -> list[int]:
    return [row_gcd(f, n) for n in range(leng)]


def row_max(f: tri, n: int) -> int:
    absf = [abs(t) for t in f(n)]
    return reduce(max, absf)


def tabl_max(f: tri, leng: int) -> list[int]:
    return [row_max(f, n) for n in range(leng)]


def trans(M: tri, V: Callable, leng: int) -> list[int]:
    return [sum(M(n, k) * V(k) for k in range(n + 1)) for n in range(leng)]


def trans_sqrs(f: tri, n: int) -> list[int]:
    return trans(f, lambda k: k * k, n)


def trans_nat0(f: tri, n: int) -> list[int]:
    return trans(f, lambda k: k, n)


def trans_nat1(f: tri, n: int) -> list[int]:
    return trans(f, lambda k: k + 1, n)


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
    print(T.sim)
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


@set_attributes(_abel, "Abel", ["A061356", "A137452", "A139526"], True)
def abel(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _abel(n).copy()
    return _abel(n)[k]


@cache
def F(n: int) -> int:
    return factorial(n) ** 3 * ((n + 1) * (n + 1) * (n + 2))


@cache
def _baxter(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + [
        (2 * F(n - 1)) // (F(k - 1) * F(n - k)) for k in range(1, n + 1)
    ]
    return row


@set_attributes(_baxter, "baxter", ["A359363", "A056939"], False)
def baxter(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _baxter(n).copy()
    return _baxter(n)[k]


@cache
def _bell(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [_bell(n - 1)[n - 1]] + _bell(n - 1)
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row


@set_attributes(_bell, "Bell", ["A011971", "A011972", "A123346"], False)
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


@set_attributes(_bessel, "Bessel", ["A001497", "A001498", "A122850", "A132062"], True)
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


@set_attributes(
    _binomial,
    "Binomial",
    [
        "A007318",
        "A074909",
        "A108086",
        "A117440",
        "A118433",
        "A130595",
        "A135278",
        "A154926",
    ],
    True,
)
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
    pow: list[int] = _catalan(n - 1) + [0]
    row: list[int] = pow.copy()
    for k in range(n - 1, 0, -1):
        row[k] = pow[k - 1] + 2 * pow[k] + pow[k + 1]
    row[n] = 1
    return row


@set_attributes(_catalan, "Catalan", ["A128899", "A039598"], False)
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


@set_attributes(
    _catalan_aerated, "CatalanAer", ["A052173", "A053121", "A112554", "A322378"], True
)
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


@set_attributes(_central_cycle, "CentralCyc", ["A111999", "A259456", "A269940"], False)
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


@set_attributes(_central_set, "CentralSet", ["A008957", "A036969", "A269945"], True)
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


@set_attributes(
    _chebyshevS, "ChebyshevS", ["A049310", "A053119", "A112552", "A168561"], True
)
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


@set_attributes(_chebyshevT, "ChebyshevT", ["A039991", "A053120", "A081265"], True)
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


@set_attributes(_chebyshevU, "ChebyshevU", ["A053117", "A053118", "A115322"], True)
def chebyshevU(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _chebyshevU(n).copy()
    return _chebyshevU(n)[k]


@cache
def _ctree(n: int) -> list[int]:
    if n % 2 == 1:
        return [1] * (n + 1)
    return [1, 0] * (n // 2) + [1]


@set_attributes(_ctree, "ChristTree", ["A106465", "A106470"], True)
def ctree(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _ctree(n).copy()
    return _ctree(n)[k]


@cache
def _compo(n: int) -> list[int]:
    if n == 0:
        return [1]
    cm = _compo_max(n)
    return [cm[k] - cm[k - 1] if k > 0 else 0 for k in range(n + 1)]


@set_attributes(_compo, "Compositions", ["A048004"], True)
def compo(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _compo(n).copy()
    return _compo(n)[k]


@cache
def _compo_max(n: int) -> list[int]:
    @cache
    def t(n: int, k: int) -> int:
        if n == 0 or k == 1:
            return 1
        return sum(t(n - j, k) for j in range(1, min(n, k) + 1))

    return [t(n, k) for k in range(n + 1)]


@set_attributes(_compo_max, "CompositionMax", ["A126198"], True)
def compo_max(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _compo_max(n).copy()
    return _compo_max(n)[k]


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


@set_attributes(_delannoy, "Delannoy", ["A008288"], False)
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


@set_attributes(_euler, "Euler", ["A109449", "A247453"], True)
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


@set_attributes(_eulerian, "Eulerian", ["A008292", "A123125", "A173018"], False)
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


@set_attributes(
    _eulerian2, "Eulerian2", ["A008517", "A112007", "A163936", "A340556"], False
)
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


@set_attributes(_eulerianB, "EulerianB", ["A060187", "A138076"], True)
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


@set_attributes(_euler_sec, "EulerSec", ["A119879", "A081658", "A153641"], True)
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


@set_attributes(
    _euler_tan,
    "EulerTan",
    ["A162660", "A350972", "A155585", "A009006", "A000182"],
    False,
)
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


@set_attributes(
    _falling_factorial,
    "FallingFact",
    ["A008279", "A068424", "A094587", "A173333", "A181511"],
    False,
)
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


@set_attributes(_fibonacci, "Fibonacci", ["A105809", "A228074", "A354267"], False)
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


@set_attributes(_fubini, "Fubini", ["A019538", "A090582", "A131689", "A278075"], False)
def fubini(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _fubini(n).copy()
    return _fubini(n)[k]


@cache
def _fuss_catalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _fuss_catalan(n - 1) + [_fuss_catalan(n - 1)[n - 1]]
    return list(accumulate(row))


@set_attributes(_fuss_catalan, "FussCatalan", ["A030237", "A054445", "A355173"], False)
def fuss_catalan(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _fuss_catalan(n).copy()
    return _fuss_catalan(n)[k]


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


@set_attributes(_gaussq2, "Gaussq2", ["A022166"], True)
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


@set_attributes(_genocchi, "Genocchi", ["A297703"], False)
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


@set_attributes(_harmonic, "Harmonic", ["A109822", "A358694"], True)
def harmonic(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _harmonic(n).copy()
    return _harmonic(n)[k]


@cache
def _hermiteE(n: int) -> list[int]:
    row: list[int] = [0] * (n + 1)
    row[n] = 1
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (n - k)
    return row


@set_attributes(_hermiteE, "HermiteE", ["A066325", "A073278", "A099174"], True)
def hermiteE(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _hermiteE(n).copy()
    return _hermiteE(n)[k]


@cache
def _hermiteH(n: int) -> list[int]:
    row: list[int] = [0] * (n + 1)
    row[n] = 2**n
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (2 * (n - k))
    return row


@set_attributes(_hermiteH, "HermiteH", ["A060821"], True)
def hermiteH(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _hermiteH(n).copy()
    return _hermiteH(n)[k]


@cache
def _laguerre(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _laguerre(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row


@set_attributes(_laguerre, "Laguerre", ["A021009", "A021010", "A144084"], True)
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


@set_attributes(
    _lah,
    "Lah",
    ["A008297", "A066667", "A089231", "A105278", "A111596", "A271703"],
    True,
)
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


@set_attributes(_lehmer, "Lehmer", ["A039621", "A354794"], True)
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


@set_attributes(_leibniz, "Leibniz", ["A003506"], False)
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


@set_attributes(_levin, "Levin", ["A356546"], False)
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


@set_attributes(_lozanic, "Lozanic", ["A034851"], True)
def lozanic(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _lozanic(n).copy()
    return _lozanic(n)[k]


@cache
def _motzkin(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]
    l = 0 if n % 2 else (_motzkin(n - 2)[n - 2] * 2 * (n - 1)) // (n // 2 + 1)
    row = _motzkin(n - 1) + [l]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row


@set_attributes(_motzkin, "Motzkin-Poly", ["A"], True)
def motzkin(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _motzkin(n).copy()
    return _motzkin(n)[k]


@cache
def _motzkin_gf(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return _motzkin_gf(n - 1)[k] if k >= 0 and k < n else 0

    row: list[int] = _motzkin_gf(n - 1) + [1]
    for k in range(0, n):
        row[k] += r(k - 1) + r(k + 1)
    return row


@set_attributes(_motzkin_gf, "Motzkin-Gf", ["A026300", "A064189", "A009766"], True)
def motzkin_gf(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _motzkin_gf(n).copy()
    return _motzkin_gf(n)[k]


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


@set_attributes(_narayana, "Narayana", ["A001263", "A090181", "A131198"], True)
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


@set_attributes(_nicomachus, "Nicomachus", ["A036561", "A081954", "A175840"], False)
def nicomachus(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _nicomachus(n).copy()
    return _nicomachus(n)[k]


@cache
def _one(n: int) -> list[int]:
    if n == 0:
        return [1]
    return _one(n - 1) + [1]


@set_attributes(_one, "One", ["A000012", "A008836", "A014077"], True)
def one(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _one(n).copy()
    return _one(n)[k]


@cache
def _ordinals(n: int) -> list[int]:
    if n == 0:
        return [0]
    return _ordinals(n - 1) + [n]


@set_attributes(
    _ordinals, "Ordinals", ["A002260", "A002262", "A004736", "A025581"], False
)
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


@set_attributes(_ordered_cycle, "OrderedCyc", ["A048594", "A075181", "A225479"], False)
def ordered_cycle(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _ordered_cycle(n).copy()
    return _ordered_cycle(n)[k]


@cache
def _part(n: int, k: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return 1 if n == 0 else 0
    return _part(n - 1, k - 1) + _part(n - k, k)


@cache
def _partnum_exact(n: int) -> list[int]:
    return [_part(n, k) for k in range(n + 1)]


@set_attributes(_partnum_exact, "Partition", ["A008284", "A058398", "A072233"], True)
def partnum_exact(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _partnum_exact(n).copy()
    return _partnum_exact(n)[k]


@cache
def _partnum_max(n: int) -> list[int]:
    return list(accumulate(_partnum_exact(n)))


@set_attributes(_partnum_max, "PartitionMax", ["A008284", "A058398", "A072233"], False)
def partnum_max(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _partnum_max(n).copy()
    return _partnum_max(n)[k]


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


@set_attributes(
    _polygonal, "Polygonal", ["A057145", "A134394", "A139600", "A139601"], False
)
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


@set_attributes(_powlag, "PowLaguerre", ["A021012", "A196347"], False)
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


@set_attributes(_rencontres, "Rencontres", ["A008290", "A098825"], True)
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


@set_attributes(
    _rising_factorial,
    "RisingFact",
    ["A008279", "A068424", "A094587", "A173333", "A181511"],
    True,
)
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


@set_attributes(
    _schroeder,
    "Schroeder",
    ["A033877", "A080245", "A080247", "A122538", "A106579"],
    True,
)
def schroeder(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _schroeder(n).copy()
    return _schroeder(n)[k]


@cache
def _schroeder_paths(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _schroeder_paths(n - 1) + [1]

    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * (2 * n - k)) // k
    row[0] = (row[0] * (4 * n - 2)) // n
    return row


@set_attributes(_schroeder_paths, "SchroederP", ["A063007", "A104684"], True)
def schroeder_paths(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _schroeder_paths(n).copy()
    return _schroeder_paths(n)[k]


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


@set_attributes(_seidel, "Seidel", ["A008281", "A008282", "A010094"], False)
def seidel(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _seidel(n).copy()
    return _seidel(n)[k]


def _seidel_boust(n: int) -> list[int]:
    return _seidel(n) if n % 2 else _seidel(n)[::-1]


@set_attributes(
    _seidel_boust, "SeidelBoust", ["A008280", "A108040", "A236935", "A239005"], False
)
def seidel_boust(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _seidel_boust(n).copy()
    return _seidel_boust(n)[k]


@cache
def _sierpinski(n: int) -> list[int]:
    return [binomial(n, k) % 2 for k in range(n + 1)]


@set_attributes(
    _sierpinski,
    "Sierpinski",
    ["A047999", "A090971", "A114700", "A143200", "A166282"],
    True,
)
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


@set_attributes(
    _stirling_cycle,
    "StirlingCyc",
    ["A008275", "A008276", "A048994", "A054654", "A094638", "A130534", "A132393"],
    True,
)
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


@set_attributes(
    _stirling_cycle2, "StirlingCyc2", ["A358622", "A008306", "A106828"], False
)
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


@set_attributes(
    _stirling_cycleB, "StirlingCycB", ["A028338", "A039757", "A039758", "A109692"], True
)
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


@set_attributes(
    _stirling_set,
    "StirlingSet",
    [
        "A008277",
        "A008278",
        "A048993",
        "A080417",
        "A106800",
        "A151511",
        "A151512",
        "A154959",
        "A213735",
    ],
    True,
)
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


@set_attributes(
    _stirling_set2, "StirlingSet2", ["A358623", "A008299", "A137375"], False
)
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


@set_attributes(_stirling_setB, "StirlingSetB", ["A154602"], True)
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


@set_attributes(_sylvester, "Sylvester", ["A341101"], False)
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


@set_attributes(_sympoly, "SymPoly", ["A093905", "A105954", "A165674", "A165675"], True)
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


@set_attributes(_ternary_tree, "TernaryTrees", ["A355172"], False)
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


@set_attributes(_ward_set, "WardSet", ["A134991", "A269939"], False)
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


@set_attributes(
    _worpitzky,
    "Worpitzki",
    ["A028246", "A053440", "A075263", "A130850", "A163626"],
    False,
)
def worpitzky(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _worpitzky(n).copy()
    return _worpitzky(n)[k]


tabl_fun: list[tri] = [
    abel,
    baxter,
    bell,
    bessel,
    binomial,
    catalan,
    catalan_aerated,
    central_cycle,
    central_set,
    chebyshevS,
    chebyshevT,
    chebyshevU,
    compo,
    compo_max,
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
    fuss_catalan,
    gaussq2,
    genocchi,
    harmonic,
    hermiteE,
    hermiteH,
    laguerre,
    lah,
    lehmer,
    leibniz,
    levin,
    lozanic,
    motzkin,
    motzkin_gf,
    narayana,
    nicomachus,
    one,
    ordinals,
    ordered_cycle,
    partnum_exact,
    partnum_max,
    polygonal,
    powlag,
    rencontres,
    rising_factorial,
    schroeder,
    schroeder_paths,
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


def GenerateCsvFile(fun: tri, dim: int = 24) -> None:
    csvfile = fun.id + ".csv"
    path = (GetCsvPath() / csvfile).resolve()
    with open(path, "w+") as dest:
        dest.write("Triangle,Trait,ANumber,Sequence\n")
        s = (
            str(fun.sim)
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace(",", "")
        )
        dest.write(f"OEIS Similars: {s},,,\n")
        Traits(fun, dim, True, dest)


def GenerateAllCsvFiles(dim: int = 24) -> None:
    for fun in tabl_fun:
        print(fun.id)
        GenerateCsvFile(fun, dim)


def AllTraits(seqnum: bool = False) -> None:
    dim = 28
    csvfile = open(GetAllCsvPath(), "w")
    if seqnum:
        csvfile.write("Triangle,Trait,ANumber,Sequence\n")
    else:
        csvfile.write("Triangle,Trait,Sequence\n")
    for fun in tabl_fun:  # is in tabl.py
        Traits(fun, dim, False, csvfile)
    csvfile.close()


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


Header = [
    "<!DOCTYPE html>",
    "<html lang='en'><head><meta charset='UTF-8'/>",
    "<meta name='viewport' content='width=device-width, initial-scale=1.0'/>",
]
CSS = [
    "<head><style> table, td, th, p {border-collapse: collapse; font-family: sans-serif; color: blue;}",
    "td, th {border-bottom: 0; padding: 4px}",
    "td {text-align: left}",
    "tr:nth-child(odd) {background: #eee;}",
    "tr:nth-child(even) {background: #fff;}",
    "tr.header {background: orange !important; color: white; font-weight: bold;}",
    "tr.subheader {background: lightgray !important; color: black;}",
    "tr.headerLastRow {border-bottom: 2px solid black;}",
    "th.rowNumber, td.rowNumber {text-align: right;}",
    "a {text-decoration: none; color:brown;}",
    "a:hover {background-color: #AFE1AF;} </style></head><body>",
]
Table = [
    "<table>",
    "<tr class = 'header headerLastRow'>",
    "<th style = 'text-align: left;'>Trait</th>",
    "<th style = 'text-align: left;'>ANumber</th>",
    "<th style = 'text-align: left;'>Sequence</th>",
    "</tr>",
]
Footer = [
    "<p>Note: The A-numbers are based on a finite number of numerical comparisons. ",
    "They ignore the offset and<br>sign, and might differ in the first few values.",
    "<i>Go to the <a href='https://luschny.de/math/oeis/index.html'>index</a>, ",
    "to the <a href='https://luschny.de/math/oeis/tables.html'>tables</a>, ",
    "or the <a href='https://github.com/PeterLuschny/tabl'>Python sources</a> on GitHub.</i></p>",
    "<p>&nbsp;</p>" "</body></html>",
]


def CsvToHtml(fun: tri, csvpath: str, outpath: str) -> None:
    name = fun.id
    csvfile = (csvpath / (name + ".csv")).resolve()
    outfile = (outpath / (name + ".html")).resolve()
    with open(csvfile, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip the first row
        with open(outfile, "w") as outfile:
            for l in Header:
                outfile.write(l)
            outfile.write(f"<title>{name} : IntegerTriangles.py</title>")
            for l in CSS:
                outfile.write(l)
            l = next(reader)
            outfile.write(
                f"<p><b>{name.upper()}</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{l[0]}\n</p>"
            )
            for l in Table:
                outfile.write(l)
            for line in reader:
                if line[0][0] == "#":
                    break
                outfile.write(f"<tr><td><b>{line[1]}</b></td>")
                if line[2] == "nothing":
                    seq = line[3].replace(" ", "+")
                    outfile.write(
                        f"<td><a href='https://oeis.org/?q={seq}&sort=&language=&go=Search' target='_blank'>search </a></td>"
                    )
                else:
                    outfile.write(
                        f"<td><a href='https://oeis.org/{line[2]}'>{line[2]}</a></td>"
                    )
                outfile.write(f"<td>{line[3]}</td></tr>")
            outfile.write(f"</table><p>{line[1]}, {line[2]}, ({line[3]}).</p>")
            for l in Footer:
                outfile.write(l)


def AllCsvToHtml(csvpath, outpath) -> None:
    for fun in tabl_fun:
        CsvToHtml(fun, csvpath, outpath)


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
            if count > 6:
                break
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


def md_table() -> None:
    """Writes a table in markdown style (for readme.md)
    Uses stored data from fun.sim (no searching)

    """
    print("Tables |  Src   | Traits   |  OEIS  SIMILARS |")
    print("| :--- | :---   | :---     |    :---         |")
    for fun in tabl_fun:
        id = fun.id
        similars = fun.sim
        anum = ""
        s = str(similars).replace("[", "").replace("]", "").replace("'", "")
        for sim in similars:
            anum += "%7Cid%3A" + sim
        print(
            f"| [{id}](https://github.com/PeterLuschny/tabl/blob/main/tables.md#{id}) | [src](https://github.com/PeterLuschny/tabl/blob/main/src/{id}.py) | [traits](https://luschny.de/math/oeis/{id}.html) | [{s}](https://oeis.org/search?q={anum}) |\n"
        )


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


def FindSequence(seq: str) -> str:
    """Search for a match in the database.
    Nota bene: The database is assumed to have abs terms!
    Args:
        seq (str): The stringified sequence
    Returns:
        str: The oeis A-number if found, "" otherwise.
    """
    datapath = GetDataPath()
    with open(datapath, "r") as database:
        for data in database:
            if seq in data:
                return data[:6]
    return ""


def GetAnumber(seq: list[int]) -> str:
    """Search for a match in the database.
    Increase the 'offset' twice if not found.
    Args:
        seq (list[int]): The sequence as a list of integers
    Returns:
        str: The oeis A-number if found, "" otherwise
    """
    for n in range(3):
        seqstr = SeqToFixlenString(seq[n:], 100, ",")
        abstr = seqstr.replace("-", "").replace(" ", "")[1:-1]
        anum = FindSequence(abstr)
        if anum != "":
            return anum
    return ""


def flat(t: tabl) -> list[int]:
    """Flatten table to sequence
    Args:
        t (tabl): table
    Returns:
        list[int]: sequence
    """
    if t == [] or t == None:
        return []
    return [i for row in t for i in row]


def Traits(f: tri, dim: int, seqnum: bool = False, csvfile=None) -> None:
    """Generate the traits of a triangle and look them up
    in the database, then write the result in a csv file.
    Args:
        f (tri): Triangle (function)
        dim (int): Length of triangle table to generate
        seqnum (bool, optional): Look up the oeis A-number. Defaults to False.
        csvfile (TextIOWrapper, optional): Open csv file. Defaults to None.
    """
    T = f.tab(dim)
    R = f.rev(dim)
    I = f.inv(dim)
    RI = f.revinv(dim)
    IR = f.invrev(dim)
    # funname = f.id
    funname = f.__name__
    maxlen = (dim * (dim + 1)) // 2
    count_all_traits = count()
    count_traits_with_anum = count()
    no_oeis = []

    def printer(seq: list[int], traitname: str, tria: bool = False) -> None:
        """Writes to the csv file if given or prints otherwise.
        Args:
            seq (list[int]): sequence
            traitname (str): trait
            tria (bool, optional): Is seq a triangle?. Defaults to False.
        """
        next(count_all_traits)
        seqstr = SeqToFixlenString(seq, 70, " ")
        line = ""
        if seqnum:
            # if tria:  # needs function, not tabl
            #    anum = GetSimilarTriangles()
            # else:
            anum = GetAnumber(seq)
            if anum == "":
                sanum = "nothing"
                no_oeis.append(traitname)
            else:
                next(count_traits_with_anum)
                sanum = "A" + str(anum)
            line = f"{funname},{traitname},{sanum},{seqstr}"
            if csvfile != None:
                csvfile.write(line + "\n")
        else:
            line = f"{funname},{traitname},{seqstr}"
            if csvfile != None:
                csvfile.write(line + "\n")
        print(line)

    printer(flat(T), "Triangle ")
    printer(flat(R), "TriRev   ")
    if I != []:
        printer(flat(I), "TriInv   ")
        printer(flat(RI), "TriRevInv")
    if IR != []:
        printer(flat(IR), "TriInvRev")
    printer(flat_acc(T), "TriAcc   ", True)
    printer(flat_revacc(T), "TriRevAcc", True)
    printer(flat_accrev(T), "TriAccRev", True)
    printer(flat(diag_tabl(T)), "TriDiag  ", True)
    printer(flat(poly_tabl(f, dim)), "TriPoly  ", True)
    printer(flat(trans_self(f, dim)), "TriConv  ", True)
    printer(flat(transbin_tabl(f, dim)), "TriBin   ", True)
    printer(flat(invtransbin_tabl(f, dim)), "TriInvBin", True)
    printer(tabl_sum(T), "Sum      ")
    printer(tabl_evensum(T), "EvenSum  ")
    printer(tabl_oddsum(T), "OddSum   ")
    printer(tabl_altsum(T), "AltSum   ")
    printer(tabl_accsum(T), "AccSum   ")
    printer(tabl_accrevsum(T), "AccRevSum")
    printer(tabl_revaccsum(T), "RevAccSum")
    printer(tabl_diagsum(T), "DiagSum  ")
    printer(tabl_lcm(f, dim), "RowLcm   ")
    printer(tabl_gcd(f, dim), "RowGcd   ")
    printer(tabl_max(f, dim), "RowMax   ")
    printer(middle(T), "Middle   ")
    printer(central(T), "Central  ")
    printer(left_side(T), "LeftSide ")
    printer(right_side(T), "RightSide")
    printer(pos_half(T), "PosHalf  ")
    printer(neg_half(T), "NegHalf  ")
    printer(transbin_val(f, maxlen), "Bin      ")
    printer(invtransbin_val(f, maxlen), "InvBin   ")
    printer(trans_sqrs(f, maxlen), "TransSqrs")
    printer(trans_nat0(f, maxlen), "TransNat0")
    printer(trans_nat1(f, maxlen), "TransNat1")
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
    if seqnum:
        atraits = next(count_all_traits)
        ntraits = next(count_traits_with_anum)
        perc = floor(100 * ntraits / atraits)
        w = f"# {f.__name__}, {atraits} traits, {ntraits} A-numbers,{perc}%"
        if csvfile != None:
            csvfile.write(w)
        print(w)
        print(f"Not found in the OEIS: {no_oeis}\n")
