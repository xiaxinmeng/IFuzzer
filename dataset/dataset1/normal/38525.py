class A:
    def __init__(self, x, y):
        if x: self.x = x
        if y: self.y = y

a = A(1, 2)
print(list(iter(a.__dict__)))
print(list(reversed(a.__dict__)))
b = A(1, 0)
print(list(iter(b.__dict__)))
print(list(reversed(b.__dict__)))
