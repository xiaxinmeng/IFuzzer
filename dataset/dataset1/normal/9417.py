import gc
from pprint import pprint
gc.set_debug(gc.DEBUG_SAVEALL)

class MyClass(object): pass
del MyClass

print(gc.collect())
pprint(gc.garbage)
