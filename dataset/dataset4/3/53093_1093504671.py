class Crasher(tuple): pass
foo = Crasher()
a = [1] + foo
b=a[0]
print (type(a), len(a), type(b), len(type(b)), type(type(b)))