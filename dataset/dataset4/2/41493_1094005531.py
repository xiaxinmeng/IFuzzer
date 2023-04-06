from sys import *
n = 30000
setrecursionlimit(n+1)

def fact(n):
   if n==1:
      return 1
   return fact(n-1)*n

fact(n)