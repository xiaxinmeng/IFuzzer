import timeit

setup = """
class A:
    def f(self): pass
class B(A):
    def g(self): super().f()
    def h(self): self.f()

b = B()
"""

# super() call
print(timeit.timeit("b.g()", setup=setup, number=20_000_000))
# reference
print(timeit.timeit("b.h()", setup=setup, number=20_000_000))