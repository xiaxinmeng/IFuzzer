class Foo(object):

    def __init__(self):
        self.foo = 1
        self.data = {"bing": 4}

    def __getattr__(self, name):
        print(f'Getting {name}')
        return self.data.get(name)

    @property
    def bar(self):
        return 3

    @property
    def bing(self):
        raise AttributeError("blarg")

f = Foo()
print('foo', f.foo)
print('__str__', f.__str__)
print('bar', f.bar)
print('bing', f.bing)
f.__getattribute__('bing')