
from typing import Protocol


class P(Protocol):
    pm: str  # no default value, but still a protocol member


class C(P):
    # inherits P but does NOT implement pm, since P did not provide a default value
    pass

    
assert isinstance(C(), P)  # violates the PEP 544 requirement cited above

C().pm  # raises: AttributeError: 'C' object has no attribute 'pm'
