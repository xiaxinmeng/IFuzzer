class SupportsInt(ABC):
    @classmethod
    def __subclasshook__(cls, C):
        return hasattr(C, '__int__')