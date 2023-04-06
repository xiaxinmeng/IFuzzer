from enum import Enum
import operator
from statistics import median



class C(Enum):
    red = 1
    grn = 2
    blu = 3
    

    def __lt__(self, other):
        return operator.__lt__(self.value, other.value)


    def __le__(self, other):
        return operator.__le__(self.value, other.value)


    def __eq__(self, other):
        return operator.__eq__(self.value, other.value)


    def __ne__(self, other):
        return operator.__ne__(self.value, other.value)


    def __gt__(self, other):
        return operator.__gt__(self.value, other.value)


    def __ge__(self, other):
        return operator.__ge__(self.value, other.value)

    
b = [C.blu, C.blu, C.red, C.grn]
print(median(b))    
