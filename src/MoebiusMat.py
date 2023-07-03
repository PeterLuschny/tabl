from functools import cache
from _tabltypes import set_attributes

'''
The Moebius matrix, the indicator function for divisibility.

[ 0]  1
[ 1]  0  1
[ 2]  0  1  1
[ 3]  0  1  0  1
[ 4]  0  1  1  0  1
[ 5]  0  1  0  0  0  1
[ 6]  0  1  1  1  0  0  1
[ 7]  0  1  0  0  0  0  0  1
[ 8]  0  1  1  0  1  0  0  0  1
[ 9]  0  1  0  1  0  0  0  0  0  1
[10]  0  1  1  0  0  1  0  0  0  0  1
'''

@cache
def moebiusmat(n: int) -> list[int]:
    return [1 if k > 0 and n % k == 0 else int(n == 0) 
            for k in range(n + 1)]


@set_attributes(
    moebiusmat,
    "MoebiusMat",
    ['A113704', 'A051731'],
    True)
def MoebiusMat(n: int, k: int) -> int:
    return moebiusmat(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(MoebiusMat)