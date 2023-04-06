class MyInt(object):
    def __init__(self, n):
        self.n = n

    def __coerce__(self, other):
        if type(other) is float:
            return float(self.n), other

x = MyInt(3)