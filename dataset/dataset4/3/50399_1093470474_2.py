import weakref

class Foo(object):
    pass
    
mydict = dict((k, Foo()) for k in range(10))

w = weakref.WeakValueDictionary(mydict)