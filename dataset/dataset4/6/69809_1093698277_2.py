import collections
try:
    collections.OrderedDict = collections._OrderedDict
except AttributeError:
    pass