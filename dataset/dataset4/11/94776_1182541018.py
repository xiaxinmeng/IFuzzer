
class A(object):
    def __hash__(self):
        print("--> hashing")
        return super().__hash__()
    
a=A()    
d={A(): 0}
