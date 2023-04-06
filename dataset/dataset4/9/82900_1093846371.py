from dataclasses import InitVar, dataclass

@dataclass
class Foo:
    bar: InitVar[str]
    quux: InitVar[str]

    def __post_init__(self, quux: str, bar: str) -> None:
        print(f"bar is {bar}; quux is {quux}")

Foo(bar="a", quux="b")