class Crasher(tuple): pass
foo = Crasher()
x = [1]
a = x + foo
b=a[0]

if id(b) == id(x):
  raise Exception("It's the C compiler what did it!")