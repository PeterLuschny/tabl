from difflib import SequenceMatcher
import csv

# #@

# We say two sequences are 'essentially equal' if there is a
# neighborhood of infinity where they agree. By a sequence, we
# mean a strictly ordered infinite set S = [a, b, c, d, ...].
#
# A sequence doesn't have an 'offset' or anything like that,
# and when we index it, we start at 0. This also applies to
# sequences in the OEIS, where we ignore everything that is
# said there about offset.
#
# We say two sequences are 'absolutely essentially equal' if
# the sequences of their absolute values are 'essentially equal'.
# In the following, we will always understand comparisons in
# the absolute sense and write a ~= b if two sequences are
# absolutely essentially equal.
#
# We use the following algorithm to decide if two sequences
# are '~='. Given two sequences s and t, the function 'ess_equal'
# returns a pair of integers (n, k) such that, after cutting the
# first n items from s and the first k items from t, the remaining
# sequences are equal; or (-1, -1) if there is no such pair.
# By convention, we look for the smallest n and k, which meet this
# requirement, although this is in fact irrelevant to the criterion.
#
# But there is one necessary restriction: since the search
# algorithm must be finite, the statement is relative to a
# constant K up to which the terms of the sequences are compared.
# In this sense, it is always only a conjecture that the sequences
# are essentially equal.

def compact_absstr(s: list[int]) -> str:
    return str(s).replace("-", "").replace(",", "").replace(" ", "")[1:-1]


def compact_absstr2(s: str) -> str:
    return s.replace("-", "").replace(",", "").replace(" ", "")[:-1]


def SequenceMatch(a: list[int], b: list[int]) -> tuple[int, int, int]:
    str_a = compact_absstr(a)
    str_b = compact_absstr(b)
    s = SequenceMatcher(None, str_a, str_b)
    m = s.find_longest_match()
    return (m.a, m.b, m.size)


def SequenceMatch2(a: list[int], b: str) -> tuple[int, int, int]:
    str_a = compact_absstr(a)
    s = SequenceMatcher(None, str_a, b)
    m = s.find_longest_match()
    return (m.a, m.b, m.size)


def ess_equal(s: list[int], t: list[int]) -> tuple[int, int, int]:

    K = len(s) // 2
    if len(t) >= 2 * K:
        for i in range(K):
            S = [abs(s[i + n]) for n in range(K)]
            for k in range(K):
                T = [abs(t[k + n]) for n in range(K)]
                if S == T:
                    return (i, k, K)
    return (-1, -1, 0)


def read_seqdata(datapath: str) -> list[list]:

    seq_list = []
    with open(datapath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        seq_list = [[seq[0], [int(t) for t in seq[1:-1]]] for seq in reader]

    return seq_list


def SimilarSequences(datapath: str, A: list[int]) -> list:
    Seqs = read_seqdata(datapath)
    candidates = []
    count = 0
    for seq in Seqs:
        a, b, size = ess_equal(A, seq[1])
        if size > 0:
            candidates.append([seq[0], (a, b, size)])
            count += 1
        if count > 5: break
    return candidates


def SimilarSequences2(datapath: str, A: list[int]) -> list:
    candidates = []
    count = 0
    with open(datapath, "r") as oeisdata:
        for line in oeisdata:
            seq = compact_absstr2(line[7:-1])
            found = SequenceMatch2(A, seq)
            if found[2] < 28:
                continue
            candidates.append([line[:7], found])
            count += 1
            if count > 5: break
    return candidates


if __name__ == "__main__":

    from pathlib import Path
    from Lah import lah

    path = Path(__file__).parent.parent
    reldatapath = "data/oeis_data.csv"
    datapath = (path / reldatapath).resolve()

    """
    lah.flat(8) =
    [1, 0, 1, 0, 2, 1, 0, 6, 6, 1, 0, 24, 36, 12, 1, 0, 120, 
    240, 120, 20, 1, 0, 720, 1800, 1200, 300, 30, 1, 0, 5040, 
    15120, 12600, 4200, 630, 42, 1]
    Similar sequences are:
    ['A111596', (0, 0, 74)]
    ['A271703', (0, 0, 74)]
    """

    candidates = SimilarSequences2(datapath, lah.flat(8))
    print("Similar sequences are:")
    for cand in candidates: print(cand)
    print("done")

    # takes too long ?
    # candidates = SimilarSequences2(datapath, lah.flat(8))
