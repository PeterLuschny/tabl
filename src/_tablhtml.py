import csv
from pathlib import Path
from _tabltypes import tgen
from _tablpaths import GetCsvPath, GetHtmlPath
from tabl import tabl_fun

# #@

def GetFormulas() -> dict[str, str]:
    FORMULA: dict[str, str] = {}

    FORMULA['Tabl']         = 'T(n, k), 0 &le; k &le; n'
    FORMULA['RevTabl']      = 'T(n, n - k), 0 &le; k &le; n'
    FORMULA['InvTabl']      = 'T<sup>-1</sup>(n, k), 0 &le; k &le; n'
    FORMULA['RevInvTabl']   = 'T<sup>-1</sup>(n, n - k), 0 &le; k &le; n'
    FORMULA['InvRevTabl']   = '(T(n, n - k))<sup>-1</sup>, 0 &le; k &le; n'
    FORMULA['AccTabl']      = 'see docs'
    FORMULA['RevAccTabl']   = 'see docs'
    FORMULA['AccRevTabl']   = 'see docs'
    FORMULA['AntiDiagTabl'] = 'see docs'
    FORMULA['BinTabl']      = 'see docs'
    FORMULA['InvBinTabl']   = 'see docs'
    FORMULA['DiffxTabl']    = 'T(n, k) (k+1)'
    FORMULA['RowSum']       = '&sum;<sub> k=0..n </sub> T(n, k)'
    FORMULA['EvenSum']      = '&sum;<sub> k=0..n </sub> T(n, k) even(k)'
    FORMULA['OddSum']       = '&sum;<sub> k=0..n </sub> T(n, k) odd(k)'
    FORMULA['AltSum']       = '&sum;<sub> k=0..n </sub> T(n, k) (-1)^k'
    FORMULA['AntiDiagSum']  = '&sum;<sub> k=0..n // 2 </sub> T(n - k, k)'
    FORMULA['AccSum']       = '&sum;<sub> k=0..n </sub>&sum;<sub> j=0..k </sub> T(n, j)'
    FORMULA['AccRevSum']    = '&sum;<sub> k=0..n </sub>&sum;<sub> j=0..k </sub> T(n, n - j)'
    FORMULA['RowLcm']       = 'Lcm<sub> k=0..n </sub> | T(n, k) | &gt; 1'
    FORMULA['RowGcd']       = 'Gcd<sub> k=0..n </sub> | T(n, k) | &gt; 1'
    FORMULA['RowMax']       = 'Max<sub> k=0..n </sub> | T(n, k) |'
    FORMULA['ColMiddle']    = 'T(n, n // 2)'
    FORMULA['ColECentral']  = 'T(2 n, n)'
    FORMULA['ColOCentral']  = 'T(2 n + 1, n)'
    FORMULA['ColLeft']      = 'T(n, 0)'
    FORMULA['ColRight']     = 'T(n, n)'
    FORMULA['BinConv']      = '&sum;<sub> k=0..n </sub> C(n, k) T(n, k)'
    FORMULA['InvBinConv']   = '&sum;<sub> k=0..n </sub> C(n, k) T(n, n - k) (-1)^k'
    FORMULA['TransSqrs']    = '&sum;<sub> k=0..n </sub> T(n, k) k^2'
    FORMULA['TransNat0']    = '&sum;<sub> k=0..n </sub> T(n, k) k'
    FORMULA['TransNat1']    = '&sum;<sub> k=0..n </sub> T(n, k) (k + 1)^k'
    FORMULA['DiagRow1']     = 'T(n + 1, n)'
    FORMULA['DiagRow2']     = 'T(n + 2, n)'
    FORMULA['DiagRow3']     = 'T(n + 3, n)'
    FORMULA['DiagCol1']     = 'T(n + 1, 1)'
    FORMULA['DiagCol2']     = 'T(n + 2, 2)'
    FORMULA['DiagCol3']     = 'T(n + 3, 3)'
    FORMULA['PolyTabl']     = 'see docs'
    FORMULA['PolyRow1']     = '&sum;<sub> k=0..1 </sub>T(1, k) n^k'
    FORMULA['PolyRow2']     = '&sum;<sub> k=0..2 </sub>T(2, k) n^k'
    FORMULA['PolyRow3']     = '&sum;<sub> k=0..3 </sub>T(3, k) n^k'
    FORMULA['PolyCol2']     = '&sum;<sub> k=0..n </sub>T(n, k) 2^k'
    FORMULA['PolyCol3']     = '&sum;<sub> k=0..n </sub>T(n, k) 3^k'
    FORMULA['PolyDiag']     = '&sum;<sub> k=0..n </sub>T(n, k) n^k'
    FORMULA['PosHalf']      = '&sum;<sub> k=0..n </sub>2^n T(n, k) (1/2)^k'
    FORMULA['NegHalf']      = '&sum;<sub> k=0..n </sub>(-2)^n T(n, k) (-1/2)^k'

    return FORMULA


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
    "#rcor1 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 40px; height: 0px;} ",
    "#rcor2 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 550px; height: 0px;} ",
    "#rcor3 {border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 88px; height: 20px; font-weight: 700; text-align: center;} ",
    ".center {margin-top: 1em;} ",
    ".tooltip { position: relative; display: inline-block; font-weight: 600;} ",
    ".tooltip .formula { visibility: hidden; width: 200px; background-color: lightgray; text-align: center; border-radius: 6px; padding: 5px 0; position: absolute; z-index: 1; top: +2px; left: 105%;} ",
    ".tooltip:hover .formula { visibility: visible; } ",
    "</style></head><body>"]

 
