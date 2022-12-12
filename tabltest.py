from codetiming import Timer
from pathlib import Path
from tabl import PrintViews, PrintExtendedProfile, PrintProfile, SaveExtendedProfiles, SaveProfiles, SaveTables, SaveExtendedTables, sortfile, tabl_fun, SimilarTriangles


if __name__ == "__main__":

    path = Path(__file__).parent
    relprofpath = 'data/profiles.csv'
    relsortpath = 'data/sortedprofiles.csv'
    propath = (path / relprofpath).resolve()
    sorpath = (path / relsortpath).resolve()


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
        path = Path(__file__).parent
        relshortdatapath = 'data/short_data.csv'
        shortdatapath = (path / relshortdatapath).resolve()
        SimilarTriangles(shortdatapath)


    def test5() -> None:
        @Timer()
        def time_me() -> None:
            SaveExtendedTables()
        time_me()


    def main(test: int) -> None:
        print("... bussy")
        match test:
            case 1: test1()
            case 2: test2()
            case 3: test3()
            case 4: test4()
            case 5: test5()
        print("Done")

    main(2)
