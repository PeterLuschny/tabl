import gzip
import csv
import sqlite3
import urllib.request
import urllib.error
import time
from pathlib import Path
import requests
from requests import get
import traceback
import pandas as pd
from _tablpaths import GetDataPath, strippedpath, oeisnamespath
from _tabltypes import tgen, InvTable, RevTable, AltTable, SeqString
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

# #@

'''
This is a very sensible value. It is the number of terms used to calculate the hash.
'''
MINTERMS = 24
'''
To guarantee MINTERMS = 16 for sequences like the center column of the triangle,
we need to use a triangle with 31 rows (0..30). But 16 is too small!
'''
MINROWS = 2 * MINTERMS
'''
Needed for anti-diagonal traits of the triangle.
'''
DIAGSIZE = MINROWS + MINROWS // 2
'''
Maximal length of the string representing the sequence.
'''
MAXSTRLEN = 100

def GetMaxStrLen() -> int:
    return MAXSTRLEN


def fnv(data: bytes) -> int:
    """
    This function calculates the FNV-1a hash value for the given data.

    Args:
        data (bytes): The input data to be hashed.

    Returns:
        int: The calculated hash value.
   """
    assert isinstance(data, bytes)

    hval = 0xCBF29CE484222325
    for byte in data:
        hval ^= byte
        hval *= 0x100000001B3
        hval &= 0xFFFFFFFFFFFFFFFF
    return hval


def FNVhash(seq: list[int], absolut: bool = False) -> str:
    """Returns the fnv-hash of an integer sequence based on the first MINTERMS terms.

    Args:
        seq (list[int]):
        absolut (bool, optional): Take the absolute value of the terms? Defaults to False.

    Returns:
        str: The hex value of the hash without the '0x'-head.
    """
    if len(seq) < MINTERMS:
        for line in traceback.format_stack():
            print(line.strip())
        raise Exception(f"*** Error *** Data has only {len(seq)} terms, {MINTERMS} required.")

    if absolut:
        x = ' '.join(str(abs(i)) for i in seq[0:MINTERMS])
    else:
        x = ' '.join(str(i) for i in seq[0:MINTERMS])

    return hex(fnv(bytes(x, encoding="ascii")))[2:]


def isInOEIS(seq: list[int]) -> bool:
    """
    Check if a given sequence is present in the OEIS (Online Encyclopedia of Integer Sequences).
    The search uses seq[3:] with max string length 160.

    Args:
        seq (list[int]): The sequence to check.

    Returns:
        bool: True if the sequence is found in the OEIS, False otherwise.

    Raises:
        Exception: If the OEIS server cannot be reached after multiple attempts.
    """
    strseq = SeqString(seq, 140, 24, ",", 3)
    url = f"https://oeis.org/search?q={strseq}&fmt=json"

    for _ in range(3):
        time.sleep(0.5)  # give the OEIS server some time to relax
        try:
            with urllib.request.urlopen(url) as response:
                page = response.read()
                return -1 == page.find(b'"count": 0')
        except urllib.error.HTTPError as he:
            print(he.__dict__)
        except urllib.error.URLError as ue:
            print(ue.__dict__)

    raise Exception(f"Could not open {url}.")


def IsInOEIS(seq: list[int]) -> str:
    """
    Check if a given sequence is present in the OEIS (Online Encyclopedia of Integer Sequences).
    The search uses seq[3:] with max string length 160.

    Args:
        seq (list[int]): The sequence to check.

    Returns:
        str: The A-number of the sequence if found in OEIS, otherwise an empty string.

    Raises:
        Exception: If the OEIS server cannot be reached after multiple attempts.
    """
    strseq = SeqString(seq, 140, 24, ",", 3)
    url = f"https://oeis.org/search?q={strseq}&fmt=json"

    for _ in range(3):
        time.sleep(0.5)  # give the OEIS server some time to relax
        try:
            jdata = get(url, timeout=10).json()
            anumber = ""
            if jdata["count"] > 0:
                number = jdata["results"][0]["number"]
                anumber = f"B{(6 - len(str(number))) * '0' + str(number)}"
            return anumber
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    raise Exception(f"Could not open {url}.")


