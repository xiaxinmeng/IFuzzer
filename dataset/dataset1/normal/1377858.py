import weakref

ref = None
class Target(object):
    def __del__(self):
        global ref
        ref = weakref.ref(self)

def g():
    w = Target()
    w = None
    print (ref())

g()



 	  	 
