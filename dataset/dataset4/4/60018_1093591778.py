d = {}
o = some_object
m = memoryview(o)
d[m] = -1
o.modify()  # so that hash(m) changes
print(d[m]) # keyerror, even though m in d.keys()