
class SecondClassMeta(type):
    descriptor = Descriptor()

class SecondClass(metaclass=SecondClassMeta):
    descriptor = None

SecondClass.descriptor = None
