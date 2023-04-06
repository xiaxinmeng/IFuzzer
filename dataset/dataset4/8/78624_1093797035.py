import enum

class X:
   class I:
      pass

class Y:
   class I(enum.Enum):
      pass

print(X.I)
print(Y.I)