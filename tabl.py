from functools import cache
from itertools import accumulate
from sys import setrecursionlimit
from typing import Callable, TypeAlias
setrecursionlimit(2000) 
'''table row'''
trow: TypeAlias = list[int]
'''table'''
tabl: TypeAlias = list[list[int]]
'''row generator'''
rgen: TypeAlias = Callable[[int], trow]
'''table generator'''
tgen: TypeAlias = Callable[[int, int | None], int | trow | tabl]
def TablGenerator(g: rgen, name: str, id: str) -> tgen:
    def T(n: int, k: int | None=None) -> int | trow | tabl:
        if n < 0:
            return [g(k) for k in range(-n)]
        if k == None:
            return g(n)
        return g(n)[k] 
    T.name = name
    T.id = id
    return T
def isTablGenerator(T) -> bool:
    return (
        isinstance(T, tgen)
        and isinstance(T(0, 0), int)
        and isinstance(T(0, None), list)
    )
def poly(T, n, x) -> int:
    row: list[int] = T(n)
    return sum(c * x ** k for (k, c) in enumerate(row))
def row_poly(T, n, len) -> list[int]:
    return [poly(T, n, k) for k in range(len)]
def col_poly(T, n, len) -> list[int]:
    return [poly(T, k, n) for k in range(len)]
def even_sum(L: list[int]) -> int:
    return sum(L[::2])
def odd_sum(L: list[int]) -> int:
    return sum(L[1::2])
def alt_sum(L: list[int]) -> int:
    return even_sum(L) - odd_sum(L)
def tabl_sum(T: list[list[int]]) -> list[int]:
    return [sum(row) for row in T]
def tabl_evensum(T: list[list[int]]) -> list[int]:
    return [even_sum(row) for row in T]
def tabl_oddsum(T: list[list[int]]) -> list[int]:
    return [odd_sum(row) for row in T]
def tabl_altsum(T: list[list[int]]) -> list[int]:
    return [alt_sum(row) for row in T]
def PrintSums(T: list[list[int]]) -> None:
    print(tabl_sum(T))
    print(tabl_evensum(T))
    print(tabl_oddsum(T))
    print(tabl_altsum(T))
def PrintTabl(T, k=None) -> None:
    t: list[list[int]] = T if k == None else T(-k)
    print(t)
def PrintRows(T, k=None) -> None:
    t: list[list[int]] = T if k == None else T(-k)
    for n, row in enumerate(t):
        print([n], row)
def PrintTerms(T, k=None) -> None:
    t: list[list[int]] = T if k == None else T(-k)
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print([n, k], term)
def PrintRowArray(F, rows, cols) -> None:
    for j in range(rows):
        print([F(j + k, k) for k in range(cols)])
def PrintColArray(F, rows, cols) -> None:
    for j in range(cols):
        print([F(j + k, j) for k in range(rows)])
def PrintRowPolyArray(T, rows, cols) -> None:
    for n in range(rows):
        print(row_poly(T, n, cols))
def PrintColPolyArray(T, rows, cols) -> None:
    for n in range(rows):
        print(col_poly(T, n, cols))
def PrintViews(T, rows: int=7, cono: int | None=None, verbose=True) -> None:
    print("_" * 48)
    print(T.name)
    cols: int = rows if cono == None else cono
    print()
    Tabl: list[list[int]] = T(-rows)
    if verbose: print("Triangle view")
    PrintRows(Tabl)
    print()
    if verbose: print("Row sums: all, even, odd, alternating")
    PrintSums(Tabl)
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
def Profile(T, hor=10, ver=5) -> dict[str, list[int]]:
    d: dict[str, list[int]] = {}
    tabl: list[list[int]] = T(-hor)
    # Triangle flattened
    d["tabflt"] = tabl[0] + tabl[1] + tabl[2] + tabl[3]
    # Row sums
    d["rowsum"] = tabl_sum(tabl)
    d["evesum"] = tabl_evensum(tabl)
    d["oddsum"] = tabl_oddsum(tabl)
    d["altsum"] = tabl_altsum(tabl)
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
        if j == 1: continue
        d["pocol" + str(j)] = col_poly(T, j, cols)
    return d
