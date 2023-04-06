from itertools import *
c = count()
a,b = tee(c)
for i in range(1000):
 next(a)
del(b)
