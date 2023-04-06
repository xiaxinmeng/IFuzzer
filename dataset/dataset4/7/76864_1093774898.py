from inspect import isclass
class Liar:
    def __getattribute__(self, attr):
        if attr == '__class__':
            return type
        return object.__getattribute__(self, attr)