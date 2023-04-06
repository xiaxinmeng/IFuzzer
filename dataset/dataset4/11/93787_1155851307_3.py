
# tester.py
class A:
    __var = 1

class B:
    def __init__(self, a):
        self.__var = a.__var

a = A()
b = B(a)
