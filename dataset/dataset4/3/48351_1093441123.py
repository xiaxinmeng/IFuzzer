WrapperDescriptorType = None

class Meta(type):
    def __init__(cls, *args, **kwargs):
        global WrapperDescriptorType
        type.__init__(cls, *args, **kwargs)
        WrapperDescriptorType = type(cls.__init__)

class A:
    __metaclass__ = Meta