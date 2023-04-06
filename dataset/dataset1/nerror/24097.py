class X(type("x")): 
  pass

class Y:
  __slotnames__ = [X() for i in range(2)]

  def __getattr__(self, attr):

    print("__getattr__")

    if attr=="__getstate__":
      raise AttributeError

    L = type(self).__slotnames__
    n = len(L)
    for i in range(n):
      del L[0]
      L.append(i)

y = Y()
y.__reduce__(2)
