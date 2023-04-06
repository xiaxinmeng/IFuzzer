class FakeClass:
    def __init__(self,base=False):
        self.base = base
    @property
    def __bases__(self):
        if self.base:
            return ()
        return (FakeClass(True),)
issubclass(FakeClass(), int)