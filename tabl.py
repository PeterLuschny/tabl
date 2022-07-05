from functools import cache
from itertools import accumulate
from sys import setrecursionlimit
from typing import Callable
setrecursionlimit(2000) 
def TablGenerator(g: Callable[[int], list[int]], name: str, id: str):
    def T(n, k=None):
        if n < 0:
            return [g(k) for k in range(-n)]
        if k == None:
            return g(n)
        return g(n)[k]
    T.name = name
    T.id = id
    return T
def isTablGenerator(
    T: Callable[[int, int | None], int | list[int] | list[list[int]]]
    ) -> bool:
    return (
        isinstance(T, Callable)
        and isinstance(T(0), list)
        and isinstance(T(0, None), list)
        and isinstance(T(0, 0), int)
        and isinstance(T(0)[0], int)
        and isinstance(T(-1)[0], list)
        and isinstance(T(-1)[0][0], int)
    )
def poly(T, n, x):
    row = T(n)
    return sum(c * x ** k for (k, c) in enumerate(row))
def row_poly(T, n, len):
    return [poly(T, n, k) for k in range(len)]
def col_poly(T, n, len):
    return [poly(T, k, n) for k in range(len)]
"""
The EvenSum of a list is the sum of the even indexed terms.
py> EvenSum([0, 1, 2, 3, 4, 5])
0 + 2 + 4 = 6
"""
def even_sum(L: list[int]) -> int:
    return sum(L[::2])
"""
The OddSum of a list is the sum of the odd indexed terms.
py> OddSum([0, 1, 2, 3, 4, 5])
1 + 3 + 5 = 9
"""
def odd_sum(L: list[int]) -> int:
    return sum(L[1::2])
"""
The AltSum of a list is the alternating sum.
py> AltSum([0, 1, 2, 3, 4, 5])
+ 0 - 1 + 2 - 3 + 4 - 5 = 6 - 9 = - 3
"""
def alt_sum(L: list[int]) -> int:
    return even_sum(L) - odd_sum(L)
"""
The sum of a triangle is the sequence of the sum of the rows.
"""
def tabl_sum(T: list[list[int]]) -> list[int]:
    return [sum(row) for row in T]
"""
The even sum of a triangle is the sequence of the sum of the even indexed terms of the rows.
"""
def tabl_evensum(T: list[list[int]]) -> list[int]:
    return [even_sum(row) for row in T]
"""
The odd sum of a triangle is the sequence of the sum of the odd indexed terms of the rows.
"""
def tabl_oddsum(T: list[list[int]]) -> list[int]:
    return [odd_sum(row) for row in T]
"""
The alternating sum of a triangle is the sequence of the alternating sum of the rows.
"""
def tabl_altsum(T: list[list[int]]) -> list[int]:
    return [alt_sum(row) for row in T]
"""
Print the various sums of a triangle.
"""
def PrintSums(T: list[list[int]]):
    print(tabl_sum(T))
    print(tabl_evensum(T))
    print(tabl_oddsum(T))
    print(tabl_altsum(T))
def PrintTabl(T, k=None):
    t = T if k == None else T(-k)
    print(t)
def PrintRows(T, k=None):
    t = T if k == None else T(-k)
    for n, row in enumerate(t):
        print([n], row)
def PrintTerms(T, k=None):
    t = T if k == None else T(-k)
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print([n, k], term)
def PrintRowArray(F, rows, cols):
    for j in range(rows):
        print([F(j + k, k) for k in range(cols)])
def PrintColArray(F, rows, cols):
    for j in range(cols):
        print([F(j + k, j) for k in range(rows)])
def PrintRowPolyArray(T, rows, cols):
    for n in range(rows):
        print(row_poly(T, n, cols))
def PrintColPolyArray(T, rows, cols):
    for n in range(rows):
        print(col_poly(T, n, cols))
def PrintViews(T, rows=7, cols=None, verbose=True):
    print("_" * 48)
    print(T.name)
    if cols == None:
        cols = rows
    print()
    Tabl = T(-rows)
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
@cache
def _abe(n: int) -> list[int]:
    if n == 0:
        return [1]
    return [binomial(n - 1, k - 1) * n ** (n - k) 
            if k > 0 else 0 for k in range(0, n + 1)]
