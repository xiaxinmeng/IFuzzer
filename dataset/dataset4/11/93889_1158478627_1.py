import pickle

def function(self, x):
    return x ** 2

class Foo:
    pass
foo = Foo()
foo.f2 = function.__get__(foo)
pickle.loads(pickle.dumps(foo))