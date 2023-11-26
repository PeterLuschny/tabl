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

    sql = f"SELECT DISTINCT(anum), triangle, trait FROM {dbname} WHERE anum != 'missing' GROUP BY anum;"
    res = cur.execute(sql)
    wer = res.fetchall()
    count = 1
    print("|     | A-number| trait            | A-name |")
    print("|-----|---------|------------------|--------|")
    for seq in wer:
        anum = setLength(seq[0], 7)
        trait = setLength(GetType(seq[1]) + "-" + seq[2], 16)
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
    print(f"\nA-numbers of all traits that are represented in the OEIS.")

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


def QuickStatistic(triangle: tgen, makenew: bool=False) -> None:
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

    from tabl import Euler as triangle

    print(Distribution("Abel"))

    # TuttiStats()
    # QuickStatistic(triangle)
    # ListAllAnums()

'''
|     | A-number | trait            | A-name                                                                                                                                                               |
| --- | -------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | A000027  | Std-DiagRow1     | The positive integers. Also called the natural numbers, the whole numbers or the counting numbers, but these terms are ambiguous                                     |
| 2   | A001333  | Std-ColLeft      | Numerators of continued fraction convergents to sqrt(2)                                                                                                              |
| 3   | A001541  | Std-PosHalf      | a(0) = 1, a(1) = 3; for n > 1, a(n) = 6*a(n-1) - a(n-2)                                                                                                             |
| 4   | A006012  | Std-RowSum       | a(0) = 1, a(1) = 2, a(n) = 4*a(n-1) - 2*a(n-2), n >= 2                                                                                                               |
| 5   | A008865  | Inv:Rev-PolyRow2 | a(n) = n^2 - 2                                                                                                                                                       |
| 6   | A011973  | Inv:Rev-AntiDiag | Irregular triangle of numbers read by rows: {binomial(n-k, k), n >= 0, 0 <= k <= floor(n/2)}; or, triangle of coefficients of (one version of) Fibonacci polynomials |
| 7   | A023443  | Alt-PolyRow1     | a(n) = n - 1                                                                                                                                                         |
| 8   | A025731  | Inv-DiagRow2     | Index of 8^n within sequence of numbers of form 7^i*8^j                                                                                                             |
| 9   | A056109  | Rev-PolyRow2     | Fifth spoke of a hexagonal spiral                                                                                                                                    |
| 10  | A059100  | Alt-PolyRow2     | a(n) = n^2 + 2                                                                                                                                                       |
| 11  | A077957  | Std-AltSum       | Powers of 2 alternating with zeros                                                                                                                                   |
| 12  | A083878  | Std-PolyCol2     | a(0)=1, a(1)=3, a(n) = 6*a(n-1) - 7*a(n-2), n >= 2                                                                                                                   |
| 13  | A083879  | Std-PolyCol3     | a(0)=1, a(1)=4, a(n) = 8*a(n-1) - 14*a(n-2), n >= 2                                                                                                                  |
| 14  | A084058  | Std-NegHalf      | a(n) = 2*a(n-1) + 7*a(n-2) for n>1, a(0)=1, a(1)=1                                                                                                                   |
| 15  | A084154  | Std-OddSum       | Binomial transform of sinh(x)*cosh(sqrt(2)*x)                                                                                                                        |
| 16  | A088013  | Std-EvenSum      | Binomial transform of A001541 (with interpolated zeros)                                                                                                              |
| 17  | A183199  | Std-PolyRow2     | Least integer k such that Floor(k*f(n+1)>k*f(n), where f(n)=(n^2)/(1+n^2)                                                                                            |
| 18  | A329684  | Inv-RowGcd       | Number of excursions of length n with Motzkin-steps forbidding all consecutive steps of length 2 except UD and HH                                                    |
| 19  | B008865  | Inv-PolyRow2     | a(n) = n^2 - 2                                                                                                                                                       |
| 20  | B045943  | Std-DiagRow2     | Triangular matchstick numbers: a(n) = 3*n*(n+1)/2                                                                                                                    |
| 21  | B134481  | Inv-DiagRow3     | Row sums of triangle A134480                                                                                                                                         |
| 22  | B367564  | Std-Triangle     | Triangular array read by rows: T(n, k) = binomial(n, k) * A001333(n - k)                                                                                            |
'''
