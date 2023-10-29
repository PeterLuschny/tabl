
# #@


def InverseTabl(L: list[list[int]]) -> list[list[int]]:
    # Inverse of a lower triangular matrix
    n = len(L)
    inv = [[0 for i in range(n)] for _ in range(n)]  # Identity matrix
    for i in range(n):
        inv[i][i] = 1
    for k in range(n):
        for j in range(n):
            for i in range(k):
                inv[k][j] -= inv[i][j] * L[k][i]
            a = inv[k][j]
            b = L[k][k]
            if b == 0:
                # print("Warning: Inverse does not exist!")
                return []
            a, r = divmod(a, b) # make sure that a is integer
            if r != 0:
                # print("Warning: Integer terms do not exist!")
                return []
    return [row[0:n + 1] for n, row in enumerate(inv)]


def InverseTriangle(r, dim: int) -> list[list[int]]:
    M = [[r(n)[k] if k <= n else 0 for k in range(dim)] for n in range(dim)]
    return InverseTabl(M)


if __name__ == "__main__":

    def test():
        M = [[1, 0, 0], [1, 2, 0], [1, 2, 3]]
        I = InverseTabl(M)
        print(I)

        M = [[1, 0, 0], [1, 2, 0], [1, 2, 0]]
        I = InverseTabl(M)
        print(I)

        M = [
            [1,      0,      0,     0,    0,   0,  0, 0],
            [0,      1,      0,     0,    0,   0,  0, 0],
            [0,      2,      1,     0,    0,   0,  0, 0],
            [0,      9,      6,     1,    0,   0,  0, 0],
            [0,     64,     48,    12,    1,   0,  0, 0],
            [0,    625,    500,   150,   20,   1,  0, 0],
            [0,   7776,   6480,  2160,  360,  30,  1, 0],
            [0, 117649, 100842, 36015, 6860, 735, 42, 1],
        ]
        I = InverseTabl(M)
        print(I)

    # test()

    from Abel import Abel
    from Bell import Bell
    from StirlingSet import StirlingSet

    dim = 8
    print(InverseTabl(Abel.tab(dim)))
    print(InverseTriangle(Abel.gen, dim))

    print(InverseTabl(StirlingSet.tab(dim)))
    print(InverseTriangle(StirlingSet.gen, dim))

    print(InverseTabl(Bell.tab(dim)))
    print(InverseTriangle(Bell.gen, dim))

