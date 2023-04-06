
foo = frozenset()
print(foo)             # frozenset()
foo.update({"hello"})  # AttributeError, expected
foo.__ior__({"hello"}) # AttributeError, expected
foo |= {"hello"}       # No error
print(foo)             # frozenset({"hello"})
