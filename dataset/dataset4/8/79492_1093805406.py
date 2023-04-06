
import multiprocessing

class E(Exception):
    def __init__(self, a1, a2):
        Exception.__init__(self, '{}{}'.format(a1, a2))

def f(_):
    raise E(1, 2)

multiprocessing.Pool(1).map(f, (1,))
