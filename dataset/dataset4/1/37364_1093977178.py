class C:
    def __init__(self, n=10):
        self.n = 10
    def __iter__(self):
        return self
    def next(self):
        self.n -= 1
        if self.n < 0:
            raise StopIteration
        return self
    def __hash__(self):
        raise TypeError