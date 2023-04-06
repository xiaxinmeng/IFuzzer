
import codegen
from dataclasses import dataclass

@dataclass
class AtomX:
    my_symbol: str
    quantity: str = ""


if __name__ == "__main__":
    codegen.inheritance_map(AtomX("qwerty"))

