
class C:
    def __rrshift__(self, v):
        return 1

class D:
    def __rrshift__(self, v):
        return 2

C() >> D() # 2
