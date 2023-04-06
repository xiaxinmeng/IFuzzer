@dataclass
class F:
    a: InitVar[int]
    b: InitVar[int]

    def __post_init__(self, x, y):
        print(f'{x=} {y=}')