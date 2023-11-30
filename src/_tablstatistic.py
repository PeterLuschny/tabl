import datetime
import sqlite3
from _tablpaths import GetDataPath
from _tabldata import GetType, GetNameByAnum, SaveTraitsToDB
from tabl import tabl_fun, tgen
from os import remove

# #@


def ListByAnum(dbname: str) -> None:
    """
    Retrieve and print the list of traits grouped by 'anum'
    from the 'traits' table in the specified database.

    Parameters:
    - dbname (str): The name of the database.

    Returns:
    - None
    """
    con = sqlite3.connect(GetDataPath(dbname, "db"))
    cur = con.cursor()

    sql = "SELECT anum, triangle, trait FROM traits WHERE anum != 'missing' ORDER by anum;"
    res = cur.execute(sql)
    wer = res.fetchall()
    for seq in wer:
        print("{0} {1}_{2}.".format(*seq))
    print()

    cur.close()
    con.close()


def setLength(s: str, length: int) -> str:
    """
    Truncates or pads the given string `s` to the specified `length`.

    Args:
        s (str): The input string.
        length (int): The maximum length of the resulting string.

    Returns:
        str: The modified string with length equal to `length`.
    """
    return (s + ' ' * length)[:length]


def ListByDistinctAnum(dbname: str) -> None:
    """
    Retrieve and print the list of distinct traits which are in the OEIS,
    grouped by 'anum' from the specified triangle database.

    Parameters:
    - dbname (str): The name of the database.

    Returns:
    - None
    """
    print(f"\nThe traits of the {dbname} triangle as represented in the OEIS.\n")

    con = sqlite3.connect(GetDataPath(dbname, "db"))
    cur = con.cursor()

    sql = f"SELECT DISTINCT(anum), triangle, type, trait FROM {dbname} WHERE anum != 'missing' GROUP BY anum;"
    res = cur.execute(sql)
    wer = res.fetchall()
    count = 1
    print("|     | A-number| trait            | A-name                                                                         |")
    print("|-----|---------|------------------|--------------------------------------------------------------------------------|")
    for seq in wer:
        anum = setLength(seq[0], 7)
        trait = setLength(seq[2] + "-" + seq[3], 16)
        seqname = setLength(GetNameByAnum(seq[0]), 78)
        rn = setLength(str(count), 3)
        print(f"| {rn} | {anum} | {trait} | {seqname} |")
        count += 1
    print()

    cur.close()
    con.close()


def ListAllAnums() -> None:
    """
    Retrieve and print all the A-numbers of traits that are represented in the OEIS.

    Returns:
    - None
    """
    print("\nA-numbers of all traits that are represented in the OEIS.")

    dbname = "traits"

    con = sqlite3.connect(GetDataPath(dbname, "db"))
    cur = con.cursor()

    sql = f"SELECT DISTINCT(anum) FROM {dbname} WHERE anum != 'missing'"
    res = cur.execute(sql)
    wer = res.fetchall()
    count = 0
    for seq in wer:
        if count % 6 == 0:
            print()
        print(f"{seq[0]}, ", end="")
        count += 1
    print()

    cur.close()
    con.close()


def Statistic(dbname: str) -> list:
    """
    Calculate various statistics about the given database.

    Parameters:
    dbname (str): The name of the database.

    Returns:
    list: A list containing the statistics in the following order:
        - Database name
        - Total number of A-numbers
        - Total number of distinct A-numbers
        - Total number of all hashes
        - Total number of distinct hashes
        - Total number of core triangles
        - Total number of distinct types
        - Total number of missing sequences
    """
    con = sqlite3.connect(GetDataPath(dbname, "db"))
    cur = con.cursor()

    print(f"\n* Statistic about {dbname}:")
    print("The number of ...")

    sql = f"SELECT COUNT(hash) FROM {dbname};"
    res = cur.execute(sql)
    anum = res.fetchone()
    print(f"\tall      hashes    is {anum[0]}.")

    sql = f"SELECT COUNT(DISTINCT hash) FROM {dbname};"
    res = cur.execute(sql)
    bnum = res.fetchone()
    print(f"\tdistinct hashes    is {bnum[0]}.")

    sql = f"SELECT COUNT() FROM {dbname} WHERE trait = 'Triangle' AND type = 'Std';"
    res = cur.execute(sql)
    cnum = res.fetchone()
    print(f"\tcore     triangles is {cnum[0]}.")

    sql = f"SELECT COUNT(DISTINCT type) FROM {dbname};"
    res = cur.execute(sql)
    dnum = res.fetchone()
    print(f"\tdistinct types     is {dnum[0]}.")

    sql = f"SELECT COUNT() FROM {dbname} WHERE anum = 'missing';"
    res = cur.execute(sql)
    enum = res.fetchone()
    print(f"\tmissing  sequences is {enum[0]}.")

    sql = f"SELECT COUNT() FROM {dbname} WHERE anum != 'missing';"
    res = cur.execute(sql)
    gnum = res.fetchone()
    print(f"\tall      A-numbers is {gnum[0]}.")

    sql = f"SELECT COUNT(DISTINCT anum) FROM {dbname} WHERE anum != 'missing';"
    res = cur.execute(sql)
    hnum = res.fetchone()
    print(f"\tdistinct A-numbers is {hnum[0]}.")

    con.commit()
    cur.close()
    con.close()

    return [dbname, gnum[0], hnum[0], anum[0], bnum[0], cnum[0], dnum[0], enum[0]]


