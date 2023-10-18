from Euler import euler

"""André function and Euler numbers, A346838 and A000111

[1, -1, 1, -2, 5, -16, 61, -272, 1385, -7936]
"""

# #@


def euler_num(n: int) -> int:
    return euler(n)[0]


if __name__ == "__main__":
    print([euler_num(n) for n in range(10)])

    from timeit import default_timer as timer

    start = timer()
    [euler_num(n) for n in range(1000)]
    end = timer()
    print(end - start)
