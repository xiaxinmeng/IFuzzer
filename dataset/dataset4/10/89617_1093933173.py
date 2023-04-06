import typing


class P(typing.Protocol):
    def m1(self) -> None: ...

class M:
    def __init__(self) -> None:
        super().__init__()
        self.o = True

class C(M, P):
    def __init__(self) -> None:
        super().__init__()
        self.op = True

    def m1(self) -> None:
        pass

c = C()