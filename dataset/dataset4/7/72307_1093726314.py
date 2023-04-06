class Cls:
    pass

a = Cls()
a.x = 1
a.y = 2

b = Cls()
b.x = 1
print(hasattr(b, 'y'))
print(b.__dict__.pop('y', None))