from codetiming import Timer

from tabl import PrintViews, PrintExtendedProfile, PrintProfile,  SaveExtendedProfiles, SaveProfiles, SaveTables, SaveExtendedTables, sortfile, tabl_fun


if __name__ == "__main__":

# 4239 1960

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

        #SaveProfiles(True)
        #sortfile()

        SaveExtendedProfiles()
        sortfile()

    '''About 12000 meaningful sequences in less than 4 seconds.'''
    @Timer()
    def time_me() -> None:
        SaveExtendedTables()

    #test1()
    time_me()

