class Desc(object):
    def __get__(self, instance, owner):
        return owner

class A(object):
    attr = Desc()

class B(A):
    pass

class C(B):
    pass

instance = C()