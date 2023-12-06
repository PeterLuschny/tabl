from MotzkinPoly import motzkinpoly

"""Motzkin numbers A001006

[1, 1, 2, 4, 9, 21, 51, 127, 323, 835]
"""

# #@


def motzkin_num(n: int) -> int:
    return sum(motzkinpoly(n))


if __name__ == "__main__":
    print([motzkin_num(n) for n in range(10)])

    from timeit import default_timer as timer

    start = timer()
    [motzkin_num(n) for n in range(1000)]
    end = timer()
    print(end - start)
