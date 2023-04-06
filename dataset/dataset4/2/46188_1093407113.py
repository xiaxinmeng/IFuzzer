import math

def hypot(*args):
    '''
        Return the Euclidean vector length.
        >>> from math import hypot, sqrt
        >>> hypot(5,12)    # traditional definition
        13.0
        >>> hypot()
        0.0
        >>> hypot(-6.25)
        6.25
        >>> hypot(1,1,1) == sqrt(3) # diagonal of unit box
        True
    '''
    return math.sqrt(sum(arg*arg for arg in args))