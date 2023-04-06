from dataclasses import dataclass

class A:
    __slots__ = ()
    def __init_subclass__(cls, msg):
        print(msg)

@dataclass(slots=True)
class B(A, msg="Hello world!"):
    pass