from typing import Type
foo: int = 1
Foo = Type[foo]  # equivalent to Foo = int

def bar(x: string) -> None :
    ...
Bar = Type[bar]  # equivalent to Bar = Callable[[str], None]