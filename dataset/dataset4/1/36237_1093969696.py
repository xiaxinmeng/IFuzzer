def f(x):
    a = x
    def g():
        return eval('a')
    return g