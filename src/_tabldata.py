import requests
import gzip
import csv
import sqlite3
import urllib.request
import time
import pandas as pd
from pathlib import Path
from _tablpaths import GetDataPath, strippedpath
from _tabltypes import tgen, inversion_wrapper, reversion_wrapper, revinv_wrapper, invrev_wrapper
from _tabltraits import RegisterTraits, is_tabletrait


"""
    Pretty printing of triangles trait cards.

    | A-number | Triangle   | Type | Function  | Sequence                                    |
    |----------|------------|------|-----------|---------------------------------------------|
    | A000302  | Binomial   | Std  | PolyVal3  | 1, 4, 16, 64, 256, 1024, 4096, 16384        |
    | A001333  | SchroederB | Inv  | AltSum    | 1, -1, 3, -7, 17, -41, 99, -239             |
    | A006012  | SchroederL | Inv  | AltSum    | 1, -2, 6, -20, 68, -232, 792, -2704         |
    | A026302  | Motzkin    | Rev  | Central   | 1, 2, 9, 44, 230, 1242, 6853, 38376         |
    | A103194  | Laguerre   | Std  | TransNat0 | 0, 1, 6, 39, 292, 2505, 24306, 263431       |
    | A111884  | Lah        | Std  | TransAlts | 1, -1, -1, -1, 1, 19, 151, 1091             |
    | A000000  | Laguerre   | Rev  | TransNat1 | 1, 3, 15, 97, 753, 6771, 68983, 783945      |
"""

# https://www.sqlite.org/lang_select.html
# https://www.sqlitetutorial.net/sqlite-where/
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html


# #@

def fnv(data: bytes) -> int:
    """
    FNV-1a hash algorithm.
    """
    # assert isinstance(data, bytes)

    hval = 0xCBF29CE484222325
    for byte in data:
        hval = hval ^ byte
        hval = (hval * 0x100000001B3) % 0x10000000000000000
    return hval

MINTERMS = 15

def fnv_hash(seq: list[int], absolut: bool=False) -> str:
    """Returns the fnv-hash of an integer sequence based on the first MINTERMS terms. 

    Args:
        seq (list[int]): 
        absolut (bool, optional): Take the absolute value of the terms? Defaults to False.

    Returns:
        str: The hex value of the hash without the '0x'-head.
    """
    if len(seq) < MINTERMS:
        print(f"*** Warning *** Hash based only on {len(seq)} terms.")
        if seq == []: return "0"
    if absolut:
        s = str([abs(i) for i in seq[0:MINTERMS]])
    else:
        s = str(seq[0:MINTERMS])
    x = s.translate(str.maketrans("", "", "[],"))    
    return hex(fnv(bytes(x, encoding="ascii")))[2:]


def GetCompressed() -> None:
    oeisstripped = "https://oeis.org/stripped.gz"
    r = requests.get(oeisstripped, stream=True)

    with open(strippedpath, "wb") as local:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                local.write(chunk)

    with gzip.open(strippedpath, "rb") as gz:
        with open(GetDataPath('oeis', 'csv'), "wb") as da:
            da.write(gz.read())

    print("Info: OEIS-data saved as oeis.csv in data/csv.")


def MakeOeisminiWithFnv() -> None:
    """Make all terms absolute, take MINTERMS terms, add fnv."""

    with open(GetDataPath('oeis', 'csv'), "r") as oeisdata:
        reader = csv.reader(oeisdata)
        with open(GetDataPath('oeismini', 'csv'), "w") as minidata:
            #           A000003 ,1
            seq_list = [[txt[0][0:7], [abs(int(s)) for s in txt[1:-1]]] for txt in reader]
            for s in seq_list:
                if len(s[1]) < MINTERMS:
                    continue
                x = str(s[1][0:MINTERMS]).translate(str.maketrans("", "", "[],"))
                f = hex(fnv(bytes(x, encoding="ascii")))[2:]
                minidata.write(f + "," + s[0] + "," + x + ",\n")

    print("Info: Hashed OEIS-data saved as oeismini.csv in data/csv.")


def OeisToSql() -> None:
    """Make all terms absolute, take MINTERMS terms, add fnv.
       Write (fnv, anum, seq) to oeis.db.
    """

    tabl = sqlite3.connect(GetDataPath('oeismini', 'db'))
    cur = tabl.cursor()
    sql = "CREATE TABLE sequences(hash, anum, seq)"
    cur.execute(sql)

    with open(GetDataPath('oeis', 'csv'), "r") as oeisdata:
        reader = csv.reader(oeisdata)
        
        seq_list = [[txt[0][0:7], [abs(int(s)) for s in txt[1:-1]]] for txt in reader]
        for s in seq_list:
            if len(s[1]) < MINTERMS:
                continue
            x = str(s[1][0:MINTERMS]).translate(str.maketrans("", "", "[],"))
            f = hex(fnv(bytes(x, encoding="ascii")))[2:]
            tup = (f, s[0], x )
            sql = "INSERT INTO sequences VALUES(?, ?, ?)"
            cur.execute(sql, tup)

    tabl.commit()
    tabl.close()

    print("Info: Database oeismini.db saved in data/db.")


