class Foo:
    pass

class Works(str, Foo, Enum):
    BAR = 'baz'

class Fails(Foo, str, Enum):
    BAR = 'baz'
