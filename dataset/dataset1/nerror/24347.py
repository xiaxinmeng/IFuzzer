from collections import OrderedDict
from random import randrange

class C:
    def __hash__(self):
        return randrange(100000)

d = OrderedDict()

for i in range(100):
    d[C()] = i

repr(d)



