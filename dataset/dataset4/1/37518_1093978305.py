class Meta(type):
    def __new__(meta, name, bases, dict):
        return super(Meta, name).__new__(meta, name,
bases, dict)

class AClass:
    __metaclass__ = Meta