class A(object):
    def __init__(self):
        self.r = iter(range(5))
    def __iter__(self):
        return self
    @property
    def next(self):
        return next(self.r)