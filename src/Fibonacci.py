from functools import cache
from tablgenerator import TablGenerator

"""Skew Fibonacci-Pascal triangle  A037027 

A063967 the Fibonacci triangle.
A228074	A Fibonacci-Pascal triangle
some other Fibonacci-Pascal triangles: A027926, A036355, A037027, A074829, A105809, A109906, A111006, A114197, A162741.

[0]   1;
[1]   1,   1;
[2]   2,   3,    1;
[3]   3,   7,    5,    1;
[4]   5,  15,   16,    7,    1;
[5]   8,  30,   43,   29,    9,    1;
[6]  13,  58,  104,   95,   46,   11,   1;
[7]  21, 109,  235,  271,  179,   67,  13,   1;
[8]  34, 201,  506,  705,  591,  303,  92,  15,  1;
[9]  55, 365, 1051, 1717, 1746, 1140, 475, 121, 17, 1;
"""


@cache
def _fi(n: int) -> list[int]:
    if n == 0:
        return [1]
    ro = lambda k: _fi(n - 2)[k] if k >= 0 and k <= n - 2 else 0
    rw = lambda k: _fi(n - 1)[k] if k >= 0 else 0
    row = _fi(n - 1) + [1]
    for k in range(0, n):
        row[k] += ro(k) + ro(k - 1) + rw(k - 1)
    return row


fibonacci = TablGenerator(_fi)


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(fibonacci)
