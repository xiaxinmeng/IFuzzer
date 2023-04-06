
class A:
    @ClassMethod
    def f(cls, *, x): pass

print(A.f)
A.f(x=3)
