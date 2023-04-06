from contextlib import contextmanager
import itertools as its

@contextmanager
def mp(ob, attr, new):
    old = getattr(ob, attr)
    setattr(ob, attr, new)
    yield
    setattr(ob, attr, old)

def f(): pass

print(its.count, its.cycle)
with mp(its, 'count', f), mp(its, 'cycle', f):
    print(its.count, its.cycle)
print(its.count, its.cycle)