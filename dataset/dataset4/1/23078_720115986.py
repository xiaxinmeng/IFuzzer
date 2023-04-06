
class A:

    x = 10

    def __init__(self, z):
        self.z = z

    @property
    def p2(self):
        return 2 * self.x

    @property
    def p3(self):
        return 3 * self.x

    def m5(self, y):
        return 5 * y

    def m7(self, y):
        return 7 * y

    def __getattr__(self, name):
        return ('getattr_hook', self, name)

    # def object_getattribute(obj, name):
    def __getitem__(obj, name):
        "Emulate PyObject_GenericGetAttr() in Objects/object.c"
        null = object()
        objtype = type(obj)
        value = getattr(objtype, name, null)
        if value is not null and hasattr(value, '__get__'):
            if hasattr(value, '__set__') or hasattr(value, '__delete__'):
                return value.__get__(obj, objtype)  # data descriptor
        try:
            return vars(obj)[name]                  # instance variable
        except (KeyError, TypeError):
            pass
        if hasattr(value, '__get__'):
            return value.__get__(obj, objtype)      # non-data descriptor
        if value is not null:
            return value                            # class variable
        # Emulate slot_tp_getattr_hook() in Objects/typeobject.c
        if hasattr(objtype, '__getattr__'):
            return objtype.__getattr__(obj, name)   # __getattr__ hook
        raise AttributeError(name)

class B:
    __slots__ = ['z']

    x = 15

    def __init__(self, z):
        self.z = z

    @property
    def p2(self):
        return 2 * self.x

    def m5(self, y):
        return 5 * y

    def __getattr__(self, name):
        return ('getattr_hook', self, name)

    __getitem__ = A.__getitem__

if __name__ == '__main__':

    a = A(11)
    vars(a).update(p3 = '_p3', m7 = '_m7')
    assert a.x == a['x'] == 10
    assert a.z == a['z'] == 11
    assert a.p2 == a['p2'] == 20
    assert a.p3 == a['p3'] == 30
    assert a.m5(100) == a.m5(100) == 500
    assert a.m7 == a['m7'] == '_m7'
    assert a.g == a['g'] == ('getattr_hook', a, 'g')

    b = B(22)
    assert b.x == b['x'] == 15
    assert b.z == b['z'] == 22
    assert b.p2 == b['p2'] == 30
    assert b.m5(200) == b['m5'](200) == 1000
    assert b.g == b['g'] == ('getattr_hook', b, 'g')

    print('Success.  All tests passed.')

