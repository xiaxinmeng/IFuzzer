
import dataclasses

@dataclasses.dataclass
class Foo:
    foo: int
    
    def __init__(self, *args, **kwargs):
        print('Foo.__init__')  # This is never printed

@dataclasses.dataclass
class Bar(Foo):
    bar: int

obj = Bar(1, 2)
print(vars(obj))  # {'foo': 1, 'bar': 2}
