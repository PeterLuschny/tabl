import requests
import gzip
from _tablpaths import strippedpath, datapath, oeispath

# #@


def get_compressed() -> None:
    oeisstripped = "https://oeis.org/stripped.gz"
    r = requests.get(oeisstripped, stream = True)

    with open(strippedpath, "wb") as local:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                local.write(chunk)

    with gzip.open(strippedpath, 'rb') as gz:
        with open(oeispath, 'wb') as da:
            da.write(gz.read())


def oeisabsdata() -> None:
    """Make all terms absolute."""

    with open(oeispath, "r") as oeisdata:
        with open(datapath, "w") as absdata:
            for seq in oeisdata:
                if not '#' in seq:
                    absdata.write(seq.replace("-", ""))


def GetOEISdata() -> None:
    get_compressed()
    oeisabsdata()


if __name__ == "__main__":

    #get_compressed()
    #oeisabsdata()
    GetOEISdata()
    print("Done")
