def f():
    print(len("test"))
    builtins_ns = f.__globals__['__builtins__'].__dict__
    #builtins_ns = f.__builtins__
    builtins_ns['len'] = lambda x: 7
    print(len("test"))

f()