from _tabltypes import set_attributes
from Seidel import seidel


"""Seidel boustrophedon:

[0] [ 1]
[1] [ 0,  1]
[2] [ 1,  1,   0]
[3] [ 0,  1,   2,   2]
[4] [ 5,  5,   4,   2,   0]
[5] [ 0,  5,  10,  14,  16,  16]
[6] [61, 61,  56,  46,  32,  16,   0]
[7] [ 0, 61, 122, 178, 224, 256, 272, 272]
"""

# #@

def seidelboust(n: int) -> list[int]:
    return seidel(n) if n % 2 else seidel(n)[::-1]


@set_attributes(
    seidelboust, 
    "SeidelBoust", 
    ['A008280', 'A108040', 'A236935', 'A239005'], 
    False)
def SeidelBoust(n: int, k: int) -> int: 
    return seidelboust(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(SeidelBoust)
