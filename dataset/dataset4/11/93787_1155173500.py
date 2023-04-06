
class B:  # Still wrong message. Should be '_A__var', because self.a is an attribute and instance of A, but not B instance
              # or should be Error message with not mangled name.
    a = A()

    def test_1(self):
        a = self.a.__var  # AttributeError: 'A' object has no attribute '_B__var'
        return a

    def test_2(self):
        a = self.a._A__var  # return 2
        return a


class C(A):  # Correct, because of inheritance. As documented.

    def test_1(self):
        a = self.__var  # AttributeError: 'C' object has no attribute '_C__var' 
        return a