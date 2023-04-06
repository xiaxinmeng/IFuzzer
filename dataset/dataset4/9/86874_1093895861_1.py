from multiprocessing import Pool
import defs

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(defs.f, [1, 2, 3]))