from codetiming import Timer
from pathlib import Path
from tabl import PrintViews, PrintExtendedProfile, PrintProfile, SaveExtendedProfiles, SaveProfiles, SaveTables, SaveExtendedTables, sortfile, tabl_fun


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
           PrintExtendedProfile(fun, dim, 'nonames')
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

    @Timer()
    def time_me() -> None:
        SaveExtendedTables()
    # time_me()

    print("... bussy")
    test3()
    print("Done")
