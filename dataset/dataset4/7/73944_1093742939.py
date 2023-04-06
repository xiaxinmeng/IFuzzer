class Foo_Base:
    pass

class Bar_Base:
    def get_foo(self):
        f = Foo_Base()
        return f

class Foo(Foo_Base):
    pass

class Bar(Bar_Base):
    def get_foo2(self):
        return super(Bar, self).get_foo()
    
bar = Bar()
b = bar.get_foo2()