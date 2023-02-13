import csv
from pathlib import Path

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


def ess_equal(s: list[int], tt: list[int]) -> tuple[int, int, int]:

    t = [abs(x) for x in tt]
    K = min(len(t), len(s)) // 2
    for i in range(K):
        for k in range(K):
            L = len(s[i: i + K])
            if s[i: i + K] == t[k: k + L]:
                j = 0; 
                while (i + j < len(s) and k + j < len(t) 
                        and s[i + j] == t[k + j]):
                    j += 1
                return (i, k, j)
    return (-1, -1, 0)


def read_seqdata(datapath: Path) -> list[list]:

    seq_list = []
    with open(datapath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        seq_list = [[seq[0], [int(t) for t in seq[1:-1]]] for seq in reader]

    return seq_list


def SimilarSequences(Seqs: list[list], A: list[int]) -> list:
    candidates = []
    count = 0
    Abs = [abs(x) for x in A]
    for seq in Seqs:
        a, b, size = ess_equal(Abs, seq[1])
        if size > min(16, len(A) // 2):
            candidates.append([seq[0], (a, b, size)])
            count += 1
        if count > 9: break
    return candidates


if __name__ == "__main__":

    from _tablpaths import GetDataPath

    # [],STIRLING2SET,BinConV  
    a = [1, 1, 3, 13, 71, 456, 3337, 27203, 243203, 2357356, 24554426, 272908736, 3218032897, 40065665043, 524575892037, 7197724224361, 103188239447115, 1541604242708064, 23945078236133674, 385890657416861532, 6440420888899573136, 111132957321230896024]
    # [],STIRLING2SET,IBinConV ,
    b= [ 1,1,-1,-5,15,56,-455,-237,16947,-64220,-529494,6833608,-8606015,-459331677,]
    # [],STIRLING2SET,TransSqrs,
    c =[ 0,1,5,22,99,471,2386,12867,73681,446620,2856457,19217243,135610448,]
    # [],STIRLING2SET,TransNat0,
    d = [ 0,1,3,10,37,151,674,3263,17007,94828,562595,3535027,23430840,163254885,]
    # [],STIRLING2SET,TransNat1,
    e = [ 1,2,5,15,52,203,877,4140,21147,115975,678570,4213597,27644437,190899322,]

    def test():
        search = e
        print(search)
        print("Similar sequences are:")

        seqs = read_seqdata(GetDataPath())
        anums = SimilarSequences(seqs, search)
        for anum in anums: 
            print(anum)

    def test1():
        #datapath = GetDataPath()
        #csvpath = 'data/csv/Abel.csv'
        #filepath = (datapath / csvpath).resolve()
    
        filepath = Path("C:\\Users\\User\\PythonTabl\\IntegerTriangles.py\\data\\csv\\Abel.csv")
        seq_list = []
        with open(filepath, "r") as oeisdata:
            reader = csv.reader(oeisdata)
            # Abel,Triangle  ,A137452,[1 0 1 0 
            seq_list = [[seq[0], seq[1], seq[2]] for seq in reader]

        return seq_list
        
    seqs = test1()
    for s in seqs:
        print(s)

    test1()

    print("... done")