def TuttiStats(targetname: str = "traitsstats") -> None:
    """
    Generate statistics for all databases and store them in a SQLite database.

    Parameters:
    - name (str): The name of the target base. Default is "traitsstats".

    Returns:
    - None
    """
    filename = GetDataPath(targetname, "db")
    try:
        remove(filename)
    except OSError:
        pass

    with sqlite3.connect(filename) as db:
        cur = db.cursor()
        sql = f"CREATE TABLE {targetname}(Anum, name, allanum, distanum, allhash, disthash, triangles, types, missing)"
        cur.execute(sql)

        for fun in tabl_fun:
            score = [fun.sim[0]] + Statistic(fun.id)
            sql = f"INSERT INTO {targetname} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cur.execute(sql, score)

        db.commit()

        Statistic("traits")

        print("\nRanking of triangles with regard to their impact:\n")
        cur.execute(f"SELECT * FROM {targetname} ORDER by distanum DESC")
        F = cur.fetchall()
        for f in F:
            print([f[3]], f)

        cur.close()

    print("The statistics were created on", datetime.datetime.now(), ".\n")
    print(f"Created database {targetname}.db in data/db.")


def SingleStatistic(triangle: tgen, makenew: bool=False) -> None:
    """
    Generate statistics on the given triangle.

    Args:
        triangle (tgen): The triangle the statistics are to be generated.
        makenew (bool, optional): Flag indicating whether to create a new database first. Defaults to False.

    Returns:
        None
    """
    if makenew:
        filename = GetDataPath(triangle.id, "db")
        try:
            remove(filename)
        except OSError:
            pass
        SaveTraitsToDB(triangle)

    Statistic(triangle.id)
    ListByDistinctAnum(triangle.id)


def Distribution(dbname: str) -> list | None:
    """
    Retrieves the distribution of A-numbers in the specified database.

    Args:
        dbname (str): The name of the database.

    Returns:
        list: A list of tuples containing the A-number and its count,
            sorted by count in descending order.
            Each tuple has the format (anum, cnt).

    Raises:
        sqlite3.Error: If there is an error accessing the database.

    """
    try:
        con = sqlite3.connect(GetDataPath(dbname, "db"))
        cur = con.cursor()

        print(f"\n* Distribution of A-numbers in {dbname}.")

        sql = f"SELECT anum, COUNT(anum) AS cnt FROM {dbname} GROUP BY anum ORDER BY cnt DESC"
        cur.execute(sql)
        result = cur.fetchall()

        cur.close()
        con.close()

        return result

    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
        return None


if __name__ == "__main__":
    # TODO: What A-numbers are most cited?
    # TODO: What hash values whith no A-number are most cited?

    # from tabl import Euler as triangle

    # print(Distribution("Abel"))
    ListByDistinctAnum("Abel")
    # TuttiStats()
    # QuickStatistic(triangle)
    # ListAllAnums()

