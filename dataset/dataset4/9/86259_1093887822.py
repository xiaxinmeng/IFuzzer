class Descriptor:
    pass

class C:
    def __init__(self):
        self.x = 1
    x = Descriptor()

def f(o):
    return o.x

o = C()
for i in range(10000):
    assert f(o) == 1

Descriptor.__get__ = lambda self, instance, value: 2
Descriptor.__set__ = lambda *args: None

print(f(o))