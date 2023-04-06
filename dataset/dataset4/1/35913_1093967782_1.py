# FAILS with 
# Traceback (most recent call last):
#   File "bug.py", line 18, in ?
#     print new.instancemethod(n, None, B)
# TypeError: instancemethod() argument 3 must be class,
# not type
def m(self): pass

class B(object):
    def f(self): pass