@dataclass
class X:
    def __post_init__(self, **kwargs):
        super().__post_init__(**kwargs)
        ...

@dataclass
class Y(X):
    def __post_init__(self, **kwargs):
        super().__post_init__(**kwargs)
        ...