from functools import cache
from tabl import MakeTriangle, PrintProfile 

"""
This is a demo of the most primitive use of the 'tabl' environment.

The function 'demo' computes the n-th row of a regular integer
triangle. It has to be defined for n >= 0.
"""

@cache
def demo(n: int) -> list[int]:
    R = range((n * (n + 1)) // 2, ((n + 1) * (n + 2)) // 2)
    return [i + 1 for i in R]


@MakeTriangle(demo, "Demo", ['A000027', 'A001477'], False)
def Demo(n: int, k: int) -> int:
    return demo(n)[k]


if __name__ == "__main__":
    PrintProfile(Demo) 
