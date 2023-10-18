from Lah import lah

"""Partitions into ordered subsets A000262

[1, 1, 3, 13, 73, 501, 4051, 37633, 394353, 4596553]
"""

# #@


def partlist_num(n: int) -> int:
    return sum(lah(n))


if __name__ == "__main__":
    print([partlist_num(n) for n in range(10)])

    from timeit import default_timer as timer

    start = timer()
    [lah(n) for n in range(1000)]
    end = timer()
    print(end - start)
