
import math

class A:
    def __init__(self, a):
        self.a=a
    def __hash__(self):
        return hash(self.a)
    def __eq__(self, other):
        if(math.isnan(self.a) and math.isnan(other.a)):
            return True
        return self.a == other.a
    def __repr__(self):
        return str(self.a)
        
set([A(float("nan")), A(float("nan"))])  # result: {nan}
