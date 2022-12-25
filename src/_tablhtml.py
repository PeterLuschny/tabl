import csv
from tabl import tabl_fun

# #@

Header = [
"<!DOCTYPE html>",
"<html lang='en'><head><meta charset='UTF-8'/>",
"<meta name='viewport' content='width=device-width, initial-scale=1.0'/>"]

CSS = ["<head><style> table, td, th, p {border-collapse: collapse; font-family: sans-serif; color: blue;}",
    "td, th {border-bottom: 0; padding: 4px}", 
    "td {text-align: left}",
    "tr:nth-child(odd) {background: #eee;}", 
    "tr:nth-child(even) {background: #fff;}",
    "tr.header {background: orange !important; color: white; font-weight: bold;}",
    "tr.subheader {background: lightgray !important; color: black;}",
    "tr.headerLastRow {border-bottom: 2px solid black;}",
    "th.rowNumber, td.rowNumber {text-align: right;}",
    "a {text-decoration: none; color:brown;} </style></head><body>"]


Table = [ "<table>",
    "<tr class = 'header headerLastRow'>",
    "<th style = 'text-align: left;'>Trait</th>",
    "<th style = 'text-align: left;'>ANumber</th>",
    "<th style = 'text-align: left;'>Sequence</th>",
    "</tr>" ]

Footer = [
    "Note: The A-numbers are based on a finite number of numerical comparisons.",
    "They ignore the offset and the sign, and might differ in the first few values.&nbsp;&nbsp;",
    "<a href='https://oeis.org'><i>Go to the index.<i></a>",
    "<p>&nbsp;</p>"
    "</body></html>" ]

def CsvToHtml(csvpath, outpath) -> None:

    for fun in tabl_fun:

        name = fun.id
        csvfile = (csvpath / (name + ".csv")).resolve()
        outfile = (outpath / (name + ".html")).resolve()

        with open(csvfile, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # skip the first row

            with open(outfile, 'w') as outfile:

                for l in Header: outfile.write(l)
                outfile.write(f"<title>{name} : IntegerTriangles.py</title>")
                for l in CSS: outfile.write(l)

                l = next(reader)  
                outfile.write(f"<p><b>{name.upper()}</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{l[0]}\n</p>")

                for l in Table: outfile.write(l)

                for line in reader:
                    if line[0][0] == '#': break

                    outfile.write(f"<tr><td><b>{line[1]}</b></td>")
                    outfile.write(f"<td><a href='https://oeis.org/{line[2]}'>{line[2]}</a></td>")
                    outfile.write(f"<td>{line[3]}</td></tr>")

                outfile.write(f"</table><p>{line[1]}, {line[2]}, ({line[3]}).</p>")
                for l in Footer: outfile.write(l)



if __name__ == "__main__":

    from pathlib import Path

    path = Path(__file__).parent.parent
    relprofpath = 'data/profiles.csv'
    relsortpath = 'data/sortedprofiles.csv'
    relshortdatapath = 'data/short_data.csv'
    reldatapath = 'data/oeis_data.csv'

    propath = (path / relprofpath).resolve()
    sorpath = (path / relsortpath).resolve()
    shortdatapath = (path / relshortdatapath).resolve()
    datapath = (path / reldatapath).resolve()

    relcsvpath = 'data/csv'
    csvpath = (path / relcsvpath).resolve()

    relhtmlpath = 'data/html'
    htmlpath = (path / relhtmlpath).resolve()

    CsvToHtml(csvpath, htmlpath)
    print("Done ...")