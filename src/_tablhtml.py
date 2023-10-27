import csv
from _tabltypes import tgen
from _tablpaths import GetDataPath
from _tabltraits import Formulas
from tabl import tabl_fun

# #@

Header = [
"<!DOCTYPE html>",
"<html lang='en'><head><meta charset='UTF-8'/>",
"<meta name='viewport' content='width=device-width, initial-scale=1.0'/>"
]

CSS = ["<style> body {font-family: 'Segoe UI', sans-serif;} ",
    "table, td, th, p { border-collapse: collapse; color: blue;} ",
    "td, th { border-bottom: 0; padding: 4px} ", 
    "td { text-align: left} ",
    "tr:nth-child(odd) { background: #eee;} ", 
    "tr:nth-child(even) { background: #fff;} ",
    "tr.header { background: orange !important; color: white; font-weight: 700;} ",
    "tr.subheader { background: lightgray !important; color: black;} ",
    "tr.headerLastRow { border-bottom: 2px solid black;} ",
    "th.rowNumber, td.rowNumber { text-align: right;} ",
    "a {text-decoration: none; color:brown;} ",
    "a:hover {background-color: #AFE1AF;} ",
    "#rcor1 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 60px; height: 0px;} ",
    "#rcor2 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 60px; height: 0px;} ",
    "#rcor3 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 60px; height: 0px;} ",
    "#rcor4 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 880px; height: 20px; font-weight: 700; text-align: center;} ",
    ".center {margin-top: 1em;} ",
    ".type { font-weight: 600;} ",
    ".tooltip { position: relative; font-weight: 600;} ",
    ".tooltip .formula { visibility: hidden; width: 200px; background-color: lightgray; text-align: center; border-radius: 6px; padding: 5px 0; position: absolute; z-index: 1; top: +2px; left: 95%;} ",
    ".tooltip:hover .formula { visibility: visible; } ",
    "</style></head><body>"]

# layout: index,triangle,trait,anum,seq
# 0,Abel:Std,FlatTabl,A137452,1 0 1 0 ...
Table = [ "<table class='sortable'><thead><tr>",
    "<th id='rcor1'>&#8597; Type</th>",
    "<th id='rcor2'>&#8597; Trait</th>",
    "<th id='rcor3'>&#8597; Anum</th>",
    "<th id='rcor4'>&#8597; Sequence</th>",
    "</tr></thead><tbody>" ]

SCRIPT = [ "\n<script>",
        "var table = document.querySelector('.massive')\n",
        "var tbody = table.tBodies[0]\n",
        "var rows = [].slice.call(tbody.rows, 0)\n",
        "var fragment = document.createDocumentFragment()\n",
        "for (var k = 0; k < 50; k++) {\n",
            "for (var i = 0; i < rows.length; i++) {\n",
                "fragment.appendChild(rows[i].cloneNode(true)) } }\n",
        "tbody.innerHTML = '' \n",
        "tbody.appendChild(fragment)\n",
        "</script> <script src='sortable.js'></script> <script>\n",
        "function prepareAdvancedTable() { \n",
            "var size_table = document.querySelector('.advanced-table')\n",
            "var rows = size_table.tBodies[0].rows\n",
            "for (let i = 0; i < rows.length; i++) { \n",
                "const date_element = rows[i].cells[2]\n",
                "const size_element = rows[i].cells[1]\n",
                "date_element.setAttribute('data-sort', date_element.innerText.replace",
                r"(/(\d+)\/(\d+)\/(\d+)/, '$3$1$2'))",
                "\nsize_element.setAttribute('data-sort', toBytes(size_element.innerText)) } }\n",
        "function toBytes(size) {",
            "const units = [, 'k', 'm', 'g', 't']\n",
            "const match = size.match"
            r"(/(\d+\.\d+|\d+)\s*([kmgt])b?/i)",
            "\nif (!match) return parseFloat(size)\n",
            "const [value, unit] = match.slice(1)\n",
            "const index = units.indexOf(unit.toLowerCase())\n",
            "return Math.round(parseFloat(value) * Math.pow(1024, index)) }\n",
        "prepareAdvancedTable()\n", "</script>\n" "<p>&nbsp;</p></body></html>"]

Footer = [
    "<p style='margin-left:8px'>Note: The A-numbers are based on a finite number of numerical comparisons.<br>",
    "They ignore the sign and the OEIS-offset, and might differ in the first few values.<br>"
    "Here the offset of all triangles is 0 and consequently also the offset of all sequences.</p>" ]


def HtmlTriangle(fun: tgen) -> str:
    s = ""
    for n in range(6):
        s += f"[{n}] " + str(fun.gen(n)).replace("[", "").replace("]", "") + "<br>"
    return s

