class C:
    def __init__(self, x=None):
        self.x = x if x is not None else self
    def __reduce__(self):
        return C, (self.x,)