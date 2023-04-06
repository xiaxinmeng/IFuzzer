a = dict(a=1,c=3)
b = dict(a=0,b=2)
a.update(b)
assert a == dict(a=0,b=2,c=3)