def querydbhash(H: str, oeis_cur: sqlite3.Cursor) -> str:
    """_summary_

    Args:
        H (str): hash
        oeis_cur (OEISCursor): _description_

    Returns:
        str: _description_
    """
    sql = "SELECT anum FROM sequences WHERE hash=? LIMIT 1"
    res = oeis_cur.execute(sql, (H,))
    record = res.fetchone()
    return "missing" if record == None else record[0]


def querydbseq(seq:list[int], oeis_cur) -> str:
    """_summary_

    Args:
        seq (list[int]): _description_
        oeis_cur (_type_): _description_

    Returns:
        str: _description_
    """
    x = str([abs(int(s)) for s in seq[0:MINTERMS]]).translate(str.maketrans("", "", "[],"))
    sql = "SELECT anum FROM sequences WHERE seq=? LIMIT 1"
    res = oeis_cur.execute(sql, (x,))
    record = res.fetchone()
    return "missing" if record == None else record[0]


def queryminioeis(H: str, seq:list[int], oeis_cur: sqlite3.Cursor) -> str:
    """Query oeis_mini db only.

    Args:
        H (str): _description_
        seq (list[int]): _description_
        oeis_cur (SQLCursor): _description_

    Returns:
        str: _description_
    """
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


def IsInOEIS(seq: list[int]) -> bool:
    """_summary_

    Args:
        seq (list[int]): sequence

    Returns:
        bool: found?
    """
    strseq = str(seq).replace("[", "").replace("]", "").replace(" ", "")
    url = f"https://oeis.org/search?q={strseq}&fmt=json"
    with urllib.request.urlopen(url) as response:
        page = response.read()
        return -1 == page.find(b'"count": 0', 36, 236)
    

def queryoeis(H: str, seq:list[int], oeis_cur: sqlite3.Cursor) -> str:
    """First query oeis_mini (local), 
       if nothing found query OEIS (internet). 

    Args:
        H (str): _description_
        seq (list[int]): _description_
        oeis_cur (SQLCursor): _description_

    Returns:
        str: _description_
    """
    rec = queryminioeis(H, seq, oeis_cur)
    if rec != 'missing':
        return rec
    time.sleep(1)  # give the OEIS server time to relax
    if IsInOEIS(seq[3:MINTERMS + 3]): 
        return "variant" 
    else:
        return "missing"


STRINGLENx = 100

def SaveTraits(g: tgen, size: int, traits_cur: sqlite3.Cursor, oeis_cur: sqlite3.Cursor, table: str, TRAITS: dict) -> None:
    """Warning: uses internet!

    Args:
        g : _description_
        size : _description_
        traits_cur : _description_
        oeis_cur : _description_
        table : _description_
        TRAITS : _description_
    """
    T = g.tab(size)
    r = g.gen
   
    for traitname, trait in TRAITS.items():
        seq = trait(T) if is_tabletrait(trait) else trait(r, size)
        if seq == []:
            print(f"Info: {g.id}:{traitname} does not exist.")
            continue

        fnv = fnv_hash(seq, True)
        # Much faster in the local version.
        # anum = queryminioeis(fnv, seq, oeis_cur)  # local
        anum = queryoeis(fnv, seq, oeis_cur)  # with internet
        seqstr = ""
        maxl = 0
        for trm in seq:
            s = str(trm) + ' '
            maxl += len(s) 
            if maxl > STRINGLENx: break
            seqstr += s

        tup = (g.id, traitname, fnv, anum, seqstr)
        # print(tup)
        sql = f"INSERT INTO {table} VALUES(?, ?, ?, ?, ?)"
        traits_cur.execute(sql, tup)


def SaveExtendedTraitsToDB(t: tgen, size: int, traits_cur: sqlite3.Cursor, oeis_cur: sqlite3.Cursor, table: str) -> None:
    """Warning: uses internet!

    Args:
        t (tgen): _description_
        size (int): _description_
        traits_cur (_type_): _description_
        oeis_cur (_type_): _description_
        table (_type_): _description_
    """

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


