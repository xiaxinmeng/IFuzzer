@dataclass
class NestedDataclass(object):
    name: str
    options: Dict[str, Any] = field(default_factory=dict)

@dataclass
class RootDataclass(object):
    nested_list: List[NestedDataclass]