from functools import cache

@cache
def catalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    
    pow = catalan(n - 1) + [0]
    row = pow.copy()
    for k in range(n - 1, 0, -1):
        row[k] = pow[k - 1] + 2 * pow[k] + pow[k + 1]
    row[n] = 1

    return row


if __name__ == "__main__":
    import sys

    sys.setrecursionlimit(3000)
    sys.set_int_max_str_digits(5000)
    print(sys.version_info, sys.getwindowsversion())
    print("Recursion limit is:", sys.getrecursionlimit())

    print(catalan(1000))

'''
OUTPUT WITH Python 3.12.0:

sys.version_info(major=3, minor=12, micro=0, releaselevel='final', serial=0) 
sys.getwindowsversion(major=10, minor=0, build=22000, platform=2, service_pack='')
Recursion limit is: 3000
Traceback (most recent call last):
  File "bug.py", line 27, in <module>
    catalan(1000)
  File "bug.py", line 10, in catalan
    pow = catalan(n - 1) + [0]
          ^^^^^^^^^^^^^^
  [Previous line repeated 496 more times]
RecursionError: maximum recursion depth exceeded

NOTE:
The above output is identical if the line sys.setrecursionlimit(3000)
is out-commented or not.

No problem with all Python versions < 12.0 which were tested.

OUTPUT WITH Python 3.11.6:

sys.version_info(major=3, minor=11, micro=6, releaselevel='final', serial=0) 
sys.getwindowsversion(major=10, minor=0, build=22000, platform=2, service_pack='')
Recursion limit is: 3000
'''
