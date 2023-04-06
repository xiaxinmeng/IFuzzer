class Iterable:
    ...
    def __bool__(self):
        try:
            next(iter(self))
            return True
        except StopIteration:
            return False