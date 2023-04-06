class Foo(object):
    def __getattr__(self, name):
        print(f'Getattr {name}')
        return True
    @property
    def bing(self):
        print('Property bing')
        raise AttributeError("blarg")

f = Foo()
print(f.bing)