def GetNameByAnum(anum: str) -> str:
    """
    Retrieves the name associated with the given anum.

    Parameters:
    anum (str): The OEIS A-number to search for.

    Returns:
    str: The name associated with the given anum, or an empty string if not found.
    """
    if anum[0] == 'B':
        anum = 'A' + anum[1:]

    with open(GetDataPath("oeisnames", "csv"), "r", encoding='utf8') as oeisnames:
        lines = oeisnames.readlines()
        # reader = csv.reader(oeisnames, delimiter= ",")
        for line in lines:
            rnum = line[0:7]
            if anum == rnum:
                return line[8:-2]
    return ""


def GetCompressed() -> None:
    """
    Downloads the stripped file from OEIS, extracts the CSV data, and saves it to oeis.csv.

    Raises:
        requests.exceptions.RequestException: If there is an error downloading the stripped file.
        IOError: If there is an error extracting the OEIS data.
        Exception: If any other error occurs.
    """
    # Download the stripped file
    print("Downloading OEIS stripped file...")
    oeisstripped = "https://oeis.org/stripped.gz"
    r = requests.get(oeisstripped, stream=True, timeout=10)
    r.raise_for_status()
    csvpath = GetDataPath("oeis", "csv")

    # Save the stripped file
    with open(strippedpath, "wb") as local:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                local.write(chunk)

    # Extract the CSV file from the stripped file
    with gzip.open(strippedpath, "rb") as gz:
        with open(csvpath, "wb") as da:
            da.write(gz.read())

    print(f"OEIS data saved as {csvpath}.")


def GetNames() -> None:
    """
    Downloads the names file from OEIS, extracts the CSV data, and saves it to oeisnames.csv.

    Raises:
        RequestException: If there is an error downloading the names file.
        IOError: If there is an error extracting the OEIS data.
        Exception: If any other error occurs.
    """
    # Download the name file
    print("Downloading OEIS names file...")
    oeisnames = "https://oeis.org/names.gz"
    r = requests.get(oeisnames, stream=True, timeout=10)
    r.raise_for_status()

    # Save the names file
    with open(oeisnamespath, "wb") as local:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                local.write(chunk)

    # Extract the CSV file from the names file
    csvpath = GetDataPath("oeisnames", "csv")
    with gzip.open(oeisnamespath, "rb") as gz:
        with open(csvpath, "wb") as da:
            da.write(gz.read())

    print(f"OEIS names saved as {csvpath}.")


def MakeOeisminiWithFnv() -> None:
    """
    This function reads data from a CSV file containing OEIS sequences,
    processes the data, and saves the hashed sequences into a SQLite database.

    Make all terms absolute, take MINTERMS terms, add fnv.
    """
    with open(GetDataPath("oeis", "csv"), "r") as oeisdata:
        reader = csv.reader(oeisdata)
        with open(GetDataPath("oeismini", "csv"), "w") as minidata:
            #    A000003 ,1
            seq_list = [[txt[0][0:7], [abs(int(s)) for s in txt[1:-1]]] for txt in reader]
            for seq in seq_list:
                if len(seq[1]) < MINTERMS:
                    continue

                f = FNVhash(seq[1])
                x = ' '.join(str(i) for i in seq[1])

                minidata.write(f + "," + seq[0] + "," + x + ",\n")

    print("Info: Hashed OEIS-data saved as oeismini.csv in data/csv.")


def OeisToSql() -> None:
    """
    This function reads data from a CSV file containing OEIS sequences,
    processes the data, and inserts it into 'oeismini', a SQLite database.

    The function performs the following steps:
    1. Connects to the SQLite database.
    2. Creates a table named 'sequences' if it doesn't already exist.
    3. Reads the data from the CSV file.
    4. Processes the data by making all terms absolute and taking MINTERMS terms.
    5. Calculates the FNV hash for each sequence.
    6. Inserts the (fnv, anum, seq) values into the 'sequences' table.

    Note: The function assumes the existence of the 'GetDataPath' function,
    which returns the path to the data files.

    Raises:
        Exception: If there is an error during the execution of the function.
    """
    tabl = sqlite3.connect(GetDataPath("oeismini", "db"))
    cur = tabl.cursor()
    sql = "CREATE TABLE sequences(hash, anum, seq)"
    cur.execute(sql)

    with open(GetDataPath("oeis", "csv"), "r") as oeisdata:
        reader = csv.reader(oeisdata)

        seq_list = [[txt[0][0:7], [abs(int(s)) for s in txt[1:-1]]] for txt in reader]
        for seq in seq_list:
            if len(seq[1]) < MINTERMS:
                continue

            f = FNVhash(seq[1])
            x = ' '.join(str(i) for i in seq[1])

            tup = (f, seq[0], x)
            sql = "INSERT INTO sequences VALUES(?, ?, ?)"
            cur.execute(sql, tup)

    tabl.commit()
    tabl.close()

    print("Info: Database oeismini.db saved in data/db.")


