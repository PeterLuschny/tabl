from datetime import datetime
import sqlite3
from typing import Any
from _tablpaths import GetDataPath
from _tabldata import GetNameByAnum, SaveTraitsToDB
from tabl import tabl_fun, tgen
from os import remove

# #@

textcache: list[str] = []

def Print(text: str = '') -> None:
    """
    Print the given string `text` and append it to the global `textcache`.

    Args:
        strtext (str): The input string.

    Returns:
        None
    """
    global textcache
    textcache.append(text)
    print(text)


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
    Print(f"\nThe traits of the {dbname} triangle as represented in the OEIS.\n")

    con = sqlite3.connect(GetDataPath(dbname, "db"))
    cur = con.cursor()

    sql = f"SELECT DISTINCT(anum), triangle, type, trait FROM {dbname} WHERE anum != 'missing' GROUP BY anum;"
    res = cur.execute(sql)
    wer = res.fetchall()
    count = 1
    Print("|     | A-number| trait            | A-name                                                                         |")
    Print("|-----|---------|------------------|--------------------------------------------------------------------------------|")
    for seq in wer:
        anum = setLength(seq[0], 7)
        trait = setLength(seq[2] + "-" + seq[3], 16)
        seqname = setLength(GetNameByAnum(seq[0]), 78)
        rn = setLength(str(count), 3)
        Print(f"| {rn} | {anum} | {trait} | {seqname} |")
        count += 1
    Print()

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


def Statistic(dbname: str) -> list[Any]:
    """
    Calculate various statistics about the given database.

    Parameters:
    dbname (str): The name of the database.

    Returns:
        - Total number of distinct A-numbers
    """
    con = sqlite3.connect(GetDataPath(dbname, "db"))
    cur = con.cursor()

    Print(f"\n* Statistic about {dbname}:\n")
        
    sql = f"SELECT DISTINCT type FROM {dbname};"
    res = cur.execute(sql)
    t = [typ[0] for typ in res.fetchall()]
    Print(f"\tTriangles considered: {t}.")

    sql = f"SELECT COUNT(DISTINCT anum) FROM {dbname} WHERE anum != 'missing';"
    res = cur.execute(sql)
    hnum = res.fetchone()
    Print(f"\tdistinct A-numbers  : {hnum[0]}.")
    
    sql = f"SELECT COUNT() FROM {dbname} WHERE anum != 'missing';"
    res = cur.execute(sql)
    gnum = res.fetchone()
    Print(f"\tall      A-numbers  : {gnum[0]}.")

    #sql = f"SELECT COUNT(DISTINCT hash) FROM {dbname};"
    #res = cur.execute(sql)
    #bnum = res.fetchone()
    #Print(f"\tdistinct hashes     : {bnum[0]}.")

    #sql = f"SELECT COUNT(hash) FROM {dbname};"
    #res = cur.execute(sql)
    #anum = res.fetchone()
    #Print(f"\tall      hashes     : {anum[0]}.")

    sql = f"SELECT COUNT() FROM {dbname} WHERE anum = 'missing';"
    res = cur.execute(sql)
    enum = res.fetchone()
    Print(f"\tmissing  sequences  : {enum[0]}.")

    con.commit()
    cur.close()
    con.close()

    return [hnum[0], gnum[0], enum[0]]


