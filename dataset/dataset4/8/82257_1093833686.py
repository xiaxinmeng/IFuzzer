from multiprocessing.pool import Pool
class A(object):
    def __init__(self):
        self.pool = Pool()
    def __del__(self):
        self.pool.close()
        self.pool.join()
a = A()