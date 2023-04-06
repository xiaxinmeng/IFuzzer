from os import getpid
from time import sleep, time
from multiprocessing import Pool

def f(sec):
    print("child %s: wait %s seconds" % (getpid(), sec))
    sleep(sec)

if __name__ == '__main__':
    print("parent %s: wait child" % (getpid(),))
    pool = Pool(processes=1)
    result = pool.apply_async(f, [60])
    print(result.get(timeout=120))
    print("parent: done")