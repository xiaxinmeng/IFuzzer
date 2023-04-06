
import typing

FooList1: typing.TypeAlias = list["Foo"]
FooList2: typing.TypeAlias = typing.List["Foo"]

class Foo:
    pass

