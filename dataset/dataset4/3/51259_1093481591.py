pycon
'''Shows that floats in tuples are not rounded like floats.
>>> print(.1)
0.1
>>> print((.1,))
(0.10000000000000001,)
'''
import doctest
doctest.testmod(verbose=True)
