class X:
    def meth(self):
        print(self)
        super()

def f():
    k = X()
    def g():
        return k
    return g
c = f().__closure__[0]
X.meth(c)