abel = TablGenerator(_abe, "Abel", "ABELPO")
@cache
def _bel(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [_bel(n - 1)[n - 1]] + _bel(n - 1)
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row
bell = TablGenerator(_bel, "Bell", "BELLPE")
@cache
def _bes(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = _bes(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = row[k - 1] + (2 * (n - 1) - k) * row[k]
    return row
bessel = TablGenerator(_bes, "Bessel", "BESSEL")
@cache
def _bin(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [1] + _bin(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    return row
binomial = TablGenerator(_bin, "Binomial", "BINOMC")
@cache
def _cat(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = _cat(n - 1) + [_cat(n - 1)[n - 1]]
    return list(accumulate(row))
catalan = TablGenerator(_cat, "Catalan", "CATALA")
@cache
def _cas(n: int) -> list[int]:
    if n == 0:
        return [1]
    r = lambda k: _cas(n - 1)[k] if k >= 0 and k < n else 0
    row = _cas(n - 1) + [1]
    for k in range(0, n):
        row[k] = r(k - 1) + r(k + 1)
    return row
catalan_streched = TablGenerator(_cas, "Catalan streched", "CATSTR")
@cache
def _ccf(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = _ccf(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n + k - 1) * (row[k] + row[k - 1])
    return row
cc_factorial = TablGenerator(_ccf, "Central cycle factorials", "CYCFAC")
@cache
def _csf(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = _csf(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = k ** 2 * row[k] + row[k - 1]
    return row
cs_factorial = TablGenerator(_csf, "Central set factorials", "SETFAC")
@cache
def _del(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    rowA = _del(n - 2)
    row = _del(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + rowA[k - 1]
    return row
delannoy = TablGenerator(_del, "Delannoy", "DELANO")
@cache
def _eul(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = _eul(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * n) // (k)
    row[0] = -sum((-1) ** (j // 2) * row[j] for j in range(n, 0, -2))
    return row
euler = TablGenerator(_eul, "Euler", "EULNUM")
def euler_num(n):
    return _eul(n)[0]
@cache
def _eur(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = _eur(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n - k) * row[k - 1] + (k + 1) * row[k]
    return row
eulerian = TablGenerator(_eur, "Eulerian", "EULIA1")
@cache
def _eu2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = _eu2(n - 1) + [0]
    for k in range(n, 1, -1):
        row[k] = (2 * n - k) * row[k - 1] + k * row[k]
    return row
eulerian2 = TablGenerator(_eu2, "Eulerian2", "EULIA2")
@cache
def _eub(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = _eub(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = (2 * (n - k) + 1) * row[k - 1] + (2 * k - 1) * row[k]
    return row
eulerianB = TablGenerator(_eub, "EulerianB", "EULIAB")
@cache
def _esec(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [binomial(n, k) * _esec(n - k)[0] if k > 0 else 0 
           for k in range(n + 1)]
    if n % 2 == 0:
        row[0] = -sum(row[2::2])
    return row
euler_sec = TablGenerator(_esec, "Euler secant", "EULSEC")
def eulerS(n):
    return 0 if n % 2 == 1 else _esec(n)[0]
@cache
def _etan(n: int) -> list[int]:
    row = [binomial(n, k) * _etan(n - k)[0] if k > 0 else 0 
           for k in range(n + 1)]
    if n % 2 == 1:
        row[0] = -sum(row[2::2]) + 1
    return row
euler_tan = TablGenerator(_etan, "Euler tangent", "EULTAN")
def eulerT(n):
    return 0 if n % 2 == 0 else _etan(n)[0]
@cache
def _ff(n: int) -> list[int]:
    if n == 0: 
        return [1]
    r = _ff(n - 1)
    row = [n * r[k] for k in range(-1, n)]
    row[0] = 1
    return row
falling_factorial = TablGenerator(_ff, "Falling factorial", "FALFAC")
@cache
def _fib(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = _fib(n - 1) + [1]
    s = row[1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1]
    row[0] = s
    return row
fibonacci = TablGenerator(_fib, "Fibonacci", "FIBONA")
@cache
def _fub(n: int) -> list[int]:
    if n == 0:
        return [1]
    r = lambda k: _fub(n - 1)[k] if k <= n - 1 else 0
    row = [0] + _fub(n - 1)
    for k in range(1, n + 1):
        row[k] = k * (r(k - 1) + r(k))
    return row
fubini = TablGenerator(_fub, "Fubini", "FUBINI")
@cache
def _gen(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [0] + _gen(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] += row[k + 1]
    for k in range(2, n + 2):
        row[k] += row[k - 1]
    return row[1:]
genocchi = TablGenerator(_gen, "Genocchi", "GENOCC")
@cache
def _her(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    rowA = _her(n - 1)
    row = _her(n - 1) + [0]
    for k in range(1, n):
        row[k] = rowA[k - 1] + (k + 1) * row[k + 1]
    row[0] = rowA[1]
    row[n] = 1
    return row
hermite = TablGenerator(_her, "Hermite", "HERMIT")
@cache
def _lag(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [0] + _lag(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row
laguerre = TablGenerator(_lag, "Laguerre", "LAGUER")
@cache
def _lah(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = _lah(n - 1) + [1]
    row[0] = 0
    for k in range(n - 1, 0, -1):
        row[k] = row[k] * (n + k - 1) + row[k - 1]
    return row
lah = TablGenerator(_lah, "Lah numbers", "LAHNUM")
@cache
def t(n, k, m):
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return n ** k
    return m * t(n, k - 1, m) + t(n - 1, k, m + 1)
def _lecom(n: int) -> list[int]:
    return [t(k - 1, n - k, n - k) if n != k else 1
        for k in range(n + 1) ]
lehmer = TablGenerator(_lecom, "LehmerComtet", "LEHCOM")
@cache
def _mot(n: int) -> list[int]:
    if n == 0:
        return [1]
    r = lambda k: _mot(n - 1)[k] if k >= 0 and k < n else 0
    row = _mot(n - 1) + [1]
    for k in range(0, n):
        row[k] += r(k - 1) + r(k + 1)
    return row
motzkin = TablGenerator(_mot, "Motzkin", "MOTZKI")
@cache
def _nar(n: int) -> list[int]:
    if n < 3:
        return ([1], [0, 1], [0, 1, 1])[n]
    a = _nar(n - 2) + [0, 0]
    row = _nar(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = (
            (row[k] + row[k - 1]) * (2 * n - 1)
            - (a[k] - 2 * a[k - 1] + a[k - 2]) * (n - 2)
        ) // (n + 1)
    return row
narayana = TablGenerator(_nar, "Narayana", "NARAYA")
@cache
def _osc(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = _osc(n - 1) + [0]
    row[n] = row[n] * n
    for k in range(n, 0, -1):
        row[k] = (n - 1) * row[k] + k * row[k - 1]
    return row
ordered_cycle = TablGenerator(_osc, "Ordered cycles", "ORDCYC")
@cache
def _ord(n: int) -> list[int]:
    if n == 0:
        return [0]
    return _ord(n - 1) + [n]
ordinals = TablGenerator(_ord, "Ordinals", "ORDREP")
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
partnum_exact = TablGenerator(_pn, "Partition numbers (exact)", "PARTEX")
partnum_atmost = TablGenerator(_apn, "Partition numbers (at most)", "PARMOS")
@cache
def _pol(n: int) -> list[int]:
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    arow = _pol(n - 2)
    row = _pol(n - 1) + [n]
    row[n - 1] += row[n - 2]
    for k in range(2, n - 1):
        row[k] += row[k] - arow[k]
    return row
polygonal = TablGenerator(_pol, "Polygonal numbers", "POLYGO")
@cache
def _ren(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = [(n - 1) * (_ren(n - 1)[0] + _ren(n - 2)[0])] + _ren(n - 1)
    for k in range(1, n - 1):
        row[k] = (n * row[k]) // k
    return row
rencontres = TablGenerator(_ren, "Rencontres", "RENCON")
@cache
def _rf(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [0] + _rf(n - 1)
    for k in range(0, n):
        row[k] += (n - k) * row[k + 1]
    return row
rising_factorial = TablGenerator(_rf, "Rising factorial", "RISFAC")
@cache
def _sch(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = _sch(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + row[k + 1]
    return row
schroeder = TablGenerator(_sch, "Schroeder", "SCHROD")
@cache
def _sei(n: int) -> list[int]:
    if n == 0:
        return [1]
    rowA = _sei(n - 1)
    row = [0] + _sei(n - 1)
    row[1] = row[n]
    for k in range(2, n + 1):
        row[k] = row[k - 1] + rowA[n - k]
    return row
def _seibou(n: int) -> list[int]:
    return _sei(n) if n % 2 else _sei(n)[::-1]
seidel = TablGenerator(_sei, "Seidel", "SEIDEL")
seidel_boust = TablGenerator(_seibou, "Seidel boustrophedon", "SEIBOU")
@cache
def _stc(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [0] + _stc(n - 1)
    for k in range(1, n):
        row[k] = row[k] + (n - 1) * row[k + 1]
    return row
stirling_cycle = TablGenerator(_stc, "Stirling cycle", "STICYC")
@cache
def _sts(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [0] + _sts(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row
stirling_set = TablGenerator(_sts, "Stirling set", "STISET")
@cache
def _sym(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = _sym(n - 1) + [1]
    for m in range(n - 1, 0, -1):
        row[m] = (n - m + 1) * row[m] + row[m - 1]
    row[0] *= n
    return row
sympoly = TablGenerator(_sym, "Symmetric polynomials", "SYMPOL")
@cache
def _ttr(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = _ttr(n - 1) + [_ttr(n - 1)[n - 1]]
    return list(accumulate(accumulate(row)))
ternary_tree = TablGenerator(_ttr, "Ternary trees", "TETREE")
@cache
def _uno(n: int) -> list[int]:
    if n == 0:
        return [1]
    return _uno(n - 1) + [1]
uno = TablGenerator(_uno, "Uno", "UNOALL")
@cache
def _war(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    row = _war(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k] + (n + k - 1) * row[k - 1]
    return row
ward = TablGenerator(_war, "Ward", "WARDNU")
@cache
def _wor(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = _wor(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k - 1] + (k + 1) * row[k]
    return row
worpitzky = TablGenerator(_wor, "Worpitzky", "WORPIT")
