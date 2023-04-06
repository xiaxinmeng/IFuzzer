
def log_init(cls):
    try:
        original_init = vars(cls)['__init__']
    except KeyError:
        def original_init(self, *args, **kwargs):
            super(cls, self).__init__(*args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        print(f'{cls.__name__}.__init__ was called')
        original_init(self, *args, **kwargs)
    
    cls.__init__ = __init__
    return cls

@log_init
@dataclasses.dataclass
class Foo:
    foo: int
    
@dataclasses.dataclass
class Bar(Foo):
    bar: int
    
Foo(1)  # Prints "Foo.__init__ was called"
Bar(1, 2)  # Prints nothing
