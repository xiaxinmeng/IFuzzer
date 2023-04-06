
def f():
    x = 1
    def g():
        x  # <----- 
        return eval("x")
    return g
enc = f()
enc()  # return value: 1
