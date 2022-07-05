from functools import cache
from tabltools import TablGenerator

"""Row k gives the (n-1)-st elementary symmetric polynomial of [k, k+1, k+2,..., k+n], A165675.

[0]    1;
[1]    1,     1;
[2]    2,     3,    1;
[3]    6,    11,    5,    1;
[4]   24,    50,   26,    7,   1;
[5]  120,   274,  154,   47,   9,   1;
[6]  720,  1764, 1044,  342,  74,  11,  1;
[7] 5040, 13068, 8028, 2754, 638, 107, 13, 1;
"""


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


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(sympoly)
