import foo
x = foo.C()
assert isinstance(x, foo.C) # OK
reload(foo)
assert isinstance(x, foo.C) # Fails