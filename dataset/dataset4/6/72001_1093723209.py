class FilteredExceptionMeta(type):
    def __subclasscheck__(cls, other):
        return cls.__subclasshook__(other)
    def __instancecheck__(cls, other):
        return cls.__subclasshook__(type(other))