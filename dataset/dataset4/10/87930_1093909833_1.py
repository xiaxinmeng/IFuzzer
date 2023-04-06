@dataclass
class Child(Parent, Mixin):
    __match_args__ = ()
    ...