def QueryDBbyHash(H: str, db_cur: sqlite3.Cursor) -> str:
    """
    Query the sequences table in the local database for a given hash.

    Args:
        H (str): The hash value to query.
        oeis_cur (sqlite3.Cursor): The cursor object for executing SQL queries.

    Returns:
        str: The corresponding anum value if the hash is found, otherwise "missing".
    """
    sql = "SELECT anum FROM sequences WHERE hash=? LIMIT 1"
    res = db_cur.execute(sql, (H,))
    record = res.fetchone()
    return "missing" if record is None else record[0]


def QueryDBbySeq(seq: list[int], db_cur: sqlite3.Cursor) -> str:
    """
    Query the sequences table in the database for a given sequence.

    Args:
        seq (list[int]): The sequence to query.
        oeis_cur (sqlite3.Cursor): The cursor object for executing SQL queries.

    Returns:
        str: The corresponding anum value if the sequence is found, otherwise "missing".
    """
    x = str([abs(int(s)) for s in seq[0:MINTERMS]]).translate(
        str.maketrans("", "", "[],")
    )
    sql = "SELECT anum FROM sequences WHERE seq=? LIMIT 1"
    res = db_cur.execute(sql, (x,))
    record = res.fetchone()
    return "missing" if record is None else record[0]


def QueryLocalDB(H: str, seq: list[int], db_cur: sqlite3.Cursor) -> str:
    """
    Query local database oeismini.db.

    Args:
        H (str): The hash value to query.
        seq (list[int]): The sequence to query.
        oeis_cur (sqlite3.Cursor): The cursor object for executing SQL queries.

    Returns:
        str: The corresponding anum value if the sequence is found, otherwise "missing".
    """

    if len(seq) < MINTERMS:
        for line in traceback.format_stack():
            print(line.strip())
        raise Exception(f"*** Error *** Data has only {len(seq)} terms, {MINTERMS} required.")

    sql = "SELECT anum FROM sequences WHERE hash=? LIMIT 1"
    res = db_cur.execute(sql, (H,))
    record = res.fetchone()
    return "missing" if record is None else record[0]


def QueryOeis(H: str, seq: list[int], db_cur: sqlite3.Cursor) -> str:
    """
    First query oeis_mini (local), if nothing found query OEIS (internet).

    Args:
        H (str): The hash value to query.
        seq (list[int]): The sequence to query.
        oeis_cur (sqlite3.Cursor): The cursor object for executing SQL queries.

    Returns:
        str: The corresponding anum value if the sequence is found, otherwise "missing".
    """
    rec = QueryLocalDB(H, seq, db_cur)
    if rec != "missing":
        return rec
    bnum = IsInOEIS(seq)
    if bnum == "":
        return "missing"
    return bnum


def DebugQueryOeis(H: str, seq: list[int], db_cur: sqlite3.Cursor) -> str:
    """
    First query oeis_mini (local), if nothing found query OEIS (internet).

    Args:
        H (str): The hash value to query.
        seq (list[int]): The sequence to query.
        oeis_cur (sqlite3.Cursor): The cursor object for executing SQL queries.

    Returns:
        str: The corresponding anum value if the sequence is found, otherwise "missing".
    """
    rec = QueryLocalDB(H, seq, db_cur)
    print(seq)
    if rec != "missing":
        print(f"Using hash {H} found in local database.")
        f = FNVhash(seq, True)
        print(f"{f} is actual hash.")
        return rec
    bnum = IsInOEIS(seq)
    if bnum == "":
        return "missing"
    print(f"seq found in OEIS.")
    return bnum


def GetType(name: str) -> list[str]:
    """
    There are 7 types:
        ["", "Std", "Rev", "Inv", "Rev:Inv", "Inv:Rev", "Alt"]
    """
    sp = name.split(":", 1)
    if len(sp) == 1:
        return ["", ""]
    return name.split(":", 1)


