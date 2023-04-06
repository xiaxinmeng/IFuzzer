from multiprocessing import Pool

def f(x):
    return x*x

def g(K, N):
    # Any external function that uses multiprocessing can be used here.
    with Pool(K) as p:
        x = p.map(f, [x for x in range(N)])
        return x

if __name__ == '__main__':
   # mix of different multiprocessing tasks.
   # expected output : [0, 1, 0, 1, 4]
   print(g(3,2) + g(2, 3))