
import concurrent.futures

class E(Exception):
    def __init__(self, a1, a2):
        Exception.__init__(self, '{}{}'.format(a1, a2))

def f(_):
    raise E(1, 2)

with concurrent.futures.ProcessPoolExecutor(2) as exe:
    for _ in exe.map(f, (1,)):
        pass
