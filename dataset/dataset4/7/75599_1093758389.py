class BadException(Exception):
    __module__ = None

class BadClass:
    def __del__(self):
        raise BadException

foo = BadClass()
del foo