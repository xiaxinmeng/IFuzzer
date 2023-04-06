class takewhile(pred, iterable):
    def __init__(self):
        self.pred = pred
        self.iterable = iterable
        self.failed = False
    def __iter__(self):
        for item in self.iterable:
            if self.pred(item):
                yield item
            else:
                self.failed = True
                self.lastitem = item
                return