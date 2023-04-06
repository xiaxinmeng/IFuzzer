class A:
    def __init__(self, val):
        self.val = val
    
    def __ipow__(self, other):
        return NotImplemented

class B:
    def __init__(self, val):
        self.val = val
    
    def __rpow__(self, other):
        return A(other.val ** self.val)

a = A(2)
b = B(2)
a **= b