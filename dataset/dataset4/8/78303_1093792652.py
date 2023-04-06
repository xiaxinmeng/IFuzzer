import inspect
from dataclasses import *
import enum

@dataclass
class SimpleDataObject(object):
    field_a: int = field()
    field_b: str = "asdad"