'''
The traits of the Abel triangle as represented in the OEIS.

|     | A-number| trait            | A-name
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000027 | Inv-DiagCol1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 2   | A000169 | Std-RowMax       | Number of labeled rooted trees with n nodes: n^(n-1)                           |
| 3   | A000248 | Inv-AltSum       | Expansion of e.g.f. exp(x*exp(x))                                              |
| 4   | A001477 | Std-PolyRow1     | The nonnegative integers                                                       |
| 5   | A002378 | Std-DiagRow1     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 6   | A003725 | Inv-RowSum       | E.g.f.: exp( x * exp(-x) )                                                     |
| 7   | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                                |
| 8   | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 9   | A007334 | Std-PolyCol2     | Number of spanning trees in the graph K_{n}/e, which results from contracting  |
| 10  | A009121 | Inv-EvenSum      | Expansion of e.g.f. cosh(exp(x)*x)                                             |
| 11  | A009565 | Inv-OddSum       | Expansion of e.g.f. sinh(exp(x)*x)                                             |
| 12  | A014026 | Alt-PolyDiag     | Inverse of 17th cyclotomic polynomial                                          |
| 13  | A016778 | Rev-PolyRow3     | a(n) = (3*n+1)^2                                                               |
| 14  | A028310 | Std-RowGcd       | Expansion of (1 - x + x^2) / (1 - x)^2 in powers of x                          |
| 15  | A033683 | Alt-TransNat0    | a(n) = 1 if n is an odd square not divisible by 3, otherwise 0                 |
| 16  | A036216 | Inv-DiagCol3     | Expansion of 1/(1 - 3*x)^4; 4-fold convolution of A000244 (powers of 3)        |
| 17  | A052750 | Std-PosHalf      | a(n) = (2*n + 1)^(n - 1)                                                       |
| 18  | A052752 | Rev-PolyCol3     | a(n) = (3*n+1)^(n-1)                                                           |
| 19  | A059297 | Std-Inv          | Triangle of idempotent numbers binomial(n,k)*k^(n-k), version 1                |
| 20  | A059299 | Std-RevInv       | Triangle of idempotent numbers (version 3), T(n, k) = binomial(n, k) * (n - k) |
| 21  | A060747 | Inv:Rev-PolyRow2 | a(n) = 2*n - 1                                                                 |
| 22  | A067998 | Alt-PolyRow2     | a(n) = n^2 - 2*n                                                               |
| 23  | A085527 | Std-NegHalf      | a(n) = (2n+1)^n                                                                |
| 24  | A089946 | Std-TransNat0    | Secondary diagonal of array A089944, in which the n-th row is the n-th binomia |
| 25  | A137452 | Std-Triangle     | Triangular array of the coefficients of the sequence of Abel polynomials A(n,x |
| 26  | A177885 | Std-AltSum       | a(n) = (1-n)^(n-1)                                                             |
| 27  | A193678 | Std-PolyDiag     | Discriminant of Chebyshev C-polynomials                                        |
| 28  | A195136 | Std-OddSum       | a(n) = ((n+1)^(n-1) + (n-1)^(n-1))/2 for n>=1                                  |
| 29  | A195509 | Inv:Rev-EvenSum  | Expansion of e.g.f. (exp(x*exp(x)) + exp(x/exp(x)))/2                          |
| 30  | A208879 | Inv:Rev-Poly     | Number of words A(n,k), either empty or beginning with the first letter of the |
| 31  | A216689 | Inv-NegHalf      | E.g.f. exp( x * exp(x)^2 )                                                     |
| 32  | A225497 | Std-TransSqrs    | Total number of rooted labeled trees over all forests on {1,2,...,n} in which  |
| 33  | A232006 | Std-Poly         | Triangular array read by rows: T(n,k) is the number of simple labeled graphs o |
| 34  | A274278 | Std-EvenSum      | a(n) = ((n+1)^(n-1) - (n-1)^(n-1))/2 for n>=1                                  |
| 35  | A274741 | Rev-Poly         | Table of coefficients in functions that satisfy W_n(x) = W_{n-1}(x)^W_n(x), wi |
| 36  | A275707 | Inv:Rev-NegHalf  | Number of partial functions f:{1,2,...,n}->{1,2,...,n} such that every element |
| 37  | A320258 | Inv:Rev-PolyDiag | a(n) = n! * [x^n] exp(x*exp(-n*x))                                             |
| 38  | A356819 | Inv-PosHalf      | Expansion of e.g.f. exp(-x * exp(2*x))                                         |
| 39  | A356820 | Inv:Rev-PolyCol3 | Expansion of e.g.f. exp(-x * exp(3*x))                                         |
| 40  | A360814 | Inv-DiagSum      | Expansion of Sum_{k>=0} x^(2*k) / (1 - k*x)^(k+1)                              |
| 41  | A362354 | Std-PolyCol3     | a(n) = 3*(n+3)^(n-1)                                                           |
| 42  | A367254 | Std-CentralE     | a(n) = binomial(2*n - 1, n - 1)*(2*n)^n                                        |
| 43  | A367255 | Std-AccRevSum    | a(n) = (n + 1)^(n - 2)*(3*n + 1)                                               |
| 44  | A367256 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k) * binomial(n - 1, k - 1) * n^(n - k)        |
| 45  | A367257 | Std-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n, k) * binomial(n - 1, n - k - 1) * (-n)^k       |
| 46  | A367271 | Inv-CentralE     | a(n) = binomial(2*n, n) * n^n                                                  |
| 47  | A367272 | Inv-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n, k)^2 * k^(n - k)                               |
| 48  | A367273 | Inv-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)^2 * (k - n)^k                               |
| 49  | A367274 | Inv:Rev-ColMiddl | a(n) = binomial(n, k) * (n - k)^k where k = floor(n/2)                         |
| 50  | B000272 | Std-RowSum       | Number of trees on n labeled nodes: n^(n-2) with a(0)=1                        |
| 51  | B000312 | Alt-AccRevSum    | a(n) = n^n; number of labeled mappings from n points to themselves (endofuncti |
| 52  | B001788 | Inv-DiagCol2     | a(n) = n*(n+1)*2^(n-2)                                                         |
| 53  | B053506 | Std-DiagCol2     | a(n) = (n-1)*n^(n-2)                                                           |
| 54  | B053507 | Std-DiagCol3     | a(n) = binomial(n-1,2)*n^(n-3)                                                 |
| 55  | B055541 | Alt-TransSqrs    | Total number of leaves (nodes of vertex degree 1) in all labeled trees with n  |
| 56  | B065513 | Rev-TransNat0    | Number of endofunctions of [n] with a cycle a->b->c->a and for all x in [n], s |
| 57  | B100536 | Inv:Rev-PolyRow3 | a(n) = 3*n^2 - 2                                                               |
| 58  | B366151 | Alt-PolyRow3     | a(n) = T(n, 3), where T(n, k) = Sum_{i=0..n} i^k * binomial(n, i) * (1/2)^(n-k |
'''
