class myiter:
    def __init__(self, l):
        self.l = l
    def __iter__(self):
        self.index = 0
        return self
    def next(self):
        p, m = self.l(self.index)
        self.index += 1
        return p