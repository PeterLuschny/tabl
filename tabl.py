from functools import cache
from itertools import accumulate
from cachetools import cached, LRUCache
from sys import setrecursionlimit
setrecursionlimit(2000) 
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
def PrintViews(T, rows=7, cols=None, verbose=True):
    if cols == None: cols = rows
    print()
    if verbose: print("Triangle view")
    PrintRows(T(-rows))
    print()
    if verbose: print("Diagonals -> rows")
    PrintRowArray(T, rows, cols)
    print()
    if verbose: print("Diagonals -> columns")
    PrintColArray(T, rows, cols)
    print()
from typing import Callable
def TablGenerator(g: Callable[[int], list[int]]):
    def T(n, k=None):
        if n < 0:
            return [g(k) for k in range(-n)]
        if k == None:
            return g(n)
        return g(n)[k]
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
@cache
def _abe(n: int) -> list[int]:
    if n == 0:
        return [1]
    return [binomial(n - 1, k - 1) * n ** (n - k) 
            if k > 0 else 0 for k in range(0, n + 1)]
abel = TablGenerator(_abe)
@cache
def _bel(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [_bel(n - 1)[n - 1]] + _bel(n - 1)
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row
bell = TablGenerator(_bel)
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
bessel = TablGenerator(_bes)
@cache
def _bin(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [1] + _bin(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    return row
binomial = TablGenerator(_bin)
@cache
def _cat(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = _cat(n - 1) + [0]
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row
catalan = TablGenerator(_cat)
@cache
def _cas(n: int) -> list[int]:
    if n == 0:
        return [1]
    r = lambda k: _cas(n - 1)[k] if k >= 0 and k < n else 0
    row = _cas(n - 1) + [1]
    for k in range(0, n):
        row[k] = r(k - 1) + r(k + 1)
    return row
catalan_streched = TablGenerator(_cas)
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
cc_factorial = TablGenerator(_ccf)
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
cs_factorial = TablGenerator(_csf)
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
delannoy = TablGenerator(_del)
@cache
def _eul(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = _eul(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * n) // (k)
    row[0] = -sum((-1) ** (j // 2) * row[j] for j in range(n, 0, -2))
    return row
euler = TablGenerator(_eul)
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
eulerian = TablGenerator(_eur)
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
eulerian2 = TablGenerator(_eu2)
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
eulerianB = TablGenerator(_eub)
@cache
def _esec(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [binomial(n, k) * _esec(n - k)[0] if k > 0 else 0 
           for k in range(n + 1)]
    if n % 2 == 0:
        row[0] = -sum(row[2::2])
    return row
euler_sec = TablGenerator(_esec)
def eulerS(n):
    return 0 if n % 2 == 1 else _esec(n)[0]
@cache
def _etan(n: int) -> list[int]:
    row = [binomial(n, k) * _etan(n - k)[0] if k > 0 else 0 
           for k in range(n + 1)]
    if n % 2 == 1:
        row[0] = -sum(row[2::2]) + 1
    return row
euler_tan = TablGenerator(_etan)
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
falling_factorial = TablGenerator(_ff)
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
fibonacci = TablGenerator(_fib)
@cache
def _fub(n: int) -> list[int]:
    if n == 0:
        return [1]
    r = lambda k: _fub(n - 1)[k] if k <= n - 1 else 0
    row = [0] + _fub(n - 1)
    for k in range(1, n + 1):
        row[k] = k * (r(k - 1) + r(k))
    return row
fubini = TablGenerator(_fub)
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
genocchi = TablGenerator(_gen)
@cache
def _lag(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [0] + _lag(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row
laguerre = TablGenerator(_lag)
@cache
def _lah(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = _lah(n - 1) + [1]
    row[0] = 0
    for k in range(n - 1, 0, -1):
        row[k] = row[k] * (n + k - 1) + row[k - 1]
    return row
lah = TablGenerator(_lah)
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
lehmer = TablGenerator(_lecom)
@cache
def _mot(n: int) -> list[int]:
    if n == 0:
        return [1]
    r = lambda k: _mot(n - 1)[k] if k >= 0 and k < n else 0
    row = _mot(n - 1) + [1]
    for k in range(0, n):
        row[k] += r(k - 1) + r(k + 1)
    return row
motzkin = TablGenerator(_mot)
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
narayana = TablGenerator(_nar)
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
ordered_cycle = TablGenerator(_osc)
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
partnum_exact = TablGenerator(_pn)
partnum_atmost = TablGenerator(_apn)
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
rencontres = TablGenerator(_ren)
@cache
def _rf(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [0] + _rf(n - 1)
    for k in range(0, n):
        row[k] += (n - k) * row[k + 1]
    return row
rising_factorial = TablGenerator(_rf)
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
schroeder = TablGenerator(_sch)
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
seidel = TablGenerator(_sei)
seidel_boust = TablGenerator(_seibou)
@cache
def _stc(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [0] + _stc(n - 1)
    for k in range(1, n):
        row[k] = row[k] + (n - 1) * row[k + 1]
    return row
stirling_cycle = TablGenerator(_stc)
@cache
def _sts(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = [0] + _sts(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row
stirling_set = TablGenerator(_sts)
@cache
def _ttr(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = _ttr(n - 1) + [1]
    z = 3 * n * (3 * n - 1) * (3 * n - 2)
    for k in range(n):
        u = (n - k) * (k + 2 * n) * (k + 2 * n + 1)
        row[k] = (row[k] * z) // u
    return row
ternary_tree = TablGenerator(_ttr)
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
ward = TablGenerator(_war)
@cache
def _wor(n: int) -> list[int]:
    if n == 0:
        return [1]
    row = _wor(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k - 1] + (k + 1) * row[k]
    return row
worpitzky = TablGenerator(_wor)
