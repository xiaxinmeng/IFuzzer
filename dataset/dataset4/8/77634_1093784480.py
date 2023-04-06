from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar, Any

@dataclass
class C():
    class_var: ClassVar[Any] = object()
    data: str