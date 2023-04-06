class X(object):
    pass

x = X()
items = ["foo", "bar", "baz"]

for each in items:
    setattr(x, each, lambda: each)
    
print("foo", x.foo())    
print("bar", x.bar())
print("baz", x.baz())