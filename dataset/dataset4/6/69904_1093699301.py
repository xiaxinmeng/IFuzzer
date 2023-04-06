import itertools, pickle

def foo(a, b):
    print(a, b)

a = itertools.accumulate([3, 4, 5], foo)
next(a)
next(a)   # prints: 3, 4

b = pickle.loads(pickle.dumps(a))

next(a)   # prints: None, 5
next(b)   # foo() is not called at all