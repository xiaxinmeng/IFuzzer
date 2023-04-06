from weakref import ref

def f():
    ref(lambda: 0, [])
    f()

f()