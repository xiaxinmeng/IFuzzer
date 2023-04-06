class A:
    __slots__ = ()
    x: ClassVar = set()

A()  # it's ok

@dataclass
class B:
    __slots__ = ()
    x = set()

B()  # ok too

@dataclass
class C:
    __slots__ = ()
    # cannot use set() because of error
    x: ClassVar = field(default_factory=set) 

C()  # AttributeError: 'C' object has no attribute 'x'