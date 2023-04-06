class A(object): pass

class B(A):
    def meth(self, arg):
        super(B, self).meth(arg)

class C(A): pass

class D(B, C): pass

d=D()
d.meth()