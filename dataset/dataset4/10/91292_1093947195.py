
class C(type):
    @classmethod
    def __prepare__(cls, /, *args, **kwargs):
        return dict(__name__ = "whatever")

class O(metaclass=C):
    print(__module__) # "whatever" printed
