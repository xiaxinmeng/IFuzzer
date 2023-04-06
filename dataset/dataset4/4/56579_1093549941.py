_super = super
class X(object):
    
    def __init__(self):
        _super(self, X).__init__()
    
    @property
    def __class__(self):
        return int
        
print (isinstance(X(), int))