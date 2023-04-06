class A:
    __var = 2

class B:
    @staticmethod
    def test():
        print(A._A__var)
        print(A.__var)

B.test()