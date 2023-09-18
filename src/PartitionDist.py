from functools import cache
from _tabltypes import set_attributes

"""Partitions of n having exactly k distinct parts, A365676.

[0] 1;
[1] 0, 1;
[2] 0, 2,  0;
[3] 0, 2,  1,  0;
[4] 0, 3,  2,  0, 0;
[5] 0, 2,  5,  0, 0, 0;
[6] 0, 4,  6,  1, 0, 0, 0;
[7] 0, 2, 11,  2, 0, 0, 0, 0;
[8] 0, 4, 13,  5, 0, 0, 0, 0, 0;
[9] 0, 3, 17, 10, 0, 0, 0, 0, 0, 0;
"""


@cache
def _pdist(n: int, k: int, r: int) -> int:
    if n == 0: return 1 if k == 0 else 0
    if k == 0 or r == 0: return 0
    return sum(_pdist(n - r * j, k - 1, r - 1) 
               for j in range(1, n // r + 1)) + _pdist(n, k, r - 1)

@cache
def partnumdist(n) -> list[int]:  
    return [_pdist(n, k, n) for k in range(n + 1)]


@set_attributes(
    partnumdist, 
    "PartitionDist", 
    ['A365676', 'A116608', 'A060177'], 
    False)
def PartnumDist(n: int, k: int) -> int: 
    return partnumdist(n)[k]


if __name__ == "__main__":
    # TablTest has to big test cases
    from _tablviews import PrintViews
    PrintViews(PartnumDist, 10)
