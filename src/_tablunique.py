import sqlite3
from _tabldata import GetNameByAnum
from _tablstatistic import setLength
from _tablpaths import GetDataPath

# #@


def CountDoublicates(table_name: str) -> list:
    oeis_con = sqlite3.connect(GetDataPath(table_name, "db"))
    oeis_cur = oeis_con.cursor()
    sql = f"SELECT COUNT(anum), anum, GROUP_CONCAT(type, ','), GROUP_CONCAT(trait, ','), seq FROM {table_name} WHERE anum IS NOT 'missing' GROUP BY anum ORDER BY COUNT(anum) DESC, anum"
    res = oeis_cur.execute(sql)
    ret = res.fetchall()
    oeis_con.commit()
    oeis_con.close()
    return ret


def PrintDetails(name: str):
    CD = CountDoublicates(name)
    for cd in CD[:-1]:
        z = [f"{a}-{b}" for a, b in zip(cd[2].split(','), cd[3].split(','))]
        print(cd[0], cd[1], z)
        print("         ", setLength(GetNameByAnum(cd[1]), 90))
        print("         ", cd[4])
        print()


if __name__ == "__main__":
    PrintDetails("Abel")


'''
<style>details[open]{background: black; color: white; max-width: 980px; margin-bottom: 1em;} </style></head>
<details open>
<summary>Further details:</summary>
<pre>
6 B000169 ['Std-RowMax', 'Std-DiagCol1', 'Alt-RowMax', 'Alt-DiagCol1', 'Rev-RowMax', 'Rev-DiagRow1']
          Number of labeled rooted trees with n nodes: n^(n-1)
          1 1 2 9 64 625 7776 117649 2097152 43046721 1000000000 25937424601 743008370688 23298085122481
</pre></details>
'''