def CreateTable(name: str) -> str:
    return f"CREATE TABLE {name}(triangle, type, trait, anum, hash, seq)"


def InsertTable(name: str) -> str:
    return f"INSERT INTO {name} VALUES(?, ?, ?, ?, ?, ?)"


def FilterTraits(anum: str, anumsonly: bool=False) -> bool:
    """
    Filter traits to remove traits that are not interresting.

    Args:
        anumber (str): The traits as A-number.
        anumsonly (bool, optional): Disregard missing anums. Defaults to False.

    Returns:
        True if the trait should be discarded.
    """
    lame = ["A000012", "A000007", "A000004"]
    if anumsonly:
        lame.append("missing")

    return anum in lame


def SaveTraits(fun: tgen, size: int, traits_cur: sqlite3.Cursor, oeis_cur: sqlite3.Cursor, table: str, TRAITS: dict) -> None:
    """Saves traits data to a database table.

    This function saves traits data to a specified database table. It uses the provided
    triangle generator `g` and size `size` to generate the traits data. The traits data is then
    stored in the `traits_cur` cursor object. The `oeis_cur` cursor object is used to
    query the OEIS (Online Encyclopedia of Integer Sequences) for additional information
    about the traits data. The `table` parameter specifies the name of the database table
    to store the traits data. The `TRAITS` dictionary contains the traits to be saved.

    Args:
        fun (tgen): The generator used to generate the traits data.
        size (int): The size of the traits data.
        traits_cur (sqlite3.Cursor): The cursor object for the traits table.
        oeis_cur (sqlite3.Cursor): The cursor object for the OEIS table.
        table (str): The name of the database table to store the traits data.
        TRAITS (dict): A dictionary containing the traits to be saved.

    Returns:
        None
    """
    T = fun.tab(size)
    if size < MINROWS:
        raise Exception(f"*** Error *** Table {fun.id} has only {size} rows, min {MINROWS} required.")

    r = fun.gen
    triname = fun.id
    funname, trityp = GetType(triname)
 
    for traitname, trait in TRAITS.items():
        if trityp == traitname:
            continue

        seq = trait(T) if is_tabletrait(trait) else trait(r, size)
        if seq == []:
            print(f"Info: {triname} -> {traitname} does not exist.")
            continue

        if len(seq) < MINTERMS:
            for line in traceback.format_stack():
                print(line.strip())
            raise Exception(f"*** Error *** Table {fun.id} and trait {traitname} has only {len(seq)}, min {MINTERMS} required.")

        print(f"Processing {triname}, {traitname}, {len(seq)} ")

        fnvhash = FNVhash(seq, True)
        # anum = queryminioeis(fnvhash, seq, oeis_cur)  # local
        anum = QueryOeis(fnvhash, seq, oeis_cur)  # with internet

        if FilterTraits(anum):  # discard traits that are not interresting
            continue

        seqstr = SeqString(seq, MAXSTRLEN, 99)

        tup = (funname, trityp, traitname, anum, fnvhash, seqstr)
        sql = InsertTable(table)
        traits_cur.execute(sql, tup)


def SaveExtendedTraitsToDB(fun: tgen, size: int, traits_cur: sqlite3.Cursor, oeis_cur: sqlite3.Cursor, table: str) -> None:
    """
    Saves the extended traits of a triangle to a SQLite database.

    Args:
        fun (tgen): The triangle whose extended traits are to be saved.
        size (int): The size of the triangle.
        traits_cur (sqlite3.Cursor): The cursor for the traits database.
        oeis_cur (sqlite3.Cursor): The cursor for the OEIS database.
        table (str): The name of the triangle.

    Raises:
        Exception: If there is an error while saving the extended traits to the database.

    Returns:
        None
    """

    Tid = fun.id
    fun.id = fun.id + ":Std"

    TRAITS = RegisterTraits()

    thash = FNVhash(fun.flat(DIAGSIZE))
    SaveTraits(fun, size, traits_cur, oeis_cur, table, TRAITS)
    fun.id = Tid

    a = AltTable(fun, DIAGSIZE)
    SaveTraits(a, size, traits_cur, oeis_cur, table, TRAITS)

    r = RevTable(fun, DIAGSIZE)
    rhash = FNVhash(r.flat(DIAGSIZE))
    if thash != rhash:
        SaveTraits(r, size, traits_cur, oeis_cur, table, TRAITS)

        # ir = InvRevTable(t, DIAGSIZE)
        ir = InvTable(r, DIAGSIZE)
        if ir is not None:
            SaveTraits(ir, size, traits_cur, oeis_cur, table, TRAITS)

    i = InvTable(fun, DIAGSIZE)
    ihash = "0"
    if i is not None:
        ihash = FNVhash(i.flat(DIAGSIZE))
        SaveTraits(i, size, traits_cur, oeis_cur, table, TRAITS)

        # ri = RevInvTable(t, DIAGSIZE)
        ri = RevTable(i, DIAGSIZE)
        if ri is not None:
            rihash = FNVhash(ri.flat(DIAGSIZE))
            if ihash != rihash:
                SaveTraits(ri, size, traits_cur, oeis_cur, table, TRAITS)


