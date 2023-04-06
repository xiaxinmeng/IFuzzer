class Name(str):
  def __eq__(self, other):
     del x[self]
     return str.__eq__(self, other)
  def __hash__(self):
     return str.__hash__(self)

x = {Name("a"):1, Name("b"):2}
def f(a, b): print( a,b)

f(**x)   # Segfault
