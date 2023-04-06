import weakref

class MyRef(weakref.ref):
    pass

def callback(wr):
    print ("starting callback")
    print (wr)
    print (wr.cycle)  # Segfault
    print ("finishing callback")

class Dummy(object):
    pass

d = Dummy()
x = MyRef(d, callback)
x.cycle = d
del d
