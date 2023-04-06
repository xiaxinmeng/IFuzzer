@dataclass
class Parent:
    i: int
    j: int = 0


@dataclass
class Child(Parent):
    k: int
    l: int = 1