class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int