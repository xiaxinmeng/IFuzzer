class MyClass(object):
    def __init__(self, *args, **kwargs):
        # setting access to getter by attribute
        # without use of property decorator
        self.__dict__['myproperty'] = self._myproperty()

    def __getattr__(self, name):
        print('__getattr__ <<', name)
        raise AttributeError(name)
        return 'need know the question'

    def _myproperty(self):
        print(self.missing_attribute)
        return 42

my_inst = MyClass()
print(my_inst.myproperty)