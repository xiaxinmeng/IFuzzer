import inspect

class Foo():

    @property
    def bar(self):
        raise NotImplementedError

print(inspect.getmembers(Foo()))