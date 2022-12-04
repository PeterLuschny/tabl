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
        return []
    T = [[I[n, k] for k in range(n + 1)] for n in range(dim)]
    if not isintegerinv(T): return []
    return T
