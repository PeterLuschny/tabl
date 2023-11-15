import sqlite3
from _tablpaths import GetDataPath
from tabl import tabl_fun
from os import remove

# #@


def Statistic(dbname: str):
    con = sqlite3.connect(GetDataPath(dbname, "db"))
    cur = con.cursor()

    #sql = "SELECT anum, triangle, trait FROM traits WHERE anum != 'variant' AND anum != 'missing' ORDER by anum;"
    #res = cur.execute(sql)
    #wer = res.fetchall()
    #for seq in wer: print("{0} {1}_{2}.".format(*seq))
    #print()

    #sql = "SELECT DISTINCT(anum), triangle FROM traits WHERE anum != 'variant' AND anum != 'missing' GROUP BY anum;"
    #res = cur.execute(sql)
    #wer = res.fetchall()
    #for seq in wer:
        # print("{0} {1}".format(*seq))
        # print("{0}, ".format(*seq), end="")
    #print()

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

    sql = f"SELECT COUNT() FROM {dbname} WHERE anum = 'variant';"
    res = cur.execute(sql)
    fnum = res.fetchone()
    print(f"\tsimilar  sequences is {fnum[0]}.")

    sql = f"SELECT COUNT() FROM {dbname} WHERE anum != 'variant' AND anum != 'missing';"
    res = cur.execute(sql)
    gnum = res.fetchone()
    print(f"\tall      A-numbers is {gnum[0]}.")

    sql = f"SELECT COUNT(DISTINCT anum) FROM {dbname} WHERE anum != 'variant' AND anum != 'missing';"
    res = cur.execute(sql)
    hnum = res.fetchone()
    print(f"\tdistinct A-numbers is {hnum[0]}.")

    con.commit()
    cur.close()
    con.close()

    return [dbname, anum[0], bnum[0], cnum[0], dnum[0], enum[0], fnum[0], gnum[0], hnum[0]] 


def TuttiStats(name: str = "traitsstats") -> None:
    
    filename = GetDataPath(name, "db")
    try:
        remove(filename)
    except OSError:
        pass

    with sqlite3.connect(filename) as db:
        cur = db.cursor()
        sql = f"CREATE TABLE {name}(Anum, name, allhash, disthash, triangles, types, missing, similar, allanum, distanum)"
        cur.execute(sql)

        for fun in tabl_fun:
            score = [fun.sim[0]] + Statistic(fun.id)
            sql = f"INSERT INTO {name} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cur.execute(sql, score)

        db.commit()

        # Summary:
        Statistic("traits")

        print("\nRanking of triangles with regard to their impact:\n")
        cur.execute(f"SELECT * FROM {name} ORDER by distanum DESC")
        F = cur.fetchall()
        for f in F:
            print([f[9] + f[7] // 2], f)
    
        cur.close()

    print(f"Info: Created database {name}.db in data/db.")


if __name__ == "__main__":
    TuttiStats()    
