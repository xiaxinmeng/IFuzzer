# descriptors.py
class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Foo():
    attr = Verbose_attribute()


class Bar():
    pass


foo = Foo()
print(foo.__class__.__dict__["attr"].__dict__)

bar = Bar()

descr = Verbose_attribute()
Bar.attr = descr
print(bar.__class__.__dict__["attr"].__dict__)

descr.__set_name__(bar, "attr")
print(bar.__class__.__dict__["attr"].__dict__)