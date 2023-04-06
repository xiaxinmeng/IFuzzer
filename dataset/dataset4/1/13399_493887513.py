import pathlib
class MyPath(type(pathlib.Path())):
    def __init__(self, *args, foo):
        self.foo = foo
path = MyPath('bar', foo=42)
assert path.foo == 42