from collections import OrderedDict
od = OrderedDict()
for i in range(10):
    od[str(i)] = i

for i in range(9):
    dict.__delitem__(od, str(i))

list(od)