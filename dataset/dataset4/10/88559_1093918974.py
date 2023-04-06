import sys

def recurse(n: int) -> int:
    recurse(n)

sys.setrecursionlimit(2**16-1)

recurse(1000000)