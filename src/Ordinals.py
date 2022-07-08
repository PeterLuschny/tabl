from functools import cache
from tabltypes import *

"""von Neumann ordinals (kind of), A002262.

[0] [0]
[1] [0,  1]
[2] [0,  1,  2]
[3] [0,  1,  2,  3]
[4] [0,  1,  2,  3,  4]
[5] [0,  1,  2,  3,  4,  5]
[6] [0,  1,  2,  3,  4,  5,  6]
[7] [0,  1,  2,  3,  4,  5,  6,  7]
"""


@cache
def _ordinals(n: int) -> list[int]:
    if n == 0:
        return [0]

    return _ordinals(n - 1) + [n]


ordinals: tgen = TablGenerator(_ordinals, "Ordinals", "ORDREP")


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(ordinals)