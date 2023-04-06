# a usual function works
## def works as well
f = lambda x : x 
f(1e+6)
# 1000000.0
import itertools
# islice without scientific notation works
itertools.islice([], 1000000)
# <itertools.islice object at 0x7fc7ce55be90>
itertools.islice([], 1e+6)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: Stop argument for islice() must be None or an integer: 0 <= x <= sys.maxsize.