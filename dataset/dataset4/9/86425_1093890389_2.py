
import pprint

class ReallyNiceObject:
    def __str__(self):
        return pprint.saferepr(self.__dict__)
    def __repr__(self):
        return str(self)
