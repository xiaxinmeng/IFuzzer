class XBase(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        attrs.pop('__module__')
        return super().__new__(cls, name, bases, attrs, **kwargs)

class X(metaclass=XBase): ...