
from collections import OrderedDict

d = dict(C='carbon')
o = OrderedDict(d)
assert d == o
assert d.viewitems() == o.viewitems()
