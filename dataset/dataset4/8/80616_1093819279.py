import multiprocessing

def f(n):
    return n+1

with multiprocessing.Pool() as p:
    for n in p.map(f, [1,2,3]):
        print(n)