class Iterator:
    def __init__(self, obj):
        self.obj = obj

    def __next__(self):
        if self.obj is None:
            raise StopIteration
        return next(self.obj)

    def __iter__(self):
        return self

    def close(self):
        self.obj = None