
oldproperty = property

class propertymeta(type):
    def __instancecheck__(cls, obj):
        return super().__instancecheck__(obj) or (
            isinstance(obj, classmethod)
            and super().__instancecheck__(obj.__func__)
            )


class property(oldproperty, metaclass=propertymeta): pass
