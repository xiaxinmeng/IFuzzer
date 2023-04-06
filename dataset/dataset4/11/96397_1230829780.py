
class C:
    pass

class IdWithUnit(str):
    def __eq__(self, other):
        s = self.split()[0]
        return s.__eq__(other)
    def __hash__(self):
        s = self.split()[0]
        return s.__hash__()

def f(a, **kwargs):
    return f'a={a}, kwargs={kwargs}'


awu = IdWithUnit("a ft")
assert(awu == "a")
assert(str(awu) == "a ft")

# An IdWithUnit functions as a keyword assignment
assert(f(**{awu: 42}) == "a=42, kwargs={}")

# Objects with __dict__ accept IdWithUnit as attribute names
c = C()
setattr(c, awu, 42)
assert(getattr(c, awu) == 42)

# The IdWithUnit attribute retains its full name
assert(IdWithUnit in map(type, c.__dict__.keys()))
assert("a ft" in map(str, c.__dict__.keys()))

# Use of an IdWithUnit establishes an attribute with the plain name
assert(c.a == 42)
