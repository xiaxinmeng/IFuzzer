class LRU:

    def __init__(self, func, maxsize=128):
        self.func = func
        self.d = OrderedDict()

    def __call__(self, *args):
        if args in self.d:
            value = self.d[args]
            self.d.move_to_end(args)
            return value
        value = self.func(*args)
        if len(self.d) >= self.maxsize:
            self.d.popitem(False)
        self.d[args] = value
        return value