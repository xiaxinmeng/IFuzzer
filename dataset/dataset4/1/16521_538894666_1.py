class Foo:
    pass

# Will return [] if getattr_static is used
inspect.getmembers(Foo('test'), inspect.isclass)