
import collections, types
dd = collections.defaultdict(set)
mpt = types.MappingProxyType(dd)
mpt['__getitem__'] # key inserted
mpt.get('get') # key not inserted
print(dd.items()) # dict_items([('__getitem__', set())])
