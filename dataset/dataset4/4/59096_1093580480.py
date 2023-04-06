def f(x):
    def g():
        x = x + "a"
        return x
    return g()
f("b")