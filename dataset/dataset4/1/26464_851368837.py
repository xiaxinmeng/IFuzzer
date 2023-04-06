
import _decimal
import gc
import collections.abc

ctx = _decimal.Context
SignalDict = None
for cls in collections.abc.MutableMapping.__subclasses__():
    if cls.__name__.split('.')[-1] == 'SignalDict':
        SignalDict = cls
        break
else:
    raise Exception("not found")
SignalDictMixin = SignalDict.__bases__[0]
assert SignalDictMixin.__name__.split('.')[0] == 'SignalDictMixin'

s = SignalDictMixin()
repr(s)
