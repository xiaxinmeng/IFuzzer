
class Meta(type): pass

class X(metaclass=Meta):
    def __class_getitem__(cls, key):
        return key

X[10]
