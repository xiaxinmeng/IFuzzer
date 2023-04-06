class Y:
    pass
class X:
    def __init__(self):
        self.y = Y()
        self.y.x = self
    pass

def dump():
    import gc
#    gc.collect()
    objs = gc.get_objects()
    for obj in objs:
        if isinstance(obj, X):
            print(obj)

def f():
    x = X()
    raise Exception()

f()