import sys

def gen():
    print(sys.exc_info())
    yield

g = gen()
try:
    raise ValueError
except Exception:
    next(g)