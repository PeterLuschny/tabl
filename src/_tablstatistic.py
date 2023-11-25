import datetime
import sqlite3
from _tablpaths import GetDataPath
from _tabldata import GetType, SaveTraitsToDB
from tabl import tabl_fun, tgen
from os import remove

# #@


def ListByAnum(dbname: str) -> None:
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


def ListByDistinctAnum(dbname: str) -> None:
    print(f"\nThe traits of the {dbname} triangle as represented in the OEIS.\n")

    con = sqlite3.connect(GetDataPath(dbname, "db"))
    cur = con.cursor()

    sql = f"SELECT DISTINCT(anum), triangle, trait FROM {dbname} WHERE anum != 'missing' GROUP BY anum;"
    res = cur.execute(sql)
    wer = res.fetchall()
    count = 1
    for seq in wer:
        trait = GetType(seq[1]) + "-" + seq[2]
        print(f"[{count}] {seq[0]} {trait}")
        count += 1
    print()

    cur.close()
    con.close()


def ListAllAnums() -> None:
    print(f"\nA-numbers of all traits that are represented in the OEIS.")

    dbname = "traits"

    con = sqlite3.connect(GetDataPath(dbname, "db"))
    cur = con.cursor()

    sql = f"SELECT DISTINCT(anum) FROM {dbname} WHERE anum != 'missing' GROUP BY anum;"
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


def Statistic(dbname: str):
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


def TuttiStats(name: str = "traitsstats") -> None:

    filename = GetDataPath(name, "db")
    try:
        remove(filename)
    except OSError:
        pass

    with sqlite3.connect(filename) as db:
        cur = db.cursor()
        sql = f"CREATE TABLE {name}(Anum, name, allanum, distanum, allhash, disthash, triangles, types, missing)"
        cur.execute(sql)

        for fun in tabl_fun:
            score = [fun.sim[0]] + Statistic(fun.id)
            sql = f"INSERT INTO {name} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cur.execute(sql, score)

        db.commit()

        Statistic("traits")

        print("\nRanking of triangles with regard to their impact:\n")
        cur.execute(f"SELECT * FROM {name} ORDER by distanum DESC")
        F = cur.fetchall()
        for f in F:
            print([f[3]], f)

        cur.close()

    print("The statistics were created on", datetime.datetime.now(), ".\n")
    print(f"Created database {name}.db in data/db.")


def QuickCheck(triangle: tgen, makenew: bool=False) -> None:

    if makenew:
        filename = GetDataPath(triangle.id, "db")
        try:
            remove(filename)
        except OSError:
            pass
        SaveTraitsToDB(triangle)

    Statistic(triangle.id)
    ListByDistinctAnum(triangle.id)


if __name__ == "__main__":
    from tabl import BinomialMinus as triangle

    # TuttiStats()
    # QuickCheck(triangle)

    # ListAllAnums()
