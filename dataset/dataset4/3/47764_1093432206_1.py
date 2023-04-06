class Foo:
    def __init__(self):
        self.foo = {}

    def __getattr__(self, key):
        self.foo[5]