import multiprocessing
import multiprocessing.managers

def f(n):
    return n * n

def worker(pool):
    with pool:
        pool.apply_async(f, (10, ))

manager = multiprocessing.managers.SyncManager()
manager.start()
pool = manager.Pool(processes=4)
proc = multiprocessing.Process(target=worker, args=(pool, ))
proc.start()
proc.join()