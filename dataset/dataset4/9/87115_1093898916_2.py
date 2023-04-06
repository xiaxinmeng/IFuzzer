
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    __spec__ = None
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