def TuttiStats(targetname: str = "traitsstats") -> None:
    """
    Generate statistics for all tables and store them in a SQLite database.

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
        sql = f"CREATE TABLE {targetname}(Anum, name, distanum, allanum, missing)"
        cur.execute(sql)

        for fun in tabl_fun:
            if fun.id == "StirlingCycle2": continue
            if fun.id == "StirlingCycleB": continue
            
            score = [fun.sim[0], fun.id] + Statistic(fun.id)
            sql = f"INSERT INTO {targetname} VALUES(?, ?, ?, ?, ?)"
            cur.execute(sql, score)

        db.commit()

        Statistic("traits")

        print("\nRanking of triangles with regard to their impact:\n")
        cur.execute(f"SELECT * FROM {targetname} ORDER by distanum DESC")
        F = cur.fetchall()
        rank = 1
        for f in F:
            print(f"({rank})", [f[2]], f[0], f[1], f[2], f[3], f[4])
            rank += 1

        cur.close()

    print("The statistics were created on", datetime.now(), ".\n")
    print(f"Created database {targetname}.db in data/db.")


def StatisticReport(
    triangle: tgen, 
    apptosrc: bool=False,
    makenew: bool=False,
) -> None:
    """
    Generate statistics on the given triangle.

    Args:
        triangle (tgen): The triangle the statistics are to be generated.
        apptosrc (bool, optional): Flag indicating whether to append the statistics to the source file. Defaults to False.
        makenew (bool, optional): Flag indicating whether to create a new database. Defaults to False.

    Returns:
        None
    """
    global textcache; textcache = []

    if makenew:
        filename = GetDataPath(triangle.id, "db")
        try:
            remove(filename)
        except OSError:
            pass
        SaveTraitsToDB(triangle)

    ListByDistinctAnum(triangle.id)
    Statistic(triangle.id)
    Print()
    Distribution(triangle.id)
    Print()
    Print("A related webpage is: " + f"https://peterluschny.github.io/tabl/{triangle.id}.html .")
    now = datetime.now() # current date and time
    Print(now.strftime("%Y/%m/%d"))
    Print()

    if apptosrc:
        with open(f"src/{triangle.id}.py", "a", encoding='utf-8') as f:
            f.write("\n")
            f.write("''' OEIS\n")
            for t in textcache:
                f.write(t + "\n")
            f.write("'''\n")


def Distribution(dbname: str) -> list[Any] | None:
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

        #Print(f"\n* Distribution of A-numbers in {dbname}.\n")

        sql = f"SELECT anum, COUNT(anum) AS cnt FROM {dbname} GROUP BY anum ORDER BY cnt DESC"
        cur.execute(sql)
        result = cur.fetchall()

        cur.close()
        con.close()
        
        Print(str(result))
        return result

    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
        return None


def DistinctAnumbers(table_name: str) -> list[Any]:
    """
    Count the number of distinct A-numbers in a table.
    Group the traits by A-number.

    Args:
        table_name (str): The name of the table.

    Returns:
        list: A list of tuples containing the count, anum, type, trait, and seq of the A-numbers.
    """
    oeis_con = sqlite3.connect(GetDataPath(table_name, "db"))
    oeis_cur = oeis_con.cursor()
    sql = f"""
        SELECT COUNT(anum), anum, GROUP_CONCAT(type, ','), GROUP_CONCAT(trait, ','), seq
        FROM {table_name}
        WHERE anum IS NOT 'missing'
        GROUP BY anum
        ORDER BY COUNT(anum) DESC, anum
    """
    res = oeis_cur.execute(sql)
    ret = res.fetchall()
    oeis_con.commit()
    oeis_con.close()
    return ret


def SummaryReport(name: str) -> None:
    """
    Print a summary of all traits of the table with the given name.

    Args:
        name (str): The name to summarize.
    """
    CD = DistinctAnumbers(name)
    for cd in CD[:-1]:
        z = [f"{a}-{b}" for a, b in zip(cd[2].split(','), cd[3].split(','))]
        print(cd[0], cd[1], z)
        print("         ", setLength(GetNameByAnum(cd[1]), 90))
        print("         ", cd[4])
        print()


if __name__ == "__main__":
    # TODO: What hash values whith no A-number are the most frequent?

    #from tabl import Abel as triangle

    #for fun in tabl_fun: StatisticReport(fun)
    
    #StatisticReport(triangle)

    # print(Distribution(triangle.id))
    # ListByDistinctAnum("Abel")
    TuttiStats()
    # ListAllAnums()
    # SummaryReport(triangle.id)
    print()

'''
    StatisticReport(Abel)

The traits of the Abel triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-RowGcd       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000169 | Std-RowMax       | Number of labeled rooted trees with n nodes: n^(n-1)                           |
| 5   | A000248 | Inv-AltSum       | Expansion of e.g.f. exp(x*exp(x))                                              |
| 6   | A000272 | Std-RowSum       | Number of trees on n labeled nodes: n^(n-2) with a(0)=1                        |
| 7   | A000312 | Std-AltSum       | a(n) = n^n; number of labeled mappings from n points to themselves (endofuncti |
| 8   | A001788 | Inv-DiagCol2     | a(n) = n*(n+1)*2^(n-2)                                                         |
| 9   | A002378 | Std-DiagRow1     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 10  | A003725 | Inv-RowSum       | E.g.f.: exp( x * exp(-x) )                                                     |
| 11  | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                                |
| 12  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 13  | A007334 | Std-PolyCol2     | Number of spanning trees in the graph K_{n}/e, which results from contracting  |
| 14  | A009121 | Inv-EvenSum      | Expansion of e.g.f. cosh(exp(x)*x)                                             |
| 15  | A009565 | Inv-OddSum       | Expansion of e.g.f. sinh(exp(x)*x)                                             |
| 16  | A016778 | Rev-PolyRow3     | a(n) = (3*n+1)^2                                                               |
| 17  | A036216 | Inv-DiagCol3     | Expansion of 1/(1 - 3*x)^4; 4-fold convolution of A000244 (powers of 3)        |
| 18  | A052750 | Std-PosHalf      | a(n) = (2*n + 1)^(n - 1)                                                       |
| 19  | A052752 | Rev-PolyCol3     | a(n) = (3*n+1)^(n-1)                                                           |
| 20  | A053506 | Std-DiagCol2     | a(n) = (n-1)*n^(n-2)                                                           |
| 21  | A053507 | Std-DiagCol3     | a(n) = binomial(n-1,2)*n^(n-3)                                                 |
| 22  | A055541 | Alt-TransSqrs    | Total number of leaves (nodes of vertex degree 1) in all labeled trees with n  |
| 23  | A059297 | Std-Inv          | Triangle of idempotent numbers binomial(n,k)*k^(n-k), version 1                |
| 24  | A059299 | Std-RevInv       | Triangle of idempotent numbers (version 3), T(n, k) = binomial(n, k) * (n - k) |
| 25  | A063524 | Alt-TransNat0    | Characteristic function of 1                                                   |
| 26  | A065513 | Rev-TransNat0    | Number of endofunctions of [n] with a cycle a->b->c->a and for all x in [n], s |
| 27  | A085527 | Std-NegHalf      | a(n) = (2n+1)^n                                                                |
| 28  | A089946 | Std-TransNat0    | Secondary diagonal of array A089944, in which the n-th row is the n-th binomia |
| 29  | A100536 | Inv:Rev-PolyRow3 | a(n) = 3*n^2 - 2                                                               |
| 30  | A137452 | Std-Triangle     | Triangular array of the coefficients of the sequence of Abel polynomials A(n,x |
| 31  | A193678 | Std-PolyDiag     | Discriminant of Chebyshev C-polynomials                                        |
| 32  | A195136 | Std-OddSum       | a(n) = ((n+1)^(n-1) + (n-1)^(n-1))/2 for n>=1                                  |
| 33  | A195509 | Inv:Rev-EvenSum  | Expansion of e.g.f. (exp(x*exp(x)) + exp(x/exp(x)))/2                          |
| 34  | A216689 | Inv-NegHalf      | Expansion of e.g.f. exp( x * exp(x)^2 )                                        |
| 35  | A225497 | Std-TransSqrs    | Total number of rooted labeled trees over all forests on {1,2,...,n} in which  |
| 36  | A232006 | Std-Poly         | Triangular array read by rows: T(n,k) is the number of simple labeled graphs o |
| 37  | A274278 | Std-EvenSum      | a(n) = ((n+1)^(n-1) - (n-1)^(n-1))/2 for n>=1                                  |
| 38  | A275707 | Inv:Rev-NegHalf  | Number of partial functions f:{1,2,...,n}->{1,2,...,n} such that every element |
| 39  | A320258 | Inv:Rev-PolyDiag | a(n) = n! * [x^n] exp(x*exp(-n*x))                                             |
| 40  | A356819 | Inv-PosHalf      | Expansion of e.g.f. exp(-x * exp(2*x))                                         |
| 41  | A356820 | Inv:Rev-PolyCol3 | Expansion of e.g.f. exp(-x * exp(3*x))                                         |
| 42  | A360814 | Inv-DiagSum      | Expansion of Sum_{k>=0} x^(2*k) / (1 - k*x)^(k+1)                              |
| 43  | A362354 | Std-PolyCol3     | a(n) = 3*(n+3)^(n-1)                                                           |
| 44  | A366151 | Alt-PolyRow3     | a(n) = T(n, 3), where T(n, k) = Sum_{i=0..n} i^k * binomial(n, i) * (1/2)^(n-k |
| 45  | A367254 | Std-CentralE     | a(n) = binomial(2*n - 1, n - 1)*(2*n)^n                                        |
| 46  | A367255 | Std-AccRevSum    | a(n) = (n + 1)^(n - 2)*(3*n + 1)                                               |
| 47  | A367256 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k) * binomial(n - 1, k - 1) * n^(n - k)        |
| 48  | A367257 | Std-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n, k) * binomial(n - 1, n - k - 1) * (-n)^k       |
| 49  | A367271 | Inv-CentralE     | a(n) = binomial(2*n, n) * n^n                                                  |
| 50  | A367272 | Inv-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n, k)^2 * k^(n - k)                               |
| 51  | A367273 | Inv-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)^2 * (k - n)^k                               |
| 52  | A367274 | Inv:Rev-ColMiddl | a(n) = binomial(n, k) * (n - k)^k where k = floor(n/2)                         |

* Statistic about Abel:

        Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
        distinct A-numbers  : 52.
        all      A-numbers  : 126.
        missing  sequences  : 88.

[('missing', 88), ('A000027', 10), ('A000272', 6), ('A000169', 6), ('A000012', 6), ('A002378', 5), ('A000312', 5), ('A000007', 5), ('A059297', 4), ('A000248', 4), ('A367257', 3), ('A367256', 3), ('A367255', 3), ('A367254', 3), ('A137452', 3), ('A059299', 3), ('A053507', 3), ('A053506', 3), ('A052750', 3), ('A005563', 3), ('A367273', 2), ('A367272', 2), ('A367271', 2), ('A356819', 2), ('A274278', 2), ('A195136', 2), ('A085527', 2), ('A036216', 2), ('A007334', 2), ('A005408', 2), ('A003725', 2), ('A001788', 2), ('A367274', 1), ('A366151', 1), ('A362354', 1), ('A360814', 1), ('A356820', 1), ('A320258', 1), ('A275707', 1), ('A232006', 1), ('A225497', 1), ('A216689', 1), ('A195509', 1), ('A193678', 1), ('A100536', 1), ('A089946', 1), ('A065513', 1), ('A063524', 1), ('A055541', 1), ('A052752', 1), ('A016778', 1), ('A009565', 1), ('A009121', 1)]

The related webpage is at:
https://peterluschny.github.io/tabl/Abel.html .
'''
