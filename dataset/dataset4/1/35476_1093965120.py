import weakref
ref = weakref.WeakKeyDictionary()

class MyError(Exception):
    pass

def add(self, x):
    raise MyError

def encapsulate():
    f = lambda : ()
    ref[f] = None
    return f