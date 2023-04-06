
def f():
    x = 1
    def g():
        return eval("x")
    return g
enc = f()
enc()
