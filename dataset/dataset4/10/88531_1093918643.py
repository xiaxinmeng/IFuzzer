@dataclass
class Rectangle:
    height: float
    width: float

@dataclass
class Square(Rectangle):
    side: float
    height: float = field(init=False)
    width: float = field(init=False)

    def __post_init__(self) -> None:
        super().__init__(self.side, self.side)