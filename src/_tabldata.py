import requests
import gzip
import csv
import sqlite3
from _tablpaths import strippedpath, datapath, oeispath, dbpath

# #@

def fnv(data: bytes) -> int:
    """
    FNV-1a hash algorithm.
    """
    assert isinstance(data, bytes)

    hval = 0xCBF29CE484222325
    for byte in data:
        hval = hval ^ byte
        hval = (hval * 0x100000001B3) % 0x10000000000000000
    return hval

MINTERMS = 15

def fnv_hash(seq: list[int], absolut: bool=False) -> str:
    if len(seq) < MINTERMS:
        print(f"*** Warning *** Hash based only on {len(seq)} terms.")
        return "0"
    if absolut:
        s = str([abs(i) for i in seq[0:MINTERMS]])
    else:
        s = str(seq[0:MINTERMS])
    x = s.translate(str.maketrans("", "", "[],"))    
    return hex(fnv(bytes(x, encoding="ascii")))[2:]


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

MINTERMS = 15

def oeisabsdatawithfnv() -> None:
    """Make all terms absolute, take MINTERMS terms, add fnv."""

    with open(oeispath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        with open(datapath, "w") as cleandata:
            #           A000003 ,1
            seq_list = [[txt[0][0:7], [abs(int(s)) for s in txt[1:-1]]] for txt in reader]
            for s in seq_list:
                if len(s[1]) < MINTERMS:
                    continue
                x = str(s[1][0:MINTERMS]).translate(str.maketrans("", "", "[],"))
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
            seq_list = [[txt[0][0:7], [abs(int(s)) for s in txt[1:-1]]] for txt in reader]
            for s in seq_list:
                if len(s[1]) < MINTERMS:
                    continue
                x = str(s[1][0:MINTERMS]).translate(str.maketrans("", "", "[],"))
                f = hex(fnv(bytes(x, encoding="ascii")))[2:]
                tup = (f, s[0], x )
                cur.execute("INSERT INTO sequences VALUES(?, ?, ?)", tup)

    tabl.commit()
    tabl.close()


def querydbhash(H: str) -> str:
    oeis_con = sqlite3.connect(dbpath)
    oeis_cur = oeis_con.cursor()
        
    sql = "SELECT anum FROM sequences WHERE hash=? LIMIT 1"
    res = oeis_cur.execute(sql, (H,))
    record = res.fetchone()
    oeis_con.commit()
    oeis_con.close()

    return "missing" if record == None else record[0]


def querydbseq(seq:list[int]) -> str:
    oeis_con = sqlite3.connect(dbpath)
    oeis_cur = oeis_con.cursor()
    x = str([abs(int(s)) for s in seq[0:MINTERMS]]).translate(str.maketrans("", "", "[],"))
        
    sql = "SELECT anum FROM sequences WHERE seq=? LIMIT 1"
    res = oeis_cur.execute(sql, (x,))
    record = res.fetchone()
    oeis_con.commit()
    oeis_con.close()

    return "missing" if record == None else record[0]


def GetOEISdata() -> None:
    print("Updating OEIS data!")
    # get_compressed()
    # oeisabsdata()
    # oeisabsdatawithfnv()
    oeissql()
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
        print(querydbhash("8f5854a276f4f23f"))
        print(querydbhash("10019398ce7a877b"))
        print(querydbhash("10019398ce7a877a"))
        print(querydbhash("29ecd5e3cea1a7e4"))
        print(querydbhash("39ecd5e3cea1a7e4"))

        print(querydbseq([1,1,2,2,3,4,5,6,7,8,11,12,15,16,19]))
        print(querydbseq([-1,1,2,2,3,4,5,6,7,8,11,12,15,16,19,21]))
        print(querydbseq([-1,1,2,2,3,4,5,6,7,8,11,12,15,16]))

        data = "1 1 2 2 3 4 5 6 7 8 11 12 15 16 19"
        print(hex(fnv(bytes(data, encoding="ascii"))))
        data = "1 1 6 84 600 145080 2167200 453138235200 319959556963200"
        print(hex(fnv(bytes(data, encoding="ascii"))))
        data = "-1 1 6 84 600 145080 2167200 453138235200 319959556963200"
        print(hex(fnv(bytes(data, encoding="ascii")))) 
        print(fnv_hash([i for i in range(28)]))
        print(fnv_hash([(-1)**i*i for i in range(28)]))
        # absolut values
        print(fnv_hash([i for i in range(28)], True))
        print(fnv_hash([(-1)**i*i for i in range(28)], True))

    # test4()

    # GetOEISdata()
    
