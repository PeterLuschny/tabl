"""
This module provides functionality to query the OEIS (Online Encyclopedia of Integer Sequences) 
for a given sequence and determine if it is present in the database. 

  QueryOEIS(seqlist: list[int], maxnum: int = 1, info: bool = False, minlen: int = 24) -> int:
    Queries the OEIS for a given sequence to check if it is present in the database.
      maxnum: Maximum number of sequences to be returned. Defaults to 1.
      info: If True, prints details; otherwise, is quiet except for warnings. Defaults to False.
      minlen: Minimum length of the sequence required for the query. Defaults to 24.
      The A-number of the sequence if found, 0 if the sequence was not found, 
      or -999999 if the OEIS server cannot be reached.

The module also includes a function to find the longest common substring between two strings. 
The function 'lcsubstr' is CC BY-SA 4.0 and taken from the Algorithm Implementation Wikibook.
https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring
"""

import time
from typing import TypeAlias
import requests
from requests import get
from _tabltypes import SeqToString


oeis_schema = '''{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "array",
    "items": [
      {
        "type": "object",
        "properties": {
          "greeting": {
            "type": "string"
          },
          "query": {
            "type": "string"
          },
          "count": {
            "type": "integer"
          },
          "start": {
            "type": "integer"
          },
          "results": {
            "type": "array",
            "items": [
              {
                "type": "object",
                "properties": {
                  "number": {
                    "type": "integer"
                  },
                  "id": {
                    "type": "string"
                  },
                  "data": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "comment": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "reference": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "link": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "formula": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "maple": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "mathematica": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "program": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "xref": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "keyword": {
                    "type": "string"
                  },
                  "offset": {
                    "type": "string"
                  },
                  "author": {
                    "type": "string"
                  },
                  "ext": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "references": {
                    "type": "integer"
                  },
                  "revision": {
                    "type": "integer"
                  },
                  "time": {
                    "type": "string"
                  },
                  "created": {
                    "type": "string"
                  }
                }
              }
            ]
          }
        }
      }
    ]
  }'''

OEISdata: TypeAlias = dict[str, int | str | list[str] ]

testdata: dict[str, int | str | list[str] ] = {"number": 367025, "data": "1,4,1,9,9,2,16,36,32,5,25,100,200,125,14,36,225,800,1125,504,42,49,441,2450,6125,6174,2058,132,64,784,6272,24500,43904,32928,8448,429,81,1296,14112,79380,222264,296352,171072,34749,1430", "name": "Triangle read by rows, T(n, k) = [x^k] p(n), where p(n) = (1 - hypergeom([-1/2, -n - 1, -n - 1], [1, 1], 4*x)) / (2*x).", "formula": ["T(n,k) = binomial(n+1,n-k)^2*binomial(2*k,k)/(k+1). - _Detlef Meya_, Nov 19 2023"], "example": ["Triangle T(n, k) starts:", "  [0]   1;", "  [1]   4,    1;", "  [2]   9,    9,     2;", "  [3]  16,   36,    32,      5;", "  [4]  25,  100,   200,    125,     14;", "  [5]  36,  225,   800,   1125,    504,      42;", "  [6]  49,  441,  2450,   6125,   6174,    2058,     132;", "  [7]  64,  784,  6272,  24500,  43904,   32928,    8448,    429;", "  [8]  81, 1296, 14112,  79380, 222264,  296352,  171072,  34749,   1430;", "  [9] 100, 2025, 28800, 220500, 889056, 1852200, 1900800, 868725, 143000, 4862;"], "maple": ["p := n -> (1 - hypergeom([-1/2, -n-1, -n-1], [1, 1], 4*x)) / (2*x):", "T := (n, k) -> coeff(simplify(p(n)), x, k):", "seq(seq(T(n, k), k = 0..n), n = 0..9);"], "mathematica": ["T[n_,k_]:=Binomial[n+1,n-k]^2*Binomial[2*k,k]/(k+1);Flatten[Table[T[n,k],{n,0,9},{k,0,n}]] (* _Detlef Meya_, Nov 19 2023 *)"], "xref": ["Cf. A000290 (first column), A000108 (main diagonal).", "Cf. A367022, A367023, A387024."], "keyword": "nonn,tabl", "offset": "0,2", "author": "_Peter Luschny_, Nov 07 2023", "references": 0, "revision": 14, "time": "2023-11-20T11:52:33-05:00", "created": "2023-11-07T14:43:14-05:00"}

# #@


