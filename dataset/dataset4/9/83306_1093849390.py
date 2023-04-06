class Foo:
    @property
    def bar(self) -> int: return 42

    @bar.setter
    def bar(self, value: int) -> None: pass

    def baz(self, arg: float) -> str: pass