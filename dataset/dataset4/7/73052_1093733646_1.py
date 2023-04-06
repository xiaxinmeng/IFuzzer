class Foo:
    pass

class Meta(type):
    def mro(cls):
        return (cls, Foo, object)

    def __setattr__(cls, name, value):
        setattr(Foo, name, value)

proxy = Meta('FooProxy', (), {})

proxy.x = 300
proxy.x  # don't omit
proxy.x = 0