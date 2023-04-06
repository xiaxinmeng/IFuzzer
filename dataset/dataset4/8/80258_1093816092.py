@attr.s(auto_attribs=True)
class Parent:
    foo: str
    bar: int
    baz: bool = False


@attr.s(auto_attribs=True)
class Child(Parent):
    spam: str
    baz: bool = False