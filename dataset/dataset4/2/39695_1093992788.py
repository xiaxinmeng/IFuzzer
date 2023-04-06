x = (basestring,)
for i in xrange(0, 1000000):
   x = (x,)
issubclass(str, x)