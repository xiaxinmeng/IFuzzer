import inspect

class Foo:
    x = int()

x = 1
f = Foo()
assert(f.x != x)

func = lambda: f.x == 0
assert(func())

cv = inspect.getclosurevars(func)
assert(cv.globals['f'] == f)
assert(cv.globals.get('x') != x) # <--- Assertion fails