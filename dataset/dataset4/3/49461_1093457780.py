class xfloat( float ):

    def __new__(cls,*args,**kwargs):
        return float.__new__(cls,*args,**kwargs)
        
    def __add__(self,x):
        return xfloat( float.__add__(self,x) )

    def __radd__(self,x):
        return xfloat( float.__radd__(self,x) )