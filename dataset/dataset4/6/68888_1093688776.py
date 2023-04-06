from timeit import timeit

setup = '''
from array import array
a = array("I", %s)
ac = a.__copy__
b = ac()
t = tuple(a)
u = t[:1] + t[1:]
'''
for init in ("[1]*10", "[0xffffffff]*10", "[1]*1000", "[0xffffffff]*1000"):
 print("\n", init)
 for action in ("ac()", "a == b", "a == ac()", "t == u"):
  print(("%6.2f" % timeit(action, setup % init)), action)