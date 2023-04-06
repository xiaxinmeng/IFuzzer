class A:
    """Base class"""
    def foo(self): """Some docstring"""
    def bar(self): """Other docstring"""

class B(A):
    def foo(self): pass

help(B)