class DataDescriptor1:  # missing __get__
    def __set__(self, instance, value): pass
    def __delete__(self, instance): pass

class DataDescriptor2:  # missing __set__
    def __get__(self, instance, owner=None): pass
    def __delete__(self, instance): pass

class DataDescriptor3:  # missing __delete__
    def __get__(self, instance, owner=None): pass
    def __set__(self, instance, value): pass

class A:
    x = DataDescriptor1()
    y = DataDescriptor2()
    z = DataDescriptor3()

a = A()
vars(a).update({'x': 'foo', 'y': 'bar', 'z': 'baz'})

a.x
# actual: returns 'foo'
# expected: returns 'foo'

a.y = 'qux'
# actual: raises AttributeError: __set__
# expected: vars(a)['y'] == 'qux'

del a.z
# actual: raises AttributeError: __delete__
# expected: 'z' not in vars(a)