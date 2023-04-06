class A:
    def f(x):
        # doesn't matter what the type of x is
        x.__secret = 42

from dis import dis
dis(A.f)