def SaveTraitsToDB(fun: tgen) -> None:
    """
    Saves the traits of a triangle to a SQLite database.

    Args:
        fun (tgen): The triangle whose traits are to be saved.

    Raises:
        Exception: If there is an error while saving the traits to the database.

    Returns:
        None
    """
    name = fun.id
    with sqlite3.connect(GetDataPath(name, "db")) as db:
        traits_cur = db.cursor()
        traits_cur.execute(CreateTable(name))

        with sqlite3.connect(GetDataPath("oeismini", "db")) as oeis:
            oeis_cur = oeis.cursor()
            SaveExtendedTraitsToDB(fun, MINROWS, traits_cur, oeis_cur, name)

        db.commit()

    print(f"Info: Created database {name}.db in data/db.")


def ConvertLocalDBtoCSVandMD() -> None:
    """
    This function converts the data from the SQLite database into CSV and Markdown formats.

    The function performs the following steps:
    1. Connects to the SQLite database.
    2. Retrieves all the data from the 'sequences' table.
    3. Writes the data into a CSV file.
    4. Generates a Markdown table from the data and writes it into a Markdown file.

    Note: The function assumes the existence of the 'GetDataPath' function,
    which returns the path to the data files.

    Raises:
        Exception: If there is an error during the execution of the function.
    """
    try:
        # Connect to the database
        with sqlite3.connect(GetDataPath("oeismini", "db")) as conn:
            cur = conn.cursor()

            # Retrieve all data from the 'sequences' table
            cur.execute("SELECT * FROM sequences")
            data = cur.fetchall()

            # Write the data into a CSV file
            csvpath = GetDataPath("oeismini", "csv")
            with open(csvpath, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["hash", "anum", "seq"])
                writer.writerows(data)

            # Generate a Markdown table from the data
            mdpath = GetDataPath("oeismini", "md")
            with open(mdpath, "w") as mdfile:
                mdfile.write("| hash | anum | seq |\n")
                mdfile.write("|------|------|-----|\n")
                for row in data:
                    mdfile.write(f"| {row[0]} | {row[1]} | {row[2]} |\n")

        print(f"Converted database to CSV ({csvpath}) and Markdown ({mdpath}).")
    except Exception as e:
        print(f"Error: {str(e)}")


def ConvertDBtoCSVandMD(dbpath: Path, funname: str) -> int:
    """
    Converts a SQLite database to CSV and Markdown files.

    Args:
        dbpath (str): The path to the SQLite database.
        funname (str): The name of the triangle.

    Returns:
        int: The size of the converted table.

    Raises:
        Exception: If there is an error converting the database.
    """
    size = 0
    with sqlite3.connect(dbpath) as db:
        cursor = db.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor.execute(sql)
        tables = cursor.fetchall()
        for table_name in tables:
            table_name = table_name[0]
            sql = f"SELECT triangle, type, trait, anum, seq FROM {table_name}"
            table = pd.read_sql_query(sql, db)
            csv_path = GetDataPath(table_name, "csv")
            md_path = GetDataPath(table_name, "md")
            table.to_csv(csv_path, index_label="index")
            table.to_markdown(md_path)
            size = table.size // 4
        cursor.close()

    print(f"Info: Created data/csv/{funname}.csv and data/md/{funname}.md.")
    return size


