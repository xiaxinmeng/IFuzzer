from dataclasses import dataclass, field
from typing import get_type_hints, List, ForwardRef

@dataclass
class Node:
    children: list["Node"] = field(default_factory=list)
    children2: List["Node"] = field(default_factory=list)

assert get_type_hints(Node) == {"children": list["Node"], "children2": List[Node]}
assert List["Node"].__args__ == (ForwardRef("Node"),)
assert list["Node"].__args__ == ("Node",) # No ForwardRef here, so no evaluation by get_type_hints