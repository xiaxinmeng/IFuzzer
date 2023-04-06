@dataclass
class Foo:
    bar = field(default=4)
    # assigns 4 to Foo.bar but not to foo.bar (bonus: __init__ will be faster)

    bar = field(default=some_descriptor)
    # assigns some_descriptor to Foo.bar, so Foo().bar does a __get__ on the descriptor

    bar = field(default_factory=SomeDescriptor)
    # assigns a new SomeDescriptor instance to every instance of Foo

    bar = field(default_factory=lambda: some_descriptor)
    # assigns the same descriptor object to every instance of Foo