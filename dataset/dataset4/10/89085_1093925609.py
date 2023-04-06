
import codegen
from dataclasses import dataclass

@dataclass
class AtomX:
    my_symbol: str
    quantity: str = ""

codegen.inheritance_map(AtomX("qwerty"))