def lcsubstr(s: str, t: str) -> tuple[int, int]: 
    """
    With CC BY-SA 4.0 from: https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring
    Finds the longest common substring of s and t that is contiguous.
    Args:
      s: The first string.
      t: The second string.
    Returns:
        (s, l): The matched substring starts at index 's' in the first string and has length 'l'.
    """
    m = [[0] * (1 + len(t)) for _ in range(1 + len(s))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s)):
        for y in range(1, 1 + len(t)):
            if s[x - 1] == t[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    # lcs_str =  s[x_longest - longest : x_longest] 
    return (x_longest - longest, longest)


def QueryOEIS(
        seqlist: list[int], 
        maxnum: int = 1,
        info: bool = False, 
        minlen: int = 24 
    ) -> int:
    """
    Query if a given sequence is present in the OEIS. At least 24 terms 
    of the sequence must be given. The first three terms and signs are disregard. 
    Sequences with huge terms might have to few terms to give reliable results. 
    This is a heuristic function, understand it's limited reach.

    Args:
        seqlist: The sequence to search. Must have at least 24 terms.

        maxnum: max number of sequences to be returned. Defaults to 1.

        info: Prints details, otherwise is quiet except for warnings. Defaults to False.
        
        minlen: At least {minlen} terms are required.

    Returns:
        Returns anum is the A-number of the sequence, 
        Returns 0 if the sequence was not found.
        If sl < 5 and dl > 12, then anum probably matches the sequence,
        modulo a couple of first terms and the signs.

    Raises:
        Exception: If the OEIS server cannot be reached after multiple attempts.
        Currently, the function will return -999999 if the OEIS server cannot be reached
        or if the sequence has only zeros.
    """
    if len(seqlist) < minlen:
      print(f"Sequence is too short! We require at least {minlen} terms.")
      print("You provided:", seqlist)
      return 0

    # Warning. These 'magical' constants are very sensible!
    if 0 == sum(seqlist[0:36]): return -999999  # XXXXX dont search for the all zeros sequence
    off = 0 if 0 == sum(seqlist[3:36]) else 3   # XXXXX dont skip leading terms if the rest is zero
    seqstr = SeqToString(seqlist, 160, 36, ",", off, True)
    url = f"https://oeis.org/search?q={seqstr}&fmt=json"

    for repeat in range(3):
        time.sleep(0.5)  # give the OEIS server some time to relax
        if info: print(f"[{repeat}]")
        try:
            # jdata: None | list[dict[str, int | str | list[str] ]] = get(url, timeout=20).json()
            jdata = get(url, timeout=20).json()
            if jdata == None:
                if 0 == sum(seqlist[::2]) or 0 == sum(seqlist[1::2]): 
                    seqlist = [k for k in seqlist if k != 0]
                    seqstr = SeqToString(seqlist, 160, 36, ",", 3, True)
                    if info:
                        print("Searching without zeros:", seqstr)
                    url = f"https://oeis.org/search?q={seqstr}&fmt=json"
                    raise ValueError('Try again')
                if info:
                    print("Sorry, no match found for:", seqstr)
                return 0

            number = dl = ol = 0
            for j in range(min(maxnum, len(jdata))):
                seq = jdata[j]
                number = seq["number"]
                anumber = f"A{(6 - len(str(number))) * '0' + str(number)}"
                name = seq["name"]
                data = seq["data"].replace('-', '')         # type: ignore
                seqstr = SeqToString(seqlist, 160, 25, ",", 0, True)
                start, length = lcsubstr(data, seqstr)      # type: ignore
                ol = data.count(",")                        # type: ignore
                sl = data.count(",", 0, start)              # type: ignore
                dl = data.count(",", start, start + length) # type: ignore
                if dl < 12:
                    print(f"\n*** WARNING! Only {dl} out of {ol} terms match! ***\n")
                if info or dl < 12:
                    print("You searched:", seqstr)
                    print("OEIS-data is:", data)          # type: ignore
                    # print(f"Starting at index {sl} the next {dl} consecutive terms match. The matched substring starts at {start} and has length {length}.")
                    print("***Found:", anumber, name)
                if dl > 12:
                    break

            return int(number)  

        except ValueError: 
            continue
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    #raise Exception(f"Could not open {url}.")
    print(f"Exception! Could not open {url}.")
    return -999999


if __name__ == "__main__":
    from tabl import tabl_fun # type: ignore

    data0 = [1, 1, 0, 0, 0, 0, 0, 0]
    data1 = [1, 4, 1, 9, 9, 2, 16, 36]
    data2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,17,19,20,21,22,23,24,25,26,27]
    data3 = [36,32,5,25,100,200,125,14,36,225,800,1125,504,42,49,441,2450,6125,6174,2058,132,64,784,6272]
    data4 =[1,0,1,0,2,0,2,0,4,0,4,0,8,0,10,0,20,0,30,0,56,0,94,0,180,0,316,0,596,0, 1096,0,2068,0,3856,0]

    def test() -> None:
        print(QueryOEIS(data1, 1, True)); print()
        print(QueryOEIS(data2, 1, True)); print()
        print(QueryOEIS(data3, 1, True)); print()

    def testQuerySum() -> None:
        for tab in tabl_fun[:5]:
            print(f"Searching row sums of {tab.id} {tab.sim}.")
            sumlist = [tab.sum(n) for n in range(30)]
            anum = QueryOEIS(sumlist)
            print('A' + str(anum).rjust(6, "0"))

    #test()
    #testQuerySum()
    
    off = 0 if 0 == sum(data0[3::]) else 3
    print(data0[off:])
    
'''

https://oeis.org/search?q=5,3,4,9,5,6,13,7,8,17,9,10,21,11,12,25,13,14,29,15,16,33,17,18,37,19,20,41,21,22,45,23,24,49,25,26,&fmt=json.
5,3,4,9,5,6,13,7,8,17,9,10,21,11,12,25,13,14,29,15,16,33,17,18,37,19,20,41,21,22,45,23,24,49,25,26,
https://oeis.org/search?q=4,8,4,6,12,6,8,16,8,10,20,10,12,24,12,14,28,14,16,32,16,18,36,18,20,40,20,22,44,22,24,48,24,26,52,26,&fmt=json.  
4,8,4,6,12,6,8,16,8,10,20,10,12,24,12,14,28,14,16,32,16,18,36,18,20,40,20,22,44,22,24,48,24,26,52,26,&fmt=json.  
https://oeis.org/search?q=6,4,4,10,6,6,14,8,8,18,10,10,22,12,12,26,14,14,30,16,16,34,18,18,38,20,20,42,22,22,46,24,24,50,26,26,&fmt=json.
6,4,4,10,6,6,14,8,8,18,10,10,22,12,12,26,14,14,30,16,16,34,18,18,38,20,20,42,22,22,46,24,24,50,26,26,&fmt=json.

'''