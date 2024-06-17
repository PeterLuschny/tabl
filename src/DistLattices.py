from functools import cache

# Cardinalities of finite distributive lattices

@cache
def dist_latt(n, k):
    if k == 0 or n == 0: return 1
    return (dist_latt(n, k - 1)
          + sum(dist_latt(2 * j, k - 1) * dist_latt(n - 1 - 2 * j, k)
            for j in range(1 + (n - 1) // 2)))

if __name__ == "__main__":

    for n in range(9):
        print([dist_latt(n, k) for k in range(8)])

"""
    # A050446
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 3, 6, 10, 15, 21, 28, 36, 45]
    [1, 5, 14, 30, 55, 91, 140, 204, 285]
    [1, 8, 31, 85, 190, 371, 658, 1086, 1695]
    [1, 13, 70, 246, 671, 1547, 3164, 5916, 10317]
    [1, 21, 157, 707, 2353, 6405, 15106, 31998, 62349]
    [1, 34, 353, 2037, 8272, 26585, 72302, 173502, 377739]
    [1, 55, 793, 5864, 29056, 110254, 345775, 940005, 2286648]
    [1, 89, 1782, 16886, 102091, 457379, 1654092, 5094220, 13846117]
"""
