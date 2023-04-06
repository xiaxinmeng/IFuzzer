@dataclass
class Child(Parent):
    __match_args__ = Parent.__match_args__
    ...