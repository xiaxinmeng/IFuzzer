from multiprocessing.pool import ThreadPool

pool = ThreadPool(10)

def gen():
    yield 1 + '1' # here is an error