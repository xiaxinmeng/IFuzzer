import sys, traceback

class MyException(Exception):
    def __init__(self, *args):
        1/0

def gen():
    f = open(__file__, mode='rb', buffering=0)
    yield

g = gen()
next(g)
recursionlimit = sys.getrecursionlimit()
sys.setrecursionlimit(len(traceback.extract_stack())+3)
try:
    g.throw(MyException)
finally:
    sys.setrecursionlimit(recursionlimit)
    print('Done.')