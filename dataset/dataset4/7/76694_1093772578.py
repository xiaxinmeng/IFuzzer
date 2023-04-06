@dataclass
class A:
    def __eq__(self, other): pass

@dataclass
class B:
    def __eq__(self, other): pass
    __hash__ = None