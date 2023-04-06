AD=frozendict(a=1)
@dataclass
class A:
    a: frozendict = field(default_factory=lambda:AD)