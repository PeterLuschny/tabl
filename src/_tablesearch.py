import csv
from pathlib import Path

'''
We say two sequences are 'essentially equal' if there is a neighborhood of infinity where they agree. By a sequence, we mean a strictly ordered infinite set S = [a, b, c, d, ...]. 

A sequence doesn't have an 'offset' or anything like that, but when we index it, we start at 0. This also applies to sequences in the OEIS, where we ignore everything that is said there about offset.

We say two sequences are 'absolutely essentially equal' if the sequences of their absolute values are 'essentially equal'. In the following, we will always understand comparisons in the absolute sense and write a ~= b if two sequences are absolutely essentially equal.

We use the following algorithm to decide if two sequences are '~='. Given two sequences s and t, the function 'ess_equal' returns a pair of integers (n, k) such that, after cutting the first n items from s and k items from t, the remaining sequences are equal; or (-1, -1) if there is no such pair. By convention, we look for the smallest n and k, which meet this requirement, although this is irrelevant to the criterion. 

But there is one necessary restriction: since the search algorithm must be finite, the statement is relative to a constant K up to which the terms of the sequences are compared. In this sense, it is always only an conjecture that the sequences are essentially equal in the sense of the criterion.
'''
def ess_equal(s: list[int], t: list[int]) -> list:

    K = 24
    if len(t) >= 2 * K: 
        for i in range(K):
            S = [abs(s[i + n]) for n in range(K)]
            for k in range(K):
                T = [abs(t[k + n]) for n in range(K)]
                if S == T:
                    print((i , k), S)
                    return [True, (i , k)]

    return [False, (int(-1), int(-1))]


def read_seqdata(datapath) -> list[list]: 

    D = []
    with open(datapath, 'r') as oeisdata:
        reader = csv.reader(oeisdata)
        D = [[seq[0], [int(t) for t in seq[1:-1]]] for seq in reader]

    return D


def search_oeis(datapath, A: list[int]) -> None:
    Seqs = read_seqdata(datapath)
    candidates = []
    for seq in Seqs:
        found, shifts = ess_equal(A, seq[1])
        if found:
            candidates.append([seq[0], shifts])
            print(seq)
    print("\nSimilar sequences are:")
    print(candidates)


if __name__ == "__main__":

    def test1() -> None:
        s = [0] + [(-1) ** n * n for n in range(22)]
        t = [1, 2] + [n + 3 for n in range(22)]
        print(s); print(t)
        print(ess_equal(s, t))

    Axx = [1, 1, 1, -2, 1, -3, 1, -4, 2, 1, -5, 5, 1, -6, 9, -2, 1, -7, 14, -7, 1, -8, 20, -16, 2, 1, -9, 27, -30, 9, 1, -10, 35, -50, 25, -2, 1, -11, 44, -77, 55, -11, 1, -12, 54, -112, 105, -36, 2, 1, -13, 65, -156, 182, -91, 13, 1, -14, 77, -210, 294, -196, 49, -2]

    Bxx = [1, 1, 1, -1, 1, -2, 1, -3, 1, 1, -4, 3, 1, -5, 6, -1, 1, -6, 10, -4, 1, -7, 15, -10, 1, 1, -8, 21, -20, 5, 1, -9, 28, -35, 15, -1, 1, -10, 36, -56, 35, -6, 1, -11, 45, -84, 70, -21, 1, 1, -12, 55, -120, 126, -56, 7, 1, -13, 66, -165, 210, -126, 28, -1, 1, -14, 78, -220, 330, -252, 84, -8, 1, -15, 91, -286, 495, -462, 210, -36, 1]

    path = Path(__file__).parent.parent
    reldatapath = 'data/oeis_data.csv'
    datapath = (path / reldatapath).resolve()

    print("... bussy searching")
    search_oeis(datapath, Axx)
    print("Done")

'''
Similar sequences are:
[['A034807 ', (1, 1)], ['A113279 ', (1, 1)], ['A132460 ', (0, 0)], ['A213234 ', (1, 1)]]
[['A011973 ', (0, 0)], ['A115139 ', (0, 0)]]
'''
