class B:
    def __init__(self, a, b, c):
        first_field = next(iter(fields(self)))
        setattr(self, first_field.name, a+b+c)

mydataclass = dataclass(init=False)

@mydataclass
class C(B):
    i: int

@mydataclass
class D(B):
    j: int

print(C(1, 2, 3))
print(D(4, 5, 6))