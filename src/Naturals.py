from functools import cache
from tabl import MakeTriangle, PrintProfile 

"""
This is a demo of the most primitive use of the 'tabl' module.

The function 'natural' computes the n-th row of a regular integer
triangle. It has to be defined for n >= 0.
"""

@cache
def naturals(n: int):
    R = range((n * (n + 1)) // 2, ((n + 1) * (n + 2)) // 2)
    return [i + 1 for i in R]


@MakeTriangle(naturals, "Naturals", ['A000027', 'A001477'], True)
def Naturals(n: int, k: int) -> int:
    return naturals(n)[k]


if __name__ == "__main__":
    PrintProfile(Naturals) 
