
class C:
    def __rrshift__(self, v):
        return 1

C() >> C()   # raise TypeError: unsupported operand types(s) for >>: 'C' and 'C'
