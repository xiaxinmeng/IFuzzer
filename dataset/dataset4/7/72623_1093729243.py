from types import new_class


class MyMetaclass(type):
    pass

class OtherMetaclass(type):
    pass

def metaclass_callable(name, bases, namespace):
    return new_class(name, bases, dict(metaclass=OtherMetaclass))

class MyClass(metaclass=MyMetaclass):
    pass