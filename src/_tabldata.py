import requests
import gzip
from _tablpaths import strippedpath, datapath, oeispath

# #@

def fnv(data) -> int:
    """
    FNV-1a hash algorithm.
    """
    assert isinstance(data, bytes)

    hval = 0xCBF29CE484222325
    for byte in data:
        hval = hval ^ byte
        hval = (hval * 0x100000001B3) % 0x10000000000000000
    return hval


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
    print("OEIS data updated!")


if __name__ == "__main__":

    #GetOEISdata()
    print("Done")

    '''
    data = b"1 1 1 3 30 630 3780 207900 8108100 56756700 1929727800 "
    print(hex(fnv(data)))
    data = b"[1 1 6 84 600 145080 2167200 453138235200 319959556963200 "
    print(hex(fnv(data)))
    '''
