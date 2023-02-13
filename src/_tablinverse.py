from sympy import Matrix, Rational

# #@

def isintegerinv(T: list[list[int]]) -> bool:
    for row in T:
        for k in row:
            if type(k) == Rational:
                return False
    return True


def InverseTriangle(r, dim: int) -> list[list[int]]:

    M = [[r(n)[k] if k <= n else 0 for k in range(dim)] for n in range(dim)]
    try:
        I = Matrix(M) ** -1
    except: # NonInvertibleMatrixError 
        # print("Not invertible")
        return []

    T = [[I[n, k] for k in range(n + 1)] for n in range(dim)]
    if not isintegerinv(T): 
        # print("Inverse not integer matrix")
        return []
    return T


def InverseTabl(T: list[list[int]]) -> list[list[int]]:
    M = [[T[n][k] if k <= n else 0 for k in range(len(T))] for n in range(len(T))]

    try:
        I = Matrix(M) ** -1
    except: # NonInvertibleMatrixError 
        # print("Not invertible")
        return []

    T = [[I[n, k] for k in range(n + 1)] for n in range(len(M))]
    if not isintegerinv(T): 
        # print("Inverse not integer matrix")
        return []
    return T


if __name__ == "__main__":

    from Abel import Abel
    from Bell import Bell
    from StirlingSet import StirlingSet

    print(InverseTabl(Abel.tab(8)))
    print(InverseTriangle(Abel.gen, 8))

    print(InverseTabl(StirlingSet.tab(8)))
    print(InverseTriangle(StirlingSet.gen, 8))
