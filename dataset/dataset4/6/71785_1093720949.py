class Sized(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, C):
        return (super().__subclasshook__(C) and 
                any("__len__" in B.__dict__ for B in C.__mro__))