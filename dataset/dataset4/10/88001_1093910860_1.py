@dataclasses.dataclass
class Bar(Foo):
    bar: int

    def __post_init__(self):
        Foo.__init__(self, baz=self.bar) # or whatever