import sys

def gen():
    try:
        try:
            yield
        except:
            print(sys.exc_info())
            raise TypeError()
    except Exception as exc:
        print("TypeError context:", repr(exc.__context__))
    yield

g = gen()
next(g)
try:
    raise ValueError
except Exception as exc:
    g.throw(exc)