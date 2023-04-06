class MyError(Exception):
    pass

def add(x):
    raise MyError

def encapsulate():
    f = lambda : ()
    ref[f] = None
    return f