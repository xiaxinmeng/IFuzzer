class MyType(object):
    def __format__(self, fmt):
        if fmt.endswith('f'):
            return float(self.func()).__format__(fmt)
        elif fmt.endswith('d'):
            return int(self.func()).__format__(fmt)
        else:
            return str(self.func()).__format__(fmt)

    def __init__(self, func):
        self.func = func