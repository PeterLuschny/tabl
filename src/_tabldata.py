import requests
import gzip
import csv
import sqlite3
import pandas as pd
from pathlib import Path
from _tablpaths import strippedpath, datapath, oeispath, dbpath, traitspath
from _tabltypes import tgen, inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper
from _tabltraits import RegisterTraits, is_tabletrait

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
    if seq == []: return "0"
    if len(seq) < MINTERMS:
        print(f"*** Warning *** Hash based only on {len(seq)} terms.")
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
    """Make all terms absolute, take MINTERMS terms, add fnv.
       Write (fnv, anum, seq) to oeis.db.
    """

    tabl = sqlite3.connect(dbpath)
    cur = tabl.cursor()
    cur.execute("CREATE TABLE sequences(hash, anum, seq)")

    with open(oeispath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        
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


def querydbhash(H: str, oeis_cur) -> str:
    sql = "SELECT anum FROM sequences WHERE hash=? LIMIT 1"
    res = oeis_cur.execute(sql, (H,))
    record = res.fetchone()
    return "missing" if record == None else record[0]


def querydbseq(seq:list[int], oeis_cur) -> str:
    x = str([abs(int(s)) for s in seq[0:MINTERMS]]).translate(str.maketrans("", "", "[],"))
    sql = "SELECT anum FROM sequences WHERE seq=? LIMIT 1"
    res = oeis_cur.execute(sql, (x,))
    record = res.fetchone()
    return "missing" if record == None else record[0]


def queryoeis(H: str, seq:list[int], oeis_cur) -> str:
    sql = "SELECT anum FROM sequences WHERE hash=? LIMIT 1"
    res = oeis_cur.execute(sql, (H,))
    record = res.fetchone()
    if record != None: return record[0]

    # not found by hash, perhaps shifted by one?
    x = str([abs(int(s)) for s in seq[1:MINTERMS+1]]).translate(str.maketrans("", "", "[],"))
    sql = "SELECT anum FROM sequences WHERE seq=? LIMIT 1"
    res = oeis_cur.execute(sql, (x,))
    record = res.fetchone()
    return "missing" if record == None else record[0]


STRINGLENx = 100

def SaveTraits(g: tgen, size: int, traits_cur, oeis_cur, TRAITS: dict) -> None:
    T = g.tab(size)
    r = g.gen
   
    for traitname, trait in TRAITS.items():
        seq = trait(T) if is_tabletrait(trait) else trait(r, size)
        if seq == []:
            print(f"Info: {g.id + traitname} does not exist.")
            continue

        fnv = fnv_hash(seq, True)
        anum = queryoeis(fnv, seq, oeis_cur)
        seqstr = ""
        maxl = 0
        for trm in seq:
            s = str(trm) + ' '
            maxl += len(s)
            if maxl > STRINGLENx: break
            seqstr += s

        tup = (g.id, traitname, fnv, anum, seqstr)
        print(tup)
        traits_cur.execute("INSERT INTO traits VALUES(?, ?, ?, ?, ?)", tup)


def SaveExtendedTraitsToDB(T: tgen, size: int, traits_cur, oeis_cur) -> None:

    tim: int = size + size // 2

    Tid = T.id; T.id = T.id + ":Std"

    TRAITS = RegisterTraits()

    SaveTraits(T, size, traits_cur, oeis_cur, TRAITS)
    T.id = Tid 

    r = reversion_wrapper(T, tim)
    SaveTraits(r, size, traits_cur, oeis_cur, TRAITS)

    I = inversion_wrapper(T, tim)
    if I != None:
        SaveTraits(I, size, traits_cur, oeis_cur, TRAITS)
    
    r = revinv_wrapper(T, tim)
    if r != None:
        SaveTraits(r, size, traits_cur, oeis_cur, TRAITS)

    r = invrev_wrapper(T, tim)
    if r != None:
        SaveTraits(r, size, traits_cur, oeis_cur, TRAITS)


def SaveAllTraitsToDB(tabl_fun: list[tgen]) -> None:
    traits_con = sqlite3.connect(traitspath)
    traits_cur = traits_con.cursor()
    traits_cur.execute("CREATE TABLE traits(triangle, trait, hash, anum, seq)")

    oeis_con = sqlite3.connect(dbpath)
    oeis_cur = oeis_con.cursor()

    for fun in tabl_fun:
        SaveExtendedTraitsToDB(fun, 32, traits_cur, oeis_cur)
    
    traits_con.commit()
    traits_con.close()

    oeis_con.close()

    print("Created database traits.db in", traitspath)


def SaveAsCsv(path: Path):
    with sqlite3.connect(path) as db:
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table_name in tables:
            table_name = table_name[0]
            table = pd.read_sql_query("SELECT * from %s" % table_name, db)
            table.to_csv(table_name + '.csv', index_label='index')
        cursor.close()


def GetOEISdata() -> None:
    print("Updating OEIS data!")
    get_compressed()
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


    from tabl import tabl_fun
    GetOEISdata()
    SaveAllTraitsToDB(tabl_fun)
    SaveAsCsv(traitspath)

