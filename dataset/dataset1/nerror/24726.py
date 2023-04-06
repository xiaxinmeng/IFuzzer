#Set up
from collections import OrderedDict
o = OrderedDict()
dict.__setitem__(o, 'a', 1)
print(o)
#Prints OrderedDict([<NULL>])

o = OrderedDict()
class C:
    pass
c = C()
c.__dict__ = o
c.a = 1
print(o)
#Prints OrderedDict([<NULL>])

o.popitem()
#Error: dictionary is empty

print(len(o))
#Prints 1 (correctly, but in contradiction of above)
