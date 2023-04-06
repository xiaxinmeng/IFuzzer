from dataclasses import dataclass

@dataclass
class Foo:
    foo: int
    
    def __init__(self, a, b, c):
        self.foo = a * b * c

@dataclass
class Bar(Foo):
    bar: int
    

print(Bar(1, 2))
print(Foo(1, 2, 3))