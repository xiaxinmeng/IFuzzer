from multiprocessing.pool import ThreadPool
class A(object):
    def __init__(self):
        self.pool = ThreadPool()
    def __del__(self):
        self.pool.close()
        self.pool.join()
a = A()
print(a)