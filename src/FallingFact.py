from functools import cache
from _tabltypes import set_attributes

"""Falling factorial, number of permutations of n things k at a time.

[0]  1
[1]  1,  1
[2]  1,  2,  2
[3]  1,  3,  6,   6
[4]  1,  4, 12,  24,   24
[5]  1,  5, 20,  60,  120,  120
[6]  1,  6, 30, 120,  360,  720,  720
"""


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
    ['A008279', 'A068424', 'A094587', 'A173333', 'A181511'],
    False)
def falling_factorial(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _falling_factorial(n).copy()
    return _falling_factorial(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(falling_factorial)

