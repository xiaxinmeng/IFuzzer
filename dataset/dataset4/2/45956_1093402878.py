class WithOut:
    @property
    def huh(self):
        return self.not_here

class With:
    @property
    def huh(self):
        return self.not_here
    def __getattr__(self, name):
        print('looking up %s' % name)
        raise AttributeError('%s not in class %s' % (name, type(self)))