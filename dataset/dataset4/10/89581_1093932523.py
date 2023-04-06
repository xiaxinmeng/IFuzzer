@dataclass
class Foo(Generic[T]):
    bar: list[T]
    baz: T | None