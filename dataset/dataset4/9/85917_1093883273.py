
from collections import OrderedDict
import copy


class A(OrderedDict):
    def __init__(self):
        self['123'] = 123

a = A()
del a['123']
copy.copy(a)


# --> A([('123', 123)])

