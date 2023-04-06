class C:
    def __getattr__(self, attr):
        class A: pass
        class B: pass
        A.__getattr__ = B.__getattr__ = C.__getattr__
        return (A(), B())