Foo = namedtuple('Foo', 'x y')
def frob(self):
    return self.x + self.y
# probably actually done via a @member(Foo) decorator
# so adding more code here is not a problem.
Foo.frob.__qualname__ = 'Foo.frob'
Foo.frob = frob
del frob