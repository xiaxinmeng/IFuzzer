from collections import OrderedDict
o = OrderedDict()
o['a'] = 1
o['b'] = 1
dict.__delitem__(o, 'a')