funnames = [fun.id for fun in tabl_fun]

def getprevnext(funname: list[str]) -> tuple[str, str]:
    idx = funnames.index(funname)
    prev = idx - 1; succ = idx + 1;
    if idx == 0: prev = len(tabl_fun) - 1
    if idx == len(tabl_fun) - 1: succ = 0
    return (funnames[prev], funnames[succ])


def navbar(fun: tgen) -> list[str]:
    anums = ""
    for s in fun.sim:
        anums += "%7Cid%3A" + s

    prevnext = getprevnext(fun.id)
    rc = "style='border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 108px; height: 20px; font-weight: 700; text-align: center; margin-left: 8px; margin-right: 8px;'"
    NAVBAR = ["<table class='center'><tr>"]
    NAVBAR.append(f"<td {rc};><a style='color:white' href='https://luschny.de/math/oeis/{prevnext[0]}.html'>&nbsp;&lt;&lt;&nbsp;</a></td>")
    NAVBAR.append(f"<td {rc};><a style='color:white' href='https://github.com/PeterLuschny/tabl/blob/main/data/md/{fun.id}.md'>Table</a></td>")
    NAVBAR.append(f"<td {rc};><a style='color:white' href='https://github.com/PeterLuschny/tabl/blob/main/src/{fun.id}.py'>Source</a></td>")
    NAVBAR.append(f"<td {rc};><a style='color:white' href='https://oeis.org/search?q={anums}'>Similars</a></td>")
    NAVBAR.append(f"<td {rc};><a style='color:white' href='https://luschny.de/math/oeis/index.html'>Index</a></td>")
    NAVBAR.append(f"<td {rc};><a style='color:white' href='https://luschny.de/math/oeis/{prevnext[1]}.html'>&nbsp;&gt;&gt;&nbsp;</a></td>")
    NAVBAR.append("</tr></table>")
    return NAVBAR


def CsvToHtml(fun: tgen) -> None:

    name = fun.id

    csvfile = GetDataPath(name, 'csv')
    outfile = GetDataPath(name, 'html')

    FORMULA = Formulas()

    with open(csvfile, 'r') as csvfile:
        reader = csv.reader(csvfile)

        with open(outfile, 'a') as outfile:

            for l in Header: 
                outfile.write(l)  

            outfile.write(f"<title>{name} : IntegerTriangles.py</title>") 

            for l in CSS: 
                outfile.write(l)

            l = next(reader)  # column names
            sim = str(fun.sim).replace("'", "").replace("[", "").replace("]", "")

            outfile.write("<div class='tooltip' style='border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 160px; height: 20px; font-weight: 700; text-align: center;'>")
            outfile.write(f"{name.upper()}<span class='formula' style=' background: #73AD21; font-weight:600; width: 220px;'>{HtmlTriangle(fun)}</span></div>")
            outfile.write(f"<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OEIS Similars: {sim}\n</p>")


            for l in Table: 
                outfile.write(l) 

            for line in reader:

                # Layout: index,triangle,trait,anum,seq
                # 0,Abel:Std,FlatTabl,A137452,1 0 1 0 ...
                # index = line[0]
                l = line[1]
                type = l[l.index(':')+1:]
                trait = line[2]
                anum = line[3]
                seq = line[4]

                outfile.write(f"<tr><td class='type'>{type}</td>")

                if "Flat" in trait: trait = trait.replace('Flat', '')
                tip = FORMULA[trait]
                outfile.write(f"<td class='tooltip'>{trait}<span class='formula'>{tip}</span></td>") 

                # Anum
                if anum == '':  # this will not happen ?
                    outfile.write(f"<td><a href='https://oeis.org/?q={seq}&sort=&#language=&go=search' target='_blank'>search</a></td>") 
                    #outfile.write(f"<td style='text-align:center;'><a href='http://sequencedb.net/index.html?s={sep}' target='_blank'>search</a></td>")
                else:
                    outfile.write(f"<td><a href='https://oeis.org/{anum}'>{anum}</a></td>") 

                # seq
                outfile.write(f"<td style='font-family:Consolas'>{seq}</td></tr>") 

            outfile.write("</tbody></table>") 

            for l in navbar(fun): 
                outfile.write(l)

            for l in Footer: 
                outfile.write(l)

            for l in SCRIPT:
                outfile.write(l)


def AllCsvToHtml() -> None:
    for fun in tabl_fun:
        CsvToHtml(fun)


if __name__ == "__main__":

    from Abel import Abel
    from CatalanSqr import CatalanSqr
    
    # CsvToHtml(Abel)
    AllCsvToHtml()

    print("Done ...")
