import typing

V = typing.TypeVar("V")

class Test(typing.Generic[V]):
    def __init__(self, value: V) -> None:
        self.value = value

def main():
    ts = [Test(x) for x in range(10)]
    sum(t.value for t in ts)