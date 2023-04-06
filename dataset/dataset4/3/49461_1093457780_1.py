class xcomplex( complex ):

    def __new__(cls,*args,**kwargs):
        return complex.__new__(cls,*args,**kwargs)

##    def __coerce__(self,other):
##        t = complex.__coerce__(self,other)
##        try:
##            return (self,xcomplex(t[1]))
##        except TypeError:
##            return t
        
    def __add__(self,x):
        return xcomplex( complex.__add__(self,x) )
    
    def __radd__(self,x):
        return xcomplex( complex.__radd__(self,x) )

xz = xcomplex(1+2j)
xy = float(10.0)
z = complex(10+1j)