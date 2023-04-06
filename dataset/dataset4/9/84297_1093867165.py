
class C:
    def __init__(self, n):
        if n:
            self.a = 1
            self.b = 2
            self.c = 3
        else:
            self.c = 1
            self.b = 2
            self.a = 3


o1 = C(True)
o2 = C(False)
print(o2.__dict__)  # {'c': 1, 'b': 2, 'a': 3}

d1 = {}
d1.update(o2.__dict__)  # {'a': 3, 'b': 2, 'c': 1}
print(d1)