def SaveTraitsToDB(fun: tgen) -> None:
    """Warning: uses internet!
    """
    name = fun.id
    with sqlite3.connect(GetDataPath(name, "db")) as db:
        traits_cur = db.cursor()
        sql = f"CREATE TABLE {name}(triangle, trait, hash, anum, seq)"
        traits_cur.execute(sql)

        with sqlite3.connect(GetDataPath('oeismini', 'db')) as oeis:
            oeis_cur = oeis.cursor()
            SaveExtendedTraitsToDB(fun, 32, traits_cur, oeis_cur, name)
    
        db.commit()

    print(f"Info: Created database {name}.db in data/db.")


def ConvertDBtoCSVandMD(dbpath: Path, funname: str) -> int:
    size = 0
    with sqlite3.connect(dbpath) as db:
        cursor = db.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor.execute(sql)
        tables = cursor.fetchall()
        for table_name in tables:
            table_name = table_name[0]
            sql = f'''SELECT triangle, trait, anum, seq 
                      FROM {table_name} 
                      WHERE anum != 'A000012' 
                      AND anum != 'A000007' 
                      AND anum != 'A000004' '''
            table = pd.read_sql_query(sql, db)
            table.to_csv(GetDataPath(table_name, "csv"), index_label='index')
            table.to_markdown(GetDataPath(table_name, "md"))
            size = table.size // 4
        cursor.close()

    print(f"Info: Created data/csv/{funname}.csv and data/md/{funname}.md.")
    return size


def SaveAllTraitsToDBandCSVandMD(tabl_fun: list[tgen]) -> None:
    """Warning: uses internet!
    """
    for fun in tabl_fun:
        SaveTraitsToDB(fun)
        ConvertDBtoCSVandMD(GetDataPath(fun.id, "db"), fun.id )
    return


def MergeDBs(tablfun: list[tgen]):
    destname = 'traits'
    destpath = GetDataPath(destname, 'db')
    with sqlite3.connect(destpath) as dest:
        dest_cursor = dest.cursor()
        sql = f"CREATE TABLE {destname}(triangle, trait, hash, anum, seq)"
        dest_cursor.execute(sql)
        for src in tablfun: 
            srcpath = GetDataPath(src.id, "db")
            with sqlite3.connect(srcpath) as src:
                src_cursor = src.cursor()
                sql = "SELECT name FROM sqlite_master WHERE type='table';"
                src_cursor.execute(sql)
                tables = src_cursor.fetchall()
                for table_name in tables:
                    table_name = table_name[0]
                    print(table_name)
                    sql = f"SELECT * FROM {table_name}"
                    res = src_cursor.execute(sql)
                    trs = res.fetchall()
                    sql = f"INSERT INTO {destname} VALUES(?, ?, ?, ?, ?)"
                    dest_cursor.executemany(sql, trs)
                src_cursor.close()
        dest.commit()
        dest_cursor.close()
    print("Info: Created database traits.db in data/db.")


if __name__ == "__main__":
    from tabl import tabl_fun
    
    def test1():  
        oeis_con = sqlite3.connect(GetDataPath('oeismini', 'db'))
        oeis_cur = oeis_con.cursor()
        res = oeis_cur.execute("SELECT hash, seq FROM sequences ORDER BY hash")
        hash, seq = res.fetchone()
        print(f'The highest hash is {hash!r}, which is sequence {seq}')
        oeis_con.commit()
        oeis_con.close()

    def test2():  
        oeis_con = sqlite3.connect(GetDataPath('oeismini', 'db'))
        oeis_cur = oeis_con.cursor()
        res = oeis_cur.execute("SELECT hash, anum, seq FROM sequences ORDER BY hash")
        output = res.fetchmany(5)
        for seq in output:  # print(seq) 
            print('hash: {0} anum: {1} seq: {2}.'.format(*seq))
        oeis_con.commit()
        oeis_con.close()

    def test3():  
        oeis_con = sqlite3.connect(GetDataPath('oeismini', 'db'))
        oeis_cur = oeis_con.cursor()
        sql = "SELECT hash, anum, seq FROM sequences ORDER BY anum"
        res = oeis_cur.execute(sql)
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
   
    def test7():
        from Abel import Abel
        SaveTraitsToDB(Abel)
        found = ConvertDBtoCSVandMD(GetDataPath(Abel.id, 'db'), Abel.id)
        print(f"{Abel.id}.csv references {found} sequences from OEIS.")

    def test99():
        for fun in tabl_fun:
            size = ConvertDBtoCSVandMD(GetDataPath(fun.id, 'db'), fun.id)
            print(f"{size} sequences for {fun.id} identified.")

    def test9():
        MergeDBs(tabl_fun)
            