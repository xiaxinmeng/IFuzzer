class Foo:
   attr = -13

ins = Foo()
ins.attr = 42
print(ins.attr)
del ins.attr
print(ins.attr)