
@dataclass
class A:
  pass

a = A()

d = weakref.WeakKeyDictionary()
d[a] = 3  # TypeError: unhashable type: 'A'
