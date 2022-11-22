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
def tstruct(r: rgen, id: str) -> Callable[[tgen], tgen]:
    def v(n: int, k: int) -> int: 
        return r(n)[k]
    def wrapper(f: tgen) -> tgen:
        f.row = r
        f.val = v
        f.id = id
        return f
    return wrapper
def poly(R: rgen, n: int, x: int) -> int:
    row: trow = R(n)
    return sum(c * x ** k for (k, c) in enumerate(row))
def row_poly(T: tgen, n: int, leng: int) -> trow:
    return [poly(T.row, n, k) for k in range(leng)]
def col_poly(T: tgen, n: int, leng: int) -> trow:
    return [poly(T.row, k, n) for k in range(leng)]
def trans_seq(T: tgen, a: seq, lg: int) -> trow:
    return [sum(T.val(n, k) * a(k) for k in range(n + 1)) for n in range(lg)]
def invtrans_seq(T: tgen, a: seq, lg: int) -> trow:
    return [
        sum((-1) ** (n - k) * T.val(n, k) * a(k) for k in range(n + 1))
        for n in range(lg)
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
        print(f'| trow{n} | {row} |')
def PrintTerms(t: tabl) -> None:
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print([n, k], term)
def PrintRowArray(T: tgen, rows: int, cols: int) -> None:
    print("| rdiag  |   seq  |")
    print("| :---   |  :---  |")
    for j in range(rows):
        print(f'| rdiag{j} | {[T.val(j + k, k) for k in range(cols)]}|')
def PrintColArray(T: tgen, rows: int, cols: int) -> None:
    print("| cdiag  |   seq  |")
    print("| :---   |  :---  |")
    for j in range(cols):
        print(f'| cdiag{j} | {[T.val(j + k, j) for k in range(rows)]} |')
def PrintRowPolyArray(T: tgen, rows: int, cols: int) -> None:
    print("| rpdiag  |   seq  |")
    print("| :---    |  :---  |")
    for n in range(rows):
        print(f'| rpdiag{n} | {row_poly(T, n, cols)} |')
def PrintColPolyArray(T: tgen, rows: int, cols: int) -> None:
    print("| cpdiag  |   seq  |")
    print("| :---    |  :---  |")
    for n in range(rows):
        print(f'| cpdiag{n} | {col_poly(T, n, cols)} |')
def PrintSums(t: tabl) -> None:
    print("| sum       |   seq  |")
    print("| :---      |  :---  |")
    print(f'| sum       | {tabl_sum(t)} |')
    print(f'| evensum   | {tabl_evensum(t)} |')
    print(f'| oddsum    | {tabl_oddsum(t)} |')
    print(f'| altsum    | {tabl_altsum(t)} |')
    print(f'| diagsum   | {tabl_diagsum(t)} |')
    print(f'| cumsum    | {tabl_cumsum(t)} |')
    print(f'| revcumsum | {tabl_revcumsum(t)} |')
def PrintFlats(t: tabl) -> None:
    print("| flat      |   seq  |")
    print("| :---      |  :---  |")
    print(f'| tabl     | {flat_tabl(t)} |')
    print(f'| rev      | {flat_rev(t)} |')
    print(f'| cum      | {flat_cum(t)} |')
    print(f'| revcum   | {flat_revcum(t)} |')
    print(f'| cumrev   | {flat_cumrev(t)} |')
    print(f'| diag     | {flat_diag(t)} |')
def PrintViews(T: tgen, rows: int = 7, cono: int | None = None, 
    verbose: bool = True) -> None:
    print("# " + T.__name__)
    cols: int = rows if cono is None else cono
    print()
    t: tabl = T(rows)
    if verbose: print("Triangle view")
    PrintRows(t)
    print()
    if verbose: print("Flattened seqs")
    PrintFlats(t)
    print()
    if verbose: print("Row sums")
    PrintSums(t)
    print()
    if verbose: print("Diagonals as rows")
    PrintRowArray(T, rows, cols)
    print()
    if verbose: print("Diagonals as columns")
    PrintColArray(T, rows, cols)
    print()
    if verbose: print("Polynomial values as rows")
    PrintRowPolyArray(T, rows, cols)
    print()
    if verbose: print("Polynomial values as columns")
    PrintColPolyArray(T, rows, cols)
    print()
def Profile(T: tgen, hor: int = 10, ver: int = 5) -> dict[str, list[int]]:
    d: dict[str, list[int]] = {}
    t: tabl = T(hor)  
    # Triangle flattened
    d["tabflt"] = flat_tabl(T(6))
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
        d["dirow" + str(j)] = [T.val(j + k, k) for k in range(cols)]  
    # DiagsAsColArray
    rows: int = hor
    cols: int = ver
    for j in range(cols):
        d["dicol" + str(j)] = [T.val(j + k, j) for k in range(rows)]  
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
def PrintProfile(T: tgen) -> None:
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
    return [binomial.val(n - 1, k - 1) * n ** (n - k) 
           if k > 0 else 0 for k in range(n + 1)]
@tstruct(_abel, "ABELPOLYNOMS")
def abel(size: int) -> tabl: 
    return [_abel(j) for j in range(size)]
@cache
def _bell(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [_bell(n - 1)[n - 1]] + _bell(n - 1)
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row
@tstruct(_bell, "BELLTRIANGLE")
def bell(size: int) -> tabl: 
    return [_bell(j) for j in range(size)]
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
@tstruct(_bessel, "BESSELPOLYNO")
def bessel(size: int) -> tabl: 
    return [_bessel(j) for j in range(size)]
@cache
def _binomial(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [1] + _binomial(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    return row
@tstruct(_binomial, "BINOMIALCOEF")
def binomial(size: int) -> tabl:
    return [_binomial(j) for j in range(size)]
@cache
def _catalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _catalan(n - 1) + [_catalan(n - 1)[n - 1]]
    return list(accumulate(row))
@tstruct(_catalan, "FUSSCATALAN1")
def catalan(size: int) -> tabl: 
    return [_catalan(j) for j in range(size)]
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
@tstruct(_catalan_aerated, "CATALANAERAT")
def catalan_aerated(size: int) -> tabl: 
    return [_catalan_aerated(j) for j in range(size)]
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
@tstruct(_cc_factorial, "CENTRFACTCYC")
def cc_factorial(size: int) -> tabl: 
    return [_cc_factorial(j) for j in range(size)]
@cache
def _cs_factorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _cs_factorial(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = k ** 2 * row[k] + row[k - 1]
    return row
@tstruct(_cs_factorial, "CENTRFACTSET")
def cs_factorial(size: int) -> tabl: 
    return [_cs_factorial(j) for j in range(size)]
@cache
def _delannoy(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    rowA: list[int] = _delannoy(n - 2)
    row: list[int] = _delannoy(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + rowA[k - 1]
    return row
@tstruct(_delannoy, "DELANNOYTRIA")
def delannoy(size: int) -> tabl: 
    return [_delannoy(j) for j in range(size)]
@cache
def _euler(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _euler(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * n) // (k)
    row[0] = -sum((-1) ** (j // 2) * row[j] for j in range(n, 0, -2))
    return row
@tstruct(_euler, "EULERTRIANGL")
def euler(size: int) -> tabl: 
    return [_euler(j) for j in range(size)]
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
@tstruct(_eulerian, "EULERIANTRIA")
def eulerian(size: int) -> tabl: 
    return [_eulerian(j) for j in range(size)]
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
@tstruct(_eulerian2, "EULERIANORD2")
def eulerian2(size: int) -> tabl: 
    return [_eulerian2(j) for j in range(size)]
@cache
def _eulerianB(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _eulerianB(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = (2 * (n - k) + 1) * row[k - 1] + (2 * k + 1) * row[k]
    return row
@tstruct(_eulerianB, "EULERIANTYPB")
def eulerianB(size: int) -> tabl: 
    return [_eulerianB(j) for j in range(size)]
@cache
def _euler_sec(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [binomial.val(n, k) * _euler_sec(n - k)[0] if k > 0 else 0 for k in range(n + 1)]  
    if n % 2 == 0:
        row[0] = -sum(row[2::2])
    return row
@tstruct(_euler_sec, "EULERSECANTO")
def euler_sec(size: int) -> tabl: 
    return [_euler_sec(j) for j in range(size)]
def eulerS(n: int) -> int:
    return 0 if n % 2 == 1 else _euler_sec(n)[0]
@cache
def _euler_tan(n: int) -> list[int]:
    row: list[int] = [binomial.val(n, k) * _euler_tan(n - k)[0] if k > 0 else 0 for k in range(n + 1)]  
    if n % 2 == 1:
        row[0] = -sum(row[2::2]) + 1
    return row
@tstruct(_euler_tan, "EULERTANGENT")
def euler_tan(size: int) -> tabl: 
    return [_euler_tan(j) for j in range(size)]
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
@tstruct(_falling_factorial, "FALFACTORIAL")
def falling_factorial(size: int) -> tabl: 
    return [_falling_factorial(j) for j in range(size)]
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
@tstruct(_fibonacci, "FIBONACPASCA")
def fibonacci(size: int) -> tabl: 
    return [_fibonacci(j) for j in range(size)]
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
@tstruct(_fubini, "FUBINITRIANG")
def fubini(size: int) -> tabl: 
    return [_fubini(j) for j in range(size)]
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
@tstruct(_genocchi, "GENOCCHITRIA")
def genocchi(size: int) -> tabl: 
    return [_genocchi(j) for j in range(size)]
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
@tstruct(_hermite, "HERMITEPOLYC")
def hermite(size: int) -> tabl: 
    return [_hermite(j) for j in range(size)]
@cache
def _laguerre(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _laguerre(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row
@tstruct(_laguerre, "LAGUERREPOLY")
def laguerre(size: int) -> tabl: 
    return [_laguerre(j) for j in range(size)]
@cache
def _lah(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _lah(n - 1) + [1]
    row[0] = 0
    for k in range(n - 1, 0, -1):
        row[k] = row[k] * (n + k - 1) + row[k - 1]
    return row
@tstruct(_lah, "LAHTRIANGLES")
def lah(size: int) -> tabl: 
    return [_lah(j) for j in range(size)]
@cache
def t(n: int, k: int, m: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return n ** k
    return m * t(n, k - 1, m) + t(n - 1, k, m + 1)
@cache
def _lehmer(n: int) -> list[int]:
    return [t(k - 1, n - k, n - k) if n != k else 1
           for k in range(n + 1)]
@tstruct(_lehmer, "LEHMERCOMTET")
def lehmer(size: int) -> tabl: 
    return [_lehmer(j) for j in range(size)]
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
@tstruct(_motzkin, "MOTZKINTRIAN")
def motzkin(size: int) -> tabl: 
    return [_motzkin(j) for j in range(size)]
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
@tstruct(_narayana, "NARAYANATRIA")
def narayana(size: int) -> tabl: 
    return [_narayana(j) for j in range(size)]
@cache
def _ordinals(n: int) -> list[int]:
    if n == 0:
        return [0]
    return _ordinals(n - 1) + [n]
@tstruct(_ordinals, "ORDINALNUMBR")
def ordinals(size: int) -> tabl: 
    return [_ordinals(j) for j in range(size)]
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
@tstruct(_ordered_cycle, "ORDEREDCYCLE")
def ordered_cycle(size: int) -> tabl: 
    return [_ordered_cycle(j) for j in range(size)]
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
@tstruct(_partnum_exact, "PARTITIONNUM")
def partnum_exact(size: int) -> tabl: 
    return [_partnum_exact(j) for j in range(size)]
@tstruct(_partnum_atmost, "PARTITIONMAX")
def partnum_atmost(size: int) -> tabl: 
    return [_partnum_atmost(j) for j in range(size)]
@cache
def _polygonal(n: int) -> list[int]:
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    arow: list[int] = _polygonal(n - 2)
    row: list[int] = _polygonal(n - 1) + [n]
    row[n - 1] += row[n - 2]
    for k in range(2, n - 1):
        row[k] += row[k] - arow[k]
    return row
@tstruct(_polygonal, "POLYGONALNUM")
def polygonal(size: int) -> tabl: 
    return [_polygonal(j) for j in range(size)]
@cache
def _rencontres(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = [(n - 1) * (_rencontres(n - 1)[0] + _rencontres(n - 2)[0])] + _rencontres(n - 1)
    for k in range(1, n - 1):
        row[k] = (n * row[k]) // k
    return row
@tstruct(_rencontres, "RENCONTRESTR")
def rencontres(size: int) -> tabl: 
    return [_rencontres(j) for j in range(size)]
@cache
def _rising_factorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _rising_factorial(n - 1)
    for k in range(0, n):
        row[k] += (n - k) * row[k + 1]
    return row
@tstruct(_rising_factorial, "RISFACTORIAL")
def rising_factorial(size: int) -> tabl: 
    return [_rising_factorial(j) for j in range(size)]
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
@tstruct(_schroeder, "SCHROEDERTRI")
def schroeder(size: int) -> tabl: 
    return [_schroeder(j) for j in range(size)]
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
@tstruct(_seidel, "SEIDELTRIANG")
def seidel(size: int) -> tabl: 
    return [_seidel(j) for j in range(size)]
@tstruct(_seidel_boust, "SEIDELBOUSTO")
def seidel_boust(size: int) -> tabl: 
    return [_seidel_boust(j) for j in range(size)]
@cache
def _stirling_cycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _stirling_cycle(n - 1)
    for k in range(1, n):
        row[k] = row[k] + (n - 1) * row[k + 1]
    return row
@tstruct(_stirling_cycle, "STIRLINGCYC1")
def stirling_cycle(size: int) -> tabl: 
    return [_stirling_cycle(j) for j in range(size)]
@cache
def _stirling_set(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _stirling_set(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row
@tstruct(_stirling_set, "STIRLINGSET2")
def stirling_set(size: int) -> tabl: 
    return [_stirling_set(j) for j in range(size)]
@cache
def _sympoly(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _sympoly(n - 1) + [1]
    for m in range(n - 1, 0, -1):
        row[m] = (n - m + 1) * row[m] + row[m - 1]
    row[0] *= n
    return row
@tstruct(_sympoly, "SYMPOLYNOMIA")
def sympoly(size: int) -> tabl: 
    return [_sympoly(j) for j in range(size)]
@cache
def _ternary_tree(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _ternary_tree(n - 1) + [_ternary_tree(n - 1)[n - 1]]
    return list(accumulate(accumulate(row)))
@tstruct(_ternary_tree, "TERNARYTREES")
def ternary_tree(size: int) -> tabl: 
    return [_ternary_tree(j) for j in range(size)]
@cache
def _uno(n: int) -> list[int]:
    if n == 0:
        return [1]
    return _uno(n - 1) + [1]
@tstruct(_uno, "UNOPERTUTTIS")
def uno(size: int) -> tabl: 
    return [_uno(j) for j in range(size)]
@cache
def _ward(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _ward(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k] + (n + k - 1) * row[k - 1]
    return row
@tstruct(_ward, "WARDNUMBEROS")
def ward(size: int) -> tabl: 
    return [_ward(j) for j in range(size)]
@cache
def _worpitzky(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _worpitzky(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k - 1] + (k + 1) * row[k]
    return row
@tstruct(_worpitzky, "WORPITZKYNUM")
def worpitzky(size: int) -> tabl: 
    return [_worpitzky(j) for j in range(size)]
tabl_fun: list[tgen] = [
    abel,
    bell,
    bessel,
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
    hermite,
    laguerre,
    lah,
    lehmer,
    motzkin,
    narayana,
    ordinals,
    ordered_cycle,
    partnum_exact,
    partnum_atmost,
    polygonal,
    rencontres,
    rising_factorial,
    schroeder,
    seidel,
    seidel_boust,
    stirling_cycle,
    stirling_set,
    sympoly,
    ternary_tree,
    uno,
    ward,
    worpitzky,
]
