@dataclass
class B:
    a: field(type=int, keyword_only=True)
    b: int

@dataclass
class C(B):
    c: int
    d: field(type=int, keyword_only=True)