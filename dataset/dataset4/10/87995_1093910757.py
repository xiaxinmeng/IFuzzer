from nocasedict import NocaseDict, HashableMixin
from types import MappingProxyType

class HashableDict(HashableMixin, NocaseDict):
    """A hashable dictionary"""
    pass

hd = HashableDict({'a': 1, 'b': 2})
print("hash(hd): {}".format(hash(hd)))

mp = MappingProxyType(hd)
print("hash(mp): {}".format(hash(mp)))