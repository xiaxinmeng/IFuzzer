class MyException(Exception):
    pass

def gen():
    try:
        yield
    except MyException:
        pass

g = gen()
next(g)