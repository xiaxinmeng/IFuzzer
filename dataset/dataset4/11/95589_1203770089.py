
from _testcapi import HeapCTypeWithWeakref
class I3(HeapCTypeWithWeakref, list): pass

i = I3()
i.append(0)
i.weakreflist

print("OK")
