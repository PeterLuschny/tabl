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
def _abel(n: int) -> list[int]:
    if n == 0:
        return [1]
    return [binomial(n - 1, k - 1) * n ** (n - k) if k > 0 else 0 for k in range(n + 1)]
abel: tgen = TablGenerator(_abel, "Abel", "ABELPO")
@cache
def _bell(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [_bell(n - 1)[n - 1]] + _bell(n - 1)
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row
bell: tgen = TablGenerator(_bell, "Bell", "BELLPE")
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
bessel: tgen = TablGenerator(_bessel, "Bessel", "BESSEL")
@cache
def _binomial(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [1] + _binomial(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    return row
binomial: tgen = TablGenerator(_binomial, "Binomial", "BINOMC")
@cache
def _catalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _catalan(n - 1) + [_catalan(n - 1)[n - 1]]
    return list(accumulate(row))
catalan: tgen = TablGenerator(_catalan, "Catalan", "CATALA")
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
catalan_aerated: tgen = TablGenerator(_catalan_aerated, "Catalan aerated", "CATAER")
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
cc_factorial: tgen = TablGenerator(_cc_factorial, "Central cycle factorials", "CYCFAC")
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
cs_factorial: tgen = TablGenerator(_cs_factorial, "Central set factorials", "SETFAC")
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
delannoy: tgen = TablGenerator(_delannoy, "Delannoy", "DELANO")
@cache
def _euler(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _euler(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * n) // (k)
    row[0] = -sum((-1) ** (j // 2) * row[j] for j in range(n, 0, -2))
    return row
euler: tgen = TablGenerator(_euler, "Euler", "EULNUM")
def euler_num(n) -> int:
    return _euler(n)[0]
@cache
def _eulerian(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _eulerian(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n - k) * row[k - 1] + (k + 1) * row[k]
    return row
eulerian: tgen = TablGenerator(_eulerian, "Eulerian", "EULIA1")
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
eulerian2: tgen = TablGenerator(_eulerian2, "Eulerian2", "EULIA2")
@cache
def _eulerianB(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _eulerianB(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = (2 * (n - k) + 1) * row[k - 1] + (2 * k - 1) * row[k]
    return row
eulerianB: tgen = TablGenerator(_eulerianB, "EulerianB", "EULIAB")
@cache
def _euler_sec(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [binomial(n, k) * _euler_sec(n - k)[0] if k > 0 else 0 for k in range(n + 1)]  # type: ignore
    if n % 2 == 0:
        row[0] = -sum(row[2::2])
    return row
euler_sec: tgen = TablGenerator(_euler_sec, "Euler secant", "EULSEC") 
def eulerS(n) -> int:
    return 0 if n % 2 == 1 else _euler_sec(n)[0]
@cache
def _euler_tan(n: int) -> list[int]:
    row: list[int] = [binomial(n, k) * _euler_tan(n - k)[0] if k > 0 else 0 for k in range(n + 1)]  # type: ignore
    if n % 2 == 1:
        row[0] = -sum(row[2::2]) + 1
    return row
euler_tan: tgen = TablGenerator(_euler_tan, "Euler tangent", "EULTAN")
def eulerT(n) -> int:
    return 0 if n % 2 == 0 else _euler_tan(n)[0]
@cache
def _falling_factorial(n: int) -> list[int]:
    if n == 0: 
        return [1]
    r: list[int] = _falling_factorial(n - 1)
    row: list[int] = [n * r[k] for k in range(-1, n)]
    row[0] = 1
    return row
falling_factorial: tgen = TablGenerator(_falling_factorial, "Falling factorial", "FALFAC")
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
fibonacci: tgen = TablGenerator(_fibonacci, "Fibonacci", "FIBONA")
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
fubini: tgen = TablGenerator(_fubini, "Fubini", "FUBINI")
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
genocchi: tgen = TablGenerator(_genocchi, "Genocchi", "GENOCC")
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
hermite: tgen = TablGenerator(_hermite, "Hermite", "HERMIT")
@cache
def _laguerre(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _laguerre(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row
laguerre: tgen = TablGenerator(_laguerre, "Laguerre", "LAGUER")
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
def _lehmer(n: int) -> list[int]:
    return [t(k - 1, n - k, n - k) if n != k else 1
        for k in range(n + 1) ]
lehmer: tgen = TablGenerator(_lehmer, "LehmerComtet", "LEHCOM")
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
motzkin: tgen = TablGenerator(_motzkin, "Motzkin", "MOTZKI")
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
narayana: tgen = TablGenerator(_narayana, "Narayana", "NARAYA")
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
ordered_cycle: tgen = TablGenerator(_ordered_cycle, "Ordered cycles", "ORDCYC")
@cache
def _ordinals(n: int) -> list[int]:
    if n == 0:
        return [0]
    return _ordinals(n - 1) + [n]
ordinals: tgen = TablGenerator(_ordinals, "Ordinals", "ORDREP")
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
partnum_exact: tgen = TablGenerator(_partnum_exact, "Partition numbers (exact)", "PARTEX")
partnum_atmost: tgen = TablGenerator(_partnum_atmost, "Partition numbers (at most)", "PARMOS")
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
polygonal: tgen = TablGenerator(_polygonal, "Polygonal numbers", "POLYGO")
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
rencontres: tgen = TablGenerator(_rencontres, "Rencontres", "RENCON")
@cache
def _rising_factorial(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _rising_factorial(n - 1)
    for k in range(0, n):
        row[k] += (n - k) * row[k + 1]
    return row
rising_factorial: tgen = TablGenerator(_rising_factorial, "Rising factorial", "RISFAC")
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
schroeder: tgen = TablGenerator(_schroeder, "Schroeder", "SCHROD")
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
seidel: tgen = TablGenerator(_seidel, "Seidel", "SEIDEL")
seidel_boust: tgen = TablGenerator(_seidel_boust, "Seidel boustrophedon", "SEIBOU")
@cache
def _stirling_cycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _stirling_cycle(n - 1)
    for k in range(1, n):
        row[k] = row[k] + (n - 1) * row[k + 1]
    return row
stirling_cycle: tgen = TablGenerator(_stirling_cycle, "Stirling cycle", "STICYC")
@cache
def _stirling_set(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = [0] + _stirling_set(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row
stirling_set: tgen = TablGenerator(_stirling_set, "Stirling set", "STISET")
@cache
def _sympoly(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _sympoly(n - 1) + [1]
    for m in range(n - 1, 0, -1):
        row[m] = (n - m + 1) * row[m] + row[m - 1]
    row[0] *= n
    return row
sympoly: tgen = TablGenerator(_sympoly, "Symmetric polynomials", "SYMPOL")
@cache
def _ternary_tree(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row: list[int] = _ternary_tree(n - 1) + [_ternary_tree(n - 1)[n - 1]]
    return list(accumulate(accumulate(row)))
ternary_tree: tgen = TablGenerator(_ternary_tree, "Ternary trees", "TETREE")
@cache
def _uno(n: int) -> list[int]:
    if n == 0:
        return [1]
    return _uno(n - 1) + [1]
uno: tgen = TablGenerator(_uno, "Uno", "UNOALL")
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
ward: tgen = TablGenerator(_ward, "Ward", "WARDNU")
@cache
def _worpitzky(n: int) -> list[int]:
    if n == 0:
        return [1]
    row: list[int] = _worpitzky(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k - 1] + (k + 1) * row[k]
    return row
worpitzky: tgen = TablGenerator(_worpitzky, "Worpitzky", "WORPIT")
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
