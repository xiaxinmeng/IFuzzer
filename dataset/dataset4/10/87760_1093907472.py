
from abc import ABCMeta, ABC

class MetaclassMixin(ABC):
    pass 

class Meta(MetaclassMixin, ABCMeta):
    pass

class A(metaclass=Meta):
    pass

