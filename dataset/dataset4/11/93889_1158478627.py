import pickle

def function(x):
    return x ** 2

class Foo:
    def __init__(self):
        self.f = function
        def f2(self, x):
            return self.f(x)
        self.f2 = f2.__get__(self)

foo = Foo()
print(foo.f2(7)) # prints 49
pickle.loads(pickle.dumps(foo))