def SaveAllTraitsToDBandCSVandMD(tabl_fun: list[tgen]) -> None:
    """
    Saves all traits to a database, a CSV file, and Markdown file.

    This function iterates over a list of tabl_fun objects and performs the following actions for each object:
    1. Saves the traits to a database using the SaveTraitsToDB function.
    2. Converts the database file to CSV and Markdown formats using the ConvertDBtoCSVandMD function.

    Args:
        tabl_fun (list[tgen]): A list of tabl_fun objects.

    Returns:
        None
    """
    for fun in tabl_fun:
        SaveTraitsToDB(fun)
        ConvertDBtoCSVandMD(GetDataPath(fun.id, "db"), fun.id)


def MergeAllDBs(tablfun: list[tgen]):
    """
    Merge all SQLite databases into a single database.

    Args:
        tablfun (list[tgen]): List of triangles.

    Raises:
        Exception: If there is an error during the merging process.
    """
    destname = "traits"
    destpath = GetDataPath(destname, "db")
    with sqlite3.connect(destpath) as dest:
        dest_cursor = dest.cursor()
        dest_cursor.execute(CreateTable(destname))
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
                    sql = InsertTable(destname)
                    dest_cursor.executemany(sql, trs)
                src_cursor.close()
        dest.commit()
        dest_cursor.close()
    print("Info: Created database traits.db in data/db.")


if __name__ == "__main__":
    from tabl import tabl_fun
    # from Binomial import Binomial

    def test1():
        oeis_con = sqlite3.connect(GetDataPath("oeismini", "db"))
        oeis_cur = oeis_con.cursor()
        res = oeis_cur.execute("SELECT hash, seq FROM sequences ORDER BY hash")
        hash, seq = res.fetchone()
        print(f"The highest hash is {hash!r}, which is sequence {seq}")
        oeis_con.commit()
        oeis_con.close()

    def test2():
        oeis_con = sqlite3.connect(GetDataPath("oeismini", "db"))
        oeis_cur = oeis_con.cursor()
        res = oeis_cur.execute("SELECT hash, anum, seq FROM sequences ORDER BY hash")
        output = res.fetchmany(5)
        for seq in output:
            print("hash: {0} anum: {1} seq: {2}.".format(*seq))
        oeis_con.commit()
        oeis_con.close()

    def test22(hash: str):
        oeis_con = sqlite3.connect(GetDataPath("oeismini", "db"))
        oeis_cur = oeis_con.cursor()
        res = oeis_cur.execute(f"SELECT hash, anum, seq FROM sequences WHERE hash='{hash}'")
        output = res.fetchone()
        print(output)
        oeis_con.commit()
        oeis_con.close()

    def test3():
        oeis_con = sqlite3.connect(GetDataPath("oeismini", "db"))
        oeis_cur = oeis_con.cursor()
        sql = "SELECT hash, anum, seq FROM sequences ORDER BY anum"
        res = oeis_cur.execute(sql)
        output = res.fetchmany(5)
        for seq in output:
            print("anum: {1} hash: {0} seq: {2}.".format(*seq))
        oeis_con.commit()
        oeis_con.close()

    def test7():
        from Abel import Abel
        SaveTraitsToDB(Abel)

    def test77():
        from BinomialDiffPell import BinomialDiffPell
        SaveTraitsToDB(BinomialDiffPell)

    def test99():
        for fun in tabl_fun:
            size = ConvertDBtoCSVandMD(GetDataPath(fun.id, "db"), fun.id)
            print(f"{size} sequences for {fun.id} identified.")

    def test9():
        MergeAllDBs(tabl_fun)


    def test33():
        from tabl import CTree as triangle
        # from tabl import CentralE, CentralO
        # T = triangle.tab(32)
        F = triangle.flat(MINROWS)
        cthash = FNVhash(F, True)

        # ce = CentralE(T)
        # cehash = FNVhash(ce, True)
        # print(cehash, ce)

        # co = CentralO(T)
        # cohash = FNVhash(co, True)
        # print(cohash, co)

        with sqlite3.connect(GetDataPath("oeismini", "db")) as oeis:
            res = DebugQueryOeis(cthash, F, oeis.cursor())
            print("Test returns anum", res)

        print(cthash, ",FNVhash")

    # OeisToSql()
    # test33()
