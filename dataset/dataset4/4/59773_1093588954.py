class C:
    def __iter__(self): return self
    def __next__(self):
            raise StopIteration(100)


def g():
    if False:
        yield 100
    return 100

def f(val):
    x = yield from val
    print('x', x)

list(f(C()))
list(f(g()))