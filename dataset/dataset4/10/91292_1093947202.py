
# In this example, the metaclass C is intended to be a class of
# subclasses of:
B = type

class C(type(B)):
    @classmethod
    def __prepare__(cls, /, *args, **kwargs):
        return dict(__name__ = cls._name(*args, **kwargs))
    @classmethod
    def _name(cls, /, *args, **kwargs):
        # The actual value of __name__ doesn't matter much to the
        # issue, so I make this function always return the same silly
        # thing in this example.
        return type.__dict__["__name__"]

class O(B, metaclass=C):
    print(__module__ == __name__) # True
    # Could update or delete __name__ here.
