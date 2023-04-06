class A(object):
    def __new__(cls):
        self = super(cls, A).__new__(cls)
        self.a = 1
        return self
    def __setstate__(self, d):
        self.__dict__.update(d)
    def __getstate__(self):
        d = self.__dict__.copy()
        d.pop('a')
        return d