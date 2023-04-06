import sys

sys.setrecursionlimit(18063)

def f():
    g()

def g():
    f()

f()
