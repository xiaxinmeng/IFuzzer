class Foo:
    def __init__(
        self,
        x: 
            Annotated[Optional[str], "doc string"] = None,
    ):
        ...

class Foo2:
    x: Annotated[Optional[str], "doc string"] = None

get_type_hints(Foo.__init__) 
# {'x': typing.Union[typing_extensions.Annotated[typing.Union[str, NoneType], 'doc string'], NoneType]}

get_type_hints(Foo2)
# {'x': typing_extensions.Annotated[typing.Union[str, NoneType], 'doc string']}