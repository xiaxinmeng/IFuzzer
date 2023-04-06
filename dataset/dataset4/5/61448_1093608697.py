import inspect
def fun(x):
    del x
    return inspect.currentframe()

inspect.formatargvalues(*inspect.getargvalues(fun(10)))