class MyType(type):
    pass

class MyClass(object):
    __metaclass__ = MyType
    def __init__(self, a):
        pass