from functools import cache
from _tabltypes import set_attributes

"""Leibniz's Triangle, FallingFactorial(n + 1, n) / (k! * (n - k)!).
 

[0]  1
[1]  2   2
[2]  3   6    3
[3]  4  12   12    4
[4]  5  20   30   20    5
[5]  6  30   60   60   30    6
[6]  7  42  105  140  105   42    7
[7]  8  56  168  280  280  168   56    8
[8]  9  72  252  504  630  504  252   72   9
[9] 10  90  360  840 1260 1260  840  360  90  10
"""


@cache
def leibniz(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = leibniz(n - 1) + [n + 1]
    row[0] = row[n] = n + 1
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@set_attributes(leibniz, "Leibniz", ["A003506"], False)
def Leibniz(n: int, k: int) -> int:
    return leibniz(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Leibniz)
