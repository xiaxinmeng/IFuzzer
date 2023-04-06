class Foo(object):
    def __getattr__(self, name):
        return self.x  # which will recursively call __getattr__