class A: 
        def f(self): pass 
 
class C(A): 
        g = A.f 
 
import doctest, sys 
doctest.testmod(sys.modules[__name__])