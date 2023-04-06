class MyMetaclass(type):
    pass

class OtherMetaclass(type):
    pass

def metaclass_callable(name, bases, namespace):
    return OtherMetaclass(name, bases, namespace)

class MyClass(metaclass=MyMetaclass):
    pass