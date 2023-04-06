class NewKlass(object):
    def __ipow__(self, i):
        self._ipow = i
        return self 
obj = NewKlass()
obj **= 1