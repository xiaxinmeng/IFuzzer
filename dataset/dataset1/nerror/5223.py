import sys

class Foo():
    def __getattr__(self, name):
        if name=='bar':
            if not hasattr(self, 'bar'):
                self.bar = 42
            return self.bar
        raise AttributeError(name)

class Writer():
    def __init__(self, fileobj):
        self.__fileobj = fileobj

    def __getattr__(self, name):
        if name=='write':
            return self.__fileobj.write
        raise AttributeError(name)

print(Foo().bar) # prints out 42
sys.stderr = Writer(sys.stderr)
print(Foo().bar) # crashes the interpreter

