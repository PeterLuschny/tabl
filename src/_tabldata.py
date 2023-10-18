import requests
import gzip
import csv
import sqlite3
from _tablpaths import strippedpath, datapath, oeispath, dbpath
from _tabltypes import fnv

# #@


def get_compressed() -> None:
    oeisstripped = "https://oeis.org/stripped.gz"
    r = requests.get(oeisstripped, stream=True)

    with open(strippedpath, "wb") as local:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                local.write(chunk)

    with gzip.open(strippedpath, "rb") as gz:
        with open(oeispath, "wb") as da:
            da.write(gz.read())


def oeisabsdata() -> None:
    """Make all terms absolute."""

    with open(oeispath, "r") as oeisdata:
        with open(datapath, "w") as absdata:
            for seq in oeisdata:
                if not "#" in seq:
                    absdata.write(seq.replace("-", ""))


def oeisabsdatawithfnv() -> None:
    """Make all terms absolute, take 28 terms, add fnv."""

    with open(oeispath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        with open(datapath, "w") as cleandata:
            seq_list = [[seq[0], [abs(int(s)) for s in seq[1:-1]]] for seq in reader]
            for s in seq_list:
                if len(s[1]) < 28:
                    continue
                x = str(s[1][0:28]).translate(str.maketrans("", "", "[],"))
                f = hex(fnv(bytes(x, encoding="ascii")))[2:]
                cleandata.write(f + "," + s[0] + "," + x + ",\n")


def oeissql() -> None:
    """Make all terms absolute, take 28 terms, add fnv.
       Write (fnv, anum, seq) to oeis.db.
    """

    tabl = sqlite3.connect(dbpath)
    cur = tabl.cursor()
    cur.execute("CREATE TABLE sequences(hash, anum, seq)")

    with open(oeispath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        with open(datapath, "w") as cleandata:
            seq_list = [[seq[0][0:6], [abs(int(s)) for s in seq[1:-1]]] for seq in reader]
            for s in seq_list:
                if len(s[1]) < 28:
                    continue
                x = str(s[1][0:28]).translate(str.maketrans("", "", "[],"))
                f = hex(fnv(bytes(x, encoding="ascii")))[2:]
                tup = (f, s[0], x )
                cur.execute("INSERT INTO sequences VALUES(?, ?, ?)", tup)

    tabl.commit()
    tabl.close()


def querydb(H: str) -> bool:
    oeis_con = sqlite3.connect(dbpath)
    oeis_cur = oeis_con.cursor()
        
    sql = "SELECT EXISTS (SELECT hash FROM sequences WHERE hash=? LIMIT 1)"
    res = oeis_cur.execute(sql, (H,))
    record = res.fetchone()
    return record[0] == 1
    # print(f"Is sequence with hash {H} in the table? {found}!")
    # return found


def GetOEISdata() -> None:
    print("Updating OEIS data!")
    get_compressed()
    oeisabsdata()
    # oeisabsdatawithfnv()
    # oeissql()
    print("OEIS data updated!")


if __name__ == "__main__":
    
    def test1():  
        oeis_con = sqlite3.connect(dbpath)
        oeis_cur = oeis_con.cursor()
        res = oeis_cur.execute("SELECT hash, seq FROM sequences ORDER BY hash")
        hash, seq = res.fetchone()
        print(f'The highest hash is {hash!r}, which is sequence {seq}')
        oeis_con.commit()
        oeis_con.close()

    def test2():  
        oeis_con = sqlite3.connect(dbpath)
        oeis_cur = oeis_con.cursor()
        res = oeis_cur.execute("SELECT hash, anum, seq FROM sequences ORDER BY hash")
        output = res.fetchmany(5)
        for seq in output:  # print(seq) 
            print('hash: {0} anum: {1} seq: {2}.'.format(*seq))
        oeis_con.commit()
        oeis_con.close()

    def test3():  
        oeis_con = sqlite3.connect(dbpath)
        oeis_cur = oeis_con.cursor()
        res = oeis_cur.execute("SELECT hash, anum, seq FROM sequences ORDER BY anum")
        output = res.fetchmany(5)
        for seq in output:  
            print('anum: {1} hash: {0} seq: {2}.'.format(*seq))
        oeis_con.commit()
        oeis_con.close()

    def test4():
        print(querydb("8f5854a276f4f23f"))
        print(querydb("10019398ce7a877b"))
        print(querydb("10019398ce7a877a"))
        print(querydb("29ecd5e3cea1a7e4"))
        print(querydb("39ecd5e3cea1a7e4"))

    # test4()

    GetOEISdata()
