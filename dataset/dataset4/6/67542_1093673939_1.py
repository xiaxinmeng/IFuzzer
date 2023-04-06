import sys

def gen():
    try:
        yield
        raise TypeError()
    except:
        print(sys.exc_info())
    print(sys.exc_info())
    yield

g = gen()
next(g)
try:
    raise ValueError
except Exception:
    next(g)