class C:
    def __getattr__(self, a):
        return object.__getattribute__(self, a)

c = C()
str(c)