Table = [ "<table class='sortable'><thead><tr>",
    "<th id='rcor1'>&#8597; Trait</th>",
    "<th id='rcor1'>&#8597; A</th>",
    "<th id='rcor2'>Sequence</th>",
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
        s += "[{n}] " + str(fun.gen(n)).replace("[", "").replace("]", "") + "<br>"
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


def CsvToHtml(fun: tgen, csvpath: Path, outpath: Path) -> None:

    name = fun.id

    # csvfile = (csvpath / (name + "X.csv")).resolve()
    csvfile = (csvpath / (name + ".csv")).resolve()
    outfile = (outpath / (name + ".html")).resolve()

    FORMULA = GetFormulas()

    with open(csvfile, 'r') as csvfile:
        reader = csv.reader(csvfile)

        with open(outfile, 'w') as outfile:

            for l in Header: outfile.write(l)
            outfile.write(f"<title>{name} : IntegerTriangles.py</title>")
            for l in CSS: outfile.write(l)

            l = next(reader)  # column names
            sim = str(fun.sim).replace("'", "").replace("[", "").replace("]", "")

            outfile.write(f"<div class='tooltip' style='border-radius: 15px; background: #73AD21; color: white; padding: 6px; width: 160px; height: 20px; font-weight: 700; text-align: center;'>{name.upper()}<span class='formula' style=' background: #73AD21; font-weight:600; width: 220px;'>{HtmlTriangle(fun)}</span></div>")


            outfile.write(f"<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OEIS Similars: {sim}\n</p>")


            for l in Table: outfile.write(l)

            for line in reader:
                if line[0][0] == '#': continue
                if line[3] == '[]' : continue

                # trait
                l2 = line[2]
                tip = FORMULA[l2]
                if "Tabl" in l2:
                    l2 = '&#916;' + l2.replace('Tabl', '')

                outfile.write(f"<tr><td class='tooltip'>{l2}<span class='formula'>{tip}</span></td>")

                seq = line[3].replace('[', '').replace(' ]', '')

                # Anum
                if line[1] == '':
                    sep = seq.replace(' ', '+')
                    #outfile.write(f"<td><a href='https://oeis.org/?q={seq}&sort=&#language=&go=search' target='_blank'>search</a></td>")
                    outfile.write(f"<td style='text-align:center;'><a href='http://sequencedb.net/index.html?s={sep}' target='_blank'>search</a></td>")
                else:
                    outfile.write(f"<td><a href='https://oeis.org/{line[1]}'>{line[1]}</a></td>")

                # seq
                outfile.write(f"<td>{seq}</td></tr>")

            outfile.write("</tbody></table>")

            for l in navbar(fun): 
                outfile.write(l)

            for l in Footer: 
                outfile.write(l)

            for l in SCRIPT:
                outfile.write(l)


def AllCsvToHtml(csvpath: Path = GetCsvPath(), outpath: Path = GetHtmlPath()) -> None:
    for fun in tabl_fun:
        CsvToHtml(fun, csvpath, outpath)


if __name__ == "__main__":

    from Abel import Abel
    from CatalanSqr import CatalanSqr
    from PowLaguerre import PowLaguerre
    #CsvToHtml(Abel, GetCsvPath(), GetHtmlPath())

    AllCsvToHtml()

    #for n in range(10):
    #    print(Abel.gen(n))
    #    print(str(Abel.gen(n))) 

    print("Done ...")
