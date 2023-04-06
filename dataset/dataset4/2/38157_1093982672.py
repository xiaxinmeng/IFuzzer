import copy
class Foo(object):
    pass
f = Foo()
f.bar = f
g = copy.deepcopy(f)