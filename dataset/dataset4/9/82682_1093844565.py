from multiprocessing import Pool

class A(object):
    def __init__(self):
        self.pool = Pool(processes=2)

solver = A()