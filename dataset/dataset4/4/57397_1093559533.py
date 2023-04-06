def gen():
    try:
        yield
    except:
        raise

g = gen()
try:
    1/0
except ZeroDivisionError as v:
    g.throw(v)