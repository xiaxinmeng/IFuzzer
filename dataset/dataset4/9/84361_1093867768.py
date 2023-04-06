import types
class Type(type):
    __class__ = property({}.__getitem__, {}.__setitem__)
class Object(metaclass=Type):
    __slots__ = '__class__'