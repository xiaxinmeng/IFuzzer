import gc
gc.collect()
objs = gc.get_objects()
for obj in objs:
    try:
        if isinstance(obj, X):
            print(obj)
    except NameError:
        class X:
            pass

def f():
    x = X()
    raise Exception()

f()