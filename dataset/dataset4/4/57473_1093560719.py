from abc import ABCMeta

class Meta(ABCMeta):
    def __instancecheck__(cls, instance):
        # monkeypatching class method
        cls.__subclasscheck__ = super(Meta, cls).__subclasscheck__
        return super(Meta, cls).__instancecheck__(instance)

    def __subclasscheck__(cls, sub):
        return cls in sub.mro()

class A(object):
    __metaclass__ = Meta

class B(object): pass

# registering class 'B' as a virtual subclass of 'A'
A.register(B)