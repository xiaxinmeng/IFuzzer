class Foo:
    pass

inspect.getattr_static(Foo('test'), '__class__')