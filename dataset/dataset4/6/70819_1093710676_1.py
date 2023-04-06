@public
def baz(a, b):
    return a + b

@public
def buz(c, d):
    return c / d

def qux(e, f):
    return e * f

class zup:
    pass

@public
class zap:
    pass

public('CONST1')
CONST1 = 3

CONST2 = 4

public('CONST3')
CONST3 = 5