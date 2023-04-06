class Descriptor(object):
    """Doc of a non-data descriptor."""
    def __get__(self, instance, owner):
        return 42 if instance else self

class GetSetDescriptor(Descriptor):
    """Doc of a data-descriptor."""
    def __set__(self, instance, value):
        pass

class Demo(object):
    non_data = Descriptor()
    data = GetSetDescriptor()

help(Demo)