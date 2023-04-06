from collections import OrderedDict
obj = None
for _ in range(1000):
    obj = OrderedDict([(None, obj)])