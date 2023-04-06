from itertools import groupby

def f(n):
    print("enter:", n)
    if n == 5:
        list(b)
    print("leave:", n)
    return n != 6

for (k, b) in groupby(range(10), f):
    print(list(b))