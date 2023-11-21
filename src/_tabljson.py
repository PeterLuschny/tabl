from requests import get

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

# #@


def search(query: str) -> str:
    jdata = get(f"https://oeis.org/search?q={query}&fmt=json", timeout=10).json()
    count = jdata["count"]
    print(count)
    anumber = ""
    if count > 0:
        seq = jdata["results"][0]
        number = seq["number"]
        data = seq["data"]
        print(number)
        print(data)
        # [int(term) for term in data.split(",")]
        anumber = f"A{(6 - len(str(number))) * '0' + str(number)}"
        print(anumber)
    else:
        print("Sorry, nothing found!")
    return anumber


if __name__ == "__main__":
    seqs = search("1, 2, 3, 4, 5")
    seqs = search("1, 4, 1, 9, 9, 2, 16, 36,")
    seqs = search("9991, 2, 48323, 4, 0")
    print()
