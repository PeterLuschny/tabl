from BinomialCatalan import BinomialCatalan

"""Riordan numbers, A005043

[1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603]
"""

# #@


def riordan_num(n: int) -> int:
    return sum((-1) ** (n - k) * BinomialCatalan(n, k) for k in range(n + 1))


if __name__ == "__main__":
    print([riordan_num(n) for n in range(10)])

    from timeit import default_timer as timer
    start = timer()
    [riordan_num(n) for n in range(1000)]
    end = timer()
    print(end - start) 
