from types import *
class C:
    __str__ = InstanceType.__str__
str(C())