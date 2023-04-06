import os
from multiprocessing import Pool

def f(x):
    os._exit(0)
    return "success"

if __name__ == '__main__':
    with Pool(1) as p:
        print(p.map(f, [1]))