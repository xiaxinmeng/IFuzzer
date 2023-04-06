class D(Exception):
    def __init__(self, foo):
        self.foo = foo
        Exception.__init__(self)