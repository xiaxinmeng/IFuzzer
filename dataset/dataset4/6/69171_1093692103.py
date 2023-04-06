from __future__ import print_function

class MyClass(object):
    def __getattr__(self, name):
        print('__getattr__ <<', name)
        raise AttributeError(name)
        return 'need know the question'

    @property
    def myproperty(self):
        print(self.missing_attribute)
        return 42

my_inst = MyClass()
print(my_inst.myproperty)