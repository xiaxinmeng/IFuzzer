class M_A(type):
    def __new__(mcls, name, bases, ns):
       print('M_A.__new__', mcls, name, bases)
       return super().__new__(mcls, name, bases, ns)

class M_B(M_A):
    def __new__(mcls, name, bases, ns):
       print('M_B.__new__', mcls, name, bases)
       return super().__new__(mcls, name, bases, ns)

class A(metaclass=M_A): pass
class B(metaclass=M_B): pass

class C(A, B): pass
D = type('D', (A, B), {})