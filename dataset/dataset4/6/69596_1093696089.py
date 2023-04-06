from collections import OrderedDict
class X(OrderedDict):
    def __iter__(self):
        for k in OrderedDict.__iter__(self):
            if k % 2:
                yield k

od = X((i, i) for i in range(5))
print(od.copy())