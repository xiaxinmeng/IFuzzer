class C(Exception):
    """Extension with values, args not set."""
    def __init__(self, foo):
        self.foo = foo

class D(Exception):
    """Extension with values, init called with no args."""
    def __init__(self, foo):
        self.foo = foo
        Exception.__init__(self)