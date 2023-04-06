class Foo(AbstractFoo):
    bar = property(AbstractFoo.get_bar, AbstractFoo.set_bar)