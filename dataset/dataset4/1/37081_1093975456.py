class A:
    def save(self):
        return "I am 'A.save'"
class B(A):
    pass
class C(A):
    def save(self):
        return "I am 'C.save'"
class D(B,C):
    pass