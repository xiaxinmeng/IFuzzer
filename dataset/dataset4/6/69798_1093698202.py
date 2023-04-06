def g():
    yield 1
    raise
    yield 2

i = g()
try:
    1/0
except:
    next(i)
    next(i)