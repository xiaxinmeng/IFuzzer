class Foo_42(object):
    def __contains__(self,item): return 42 
    
class Foo_neg(object):
    def __contains__(self,item): return -42 
    
class Foo_None(object):
    def __contains__(self,item): return  
    
class Foo_false(object):
    def __contains__(self,item): return False 
    
class Foo_true(object):
    def __contains__(self,item): return True

for foo in [Foo_false(),Foo_None(),Foo_neg(),Foo_true(),Foo_42()]:
    print("3 in foo:" + str(3 in foo))
    print("foo.__contains__(3)" + str(foo.__contains__(3)))
    