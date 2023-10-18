from Bell import bell

"""Bell numbers A000110

[1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147]
"""

# #@


def bell_num(n: int) -> int:
    if n == 0:
        return 1
    return bell(n - 1)[-1]


if __name__ == "__main__":
    print([bell_num(n) for n in range(10)])

    from timeit import default_timer as timer

    start = timer()
    [bell_num(n) for n in range(1000)]
    end = timer()
    print(end - start)
