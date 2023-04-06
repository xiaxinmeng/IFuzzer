
from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass()
class Test:
    a: int
    b: Dict[Any, Any] = field(default_factory=dict)

print(Test.__init__.__defaults__)  # <factory>
