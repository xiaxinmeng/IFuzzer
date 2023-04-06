class A:
    def foo(self, cls): return 1

class B: pass

class B:
    bar = classmethod(A().foo)

B.bar()