class A:
    def __new__(cls, *args):
        print('__new__ called with', args)
        return object.__new__(cls)
    
    def __init__(self, *args):
        print('__init__ called with', args)
        self.args = args
        
    def __getnewargs__(self):
        print('called')
        return ()
    
a = A(1)
s = pickle.dumps(a)
a = pickle.loads(s) # __new__ called, not __init__
delattr(A, '__getnewargs__') 
a = A(1)
s = pickle.dumps(a)
a = pickle.loads(s) # __new__ called, not __init__