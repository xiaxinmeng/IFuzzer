class Class:
    pass

obj = Class()
obj.__dict__['d'] = property(lambda: print('called'))

_ = obj.d  # nothing is printed.


class Obj:
    @property
    def d(self):
        print('called')

_ = Obj.d  # nothing is printed.