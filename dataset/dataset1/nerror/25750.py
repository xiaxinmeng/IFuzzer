from datetime import timedelta

class BadInt(int):
    def __mul__(self, other):
        return Prod()

class Prod:
    def __radd__(self, other):
        return Sum()

class Sum:
    def __divmod__(self, other):
        return (0, -1)

timedelta(hours=BadInt(1))
