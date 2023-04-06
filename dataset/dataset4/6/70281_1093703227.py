import functools
def f():
    def g():
        yield 1
    return g