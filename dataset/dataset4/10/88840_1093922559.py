from frozendict import frozendict
from dataclasses import dataclass

@dataclass
class A:
    a: frozendict = frozendict(a=1)