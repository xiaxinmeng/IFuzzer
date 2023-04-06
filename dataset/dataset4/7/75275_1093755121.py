import multiprocessing as mp
from time import sleep

def func(queue):
    pass

if __name__ == '__main__':
    manager = mp.Manager()

    pool = mp.Pool(1)

    queue = manager.Queue()
    r = pool.apply_async(func, args = [queue])
    #sleep(1)
    queue = None

    pool.close()
    pool.join()