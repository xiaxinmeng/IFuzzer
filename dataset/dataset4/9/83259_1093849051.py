dataclass()
class Test:
    a: int
    b: Dict[Any, Any] = field(default_factory=dict)