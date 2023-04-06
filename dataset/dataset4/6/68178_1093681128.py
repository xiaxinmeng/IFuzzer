class GenericProxy:
    def __init__(self, proxied):
        self.proxied = proxied

    @property
    def __iter__(self):
        if not hasattr(self.proxied, '__iter__'):
            raise AttributeError
        else:
            return lambda: self
    @property
    def __next__(self):
        if not hasattr(self.proxied, '__next__'):
            raise AttributeError
        else:
            return lambda: next(self.proxied)