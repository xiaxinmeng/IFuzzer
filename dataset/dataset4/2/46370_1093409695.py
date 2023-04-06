import copy, weakref
class Test(object): pass
t = Test()
wr = weakref.ref(t)
wr_new = copy.copy(wr)