import typing

class Baz:
    pass

class Bar:
    pass

class Foo:
    baz: typing.Optional[Bar] = None
    Bar: typing.Optional[Bar] = None

class Spam:
    bar: typing.Optional[Bar] = None
    baz: typing.Optional[bar] = None

print(Foo.__dict__.get('__annotations__', {}))
print(Spam.__dict__.get('__annotations__', {}))