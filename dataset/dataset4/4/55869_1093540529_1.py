def outer():
    x = 5
    y = 6
    def f(): return x,y
    z = 7
    def g(): return z
    exec_closure(f.__code__, closure=g.__closure__)