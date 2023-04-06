@dataclass
class Bar:
    callback: Callable[[int], int] = field(init=True, default=lambda x: x**2)