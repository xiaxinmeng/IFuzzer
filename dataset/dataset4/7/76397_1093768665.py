@dataclass
class C:
    a: ...   # field without a default
    b: ... = 0 # field with a default