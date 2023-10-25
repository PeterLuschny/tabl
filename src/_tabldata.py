import requests
import gzip
import csv
import sqlite3
# import tabulate
import pandas as pd
from pathlib import Path
from _tablpaths import strippedpath, datapath, oeispath, dbpath, traitspath, traitscsvpath
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


def OeisToSql() -> None:
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
    if record != None: 
        return record[0]

    # not found by hash, perhaps shifted by one?
    H = fnv_hash(seq[1:MINTERMS + 1], True)
    res = oeis_cur.execute(sql, (H,))
    record = res.fetchone()
    return "missing" if record == None else record[0]


STRINGLENx = 100

def SaveTraits(g: tgen, size: int, traits_cur, oeis_cur, table, TRAITS: dict) -> None:
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
        traits_cur.execute(f"INSERT INTO {table} VALUES(?, ?, ?, ?, ?)", tup)


def SaveExtendedTraitsToDB(t: tgen, size: int, traits_cur, oeis_cur, table) -> None:

    tim: int = size + size // 2
    Tid = t.id; t.id = t.id + ":Std"

    TRAITS = RegisterTraits()

    thash = fnv_hash(t.tab(MINTERMS))
    SaveTraits(t, size, traits_cur, oeis_cur, table, TRAITS)
    t.id = Tid 

    r = reversion_wrapper(t, tim)
    rhash = fnv_hash(r.tab(MINTERMS))
    if thash != rhash:
        SaveTraits(r, size, traits_cur, oeis_cur, table, TRAITS)

    i = inversion_wrapper(t, tim)
    ihash = "0"
    if i != None:
        ihash = fnv_hash(i.tab(MINTERMS))
        SaveTraits(i, size, traits_cur, oeis_cur, table, TRAITS)
    
    ri = revinv_wrapper(t, tim)
    if ri != None:
        rihash = fnv_hash(ri.tab(MINTERMS))
        if ihash != rihash:
            SaveTraits(ri, size, traits_cur, oeis_cur, table, TRAITS)

    if thash != rhash:
        ir = invrev_wrapper(t, tim)
        if ir != None:
            SaveTraits(ir, size, traits_cur, oeis_cur, table, TRAITS)


def traitpath(name: str, fix: str)  -> Path:
    relpath = f"data/{name}.{fix}"
    return (Path(__file__).parent.parent / relpath).resolve()


def SaveAllTraitsToDB(tabl_fun: list[tgen]) -> None:
    with sqlite3.connect(traitspath) as db:
        traits_cur = db.cursor()
        table = "traits"
        traits_cur.execute(f"CREATE TABLE {table}(triangle, trait, hash, anum, seq)")

        with sqlite3.connect(dbpath) as oeis:
            oeis_cur = oeis.cursor()
            for fun in tabl_fun:
                SaveExtendedTraitsToDB(fun, 32, traits_cur, oeis_cur, table)
        db.commit()
    print("Created database traits.db in", traitspath)


def SaveTraitsToDB(fun) -> None:
    name = fun.id
    with sqlite3.connect(traitpath(name, "db")) as db:
        traits_cur = db.cursor()
        traits_cur.execute(f"CREATE TABLE {name}(triangle, trait, hash, anum, seq)")

        with sqlite3.connect(dbpath) as oeis:
            oeis_cur = oeis.cursor()
            SaveExtendedTraitsToDB(fun, 32, traits_cur, oeis_cur, name)
    
        db.commit()
    print(f"Created {name}.db.")


"""
Pretty printing of triangles trait cards.

| A-number | Triangle   | Form | Function  | Sequence                                    |
|----------|------------|------|-----------|---------------------------------------------|
| A000302  | Binomial   | Std  | PolyVal3  | 1, 4, 16, 64, 256, 1024, 4096, 16384        |
| A001333  | SchroederB | Inv  | AltSum    | 1, -1, 3, -7, 17, -41, 99, -239             |
| A006012  | SchroederL | Inv  | AltSum    | 1, -2, 6, -20, 68, -232, 792, -2704         |
| A026302  | Motzkin    | Rev  | Central   | 1, 2, 9, 44, 230, 1242, 6853, 38376         |
| A103194  | Laguerre   | Std  | TransNat0 | 0, 1, 6, 39, 292, 2505, 24306, 263431       |
| A111884  | Lah        | Std  | TransAlts | 1, -1, -1, -1, 1, 19, 151, 1091             |
| A000000  | Laguerre   | Rev  | TransNat1 | 1, 3, 15, 97, 753, 6771, 68983, 783945      |
"""

def SaveDbAs(dbpath: Path) -> None:
    with sqlite3.connect(dbpath) as db:
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table_name in tables:
            table_name = table_name[0]
            table = pd.read_sql_query("SELECT * from %s" % table_name, db)
            table.to_csv(traitpath(table_name, "csv"), index_label='index')
            table.to_markdown(traitpath(table_name, "md"))
        cursor.close()


def GetOEISdata() -> None:
    print("Updating OEIS data!")
    get_compressed()
    OeisToSql()
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


    #from tabl import tabl_fun
    #GetOEISdata()
    #SaveAllTraitsToDB(tabl_fun)
    #SaveDbAs(traitspath)

    #from Abel import Abel
    #SaveTraitsToDB(Abel)
   