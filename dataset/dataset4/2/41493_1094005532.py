from sys import *
n = 30000
setrecursionlimit(n+1)

def nofact(n):
    if n==1: 
        return 1
    return nofact(n-1)

nofact(n)