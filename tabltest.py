from codetiming import Timer
from pathlib import Path
from tabl import PrintViews, PrintExtendedProfile, PrintProfile, SaveExtendedProfiles, SaveProfiles, SaveTables, SaveExtendedTables, GenerateAllCsvFiles, CsvToHtml, AllCsvToHtml, SimilarTriangles, sortfile, Traits, abel, tabl_fun


if __name__ == "__main__":

    path = Path(__file__).parent
    relprofpath = 'data/profiles.csv'
    relsortpath = 'data/sortedprofiles.csv'
    relshortdatapath = 'data/short_data.csv'
    propath = (path / relprofpath).resolve()
    sorpath = (path / relsortpath).resolve()
    shortdatapath = (path / relshortdatapath).resolve()
    reldatapath = 'data/oeis_data.csv'
    datapath = (path / reldatapath).resolve()
    relcsvpath = 'data/csv'
    csvpath = (path / relcsvpath).resolve()
    relhtmlpath = 'data/html'
    htmlpath = (path / relhtmlpath).resolve()


    def main(test: int) -> None:
        print("... bussy")

        match test:
            case 1: 
                dim = 10
                format = 'twolines'
                for fun in tabl_fun:
                    PrintViews(fun)
                    # PrintExtendedProfile(fun, dim, 'nonames')
                    PrintProfile(fun, dim, format)

            case 2: 
                SaveTables()
                #SaveExtendedTables()

            case 3: 
                SaveProfiles(propath)
                sortfile(propath, sorpath)
                #SaveExtendedProfiles(propath)
                #sortfile(propath, sorpath)
                print("The profiles are in", propath)

            case 4: 
                SimilarTriangles(shortdatapath)

            case 5: 
                SaveExtendedTables()

            case 6: 
                Traits(abel, 12)

            case 7: 
                GenerateAllCsvFiles()

            case 8: 
                # CsvToHtml(abel, csvpath, htmlpath)
                AllCsvToHtml(csvpath, htmlpath)

        print("Done")

    main(8)
