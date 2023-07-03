from functools import cache
from MoebiusMat import moebiusmat

"""Number of divisors (Sigma0 or tau) A000005, 0-based by prependig 1.
Equivalently, d is a divisor of n iff d <= n and d divides n.
(See A113704 and A363914.) 

Here implemented as the row sums of the Moebius matrix (see Moebius.py). 

[1, 1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6]
"""


@cache
def divisors_num(n: int) -> int:
    return sum(moebiusmat(n))


if __name__ == "__main__":

    print([divisors_num(n) for n in range(10)])

    from timeit import default_timer as timer
    start = timer()
    [divisors_num(n) for n in range(1000)]
    end = timer()
    print(end - start) 
