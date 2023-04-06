@dataclass
class Foo:
    @descriptorA
    @descriptorB
    def bar(self):
        return some_value
    
    @bar.setter
    def bar(self, value):
        ...  # store value
    
    bar: int = field(descriptor=bar)