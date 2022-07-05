from functools import cache
from tabltools import TablGenerator

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
def _ff(n: int) -> list[int]:
    if n == 0: 
        return [1]

    r = _ff(n - 1)
    row = [n * r[k] for k in range(-1, n)]
    row[0] = 1
    return row

falling_factorial = TablGenerator(_ff, "Falling factorial", "FALFAC")


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(falling_factorial)
