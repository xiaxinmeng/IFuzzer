from unittest.mock import create_autospec

class CrazyDescriptor(object):
    def __get__(self, obj, type_):
        if obj is None:
            return lambda x: None

class MyClass(object):

    some_attr = CrazyDescriptor()

mock = create_autospec(MyClass)
mock.some_attr(1)