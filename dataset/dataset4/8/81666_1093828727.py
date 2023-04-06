import dataclasses


@dataclasses.dataclass
class A:
    def __eq__(self, other):
        return True