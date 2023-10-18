from Partition import partnumexact

"""Partition numbers A000041

[1, 1, 2, 3, 5, 7, 11, 15, 22, 30]
"""

# #@


def part_num(n: int) -> int:
    return sum(partnumexact(n))


if __name__ == "__main__":
    print([part_num(n) for n in range(10)])

    from timeit import default_timer as timer

    start = timer()
    [part_num(n) for n in range(1000)]
    end = timer()
    print(end - start)
