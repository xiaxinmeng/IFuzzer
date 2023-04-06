class Metaclass(type):
    @property
    def attribute(self):
        return True

class Class(metaclass=Metaclass):
    attribute = False

for _ in range(8):
    print(Class.attribute)