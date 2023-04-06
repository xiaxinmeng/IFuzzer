import multiprocessing.managers
def sqr(x): return x*x
if __name__ == '__main__':
    manager = multiprocessing.managers.SyncManager()
    manager.start()
    pool = manager.Pool(4)
    it = pool.imap_unordered(sqr, range(1000))
    assert sorted(it) == [sqr(x) for x in range(1000)]
    pool.terminate()
    manager.shutdown()