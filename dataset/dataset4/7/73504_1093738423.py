def func(x, y):
    print(x, y)

def proxy2(func, **kw):
    func(**kw)

def proxy1(func, **kw):
    proxy2(func, **kw)