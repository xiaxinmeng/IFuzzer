
import timeit

setup = """
class A:
    def f(self): pass
class B(A):
    def f(self): super().f()
    def g(self): A.f(self)
b = B()
"""
print(timeit.timeit("b.f()", setup=setup, number=20000000))
print(timeit.timeit("b.g()", setup=setup, number=20000000))

7.329449548968114
3.892987059080042
