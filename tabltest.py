from codetiming import Timer
from pathlib import Path
from tabl import PrintViews, PrintExtendedProfile, PrintProfile, SaveExtendedProfiles, SaveProfiles, SaveTables, SaveExtendedTables, SaveAllToCsv, CsvToHtml, SimilarTriangles, sortfile, Traits, stirling_set, tabl_fun


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


    def test1() -> None:
        dim = 10
        format = 'twolines'

        for fun in tabl_fun:
           PrintViews(fun)
           # PrintExtendedProfile(fun, dim, 'nonames')
           PrintProfile(fun, dim, format)


    def test2() -> None:
        SaveTables()
        #SaveExtendedTables()


    def test3() -> None:
        SaveProfiles(propath)
        sortfile(propath, sorpath)
        #SaveExtendedProfiles(propath)
        #sortfile(propath, sorpath)
        print("The profiles are in", propath)


    def test4() -> None:
        SimilarTriangles(shortdatapath)


    def test5() -> None:
        @Timer()
        def time_me() -> None:
            SaveExtendedTables()
        time_me()


    def test6() -> None:
        Traits(stirling_set, 12)

    # This takes very long! It builds
    # the traitcards of all sequences.
    # def test7() -> None:
        # SaveAllToCsv()

    def test8() -> None:
        CsvToHtml(csvpath, htmlpath)


    def main(test: int) -> None:
        print("... bussy")
        match test:
            case 1: test1()
            case 2: test2()
            case 3: test3()
            case 4: test4()
            case 5: test5()
            case 6: test6()
            # case 7: test7()
            case 8: test8()
        print("Done")

    main(8)
