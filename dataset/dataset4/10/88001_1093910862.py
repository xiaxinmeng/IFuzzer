
@dataclasses.dataclass
class Foo:
    foo: int
    
    def __init__(self):
        self.foo = 5
    
@dataclasses.dataclass
class Bar(Foo):
    bar: int
    
    def __post_init__(self):
        super().__init__()

bar = Bar(1)  # TypeError: __init__() missing 1 required positional argument: 'bar'
