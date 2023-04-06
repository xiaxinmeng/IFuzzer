class Iterator:
    def __init__(self, obj):
        self.obj = obj

    def __next__(self):
        return next(self.obj)

    def __iter__(self):
        return self