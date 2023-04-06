from collections import namedtuple
foo = namedtuple('foo', '')
a = [] + foo()
print (a, type(a), len(a))
# () <class 'tuple'> 0