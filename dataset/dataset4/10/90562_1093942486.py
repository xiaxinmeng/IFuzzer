import dataclasses

@dataclasses.dataclass(slots=True)
class A:
    pass


@dataclasses.dataclass(slots=True)
class B(A):
    def test(self):
        super()