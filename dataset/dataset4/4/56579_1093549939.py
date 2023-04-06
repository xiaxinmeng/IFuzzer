class X(object):
    
    def __init__(self):
        super().__init__()
    
    @property
    def __class__(self):
        return int
        
print (isinstance(X(), int))