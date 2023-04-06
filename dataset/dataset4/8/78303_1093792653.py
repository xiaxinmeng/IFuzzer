@dataclass
class SimpleDataObject(object):
    field_a: int = field(default=10)
    field_b: str = "asdad"