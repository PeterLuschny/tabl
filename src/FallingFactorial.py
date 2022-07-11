from functools import cache
from tabltypes import tabl, tvals

"""Number of permutations of n things k at a time, A008279. 

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


@tvals(_falling_factorial, "FALFAC")
def falling_factorial(size: int) -> tabl: 
    return [_falling_factorial(j) for j in range(size)]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(falling_factorial)

