from collections import OrderedDict

class C:
    def __hash__(self):
        return 1

d = OrderedDict()
d[C()] = 0
d.popitem()



