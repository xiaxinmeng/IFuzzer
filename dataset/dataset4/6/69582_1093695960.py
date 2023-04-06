from collections import OrderedDict
obj = []
for _ in range(33):
    obj = OrderedDict(((None, obj),))
for _ in range(17):
    obj = [obj]
print("Still alive, crash happens at interpreter finalization")