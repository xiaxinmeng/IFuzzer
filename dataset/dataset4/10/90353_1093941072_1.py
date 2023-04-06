from typing_extensions import Annotated, get_type_hints

class Foo:
    def __init__(
        self,
        x: 
            Annotated[Optional[str], "doc string"] = None,
    ):
        ...

get_type_hints(Foo.__init__, include_extras=True)
# {'x': typing.Union[typing_extensions.Annotated[typing.Union[str, NoneType], 'doc string'], NoneType]}