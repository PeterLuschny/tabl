from functools import cache
from itertools import accumulate
from sys import setrecursionlimit
from typing import Callable, TypeAlias

setrecursionlimit(2100)
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


def set_name(r: rgen, id: str) -> Callable[[tri], tri]:
    def maketab(n: int) -> tabl:
        return [r(j).copy() for j in range(n)]

    def wrapper(f: tri) -> tri:
        f.tab = maketab
        f.id = id
        return f

    return wrapper


def poly(R: tri, n: int, x: int) -> int:
    row: trow = R(n)
    return sum(c * x**k for (k, c) in enumerate(row))


def row_poly(T: tri, n: int, leng: int) -> trow:
    return [poly(T, n, k) for k in range(leng)]


def col_poly(T: tri, n: int, leng: int) -> trow:
    return [poly(T, k, n) for k in range(leng)]


def trans_seq(T: tri, a: seq, lg: int) -> trow:
    return [sum(T(n, k) * a(k) for k in range(n + 1)) for n in range(lg)]


def invtrans_seq(T: tri, a: seq, lg: int) -> trow:
    return [
        sum((-1) ** (n - k) * T(n, k) * a(k) for k in range(n + 1)) for n in range(lg)
    ]


def diag_tabl(t: tabl) -> tabl:
    U: tabl = []
    for n in range(1, len(t)):
        R: trow = []
        for k in range((n + 1) // 2):
            R.append(t[n - k - 1][k])
        U.append(R)
    return U


def cum_tabl(t: tabl) -> tabl:
    U: tabl = []
    for row in t:
        U.append(list(accumulate(row)))
    return U


def rev_tabl(t: tabl) -> tabl:
    U: tabl = []
    for row in t:
        U.append(list(reversed(row)))
    return U


def revcum_tabl(t: tabl) -> tabl:
    return rev_tabl(cum_tabl(t))


def cumrev_tabl(t: tabl) -> tabl:
    return cum_tabl(rev_tabl(t))


def flat_tabl(t: tabl) -> trow:
    return [i for row in t for i in row]


def flat_rev(t: tabl) -> trow:
    return [i for row in rev_tabl(t) for i in row]


def flat_diag(t: tabl) -> trow:
    return [i for row in diag_tabl(t) for i in row]


def flat_cum(t: tabl) -> trow:
    return [i for row in cum_tabl(t) for i in row]


def flat_revcum(t: tabl) -> trow:
    return [i for row in revcum_tabl(t) for i in row]


def flat_cumrev(t: tabl) -> trow:
    return [i for row in cumrev_tabl(t) for i in row]


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


def tabl_cumsum(t: tabl) -> trow:
    cumt: tabl = cum_tabl(t)
    return [sum(row) for row in cumt]


def tabl_revcumsum(t: tabl) -> trow:
    revcumt: tabl = cum_tabl(rev_tabl(t))
    return [sum(row) for row in revcumt]


def PrintTabl(t: tabl) -> None:
    print(t)


def PrintRows(t: tabl) -> None:
    print("| trow  |  list  |")
    print("| :---  |  :---  |")
    for n, row in enumerate(t):
        print(f"| trow{n} | {row} |")


def PrintTerms(t: tabl) -> None:
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print([n, k], term)


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
    print("| sum       |   seq  |")
    print("| :---      |  :---  |")
    print(f"| sum       | {tabl_sum(t)} |")
    print(f"| evensum   | {tabl_evensum(t)} |")
    print(f"| oddsum    | {tabl_oddsum(t)} |")
    print(f"| altsum    | {tabl_altsum(t)} |")
    print(f"| diagsum   | {tabl_diagsum(t)} |")
    print(f"| cumsum    | {tabl_cumsum(t)} |")
    print(f"| revcumsum | {tabl_revcumsum(t)} |")


def PrintFlats(t: tabl) -> None:
    print("| flat      |   seq  |")
    print("| :---      |  :---  |")
    print(f"| tabl     | {flat_tabl(t)} |")
    print(f"| rev      | {flat_rev(t)} |")
    print(f"| cum      | {flat_cum(t)} |")
    print(f"| revcum   | {flat_revcum(t)} |")
    print(f"| cumrev   | {flat_cumrev(t)} |")
    print(f"| diag     | {flat_diag(t)} |")


def PrintViews(
    T: tri, rows: int = 7, cono: int | None = None, verbose: bool = True
) -> None:
    print("# " + T.__name__)
    cols: int = rows if cono is None else cono
    print()
    t: tabl = T.tab(rows)
    if verbose:
        print("Triangle view")
    PrintRows(t)
    print()
    if verbose:
        print("Flattened seqs")
    PrintFlats(t)
    print()
    if verbose:
        print("Row sums")
    PrintSums(t)
    print()
    if verbose:
        print("Diagonals as rows")
    PrintRowArray(T, rows, cols)
    print()
    if verbose:
        print("Diagonals as columns")
    PrintColArray(T, rows, cols)
    print()
    if verbose:
        print("Polynomial values as rows")
    PrintRowPolyArray(T, rows, cols)
    print()
    if verbose:
        print("Polynomial values as columns")
    PrintColPolyArray(T, rows, cols)
    print()


def Profile(T: tri, hor: int = 10, ver: int = 5) -> dict[str, list[int]]:
    d: dict[str, list[int]] = {}
    t: tabl = T.tab(hor)
    # Triangle flattened
    d["tabflt"] = flat_tabl(T.tab(6))
    # Row sums
    d["rowsum"] = tabl_sum(t)
    d["evesum"] = tabl_evensum(t)
    d["oddsum"] = tabl_oddsum(t)
    d["altsum"] = tabl_altsum(t)
    d["cumsum"] = tabl_cumsum(t)
    d["revcum"] = tabl_revcumsum(t)
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


def PrintProfile(T: tri) -> None:
    d: dict[str, list[int]] = Profile(T)
    print()
    print(T.id)
    for seq in d.items():
        print(f"{seq[0]}, {seq[1]}")
    print()


@cache
def _abel(n: int) -> list[int]:
    if n == 0:
        return [1]
    return [binomial(n - 1, k - 1) * n ** (n - k) if k > 0 else 0 for k in range(n + 1)]


@set_name(_abel, "ABELPOLYNOMS")
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


@set_name(_bell, "BELLTRIANGLE")
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


@set_name(_bessel, "BESSELPOLYNO")
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


@set_name(_binomial, "BINOMIALCOEF")
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


@set_name(_catalan, "FUSSCATALAN1")
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


@set_name(_catalan_aerated, "CATALANAERAT")
def catalan_aerated(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _catalan_aerated(n).copy()
    return _catalan_aerated(n)[k]


@cache
def _cc_factorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _cc_factorial(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n + k - 1) * (row[k] + row[k - 1])
    return row


@set_name(_cc_factorial, "CENTRFACTCYC")
def cc_factorial(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _cc_factorial(n).copy()
    return _cc_factorial(n)[k]


@cache
def _cs_factorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _cs_factorial(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = k**2 * row[k] + row[k - 1]
    return row


@set_name(_cs_factorial, "CENTRFACTSET")
def cs_factorial(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _cs_factorial(n).copy()
    return _cs_factorial(n)[k]


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


@set_name(_delannoy, "DELANNOYTRIA")
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


@set_name(_euler, "EULERTRIANGL")
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


@set_name(_eulerian, "EULERIANTRIA")
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


@set_name(_eulerian2, "EULERIANORD2")
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


@set_name(_eulerianB, "EULERIANTYPB")
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


@set_name(_euler_sec, "EULERSECANTO")
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


@set_name(_euler_tan, "EULERTANGENT")
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


@set_name(_falling_factorial, "FALFACTORIAL")
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


@set_name(_fibonacci, "FIBONACPASCA")
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


@set_name(_fubini, "FUBINITRIANG")
def fubini(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _fubini(n).copy()
    return _fubini(n)[k]


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


@set_name(_genocchi, "GENOCCHITRIA")
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


@set_name(_harmonic, "HARMONICPOLY")
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


@set_name(_hermite, "HERMITEPOLYC")
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


@set_name(_laguerre, "LAGUERREPOLY")
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


@set_name(_lah, "LAHTRIANGLES")
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


@set_name(_lehmer, "LEHMERCOMTET")
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


@set_name(_leibniz, "LEIBNIZTRIAN")
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


@set_name(_levin, "LEVINSTRIANG")
def levin(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _levin(n).copy()
    return _levin(n)[k]


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


@set_name(_motzkin, "MOTZKINTRIAN")
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


@set_name(_narayana, "NARAYANATRIA")
def narayana(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _narayana(n).copy()
    return _narayana(n)[k]


@cache
def _ordinals(n: int) -> list[int]:
    if n == 0:
        return [0]
    return _ordinals(n - 1) + [n]


@set_name(_ordinals, "ORDINALNUMBR")
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


@set_name(_ordered_cycle, "ORDEREDCYCLE")
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


@set_name(_partnum_exact, "PARTITIONNUM")
def partnum_exact(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _partnum_exact(n).copy()
    return _partnum_exact(n)[k]


@set_name(_partnum_atmost, "PARTITIONMAX")
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


@set_name(_polygonal, "POLYGONALNUM")
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


@set_name(_powlag, "POWERSLAGUER")
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


@set_name(_rencontres, "RENCONTRESTR")
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


@set_name(_rising_factorial, "RISFACTORIAL")
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


@set_name(_schroeder, "SCHROEDERTRI")
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


@set_name(_bilatpath, "SCHBILATERAL")
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


@set_name(_seidel, "SEIDELTRIANG")
def seidel(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _seidel(n).copy()
    return _seidel(n)[k]


@set_name(_seidel_boust, "SEIDELBOUSTO")
def seidel_boust(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _seidel_boust(n).copy()
    return _seidel_boust(n)[k]


@cache
def _stirling_cycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _stirling_cycle(n - 1)
    for k in range(1, n):
        row[k] = row[k] + (n - 1) * row[k + 1]
    return row


@set_name(_stirling_cycle, "STIRLING1CYC")
def stirling_cycle(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _stirling_cycle(n).copy()
    return _stirling_cycle(n)[k]


@cache
def _stirling_set(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _stirling_set(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row


@set_name(_stirling_set, "STIRLING2SET")
def stirling_set(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _stirling_set(n).copy()
    return _stirling_set(n)[k]


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


@set_name(_stirling_cycle2, "STIRLCYCORD2")
def stirling_cycle2(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _stirling_cycle2(n).copy()
    return _stirling_cycle2(n)[k]


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


@set_name(_stirling_set2, "STIRLSETORD2")
def stirling_set2(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _stirling_set2(n).copy()
    return _stirling_set2(n)[k]


@cache
def _sympoly(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _sympoly(n - 1) + [1]
    for m in range(n - 1, 0, -1):
        row[m] = (n - m + 1) * row[m] + row[m - 1]
    row[0] *= n
    return row


@set_name(_sympoly, "SYMPOLYNOMIA")
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


@set_name(_ternary_tree, "TERNARYTREES")
def ternary_tree(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _ternary_tree(n).copy()
    return _ternary_tree(n)[k]


@cache
def _uno(n: int) -> list[int]:
    if n == 0:
        return [1]
    return _uno(n - 1) + [1]


@set_name(_uno, "UNOPERTUTTIS")
def uno(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _uno(n).copy()
    return _uno(n)[k]


@cache
def _ward_cycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _ward_cycle(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n + k - 1) * (row[k] + row[k - 1])
    return row


@set_name(_ward_cycle, "WARDCYCNUMBR")
def ward_cycle(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _ward_cycle(n).copy()
    return _ward_cycle(n)[k]


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


@set_name(_ward_set, "WARDSETNUMBR")
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


@set_name(_worpitzky, "WORPITZKYNUM")
def worpitzky(n: int, k: int = -1) -> list[int] | int:
    if k == -1:
        return _worpitzky(n).copy()
    return _worpitzky(n)[k]


tabl_fun: list[tgen] = [
    abel,
    bell,
    bessel,
    bilatpath,
    binomial,
    catalan,
    catalan_aerated,
    cc_factorial,
    cs_factorial,
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
    genocchi,
    harmonic,
    hermite,
    laguerre,
    lah,
    lehmer,
    leibniz,
    levin,
    motzkin,
    narayana,
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
    stirling_cycle,
    stirling_set,
    stirling_cycle2,
    stirling_set2,
    sympoly,
    ternary_tree,
    uno,
    ward_cycle,
    ward_set,
    worpitzky,
]
