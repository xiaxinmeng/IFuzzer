import multiprocessing.managers
def sqr(x): return x*x
manager = multiprocessing.managers.SyncManager()
manager.start()
pool = manager.Pool(4)
it = pool.imap_unordered(sqr, range(10000))
assert sorted(it) == map(sqr, range(10000))
pool.terminate()
manager.shutdown()