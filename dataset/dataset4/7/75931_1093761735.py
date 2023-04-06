a = [1]
def f(): return a
return type(f.__closure__[0])