def PrintProfile(T) -> None:
    d: dict[str, list[int]] = Profile(T)
    print()
    print(T.id)
    for seq in d.items():
        print(f"{seq[0]}, {seq[1]}")
    print()
@cache
def _abe(n: int) -> list[int]:
    if n == 0:
        return [1]
    return [binomial(n - 1, k - 1) * n ** (n - k) if k > 0 else 0 for k in range(n + 1)]
abel: tgen = TablGenerator(_abe, "Abel", "ABELPO")
@cache
def _bel(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [_bel(n - 1)[n - 1]] + _bel(n - 1)
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row
bell: tgen = TablGenerator(_bel, "Bell", "BELLPE")
@cache
def _bes(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _bes(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = row[k - 1] + (2 * (n - 1) - k) * row[k]
    return row
bessel: tgen = TablGenerator(_bes, "Bessel", "BESSEL")
@cache
def _bin(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [1] + _bin(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    return row
binomial: tgen = TablGenerator(_bin, "Binomial", "BINOMC")
@cache
def _cat(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _cat(n - 1) + [_cat(n - 1)[n - 1]]
    return list(accumulate(row))
catalan: tgen = TablGenerator(_cat, "Catalan", "CATALA")
@cache
def _car(n: int) -> list[int]:
    if n == 0:
        return [1]
    def r(k: int) -> int:
        return _car(n - 1)[k] if k >= 0 and k < n else 0
    row: list[int] = _car(n - 1) + [1]
    for k in range(0, n):
        row[k] = r(k - 1) + r(k + 1)
    return row
catalan_aerated: tgen = TablGenerator(_car, "Catalan aerated", "CATAER")
@cache
def _ccf(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _ccf(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n + k - 1) * (row[k] + row[k - 1])
    return row
cc_factorial: tgen = TablGenerator(_ccf, "Central cycle factorials", "CYCFAC")
@cache
def _csf(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _csf(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = k ** 2 * row[k] + row[k - 1]
    return row
cs_factorial: tgen = TablGenerator(_csf, "Central set factorials", "SETFAC")
@cache
def _del(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    rowA: list[int] = _del(n - 2)
    row: list[int] = _del(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + rowA[k - 1]
    return row
delannoy: tgen = TablGenerator(_del, "Delannoy", "DELANO")
@cache
def _eul(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _eul(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * n) // (k)
    row[0] = -sum((-1) ** (j // 2) * row[j] for j in range(n, 0, -2))
    return row
euler: tgen = TablGenerator(_eul, "Euler", "EULNUM")
def euler_num(n) -> int:
    return _eul(n)[0]
@cache
def _eur(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _eur(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n - k) * row[k - 1] + (k + 1) * row[k]
    return row
eulerian: tgen = TablGenerator(_eur, "Eulerian", "EULIA1")
@cache
def _eu2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _eu2(n - 1) + [0]
    for k in range(n, 1, -1):
        row[k] = (2 * n - k) * row[k - 1] + k * row[k]
    return row
eulerian2: tgen = TablGenerator(_eu2, "Eulerian2", "EULIA2")
@cache
def _eub(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _eub(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = (2 * (n - k) + 1) * row[k - 1] + (2 * k - 1) * row[k]
    return row
eulerianB: tgen = TablGenerator(_eub, "EulerianB", "EULIAB")
@cache
def _esec(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [binomial(n, k) * _esec(n - k)[0] if k > 0 else 0 for k in range(n + 1)]  # type: ignore
    #  p: list[int] = [binomial(n - 1, k - 1) * n ** (n - k) if k > 0 else 0 for k in range(0, n + 1)]
    if n % 2 == 0:
        row[0] = -sum(row[2::2])
    return row
euler_sec: tgen = TablGenerator(_esec, "Euler secant", "EULSEC") # type: ignore 
def eulerS(n) -> int:
    return 0 if n % 2 == 1 else _esec(n)[0]
@cache
def _etan(n: int) -> list[int]:
    row: list[int] = [binomial(n, k) * _etan(n - k)[0] if k > 0 else 0 for k in range(n + 1)]  # type: ignore
    if n % 2 == 1:
        row[0] = -sum(row[2::2]) + 1
    return row
euler_tan: tgen = TablGenerator(_etan, "Euler tangent", "EULTAN")
def eulerT(n) -> int:
    return 0 if n % 2 == 0 else _etan(n)[0]
@cache
def _ff(n: int) -> list[int]:
    if n == 0: 
        return [1]
    r: list[int] = _ff(n - 1)
    row: list[int] = [n * r[k] for k in range(-1, n)]
    row[0] = 1
    return row
falling_factorial: tgen = TablGenerator(_ff, "Falling factorial", "FALFAC")
@cache
def _fib(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _fib(n - 1) + [1]
    s: int = row[1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1]
    row[0] = s
    return row
fibonacci: tgen = TablGenerator(_fib, "Fibonacci", "FIBONA")
@cache
def _fub(n: int) -> list[int]:
    if n == 0:
        return [1]
    def r(k: int) -> int: 
        return _fub(n - 1)[k] if k <= n - 1 else 0
    row: list[int] = [0] + _fub(n - 1)
    for k in range(1, n + 1):
        row[k] = k * (r(k - 1) + r(k))
    return row
fubini: tgen = TablGenerator(_fub, "Fubini", "FUBINI")
@cache
def _gen(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _gen(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] += row[k + 1]
    for k in range(2, n + 2):
        row[k] += row[k - 1]
    return row[1:]
genocchi: tgen = TablGenerator(_gen, "Genocchi", "GENOCC")
@cache
def _her(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    rowA: list[int] = _her(n - 1)
    row: list[int] = _her(n - 1) + [0]
    for k in range(1, n):
        row[k] = rowA[k - 1] + (k + 1) * row[k + 1]
    row[0] = rowA[1]
    row[n] = 1
    return row
hermite: tgen = TablGenerator(_her, "Hermite", "HERMIT")
@cache
def _lag(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _lag(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row
laguerre: tgen = TablGenerator(_lag, "Laguerre", "LAGUER")
@cache
def _lah(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _lah(n - 1) + [1]
    row[0] = 0
    for k in range(n - 1, 0, -1):
        row[k] = row[k] * (n + k - 1) + row[k - 1]
    return row
lah: tgen = TablGenerator(_lah, "Lah numbers", "LAHNUM")
@cache
def t(n: int, k: int, m: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return n ** k
    return m * t(n, k - 1, m) + t(n - 1, k, m + 1)
def _lecom(n: int) -> list[int]:
    return [t(k - 1, n - k, n - k) if n != k else 1
        for k in range(n + 1) ]
lehmer: tgen = TablGenerator(_lecom, "LehmerComtet", "LEHCOM")
@cache
def _mot(n: int) -> list[int]:
    if n == 0:
        return [1]
    def r(k: int) -> int:
        return _mot(n - 1)[k] if k >= 0 and k < n else 0
    row: list[int] = _mot(n - 1) + [1]
    for k in range(0, n):
        row[k] += r(k - 1) + r(k + 1)
    return row
motzkin: tgen = TablGenerator(_mot, "Motzkin", "MOTZKI")
@cache
def _nar(n: int) -> list[int]:
    if n < 3:
        return ([1], [0, 1], [0, 1, 1])[n]
    a: list[int] = _nar(n - 2) + [0, 0]
    row: list[int] = _nar(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = (
            (row[k] + row[k - 1]) * (2 * n - 1)
            - (a[k] - 2 * a[k - 1] + a[k - 2]) * (n - 2)
        ) // (n + 1)
    return row
narayana: tgen = TablGenerator(_nar, "Narayana", "NARAYA")
@cache
def _osc(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _osc(n - 1) + [0]
    row[n] = row[n] * n
    for k in range(n, 0, -1):
        row[k] = (n - 1) * row[k] + k * row[k - 1]
    return row
ordered_cycle: tgen = TablGenerator(_osc, "Ordered cycles", "ORDCYC")
@cache
def _ord(n: int) -> list[int]:
    if n == 0:
        return [0]
    return _ord(n - 1) + [n]
ordinals: tgen = TablGenerator(_ord, "Ordinals", "ORDREP")
@cache
def _p(n: int, k: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return 1 if n == 0 else 0
    return _p(n - 1, k - 1) + _p(n - k, k)
@cache
def _pn(n: int) -> list[int]:
    return [_p(n, k) for k in range(n + 1)]
@cache
def _apn(n: int) -> list[int]:
    return list(accumulate(_pn(n)))
partnum_exact: tgen = TablGenerator(_pn, "Partition numbers (exact)", "PARTEX")
partnum_atmost: tgen = TablGenerator(_apn, "Partition numbers (at most)", "PARMOS")
@cache
def _pol(n: int) -> list[int]:
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    arow: list[int] = _pol(n - 2)
    row: list[int] = _pol(n - 1) + [n]
    row[n - 1] += row[n - 2]
    for k in range(2, n - 1):
        row[k] += row[k] - arow[k]
    return row
polygonal: tgen = TablGenerator(_pol, "Polygonal numbers", "POLYGO")
@cache
def _ren(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = [(n - 1) * (_ren(n - 1)[0] + _ren(n - 2)[0])] + _ren(n - 1)
    for k in range(1, n - 1):
        row[k] = (n * row[k]) // k
    return row
rencontres: tgen = TablGenerator(_ren, "Rencontres", "RENCON")
@cache
def _rf(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _rf(n - 1)
    for k in range(0, n):
        row[k] += (n - k) * row[k + 1]
    return row
rising_factorial: tgen = TablGenerator(_rf, "Rising factorial", "RISFAC")
@cache
def _sch(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _sch(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + row[k + 1]
    return row
schroeder: tgen = TablGenerator(_sch, "Schroeder", "SCHROD")
@cache
def _sei(n: int) -> list[int]:
    if n == 0:
        return [1]
    rowA: list[int] = _sei(n - 1)
    row: list[int] = [0] + _sei(n - 1)
    row[1] = row[n]
    for k in range(2, n + 1):
        row[k] = row[k - 1] + rowA[n - k]
    return row
def _seibou(n: int) -> list[int]:
    return _sei(n) if n % 2 else _sei(n)[::-1]
seidel: tgen = TablGenerator(_sei, "Seidel", "SEIDEL")
seidel_boust: tgen = TablGenerator(_seibou, "Seidel boustrophedon", "SEIBOU")
@cache
def _stc(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _stc(n - 1)
    for k in range(1, n):
        row[k] = row[k] + (n - 1) * row[k + 1]
    return row
stirling_cycle: tgen = TablGenerator(_stc, "Stirling cycle", "STICYC")
@cache
def _sts(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _sts(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row
stirling_set: tgen = TablGenerator(_sts, "Stirling set", "STISET")
@cache
def _sym(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _sym(n - 1) + [1]
    for m in range(n - 1, 0, -1):
        row[m] = (n - m + 1) * row[m] + row[m - 1]
    row[0] *= n
    return row
sympoly: tgen = TablGenerator(_sym, "Symmetric polynomials", "SYMPOL")
@cache
def _ttr(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _ttr(n - 1) + [_ttr(n - 1)[n - 1]]
    return list(accumulate(accumulate(row)))
ternary_tree: tgen = TablGenerator(_ttr, "Ternary trees", "TETREE")
@cache
def _uno(n: int) -> list[int]:
    if n == 0:
        return [1]
    return _uno(n - 1) + [1]
uno: tgen = TablGenerator(_uno, "Uno", "UNOALL")
@cache
def _war(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _war(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k] + (n + k - 1) * row[k - 1]
    return row
ward: tgen = TablGenerator(_war, "Ward", "WARDNU")
@cache
def _wor(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _wor(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k - 1] + (k + 1) * row[k]
    return row
worpitzky: tgen = TablGenerator(_wor, "Worpitzky", "WORPIT")
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
