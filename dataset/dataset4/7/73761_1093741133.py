from multiprocessing import Pool
import time

def f(x):
    time.sleep(1)
    return x*x

if __name__ == '__main__':
    start_time = time.time()
    with Pool(4) as p:
        print(p.map(f, range(20)))
    print("elapsed wall time: ", time.time()-start_time)